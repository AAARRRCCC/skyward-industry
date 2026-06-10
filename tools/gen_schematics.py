"""Generate WorldEdit-pasteable .schem files (Sponge schematic v2) for the
pack's commercial architecture: market stalls + vendor kiosk.

Conventions baked into every schematic:
  - GOLD BLOCK marks where a Numismatics vendor goes (replace by hand).
  - Pastes include a floor layer; use //paste -a (skip air) on level ground.
Output: admin_assets/schematics/*.schem  (copy into config/worldedit/schematics/)

Validated by re-parsing each file after write (gzip + NBT + dims + palette).
"""
import gzip
import io
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "admin_assets/schematics"
DATA_VERSION = 3955  # 1.21.1


# ---------------------------------------------------------------- NBT writing
def _str(s):
    b = s.encode("utf-8")
    return struct.pack(">H", len(b)) + b


def tag(tid, name, payload):
    return bytes([tid]) + _str(name) + payload


def t_short(v):
    return struct.pack(">h", v)


def t_int(v):
    return struct.pack(">i", v)


def varint(v):
    out = bytearray()
    while True:
        b = v & 0x7F
        v >>= 7
        if v:
            out.append(b | 0x80)
        else:
            out.append(b)
            return bytes(out)


def write_schem(path, grid, width, height, length):
    """grid: dict[(x,y,z)] = blockstate string; air implied elsewhere."""
    palette = {"minecraft:air": 0}
    for state in grid.values():
        palette.setdefault(state, len(palette))
    blockdata = bytearray()
    for y in range(height):
        for z in range(length):
            for x in range(width):
                blockdata += varint(palette.get(grid.get((x, y, z), "minecraft:air"), 0))

    pal_payload = b"".join(tag(3, state, t_int(idx)) for state, idx in palette.items()) + b"\x00"
    inner = (
        tag(3, "Version", t_int(2))
        + tag(3, "DataVersion", t_int(DATA_VERSION))
        + tag(2, "Width", t_short(width))
        + tag(2, "Height", t_short(height))
        + tag(2, "Length", t_short(length))
        + tag(3, "PaletteMax", t_int(len(palette)))
        + tag(10, "Palette", pal_payload)
        + tag(7, "BlockData", t_int(len(blockdata)) + bytes(blockdata))
        + b"\x00"
    )
    raw = tag(10, "Schematic", inner)
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wb") as f:
        f.write(raw)


# ---------------------------------------------------------------- NBT reading (validation)
def _read_nbt(b, pos, tid):
    if tid == 2:
        return struct.unpack(">h", b[pos:pos + 2])[0], pos + 2
    if tid == 3:
        return struct.unpack(">i", b[pos:pos + 4])[0], pos + 4
    if tid == 7:
        n = struct.unpack(">i", b[pos:pos + 4])[0]
        return b[pos + 4:pos + 4 + n], pos + 4 + n
    if tid == 8:
        n = struct.unpack(">H", b[pos:pos + 2])[0]
        return b[pos + 2:pos + 2 + n].decode(), pos + 2 + n
    if tid == 10:
        d = {}
        while True:
            t = b[pos]
            pos += 1
            if t == 0:
                return d, pos
            n = struct.unpack(">H", b[pos:pos + 2])[0]
            name = b[pos + 2:pos + 2 + n].decode()
            pos += 2 + n
            d[name], pos = _read_nbt(b, pos, t)
    raise ValueError(f"unhandled tag {tid}")


def validate(path, width, height, length):
    raw = gzip.open(path, "rb").read()
    assert raw[0] == 10
    n = struct.unpack(">H", raw[1:3])[0]
    root, _ = _read_nbt(raw, 3 + n, 10)
    assert root["Version"] == 2 and root["DataVersion"] == DATA_VERSION
    assert (root["Width"], root["Height"], root["Length"]) == (width, height, length)
    assert len(root["Palette"]) == root["PaletteMax"]
    print(f"  OK {path.name}: {width}x{height}x{length}, {root['PaletteMax']} palette entries")


