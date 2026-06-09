"""Phase 0 audit (CurseForge side): FTB mods are not on Modrinth.

Queries the curse.tools proxy for each slug, filtered to MC 1.21.1 + NeoForge,
and records project id, file id, filename, fingerprint (murmur2), and the
allowModDistribution flag (packwiz-installer needs it true for auto-download).
"""
import json
import sys
import time
import urllib.request

API = "https://api.curse.tools/v1/cf"
HEADERS = {"User-Agent": "skyward-industry-pack-audit/0.1 (rbrady.business@gmail.com)"}
NEOFORGE = 6  # modLoaderType enum

SLUGS = ["ftb-quests-forge", "ftb-teams-forge", "ftb-library-forge",
         "ftb-chunks-forge", "ftb-xmod-compat"]


def get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def main():
    out = {}
    for slug in SLUGS:
        entry = {"slug": slug}
        try:
            mods = get(f"{API}/mods/search?gameId=432&slug={slug}")["data"]
            mod = next(m for m in mods if m["slug"] == slug)
            entry["mod_id"] = mod["id"]
            entry["name"] = mod["name"]
            entry["allowModDistribution"] = mod.get("allowModDistribution")
            files = get(f"{API}/mods/{mod['id']}/files?gameVersion=1.21.1&modLoaderType={NEOFORGE}")["data"]
            if not files:
                entry["status"] = "NO 1.21.1 NEOFORGE FILE"
            else:
                f = files[0]  # newest first
                entry["status"] = "ok"
                entry["file_id"] = f["id"]
                entry["filename"] = f["fileName"]
                entry["display_name"] = f["displayName"]
                entry["date"] = f["fileDate"]
                entry["release_type"] = f["releaseType"]  # 1=release 2=beta 3=alpha
                entry["fingerprint"] = f["fileFingerprint"]
                entry["download_url"] = f.get("downloadUrl")
                sha1 = [h["value"] for h in f.get("hashes", []) if h["algo"] == 1]
                entry["sha1"] = sha1[0] if sha1 else None
                entry["dependencies"] = f.get("dependencies", [])
        except Exception as e:  # noqa: BLE001
            entry["status"] = f"ERROR: {e}"
        out[slug] = entry
        print(f"{slug}: {entry.get('status')} | id={entry.get('mod_id')} file={entry.get('file_id')} "
              f"{entry.get('filename')} dist={entry.get('allowModDistribution')}", flush=True)
        time.sleep(0.3)

    with open(sys.argv[1], "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
