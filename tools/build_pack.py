"""Build the packwiz tree at pack/ from tools/manifest.lock.json + repo sources.

Replaces the packwiz binary (not runnable in this dev environment) with the same
on-disk format:
  1. writes pack/mods/<slug>.pw.toml for every locked mod
  2. syncs kubejs/ and config/ from the repo root into pack/ (delete + copy)
  3. regenerates pack/index.toml (sha256 of every file, metafile flag on .pw.toml)
  4. rewrites pack/pack.toml with the new index hash

`packwiz refresh` run by a human on the same tree is a no-op if this is correct.
"""
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACK = ROOT / "pack"
SYNC_DIRS = ["kubejs", "config", "defaultconfigs"]  # repo root -> pack/, if present


def toml_escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def write_pw_toml(mod):
    lines = [f'name = "{toml_escape(mod["name"])}"']
    if mod["source"] == "modrinth":
        m = mod["modrinth"]
        lines += [f'filename = "{m["filename"]}"', f'side = "{mod["side"]}"', ""]
        if mod["optional"]:
            lines += ["[option]", "\toptional = true",
                      f"\tdefault = {str(mod['default']).lower()}"]
            if mod.get("note"):
                lines += [f'\tdescription = "{toml_escape(mod["note"])}"']
            lines += [""]
        lines += ["[download]", f'\turl = "{m["url"]}"',
                  '\thash-format = "sha512"', f'\thash = "{m["sha512"]}"', ""]
        lines += ["[update]", "\t[update.modrinth]",
                  f'\t\tmod-id = "{m["project_id"]}"',
                  f'\t\tversion = "{m["version_id"]}"']
    else:
        c = mod["curseforge"]
        lines += [f'filename = "{c["filename"]}"', f'side = "{mod["side"]}"', ""]
        if mod["optional"]:
            lines += ["[option]", "\toptional = true",
                      f"\tdefault = {str(mod['default']).lower()}", ""]
        lines += ["[download]", '\thash-format = "murmur2"',
                  f'\thash = "{c["fingerprint"]}"',
                  '\tmode = "metadata:curseforge"', ""]
        lines += ["[update]", "\t[update.curseforge]",
                  f'\t\tfile-id = {c["file_id"]}',
                  f'\t\tproject-id = {c["project_id"]}']
    path = PACK / "mods" / f'{mod["slug"]}.pw.toml'
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return path


def sha256_file(path):
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def main():
    lock = json.loads((ROOT / "tools/manifest.lock.json").read_text(encoding="utf-8"))

    mods_dir = PACK / "mods"
    if mods_dir.exists():
        shutil.rmtree(mods_dir)
    mods_dir.mkdir(parents=True)
    for mod in lock["mods"]:
        write_pw_toml(mod)
    print(f"wrote {len(lock['mods'])} .pw.toml files")

    for d in SYNC_DIRS:
        src, dst = ROOT / d, PACK / d
        if dst.exists():
            shutil.rmtree(dst)
        if src.exists():
            shutil.copytree(src, dst)
            n = sum(1 for _ in dst.rglob("*") if _.is_file())
            print(f"synced {d}/ ({n} files)")

    # index.toml — every file under pack/ except pack.toml and index.toml itself
    entries = []
    for p in sorted(PACK.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(PACK).as_posix()
        if rel in ("pack.toml", "index.toml"):
            continue
        entries.append((rel, sha256_file(p), rel.endswith(".pw.toml")))
    out = ['hash-format = "sha256"', ""]
    for rel, h, meta in entries:
        out += ["[[files]]", f'\tfile = "{rel}"', f'\thash = "{h}"']
        if meta:
            out += ["\tmetafile = true"]
        out += [""]
    index = PACK / "index.toml"
    index.write_text("\n".join(out), encoding="utf-8", newline="\n")
    print(f"index.toml: {len(entries)} files")

    p = lock["pack"]
    pack_toml = "\n".join([
        f'name = "{p["name"]}"',
        f'author = "{p["author"]}"',
        f'version = "{p["version"]}"',
        'pack-format = "packwiz:1.1.0"',
        "",
        "[index]",
        '\tfile = "index.toml"',
        '\thash-format = "sha256"',
        f'\thash = "{sha256_file(index)}"',
        "",
        "[versions]",
        f'\tminecraft = "{p["minecraft"]}"',
        f'\tneoforge = "{p["neoforge"]}"',
        "",
    ])
    (PACK / "pack.toml").write_text(pack_toml, encoding="utf-8", newline="\n")
    print("pack.toml written")


if __name__ == "__main__":
    main()