# ---------------------------------------------------------------- builds
def box(grid, x1, y1, z1, x2, y2, z2, state):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                grid[(x, y, z)] = state


def market_stall(awning):
    """7w x 6l x 6h stall. Front (counter + awning overhang) faces SOUTH (-z edge
    of the paste, i.e. toward the player if you stand south of the paste point).
    Gold block on the counter = vendor position."""
    g = {}
    W, L = 7, 6
    # floor: polished andesite with spruce border
    box(g, 0, 0, 0, W - 1, 0, L - 1, "minecraft:spruce_planks")
    box(g, 1, 0, 1, W - 2, 0, L - 2, "minecraft:polished_andesite")
    # corner posts
    for (x, z) in [(0, 0), (W - 1, 0), (0, L - 1), (W - 1, L - 1)]:
        box(g, x, 1, z, x, 3, z, "minecraft:stripped_spruce_log")
    # counter across the front (z=1), gap-free between posts
    box(g, 1, 1, 1, W - 2, 1, 1, "minecraft:spruce_planks")
    for x in range(1, W - 1):
        g[(x, 2, 1)] = "minecraft:spruce_slab[type=bottom]"
    # vendor marker: centered ON the counter (replace with creative vendor)
    g[(3, 2, 1)] = "minecraft:gold_block"
    # back wall with stock shelves
    box(g, 1, 1, L - 1, W - 2, 3, L - 1, "minecraft:spruce_planks")
    for x in (2, 3, 4):
        g[(x, 1, L - 2)] = "minecraft:barrel[facing=up]"
    # side rails
    for z in range(1, L - 1):
        g[(0, 1, z)] = "minecraft:spruce_fence"
        g[(W - 1, 1, z)] = "minecraft:spruce_fence"
    # awning: striped wool, sloped one step, overhanging the counter by 1
    white = "minecraft:white_wool"
    for x in range(0, W):
        stripe = awning if x % 2 == 0 else white
        g[(x, 5, 0)] = stripe          # front overhang row (high)
        g[(x, 5, 1)] = stripe
        g[(x, 4, 2)] = stripe          # step down
        g[(x, 4, 3)] = stripe
        g[(x, 4, 4)] = stripe
        g[(x, 4, 5)] = stripe
    # hanging lanterns under the front overhang
    g[(1, 4, 0)] = "minecraft:lantern[hanging=true]"
    g[(5, 4, 0)] = "minecraft:lantern[hanging=true]"
    return g, W, 6, L


def vendor_kiosk():
    """3x3 footprint single-vendor kiosk, front faces south."""
    g = {}
    box(g, 0, 0, 0, 2, 0, 2, "minecraft:spruce_planks")
    for (x, z) in [(0, 0), (2, 0), (0, 2), (2, 2)]:
        box(g, x, 1, z, x, 2, z, "minecraft:stripped_spruce_log")
    g[(1, 1, 0)] = "minecraft:spruce_planks"
    g[(1, 2, 0)] = "minecraft:gold_block"          # vendor on the counter
    g[(1, 1, 2)] = "minecraft:barrel[facing=up]"
    box(g, 0, 3, 0, 2, 3, 2, "minecraft:spruce_slab[type=bottom]")
    g[(1, 3, 1)] = "minecraft:lantern"
    return g, 3, 4, 3


