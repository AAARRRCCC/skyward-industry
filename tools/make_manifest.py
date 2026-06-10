"""Lock the Phase 0 mod decisions into tools/manifest.lock.json.

Reads docs/audit/modrinth_audit.json + docs/audit/curseforge_audit.json (raw API
captures) plus the PINS decision table below, fetches any version not already
audited, and writes a self-contained lock file. tools/build_pack.py consumes the
lock file only — re-running this script is how you bump versions.
"""
import json
import time
import urllib.request
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://api.modrinth.com/v2"
HEADERS = {"User-Agent": "skyward-industry-pack-build/0.1 (rbrady.business@gmail.com)"}

# side: both|server|client; optional mods get [option] blocks in .pw.toml
MODRINTH_PINS = [
    # slug, side, optional, default, note
    ("create",            "both",   False, True, None),
    ("create-aeronautics","both",   False, True, None),
    ("sable",             "both",   False, True, None),
    ("create-aeroworks",  "both",   False, True, None),
    # sablecompat removed 2026-06-09: 1.3.0 targets a newer Sable data format than
    # 1.2.2 (parse errors on load) and only tags blocks from mods we don't ship.
    ("kubejs",            "both",   False, True, None),
    ("rhino",             "both",   False, True, None),
    ("architectury-api",  "both",   False, True, None),
    ("numismatics",       "both",   False, True, None),
    ("jei",               "both",   False, True, None),
    ("jade",              "both",   False, True, None),
    ("lithium",           "both",   False, True, None),
    ("ferrite-core",      "both",   False, True, None),
    ("chunky",            "server", False, True, None),
    # worldedit side=both (2026-06-10): Brady preps builds in single-player too;
    # it's OP-gated on servers so client-side install is harmless.
    ("worldedit",         "both",   False, True, None),
    ("mouse-tweaks",      "client", True,  True, "Client QoL: drag-stacking"),
    ("inventory-profiles-next", "client", True, True,
     "Client QoL: inventory sorting (needs libipn + kotlin-for-forge)"),
    ("libipn",            "client", True,  True, "Dep of inventory-profiles-next"),
    ("kotlin-for-forge",  "client", True,  True, "Dep of libipn"),
    # --- manifest expansion 2026-06-09: build/QoL Create addons ---
    ("create-connected",  "both",   False, True, None),
    ("copycats",          "both",   False, True, None),
    ("copycats+-aeronautics-weight", "both", False, True, None),
    ("create-deco",       "both",   False, True, None),
    ("sable-weighted-create-deco", "both", False, True, None),
    # --- aeronautics extras ---
    ("ftbchunksaerospace", "both",  False, True, None),
    ("sable-schematic-tool", "both", False, True, None),
    ("ldlib",             "both",   False, True, "Required by sable-schematic-tool (modid ldlib2; undeclared on Modrinth)"),
    # --- performance suite ---
    ("modernfix",         "both",   False, True, None),
    ("clumps",            "both",   False, True, None),
    ("spark",             "both",   False, True, None),
    ("entityculling",     "client", True,  True, "Client perf: skip hidden entities (disable first if ships flicker)"),
    ("immediatelyfast",   "client", True,  True, "Client perf: batched immediate-mode rendering"),
    ("dynamic-fps",       "client", True,  True, "Client perf: throttle FPS when unfocused"),
    # --- optional-content tier 2026-06-10: progression-neutral by construction;
    #     nothing gated or quest-required ever references these ---
    ("cc-tweaked",        "both",   False, True, None),
    ("cc-sable",          "both",   False, True, None),
    ("advancedperipherals", "both", False, True, None),
    ("farmers-delight",   "both",   False, True, None),
    ("slice-and-dice",    "both",   False, True, None),
    ("interiors",         "both",   False, True, None),
    ("framedblocks",      "both",   False, True, None),
    # --- world shape 2026-06-10: 26k hard border, 20k charted disk (WORLD_SHAPE.md) ---
    ("chunkyborder",      "server", False, True, None),
    ("distanthorizons",   "both",   True,  True,
     "Whole-world LODs (server-side pregen + sharing). Disable client-side if FPS suffers."),
    # Terrain: spec's no-custom-worldgen rule amended by Brady 2026-06-10 —
    # established worldgen mods allowed, agent-authored worldgen still banned.
    # Enable Tectonic's "Increased Height" (y640) BEFORE world creation.
    ("tectonic",          "both",   False, True, None),
    ("lithostitched",     "both",   False, True, "Required by tectonic"),
    ("flyhigher",         "both",   False, True,
     "Configurable Aeronautics air-pressure curve; pairs with Tectonic y640 worlds"),
    ("cloth-config",      "client", False, True,
     "Required client-side by flyhigher (undeclared on Modrinth; jar mods.toml)"),
    # Chunk-gen throughput for pregen + DH (DH warns when C2ME is absent).
    # c2me-neoforge is ALPHA: first suspect on any worldgen crash/weirdness.
    ("c2me-neoforge",     "both",   False, True, None),
    # scalablelux removed 2026-06-10: Sable declares it hard-incompatible
    # (crash at mod loading). check_jar_deps now screens declared
    # incompatibilities so this class of conflict is caught offline.
]
# slugs whose pinned version differs from the audit's newest, or weren't audited
VERSION_OVERRIDES = {
    "sodium": "Pb3OXVqC",  # mc1.21.1-0.6.13-neoforge — newest *release*; audit newest was an alpha
}
EXTRA_MODRINTH = [
    ("sodium",            "client", True,  True, "Client QoL: rendering performance"),
]

