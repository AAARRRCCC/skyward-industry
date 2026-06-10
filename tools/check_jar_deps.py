"""Ground-truth dependency check: read META-INF/neoforge.mods.toml inside every
jar in the manifest (recursing jar-in-jar), collect provided mod IDs and required
dependencies, and report any required dep no jar provides.

Catches deps that Modrinth/CurseForge metadata fails to declare (e.g. Sable
Schematic Tool -> ldlib2). Jars are cached in %TEMP%/skyward-jarcache.
"""
import io
import json
import os
import tomllib
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = Path(os.environ.get("TEMP", "/tmp")) / "skyward-jarcache"
HEADERS = {"User-Agent": "skyward-industry-pack-build/0.1 (rbrady.business@gmail.com)"}
BUILTIN = {"minecraft", "neoforge", "forge", "java"}


def fetch(url, filename):
    CACHE.mkdir(parents=True, exist_ok=True)
    p = CACHE / filename
    if p.exists():
        return p.read_bytes()
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=180) as r:
        data = r.read()
    p.write_bytes(data)
    return data


def scan_jar(data, source, provided, required):
    z = zipfile.ZipFile(io.BytesIO(data))
    names = z.namelist()
    for toml_name in ("META-INF/neoforge.mods.toml", "META-INF/mods.toml"):
        if toml_name in names:
            try:
                t = tomllib.loads(z.read(toml_name).decode("utf-8"))
            except Exception as e:  # noqa: BLE001
                print(f"  WARN {source}: cannot parse {toml_name}: {e}")
                break
            for mod in t.get("mods", []):
                provided.setdefault(mod["modId"], source)
            for dep_modid, deps in t.get("dependencies", {}).items():
                for d in deps:
                    dtype = d.get("type", "required").lower()
                    if dtype == "required":
                        required.append((dep_modid, d["modId"], d.get("versionRange", ""),
                                         d.get("side", "BOTH"), source))
            break
    for nested in [n for n in names if n.startswith("META-INF/jarjar/") and n.endswith(".jar")]:
        scan_jar(z.read(nested), f"{source}!{Path(nested).name}", provided, required)


def main():
    lock = json.loads((ROOT / "tools/manifest.lock.json").read_text(encoding="utf-8"))
    cf = json.loads((ROOT / "docs/audit/curseforge_audit.json").read_text(encoding="utf-8"))
    provided, required = {}, []
    for m in lock["mods"]:
        if "modrinth" in m:
            url, fn = m["modrinth"]["url"], m["modrinth"]["filename"]
        else:
            e = cf.get(m["slug"], {})
            url, fn = e.get("download_url"), e.get("filename")
            if not url:
                print(f"  skip {m['slug']} (no CF download url)")
                continue
        try:
            scan_jar(fetch(url, fn), m["slug"], provided, required)
        except Exception as e:  # noqa: BLE001
            print(f"  ERROR {m['slug']}: {e}")
    print(f"provided mod ids: {len(provided)}")

    missing = []
    for owner, dep, ver, side, source in required:
        if dep not in provided and dep not in BUILTIN:
            missing.append((owner, dep, ver, side, source))
    if missing:
        print("\nMISSING REQUIRED DEPENDENCIES:")
        for owner, dep, ver, side, source in sorted(set(missing)):
            print(f"  {source} (mod '{owner}') requires '{dep}' {ver} side={side}")
        raise SystemExit(1)
    print("all required dependencies satisfied")


if __name__ == "__main__":
    main()
