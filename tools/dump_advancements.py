"""Quest-gating research: dump every advancement (id, parent, trigger types,
lang title/description) from the jars that matter for quests, plus item
registries for the decor mods we haven't extracted yet.

Reads jars from the %TEMP%/skyward-jarcache populated by check_jar_deps.py.
Outputs docs/audit/advancements.md and docs/audit/jars/<slug>_<ns>_items.txt.
"""
import io
import json
import os
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = Path(os.environ["TEMP"]) / "skyward-jarcache"
OUT = ROOT / "docs/audit"

ADV_SLUGS = ["create", "create-aeronautics", "create-aeroworks", "numismatics",
             "create-deco", "copycats", "create-connected"]
ITEM_SLUGS = ["create-deco", "copycats", "create-connected"]


def jar_for(slug, lock):
    m = next(x for x in lock["mods"] if x["slug"] == slug)
    return CACHE / m["modrinth"]["filename"]


def zips_in(path):
    """Yield (label, ZipFile) for the jar AND any nested jarjar mod jars."""
    z = zipfile.ZipFile(path)
    yield path.stem, z
    for nj in [n for n in z.namelist() if n.startswith("META-INF/jarjar/") and n.endswith(".jar")]:
        yield Path(nj).stem.split(".")[-1], zipfile.ZipFile(io.BytesIO(z.read(nj)))


def main():
    lock = json.loads((ROOT / "tools/manifest.lock.json").read_text(encoding="utf-8"))
    lines = ["# Advancement inventory (quest gating hooks)", "",
             "`(R)` = recipe-unlock advancement, ignore. Trigger `impossible` = ",
             "granted only by mod code (best kind of gate: fires on real behavior).", ""]
    for slug in ADV_SLUGS:
        for label, z in zips_in(jar_for(slug, lock)):
            names = z.namelist()
            langs = {}
            for n in names:
                if n.endswith("/lang/en_us.json"):
                    try:
                        langs.update(json.loads(z.read(n).decode("utf-8")))
                    except Exception:  # noqa: BLE001
                        pass
            advs = [n for n in names if "/advancement/" in n and n.endswith(".json")
                    and "/recipes/" not in n and "/recipe/" not in n]
            if not advs:
                continue
            lines.append(f"## {slug} ({label}): {len(advs)} advancements")
            lines.append("")
            for n in sorted(advs):
                ns, _, rest = n[len("data/"):].partition("/advancement/")
                aid = f"{ns}:{rest[:-5]}"
                try:
                    j = json.loads(z.read(n).decode("utf-8"))
                except Exception:  # noqa: BLE001
                    continue
                triggers = sorted({c.get("trigger", "?") for c in j.get("criteria", {}).values()})
                title = j.get("display", {}).get("title", {})
                tkey = title.get("translate") if isinstance(title, dict) else None
                tval = langs.get(tkey, tkey or "")
                dkey = j.get("display", {}).get("description", {})
                dkey = dkey.get("translate") if isinstance(dkey, dict) else None
                dval = langs.get(dkey, "")
                parent = j.get("parent", "")
                lines.append(f"- `{aid}` — **{tval}** — _{dval}_  (parent: `{parent}`; triggers: {triggers})")
            lines.append("")
    (OUT / "advancements.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote docs/audit/advancements.md")

    for slug in ITEM_SLUGS:
        for label, z in zips_in(jar_for(slug, lock)):
            names = z.namelist()
            for n in names:
                if n.endswith("/lang/en_us.json"):
                    ns = n.split("/")[1]
                    try:
                        lang = json.loads(z.read(n).decode("utf-8"))
                    except Exception:  # noqa: BLE001
                        continue
                    items = sorted(k for k in lang if k.startswith((f"item.{ns}.", f"block.{ns}.")))
                    if items:
                        p = OUT / "jars" / f"{slug}_{ns}_items.txt"
                        p.write_text("\n".join(items) + "\n", encoding="utf-8")
                        print(f"wrote {p.name} ({len(items)} keys)")


if __name__ == "__main__":
    main()
