"""Generate the Crossing destination as a single paste-ready schematic.

One paste, one origin: every loot chest's offset is recorded relative to the
schematic's min corner (marked with a LODESTONE at local 0,0,0) and written
into datapacks/skyward/data/skyward/function/bind_loot.mcfunction, so binding
all loot tables is one /execute positioned ... run function command.

Deterministic (fixed seed). Output:
  admin_assets/schematics/crossing_island.schem
  datapacks/skyward/data/skyward/function/bind_loot.mcfunction
"""
import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_schematics import write_schem, validate, box  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "admin_assets/schematics"
FUNC = ROOT / "datapacks/skyward/data/skyward/function/bind_loot.mcfunction"

W, H, L = 128, 72, 128
CX, CZ = 64, 64
R = 50
SEED = 20260610
rng = random.Random(SEED)

# ------------------------------------------------------------- value noise
def make_noise(cell):
    pts = {}
    r = random.Random(rng.random())
    def n(x, z):
        gx, gz = x / cell, z / cell
        x0, z0 = int(gx), int(gz)
        fx, fz = gx - x0, gz - z0
        def p(ix, iz):
            if (ix, iz) not in pts:
                pts[(ix, iz)] = r.random()
            return pts[(ix, iz)]
        a = p(x0, z0) * (1 - fx) + p(x0 + 1, z0) * fx
        b = p(x0, z0 + 1) * (1 - fx) + p(x0 + 1, z0 + 1) * fx
        return a * (1 - fz) + b * fz
    return n

n_shape = make_noise(34)
n_top = make_noise(18)
n_depth = make_noise(26)
n_vein = make_noise(7)
n_flora = make_noise(9)


def cell_hash(x, y, z):
    return random.Random((x * 73856093) ^ (y * 19349663) ^ (z * 83492791) ^ SEED).random()


# ------------------------------------------------------------- terrain fields
top = [[0] * L for _ in range(W)]
bot = [[0] * L for _ in range(W)]
inside = [[False] * L for _ in range(W)]

for x in range(W):
    for z in range(L):
        d = math.hypot(x - CX, z - CZ)
        rad = R * (0.72 + 0.34 * n_shape(x, z))
        if d >= rad:
            continue
        e = d / rad  # 0 center -> 1 edge
        inside[x][z] = True
        t = 40 + int(7 * (1 - e * e)) + int(5 * n_top(x, z))
        depth = 4 + (1 - e) ** 1.4 * (16 + 22 * n_depth(x, z))
        b = max(4, int(t - depth))
        top[x][z], bot[x][z] = t, b


def ground(x, z):
    return top[x][z] if 0 <= x < W and 0 <= z < L and inside[x][z] else None


grid = {}
manifest = []  # (label, x, y, z, loot_table)

for x in range(W):
    for z in range(L):
        if not inside[x][z]:
            continue
        t, b = top[x][z], bot[x][z]
        for y in range(b, t + 1):
            if y == t:
                state = "minecraft:grass_block"
            elif y >= t - 2:
                state = "minecraft:dirt"
            elif y <= b + 1:
                state = "minecraft:cobbled_deepslate"
            else:
                h = cell_hash(x, y, z)
                state = "minecraft:tuff" if h < 0.18 else ("minecraft:stone" if h < 0.34 else "minecraft:deepslate")
                # teal veins near the cliff band
                e = math.hypot(x - CX, z - CZ) / (R * 1.06)
                if e > 0.62 and n_vein(x + y * 3, z - y * 2) > 0.80:
                    state = "minecraft:oxidized_copper"
            grid[(x, y, z)] = state

# surface flora: warped patches where the stone "glows", scattered roots/ferns
for x in range(W):
    for z in range(L):
        if not inside[x][z]:
            continue
        t = top[x][z]
        f = n_flora(x, z)
        if f > 0.78:
            grid[(x, t, z)] = "minecraft:warped_nylium"
            if cell_hash(x, t + 1, z) < 0.45:
                grid[(x, t + 1, z)] = "minecraft:warped_roots"
        elif cell_hash(x, t + 1, z) < 0.05:
            grid[(x, t + 1, z)] = "minecraft:fern"

# embedded aetherium blocks (mineable bonus). Kept scarce on purpose: each
# block is 9 aetherium, and loot is meant to stay the primary source.
cliff_cells = [(x, z) for x in range(W) for z in range(L)
               if inside[x][z] and top[x][z] - bot[x][z] > 8
               and math.hypot(x - CX, z - CZ) > R * 0.35]