def industrial_stall(metal, accent_floor):
    """7w x 6l x 6h industrial stall (Create / Create Deco palette). Front faces
    SOUTH. Gold block on the counter = vendor position.
    metal: createdeco material prefix ('industrial_iron', 'copper', 'andesite')."""
    g = {}
    W, L = 7, 6
    support = f"createdeco:{metal}_support"
    hull = f"createdeco:{metal}_hull"
    sheet = f"createdeco:{metal}_sheet_metal"
    catwalk = f"createdeco:{metal}_catwalk"
    # floor: industrial iron border, accent center
    box(g, 0, 0, 0, W - 1, 0, L - 1, "create:industrial_iron_block")
    box(g, 1, 0, 1, W - 2, 0, L - 2, accent_floor)
    # corner posts
    for (x, z) in [(0, 0), (W - 1, 0), (0, L - 1), (W - 1, L - 1)]:
        box(g, x, 1, z, x, 4, z, support)
    # counter across the front: hull blocks with a smooth stone work surface
    box(g, 1, 1, 1, W - 2, 1, 1, hull)
    for x in range(1, W - 1):
        g[(x, 2, 1)] = "minecraft:smooth_stone_slab[type=bottom]"
    g[(3, 2, 1)] = "minecraft:gold_block"          # vendor position
    # back wall: sheet metal, barrels + crate shelf
    box(g, 1, 1, L - 1, W - 2, 3, L - 1, sheet)
    for x in (2, 3, 4):
        g[(x, 1, L - 2)] = "minecraft:barrel[facing=up]"
    g[(1, 1, L - 2)] = "create:andesite_casing"
    g[(5, 1, L - 2)] = "create:andesite_casing"
    # side rails: girders read as exposed steel frame
    for z in (2, 3):
        g[(0, 1, z)] = "create:metal_girder"
        g[(W - 1, 1, z)] = "create:metal_girder"
    # flat catwalk canopy with a one-block front overhang
    for x in range(0, W):
        for z in range(0, L):
            g[(x, 5, z)] = catwalk
    # hanging lanterns at the front corners
    g[(1, 4, 0)] = "minecraft:lantern[hanging=true]"
    g[(5, 4, 0)] = "minecraft:lantern[hanging=true]"
    return g, W, 6, L


def industrial_kiosk():
    """3x3 single-vendor kiosk, industrial palette, front faces south."""
    g = {}
    box(g, 0, 0, 0, 2, 0, 2, "create:industrial_iron_block")
    for (x, z) in [(0, 0), (2, 0), (0, 2), (2, 2)]:
        box(g, x, 1, z, x, 2, z, "createdeco:industrial_iron_support")
    g[(1, 1, 0)] = "createdeco:industrial_iron_hull"
    g[(1, 2, 0)] = "minecraft:gold_block"          # vendor on the counter
    g[(1, 1, 2)] = "minecraft:barrel[facing=up]"
    box(g, 0, 3, 0, 2, 3, 2, "createdeco:industrial_iron_catwalk")
    g[(1, 3, 1)] = "minecraft:lantern"
    return g, 3, 4, 3


AWNINGS = {
    "market_stall_red": "minecraft:red_wool",
    "market_stall_lime": "minecraft:lime_wool",
    "market_stall_blue": "minecraft:blue_wool",
    "market_stall_yellow": "minecraft:yellow_wool",
}
INDUSTRIAL = {
    "industrial_stall_iron": ("industrial_iron", "minecraft:polished_andesite"),
    "industrial_stall_copper": ("copper", "minecraft:oxidized_cut_copper"),
    "industrial_stall_andesite": ("andesite", "minecraft:polished_andesite"),
}


def main():
    for name, wool in AWNINGS.items():
        g, w, h, l = market_stall(wool)
        p = OUT / f"{name}.schem"
        write_schem(p, g, w, h, l)
        validate(p, w, h, l)
    for name, (metal, floor) in INDUSTRIAL.items():
        g, w, h, l = industrial_stall(metal, floor)
        p = OUT / f"{name}.schem"
        write_schem(p, g, w, h, l)
        validate(p, w, h, l)
    g, w, h, l = vendor_kiosk()
    p = OUT / "vendor_kiosk.schem"
    write_schem(p, g, w, h, l)
    validate(p, w, h, l)
    g, w, h, l = industrial_kiosk()
    p = OUT / "industrial_kiosk.schem"
    write_schem(p, g, w, h, l)
    validate(p, w, h, l)
    print("done")


if __name__ == "__main__":
    main()