GAME_VERSIONS = urllib.parse.quote('["1.21.1"]')
LOADERS = urllib.parse.quote('["neoforge"]')


def get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def primary_file(version):
    files = version["files"]
    for f in files:
        if f.get("primary"):
            return f
    return files[0]


def main():
    audit = json.loads((ROOT / "docs/audit/modrinth_audit.json").read_text(encoding="utf-8"))["audited"]
    cf = json.loads((ROOT / "docs/audit/curseforge_audit.json").read_text(encoding="utf-8"))

    mods = []
    for slug, side, optional, default, note in MODRINTH_PINS + EXTRA_MODRINTH:
        if slug in VERSION_OVERRIDES:
            v = get(f"{API}/version/{VERSION_OVERRIDES[slug]}")
            p = get(f"{API}/project/{slug}")
            title, project_id = p["title"], p["id"]
            f = primary_file(v)
            file_info = {"filename": f["filename"], "url": f["url"],
                         "sha512": f["hashes"]["sha512"], "size": f["size"]}
            vnum, vid = v["version_number"], v["id"]
            time.sleep(0.2)
        elif slug in audit and audit[slug].get("status") == "ok":
            e = audit[slug]
            title, project_id = e["title"], e["project_id"]
            files = e["files"]
            f = next((x for x in files if x.get("primary")), files[0])
            file_info = {"filename": f["filename"], "url": f["url"],
                         "sha512": f["sha512"], "size": f["size"]}
            vnum, vid = e["version_number"], e["version_id"]
        else:
            # not audited yet (libipn, kotlin-for-forge): fetch newest 1.21.1 neoforge release
            vers = get(f"{API}/project/{slug}/version?game_versions={GAME_VERSIONS}&loaders={LOADERS}")
            rel = [v for v in vers if v["version_type"] == "release"] or vers
            v = rel[0]
            p = get(f"{API}/project/{slug}")
            title, project_id = p["title"], p["id"]
            f = primary_file(v)
            file_info = {"filename": f["filename"], "url": f["url"],
                         "sha512": f["hashes"]["sha512"], "size": f["size"]}
            vnum, vid = v["version_number"], v["id"]
            time.sleep(0.2)
        mods.append({
            "name": title, "slug": slug, "side": side, "optional": optional,
            "default": default, "note": note, "source": "modrinth",
            "modrinth": {"project_id": project_id, "version_id": vid,
                         "version_number": vnum, **file_info},
        })
        print(f"locked {slug} {vnum}")

    CF_SIDES = {"ftb-quests-forge": "both", "ftb-teams-forge": "both",
                "ftb-library-forge": "both", "ftb-chunks-forge": "both",
                "ftb-xmod-compat": "both"}
    for slug, e in cf.items():
        if e.get("status") != "ok":
            raise SystemExit(f"CF audit entry not ok: {slug}")
        mods.append({
            "name": e["name"], "slug": slug, "side": CF_SIDES[slug],
            "optional": False, "default": True, "note": None, "source": "curseforge",
            "curseforge": {"project_id": e["mod_id"], "file_id": e["file_id"],
                           "filename": e["filename"], "fingerprint": e["fingerprint"]},
        })
        print(f"locked {slug} {e['filename']}")

    lock = {
        "pack": {"name": "Skyward Industry", "author": "Brady", "version": "0.1.0",
                 "minecraft": "1.21.1", "neoforge": "21.1.233"},
        "mods": mods,
    }
    out = ROOT / "tools/manifest.lock.json"
    out.write_text(json.dumps(lock, indent=2) + "\n", encoding="utf-8")
    print(f"\nwrote {out} with {len(mods)} mods")


if __name__ == "__main__":
    main()
