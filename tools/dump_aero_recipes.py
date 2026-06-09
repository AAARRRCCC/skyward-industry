"""Dump every recipe (id, type, output) from the aeronautics ecosystem jars so
Phase 2 removals/replacements target real recipe IDs. Output:
docs/audit/recipes_aero.md"""
import hashlib
import io
import json
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEADERS = {"User-Agent": "skyward-industry-pack-build/0.1 (rbrady.business@gmail.com)"}


def fetch(url, sha512):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    assert hashlib.sha512(data).hexdigest() == sha512
    return data


def out_id(j):
    r = j.get("result") or (j.get("results") or [{}])[0]
    if isinstance(r, dict):
        return r.get("id") or r.get("item") or "?"
    return str(r)


def walk(z, source, rows):
    for n in z.namelist():
        if "/recipe/" in n and n.endswith(".json") and "/advancement" not in n:
            try:
                j = json.loads(z.read(n).decode("utf-8"))
            except Exception:  # noqa: BLE001
                continue
            if "type" not in j:
                continue
            ns, _, rest = n[len("data/"):].partition("/recipe/")
            rid = f"{ns}:{rest[:-5]}"
            rows.append((source, rid, j["type"], out_id(j), json.dumps(j)))


def main():
    lock = json.loads((ROOT / "tools/manifest.lock.json").read_text(encoding="utf-8"))
    mods = {m["slug"]: m["modrinth"] for m in lock["mods"] if "modrinth" in m}
    rows = []
    for slug in ("create-aeronautics", "create-aeroworks"):
        m = mods[slug]
        data = fetch(m["url"], m["sha512"])
        z = zipfile.ZipFile(io.BytesIO(data))
        inner = [n for n in z.namelist() if n.endswith(".jar")]
        if inner:
            for nj in inner:
                walk(zipfile.ZipFile(io.BytesIO(z.read(nj))), Path(nj).stem.split(".")[-1], rows)
        else:
            walk(z, slug, rows)

    lines = ["# All recipes in aeronautics ecosystem jars", ""]
    for source, rid, t, out, _ in sorted(rows, key=lambda r: (r[0], r[2], r[1])):
        lines.append(f"- [{source}] `{rid}` ({t}) -> `{out}`")
    # full JSON appendix for the ones we will re-price
    interesting = ("engine_assembly", "gyroscopic_mechanism", "propeller", "gyroscope",
                   "joystick", "servo", "levitite", "envelope", "portable_engine",
                   "physics_assembler", "navigation_table", "docking", "steam_vent",
                   "burner", "sail", "spring", "winch", "swivel", "steering", "throttle")
    lines += ["", "# Full JSON for sink-relevant recipes", ""]
    for source, rid, t, out, raw in sorted(rows):
        if any(k in rid for k in interesting):
            lines += [f"## `{rid}` ({t}) -> `{out}`", "```json", raw, "```", ""]
    (ROOT / "docs/audit/recipes_aero.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(rows)} recipes dumped to docs/audit/recipes_aero.md")


if __name__ == "__main__":
    main()
