"""Recurse into the Aeronautics bundled jar (META-INF/jarjar) and inspect the
inner mod jar(s) the same way inspect_jars.py does for flat jars."""
import hashlib
import io
import json
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs/audit/jars"
HEADERS = {"User-Agent": "skyward-industry-pack-build/0.1 (rbrady.business@gmail.com)"}


def main():
    lock = json.loads((ROOT / "tools/manifest.lock.json").read_text(encoding="utf-8"))
    m = next(x for x in lock["mods"] if x["slug"] == "create-aeronautics")["modrinth"]
    req = urllib.request.Request(m["url"], headers=HEADERS)
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    assert hashlib.sha512(data).hexdigest() == m["sha512"]
    outer = zipfile.ZipFile(io.BytesIO(data))
    inner_jars = [n for n in outer.namelist() if n.endswith(".jar")]
    print("nested jars:", inner_jars)
    for nj in inner_jars:
        z = zipfile.ZipFile(io.BytesIO(outer.read(nj)))
        names = z.namelist()
        namespaces = sorted({n.split("/")[1] for n in names
                             if n.startswith(("assets/", "data/")) and len(n.split("/")) > 2})
        recipe_files = [n for n in names if "/recipe" in n and n.endswith(".json")]
        types = {}
        for n in recipe_files:
            try:
                j = json.loads(z.read(n).decode("utf-8"))
                t = j.get("type", "?")
                types.setdefault(t, (n, j))
            except Exception:  # noqa: BLE001
                pass
        base = Path(nj).stem
        lines = [f"# Nested jar: {nj}", "", f"namespaces: {namespaces}",
                 f"recipe files: {len(recipe_files)}; types: {sorted(types)}"]
        for t, (n, j) in sorted(types.items()):
            lines += ["", f"## type `{t}`  (example: {n})", "```json",
                      json.dumps(j, indent=2)[:2200], "```"]
        for ns in namespaces:
            lang_path = f"assets/{ns}/lang/en_us.json"
            if lang_path in names:
                lang = json.loads(z.read(lang_path).decode("utf-8"))
                items = sorted(k for k in lang if k.startswith(f"item.{ns}."))
                blocks = sorted(k for k in lang if k.startswith(f"block.{ns}."))
                (OUT / f"nested_{base}_{ns}_items.txt").write_text(
                    "\n".join(items + [""] + blocks) + "\n", encoding="utf-8")
                lines += [f"lang {ns}: {len(items)} items, {len(blocks)} blocks "
                          f"-> nested_{base}_{ns}_items.txt"]
        (OUT / f"nested_{base}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"  {nj}: ns={namespaces} recipes={len(recipe_files)} types={sorted(types)[:8]}")


if __name__ == "__main__":
    main()