rng.shuffle(cliff_cells)
for x, z in cliff_cells[:3]:
    y = rng.randrange(bot[x][z] + 3, top[x][z] - 4)
    grid[(x, y, z)] = "kubejs:aetherium_block"

# ------------------------------------------------------------- the wreck (east rim)
WX, WZ = 98, 60
wy = (ground(WX, WZ) or 44) + 1
hull = "createdeco:copper_hull"
deck = "minecraft:stripped_spruce_log[axis=x]"
# two broken hull segments, second one listing a block lower and skewed
for seg, (ox, oz, oy, ln) in enumerate([(0, 0, 0, 9), (11, 2, -1, 6)]):
    x0, z0, y0 = WX + ox, WZ + oz, wy + oy
    box(grid, x0, y0, z0, x0 + ln, y0, z0 + 4, hull)
    box(grid, x0, y0 + 1, z0, x0 + ln, y0 + 1, z0, hull)
    box(grid, x0, y0 + 1, z0 + 4, x0 + ln, y0 + 1, z0 + 4, hull)
    box(grid, x0, y0 + 1, z0 + 1, x0 + ln, y0 + 1, z0 + 3, deck)
    # rip the hulls open
    for _ in range(7 + seg * 3):
        bx = x0 + rng.randrange(ln + 1)
        bz = z0 + rng.randrange(5)
        grid[(bx, y0 + 1, bz)] = "minecraft:air"
# mast stub + collapsed mast
box(grid, WX + 4, wy + 2, WZ + 2, WX + 4, wy + 4, WZ + 2, "minecraft:stripped_spruce_log[axis=y]")
box(grid, WX + 5, wy + 2, WZ + 3, WX + 9, wy + 2, WZ + 3, "minecraft:stripped_spruce_log[axis=x]")
# deflated envelope draped over the rocks north of the hull
for dx in range(-2, 9):
    for dz in range(-7, -1):
        if cell_hash(dx, 9, dz) < 0.78:
            gx, gz = WX + dx, WZ + dz
            gy = ground(gx, gz)
            if gy:
                grid[(gx, gy + 1, gz)] = "minecraft:white_wool" if cell_hash(dx, 1, dz) < 0.7 else "minecraft:light_gray_wool"
# landfall chest in the forward hold
grid[(WX + 2, wy + 1, WZ + 2)] = "minecraft:chest[facing=west]"
manifest.append(("landfall (wreck hold)", WX + 2, wy + 1, WZ + 2, "skyward:chests/crossing_landfall"))

# ------------------------------------------------------------- breadcrumb path wreck -> ruin
RX, RZ = 46, 66
steps = 64
for i in range(steps + 1):
    f = i / steps
    px = int(WX + (RX - WX) * f + 3 * math.sin(f * 9))
    pz = int(WZ + (RZ - WZ) * f + 3 * math.cos(f * 7))
    for dx in (-1, 0, 1):
        for dz in (-1, 0, 1):
            gx, gz = px + dx, pz + dz
            gy = ground(gx, gz)
            if gy and cell_hash(gx, 7, gz) < 0.6:
                grid[(gx, gy, gz)] = "minecraft:gravel" if cell_hash(gx, 8, gz) < 0.5 else "minecraft:mossy_cobblestone"
                if (gx, gy + 1, gz) in grid:
                    grid[(gx, gy + 1, gz)] = "minecraft:air"  # clear flora off the path

# ------------------------------------------------------------- ruin tower + vault
ry = (ground(RX, RZ) or 44) + 1
RAD = 6
for ang in range(0, 360, 3):
    a = math.radians(ang)
    tx = int(round(RX + math.cos(a) * RAD))
    tz = int(round(RZ + math.sin(a) * RAD))
    # broken crown: height varies around the ring, lowest at the south breach
    hgt = 4 + int(9 * (0.5 + 0.5 * math.sin(a * 2 + 1.2)) * cell_hash(tx, 0, tz))
    if 150 < ang < 210:
        hgt = min(hgt, 2)  # doorway breach, south side
    for y in range(hgt):
        h = cell_hash(tx, y, tz)
        state = ("minecraft:cracked_deepslate_bricks" if h < 0.3
                 else "minecraft:deepslate_bricks" if h < 0.85
                 else "minecraft:mossy_stone_bricks")
        grid[(tx, ry + y, tz)] = state
