"""Convert a vanilla structure-template .nbt (the format createmod.com serves
for Create's schematicannon) into a WorldEdit-pasteable Sponge v2 .schem.

Usage:
  py tools/nbt2schem.py <file.nbt> [more.nbt ...]   -> writes <file>.schem beside it
  py tools/nbt2schem.py --selftest                  -> roundtrip sanity check

Caveats: block entities (chest contents, Create machine configs) are dropped;
blocks from mods not installed paste as air. Fine for static landmark builds.
"""
import gzip
import struct
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_schematics import write_schem, validate  # noqa: E402


# ---------------------------------------------------------------- NBT reader
def read_tag(b, pos, tid):
    if tid == 1:
        return b[pos], pos + 1
    if tid == 2:
        return struct.unpack(">h", b[pos:pos + 2])[0], pos + 2
    if tid == 3:
        return struct.unpack(">i", b[pos:pos + 4])[0], pos + 4
    if tid == 4:
        return struct.unpack(">q", b[pos:pos + 8])[0], pos + 8
    if tid == 5:
        return struct.unpack(">f", b[pos:pos + 4])[0], pos + 4
    if tid == 6:
        return struct.unpack(">d", b[pos:pos + 8])[0], pos + 8
    if tid == 7:
        n = struct.unpack(">i", b[pos:pos + 4])[0]
        return bytes(b[pos + 4:pos + 4 + n]), pos + 4 + n
    if tid == 8:
        n = struct.unpack(">H", b[pos:pos + 2])[0]
        return b[pos + 2:pos + 2 + n].decode("utf-8"), pos + 2 + n
    if tid == 9:
        etype = b[pos]
        n = struct.unpack(">i", b[pos + 1:pos + 5])[0]
        pos += 5
        out = []
        for _ in range(n):
            v, pos = read_tag(b, pos, etype)
            out.append(v)
        return out, pos
    if tid == 10:
        d = {}
        while True:
            t = b[pos]
            pos += 1
            if t == 0:
                return d, pos
            n = struct.unpack(">H", b[pos:pos + 2])[0]
            name = b[pos + 2:pos + 2 + n].decode("utf-8")
            pos += 2 + n
            d[name], pos = read_tag(b, pos, t)
    if tid == 11:
        n = struct.unpack(">i", b[pos:pos + 4])[0]
        vals = struct.unpack(f">{n}i", b[pos + 4:pos + 4 + 4 * n])
        return list(vals), pos + 4 + 4 * n
    if tid == 12:
        n = struct.unpack(">i", b[pos:pos + 4])[0]
        vals = struct.unpack(f">{n}q", b[pos + 4:pos + 4 + 8 * n])
        return list(vals), pos + 4 + 8 * n
    raise ValueError(f"unhandled NBT tag {tid}")


def read_nbt_file(path):
    raw = Path(path).read_bytes()
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    assert raw[0] == 10, "expected compound root"
    n = struct.unpack(">H", raw[1:3])[0]
    root, _ = read_tag(raw, 3 + n, 10)
    return root


# ---------------------------------------------------------------- conversion
def state_string(entry):
    name = entry["Name"]
    props = entry.get("Properties", {})
    if not props:
        return name
    inner = ",".join(f"{k}={v}" for k, v in sorted(props.items()))
    return f"{name}[{inner}]"


def convert(path):
    root = read_nbt_file(path)
    if "size" not in root:  # some files nest under an unnamed/named wrapper
        for v in root.values():
            if isinstance(v, dict) and "size" in v:
                root = v
                break
    sx, sy, sz = root["size"]
    palette = [state_string(e) for e in root["palette"]]
    grid = {}
    for blk in root["blocks"]:
        x, y, z = blk["pos"]
        state = palette[blk["state"]]
        if state == "minecraft:air":
            continue
        grid[(x, y, z)] = state
    out = Path(path).with_suffix(".schem")
    write_schem(out, grid, sx, sy, sz)
    validate(out, sx, sy, sz)
    print(f"  {Path(path).name}: {sx}x{sy}x{sz}, {len(grid)} blocks, "
          f"{len(set(grid.values()))} distinct states -> {out.name}")
    return out


# ---------------------------------------------------------------- selftest
def _nbt_str(s):
    b = s.encode()
    return struct.pack(">H", len(b)) + b


def selftest(tmpdir):
    # hand-build a tiny 2x1x1 structure nbt: stone + oak_stairs[facing=east]
    def tag(tid, name, payload):
        return bytes([tid]) + _nbt_str(name) + payload

    def t_int(v):
        return struct.pack(">i", v)

    def int_list(vals):
        return bytes([3]) + struct.pack(">i", len(vals)) + b"".join(t_int(v) for v in vals)

    pal0 = tag(8, "Name", _nbt_str("minecraft:stone")) + b"\x00"
    props = tag(10, "Properties", tag(8, "facing", _nbt_str("east")) + b"\x00")
    pal1 = tag(8, "Name", _nbt_str("minecraft:oak_stairs")) + props + b"\x00"
    palette = bytes([10]) + struct.pack(">i", 2) + pal0 + pal1
    blk0 = tag(9, "pos", int_list([0, 0, 0])) + tag(3, "state", t_int(0)) + b"\x00"
    blk1 = tag(9, "pos", int_list([1, 0, 0])) + tag(3, "state", t_int(1)) + b"\x00"
    blocks = bytes([10]) + struct.pack(">i", 2) + blk0 + blk1
    raw = bytes([10]) + _nbt_str("") + (
        bytes([9]) + _nbt_str("size") + int_list([2, 1, 1])
        + bytes([9]) + _nbt_str("palette") + palette
        + bytes([9]) + _nbt_str("blocks") + blocks
        + bytes([3]) + _nbt_str("DataVersion") + t_int(3955)
        + b"\x00")
    p = Path(tmpdir) / "selftest.nbt"
    p.write_bytes(gzip.compress(raw))
    out = convert(p)
    root = read_nbt_file_schem_check(out)
    assert root["Width"] == 2 and "minecraft:oak_stairs[facing=east]" in root["Palette"]
    print("selftest OK")


def read_nbt_file_schem_check(path):
    raw = gzip.open(path, "rb").read()
    n = struct.unpack(">H", raw[1:3])[0]
    root, _ = read_tag(raw, 3 + n, 10)
    return root


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
    elif sys.argv[1] == "--selftest":
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            selftest(td)
    else:
        for f in sys.argv[1:]:
            convert(f)
