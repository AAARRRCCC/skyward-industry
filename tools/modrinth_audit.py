"""Phase 0 audit: query Modrinth for each candidate mod, pinned to MC 1.21.1 + NeoForge.

Writes docs/audit/modrinth_audit.json with project metadata, the newest matching
version, and that version's dependency list (project IDs resolved to slugs).
"""
import json
import sys
import time
import urllib.request
import urllib.parse

API = "https://api.modrinth.com/v2"
HEADERS = {"User-Agent": "skyward-industry-pack-audit/0.1 (rbrady.business@gmail.com)"}

SLUGS = [
    # core tech
    "create", "create-aeronautics", "sable", "create-aeroworks",
    # scripting / quests
    "kubejs", "rhino", "architectury-api",
    "ftb-quests", "ftb-teams", "ftb-library",
    # economy
    "numismatics", "lightmans-currency",
    # admin
    "chunky", "worldedit",
    # qol / perf candidates
    "emi", "jei", "jade", "ftb-chunks", "inventory-sorter",
    "mouse-tweaks", "sodium", "lithium", "ferrite-core",
    # aeronautics ecosystem extras seen in search
    "sablecompat", "create-aeronautics-compatability", "copycats+-aeronautics-weight",
]

GAME_VERSIONS = urllib.parse.quote('["1.21.1"]')
LOADERS = urllib.parse.quote('["neoforge"]')


def get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def main():
    out = {}
    id_to_slug = {}
    for slug in SLUGS:
        entry = {"slug": slug}
        try:
            p = get(f"{API}/project/{slug}")
            entry["title"] = p["title"]
            entry["project_id"] = p["id"]
            entry["license"] = p.get("license", {}).get("id")
            entry["client_side"] = p["client_side"]
            entry["server_side"] = p["server_side"]
            id_to_slug[p["id"]] = slug
            vers = get(f"{API}/project/{slug}/version?game_versions={GAME_VERSIONS}&loaders={LOADERS}")
            if not vers:
                entry["status"] = "NO 1.21.1 NEOFORGE VERSION"
            else:
                v = vers[0]  # newest first
                entry["status"] = "ok"
                entry["version_number"] = v["version_number"]
                entry["version_id"] = v["id"]
                entry["date_published"] = v["date_published"]
                entry["version_type"] = v["version_type"]
                entry["loaders"] = v["loaders"]
                entry["game_versions"] = v["game_versions"]
                entry["files"] = [
                    {
                        "filename": f["filename"],
                        "url": f["url"],
                        "sha512": f["hashes"]["sha512"],
                        "sha1": f["hashes"]["sha1"],
                        "size": f["size"],
                        "primary": f["primary"],
                    }
                    for f in v["files"]
                ]
                entry["dependencies"] = v.get("dependencies", [])
        except Exception as e:  # noqa: BLE001
            entry["status"] = f"ERROR: {e}"
        out[slug] = entry
        print(f"{slug}: {entry.get('status')} {entry.get('version_number', '')}", flush=True)
        time.sleep(0.2)

    # resolve dependency project ids -> slugs/titles
    dep_ids = set()
    for e in out.values():
        for d in e.get("dependencies", []):
            if d.get("project_id"):
                dep_ids.add(d["project_id"])
    unresolved = [i for i in dep_ids if i not in id_to_slug]
    dep_info = {}
    for pid in unresolved:
        try:
            p = get(f"{API}/project/{pid}")
            dep_info[pid] = {"slug": p["slug"], "title": p["title"]}
        except Exception as e:  # noqa: BLE001
            dep_info[pid] = {"slug": f"ERROR: {e}", "title": ""}
        time.sleep(0.2)
    for pid, slug in id_to_slug.items():
        dep_info[pid] = {"slug": slug, "title": out[slug].get("title", slug)}

    result = {"audited": out, "dep_project_index": dep_info}
    with open(sys.argv[1], "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print("\nDependency index:")
    for pid, info in dep_info.items():
        print(f"  {pid} -> {info['slug']}")


if __name__ == "__main__":
    main()