# interior floor + clear interior
for dx in range(-RAD + 1, RAD):
    for dz in range(-RAD + 1, RAD):
        if dx * dx + dz * dz <= (RAD - 1) ** 2:
            gx, gz = RX + dx, RZ + dz
            grid[(gx, ry - 1, gz)] = "minecraft:polished_deepslate"
            for y in range(ry, ry + 13):
                if (gx, y, gz) in grid:
                    grid[(gx, y, gz)] = "minecraft:air"
# glow ring fragments on the crown
for (gx, gz) in [(RX + RAD, RZ), (RX - RAD, RZ), (RX, RZ + RAD)]:
    gy = next((y for y in range(ry + 12, ry, -1) if (gx, y, gz) in grid and grid[(gx, y, gz)] != "minecraft:air"), None)
    if gy:
        grid[(gx, gy + 1, gz)] = "minecraft:sea_lantern"

# stairwell down: 2x2 shaft at tower center, east wall holds ladders (visual only)
VY = ry - 12
for y in range(VY, ry):
    for (sx, sz) in [(RX, RZ), (RX + 1, RZ), (RX, RZ + 1), (RX + 1, RZ + 1)]:
        grid[(sx, y, sz)] = "minecraft:air"
    grid[(RX + 2, y, RZ)] = "minecraft:deepslate_tiles"
    grid[(RX + 2, y, RZ + 1)] = "minecraft:deepslate_tiles"
# vault chamber 11x5x9 south of the shaft
vx0, vz0 = RX - 5, RZ + 3
box(grid, vx0 - 1, VY - 1, vz0 - 1, vx0 + 11, VY + 5, vz0 + 9, "minecraft:deepslate_tiles")
box(grid, vx0, VY, vz0, vx0 + 10, VY + 4, vz0 + 8, "minecraft:air")
# connect shaft to vault
box(grid, RX, VY, RZ + 1, RX + 1, VY + 2, vz0, "minecraft:air")
box(grid, RX - 1, VY - 1, RZ + 1, RX + 2, VY - 1, vz0, "minecraft:deepslate_tiles")
# dais + vault chest + lighting (single aetherium centerpiece under the chest)
box(grid, vx0 + 4, VY, vz0 + 4, vx0 + 6, VY, vz0 + 5, "minecraft:polished_deepslate")
grid[(vx0 + 5, VY, vz0 + 4)] = "kubejs:aetherium_block"
grid[(vx0 + 5, VY + 1, vz0 + 4)] = "minecraft:chest[facing=north]"
manifest.append(("vault (under ruin)", vx0 + 5, VY + 1, vz0 + 4, "skyward:chests/crossing_vault"))
for (lx, lz) in [(vx0, vz0), (vx0 + 10, vz0), (vx0, vz0 + 8), (vx0 + 10, vz0 + 8)]:
    grid[(lx, VY + 3, lz)] = "minecraft:sea_lantern"

# ------------------------------------------------------------- cache barrels (8)
cache_spots = [
    ("wreck stern", WX + 13, WZ + 4),
    ("wreck beach", WX - 4, WZ - 5),
    ("path north", 86, 52),
    ("path mid", 74, 64),
    ("path south", 60, 72),
    ("ruin perimeter E", RX + 9, RZ - 2),
    ("ruin perimeter W", RX - 9, RZ + 5),
    ("under-ledge", 64, 92),
]
for label, cx, cz in cache_spots:
    gy = ground(cx, cz)
    if gy is None:  # snap inward until on the island
        for k in range(1, 30):
            nx = cx + (1 if cx < CX else -1) * k
            nz = cz + (1 if cz < CZ else -1) * k
            gy = ground(nx, nz)
            if gy:
                cx, cz = nx, nz
                break
    y = gy + 1
    if label == "under-ledge":  # tucked into the underside taper
        y = bot[cx][cz] + 1
        grid[(cx, y - 1, cz)] = "minecraft:deepslate_tiles"
    grid[(cx, y, cz)] = "minecraft:barrel[facing=up]"
    manifest.append((f"cache: {label}", cx, y, cz, "skyward:chests/crossing_cache"))

# anchor marker at local origin
grid[(0, 0, 0)] = "minecraft:lodestone"

# ------------------------------------------------------------- write + validate
path = OUT / "crossing_island.schem"
write_schem(path, grid, W, H, L)
validate(path, W, H, L)

lines = [
    "# Skyward: bind Crossing loot tables. Run ONCE, positioned at the paste",
    "# anchor (the lodestone = schematic min corner):",
    "#   /execute positioned <ax> <ay> <az> run function skyward:bind_loot",
]
for label, x, y, z, table in manifest:
    lines.append(f"data merge block ~{x} ~{y} ~{z} {{LootTable:\"{table}\"}}")
