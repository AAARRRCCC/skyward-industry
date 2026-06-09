"""Download pinned jars (data inspection only) and extract modding facts we must
not guess at: mod namespaces, item registry IDs (from lang files), recipe folder
layout and JSON shapes, and KubeJS plugin markers.

Writes one summary per mod into docs/audit/jars/<slug>.md and full lang item key
lists into docs/audit/jars/<slug>_items.txt.
"""
import hashlib
import io
import json
import sys
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs/audit/jars"
HEADERS = {"User-Agent": "skyward-industry-pack-build/0.1 (rbrady.business@gmail.com)"}

INSPECT = ["create", "create-aeronautics", "create-aeroworks", "sable",
           "numismatics", "kubejs", "create-aeronautics" ]


def fetch(url, sha512):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    if hashlib.sha512(data).hexdigest() != sha512:
        raise SystemExit(f"sha512 mismatch for {url}")
    return data


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    lock = json.loads((ROOT / "tools/manifest.lock.json").read_text(encoding="utf-8"))
    mods = {m["slug"]: m for m in lock["mods"]}
    for slug in dict.fromkeys(INSPECT):
        m = mods[slug]["modrinth"]
        print(f"== {slug} ({m['filename']}, {m['size']//1024} KiB)", flush=True)
        z = zipfile.ZipFile(io.BytesIO(fetch(m["url"], m["sha512"])))
        names = z.namelist()

        namespaces = sorted({n.split("/")[1] for n in names
                             if n.startswith(("assets/", "data/")) and len(n.split("/")) > 2})
        lines = [f"# Jar inspection: {slug} ({m['version_number']})", "",
                 f"namespaces: {namespaces}", ""]

        # recipe dirs + one example of each recipe type
        recipe_files = [n for n in names if "/recipe" in n and n.endswith(".json")]
        types = {}
        for n in recipe_files:
            try:
                j = json.loads(z.read(n).decode("utf-8"))
                t = j.get("type", "?")
                if t not in types:
                    types[t] = (n, j)
            except Exception:  # noqa: BLE001
                pass
        lines.append(f"recipe files: {len(recipe_files)}; distinct types: {len(types)}")
        for t, (n, j) in sorted(types.items()):
            lines += ["", f"## type `{t}`  (example: {n})", "```json",
                      json.dumps(j, indent=2)[:2200], "```"]

        # kubejs integration markers
        kjs = [n for n in names if "kubejs" in n.lower()]
        lines += ["", f"kubejs markers in jar: {kjs[:20]}"]

        # lang -> item ids
        for ns in namespaces:
            lang_path = f"assets/{ns}/lang/en_us.json"
            if lang_path in names:
                lang = json.loads(z.read(lang_path).decode("utf-8"))
                items = sorted(k for k in lang if k.startswith(f"item.{ns}."))
                blocks = sorted(k for k in lang if k.startswith(f"block.{ns}."))
                (OUT / f"{slug}_{ns}_items.txt").write_text(
                    "\n".join(items + [""] + blocks) + "\n", encoding="utf-8")
                lines += ["", f"lang {ns}: {len(items)} item keys, {len(blocks)} block keys "
                          f"-> {slug}_{ns}_items.txt"]

        (OUT / f"{slug}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"   namespaces={namespaces} recipes={len(recipe_files)} types={len(types)}")


if __name__ == "__main__":
    main()