lines.append('tellraw @a {"text":"[Skyward] Crossing loot bound: '
             f'{len(manifest)} containers.","color":"aqua"}}')
FUNC.parent.mkdir(parents=True, exist_ok=True)
FUNC.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

print(f"manifest: {len(manifest)} loot containers")
for label, x, y, z, table in manifest:
    print(f"  ({x:3},{y:3},{z:3})  {table.split('/')[-1]:<18} {label}")
print(f"wrote {FUNC.relative_to(ROOT)}")
chest_states = sum(1 for s in grid.values() if s.startswith(("minecraft:chest", "minecraft:barrel")))
assert chest_states >= len(manifest), "container blocks missing from grid"
print(f"grid: {len(grid)} non-air blocks, {chest_states} containers present")

# ------------------------------------------------------------- preview PNGs
import struct as _st  # noqa: E402
import zlib as _zl  # noqa: E402

COLORS = {
    "minecraft:grass_block": (96, 144, 72), "minecraft:dirt": (121, 85, 58),
    "minecraft:deepslate": (70, 70, 76), "minecraft:stone": (125, 125, 125),
    "minecraft:tuff": (108, 110, 102), "minecraft:cobbled_deepslate": (52, 52, 58),
    "minecraft:oxidized_copper": (82, 162, 132), "minecraft:warped_nylium": (43, 114, 101),
    "minecraft:warped_roots": (20, 138, 124), "minecraft:fern": (110, 150, 80),
    "minecraft:gravel": (130, 127, 126), "minecraft:mossy_cobblestone": (100, 118, 92),
    "minecraft:deepslate_bricks": (80, 80, 86), "minecraft:cracked_deepslate_bricks": (66, 66, 72),
    "minecraft:mossy_stone_bricks": (95, 112, 88), "minecraft:polished_deepslate": (88, 88, 94),
    "minecraft:deepslate_tiles": (60, 60, 66), "minecraft:sea_lantern": (200, 230, 220),
    "minecraft:white_wool": (235, 235, 235), "minecraft:light_gray_wool": (160, 160, 160),
    "createdeco:copper_hull": (190, 110, 70), "minecraft:lodestone": (255, 255, 0),
    "kubejs:aetherium_block": (60, 240, 220), "minecraft:lantern": (250, 200, 120),
}
MARKERS = {"minecraft:chest": (255, 40, 40), "minecraft:barrel": (255, 150, 30)}
DEFAULT = (150, 120, 150)
SCALE = 4


def _png(path, px, w, h):
    rows = b"".join(b"\x00" + bytes(c for p in row for c in p) for row in px)

    def chunk(t, d):
        c = t + d
        return _st.pack(">I", len(d)) + c + _st.pack(">I", _zl.crc32(c))

    hdr = _st.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)
    path.write_bytes(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", hdr)
                     + chunk(b"IDAT", _zl.compress(rows, 9)) + chunk(b"IEND", b""))


def _color(state, y):
    base = next((c for k, c in MARKERS.items() if state.startswith(k)), None)
    if base:
        return base
    c = COLORS.get(state.split("[")[0], DEFAULT)
    f = 0.55 + 0.45 * (y / H)  # height shading
    return tuple(min(255, int(v * f)) for v in c)


PREV = ROOT / "admin_assets/previews"
PREV.mkdir(parents=True, exist_ok=True)
# top-down
img = [[(14, 16, 26)] * W for _ in range(L)]
for x in range(W):
    for z in range(L):
        for y in range(H - 1, -1, -1):
            s = grid.get((x, y, z))
            if s and s != "minecraft:air":
                img[z][x] = _color(s, y)
                break
big = [[img[z // SCALE][x // SCALE] for x in range(W * SCALE)] for z in range(L * SCALE)]
_png(PREV / "crossing_topdown.png", big, W * SCALE, L * SCALE)
# cross-section through the vault (z = 73)
ZS = 73
img2 = [[(14, 16, 26)] * W for _ in range(H)]
for x in range(W):
    for y in range(H):
        s = grid.get((x, y, ZS))
        if s and s != "minecraft:air":
            img2[H - 1 - y][x] = _color(s, y)
big2 = [[img2[r // SCALE][x // SCALE] for x in range(W * SCALE)] for r in range(H * SCALE)]
_png(PREV / "crossing_section_z73.png", big2, W * SCALE, H * SCALE)
print(f"previews: {PREV.relative_to(ROOT)}\\crossing_topdown.png + crossing_section_z73.png")
