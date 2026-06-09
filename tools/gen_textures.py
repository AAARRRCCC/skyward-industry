"""Generate 16x16 PNG textures for the pack's custom KubeJS items/blocks.

Pixel art is encoded as ASCII grids + per-texture palettes; PNGs are written
with zlib directly (no Pillow dependency). Deterministic output.
"""
import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ITEM_DIR = ROOT / "kubejs/assets/kubejs/textures/item"
BLOCK_DIR = ROOT / "kubejs/assets/kubejs/textures/block"

T = (0, 0, 0, 0)  # transparent


def png(path, grid, palette):
    rows = []
    for line in grid:
        row = bytearray([0])  # filter type 0
        for ch in line:
            r, g, b, a = palette.get(ch, T) if ch != "." else T
            row += bytes((r, g, b, a))
        rows.append(bytes(row))
    raw = b"".join(rows)

    def chunk(tag, data):
        c = tag + data
        return struct.pack(">I", len(data)) + c + struct.pack(">I", zlib.crc32(c))

    ihdr = struct.pack(">IIBBBBB", 16, 16, 8, 6, 0, 0, 0)
    out = (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr)
           + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(out)
    print(f"wrote {path.relative_to(ROOT)}")


# ---- calibrated shaft: steel rod, diagonal, with cyan calibration ticks ----
CALIBRATED_SHAFT = [
    "................",
    "..............kk",
    ".............ksk",
    "............kshk",
    "...........kshk.",
    "..........kshk..",
    ".........kshk...",
    "....c...kshk....",
    ".......kshk..c..",
    "......kshk......",
    ".....kshk.......",
    "....kshk........",
    "...kshk....c....",
    "..kshk..........",
    ".kkhk...........",
    ".kk.............",
]
P_SHAFT = {
    "k": (43, 47, 56, 255),     # dark outline
    "s": (142, 150, 162, 255),  # steel
    "h": (208, 214, 222, 255),  # highlight
    "c": (90, 220, 230, 255),   # calibration tick
}

# ---- tempered casing: brass frame, scorched edges ----
TEMPERED_CASING = [
    "................",
    ".dddddddddddddd.",
    ".dbbbbbbbbbbbbd.",
    ".dbgggggggggghd.",
    ".dbgddddddddghd.",
    ".dbgdssssssdghd.",
    ".dbgdswwwwsdghd.",
    ".dbgdswssssdghd.",
    ".dbgdswssssdghd.",
    ".dbgdssssssdghd.",
    ".dbgddddddddghd.",
    ".dbghhhhhhhhghd.",
    ".dbhhhhhhhhhhhd.",
    ".ddddddddddddhd.",
    ".dddddddddddddd.",
    "................",
]
P_CASING = {
    "d": (66, 44, 28, 255),     # scorched dark
    "b": (158, 110, 48, 255),   # brass dark
    "g": (196, 148, 66, 255),   # brass
    "h": (228, 186, 100, 255),  # brass light
    "s": (104, 78, 50, 255),    # inner shadow
    "w": (240, 220, 160, 255),  # heat glow
}

# ---- resonant coil: copper windings on a dark core ----
RESONANT_COIL = [
    "................",
    ".....kkkkkk.....",
    "...kkcccccckk...",
    "..kcchccchcck...",
    "..kchccchccck...",
    ".kcchccchcchck..",
    ".kchccchccchck..",
    ".kcdddddddddck..",
    ".kcdgggggggdck..",
    ".kcdddddddddck..",
    ".kchccchccchck..",
    ".kcchccchcchck..",
    "..kchccchccck...",
    "..kcchccchcck...",
    "...kkcccccckk...",
    ".....kkkkkk.....",
]
P_COIL = {
    "k": (40, 32, 30, 255),     # outline
    "c": (184, 102, 60, 255),   # copper
    "h": (232, 156, 96, 255),   # copper highlight
    "d": (60, 50, 46, 255),     # core dark
    "g": (255, 222, 120, 255),  # resonance glow
}

# ---- aetherium: luminous teal crystal shard ----
AETHERIUM = [
    "................",
    "......kk........",
    ".....kwtk.......",
    ".....kwttk......",
    "....kwtttak.....",
    "....kwttaak.....",
    "...kwtttaaak....",
    "...kwttaaaak....",
    "..kwtttaaaaak...",
    "..kwttaaaddak...",
    "..kttaaaddak....",
    "...ktaaddak.....",
    "...ktaddak......",
    "....kddak.......",
    ".....kdk........",
    "......k.........",
]
P_AETHERIUM = {
    "k": (20, 44, 52, 255),     # outline
    "w": (225, 255, 252, 255),  # bright facet
    "t": (120, 235, 220, 255),  # teal
    "a": (52, 180, 175, 255),   # deep teal
    "d": (28, 110, 120, 255),   # shadow facet
}

# ---- ship's log: weathered journal with ribbon ----
SHIPS_LOG = [
    "................",
    "..kkkkkkkkkkk...",
    ".kbbbbbbbbbbpk..",
    ".kbwwwwwwwwbpk..",
    ".kbwllllllwbpk..",
    ".kbwwwwwwwwbpk..",
    ".kbwllllwwwbpk..",
    ".kbwwwwwwwwbpk..",
    ".kbwllllllwbpk..",
    ".kbwwwwwwwwbpk..",
    ".kbwllwwwwwbpk..",
    ".kbwwwwwwwwbpk..",
    ".kbbbbbbbbbbpk..",
    ".krrkkkkkkkkk...",
    "..krr...........",
    "...k............",
]
P_LOG = {
    "k": (44, 32, 24, 255),     # outline
    "b": (122, 84, 50, 255),    # leather
    "p": (90, 60, 36, 255),     # spine shadow
    "w": (226, 210, 178, 255),  # parchment
    "l": (110, 100, 86, 255),   # faded ink
    "r": (160, 50, 44, 255),    # ribbon
}

# ---- aetherium block: tiled crystalline ----
AETHERIUM_BLOCK = [
    "kddddddkkddddddk",
    "dtaaaatddtaaaatd",
    "dawwtaadda tttad".replace(" ", "t"),
    "dataataddattatad",
    "dataataddatwttad",
    "dawttaadda ttaad".replace(" ", "t"),
    "dtaaaatddtaaaatd",
    "kddddddkkddddddk",
    "kddddddkkddddddk",
    "dtaaaatddtaaaatd",
    "dat ttaddawttaad".replace(" ", "w"),
    "dattataddataatad",
    "dawtataddataatad",
    "datttaaddawttaad",
    "dtaaaatddtaaaatd",
    "kddddddkkddddddk",
]
P_AETHERIUM_BLOCK = {
    "k": (16, 36, 44, 255),
    "d": (28, 92, 100, 255),
    "a": (52, 170, 165, 255),
    "t": (110, 225, 212, 255),
    "w": (215, 255, 250, 255),
}


def main():
    png(ITEM_DIR / "calibrated_shaft.png", CALIBRATED_SHAFT, P_SHAFT)
    png(ITEM_DIR / "tempered_casing.png", TEMPERED_CASING, P_CASING)
    png(ITEM_DIR / "resonant_coil.png", RESONANT_COIL, P_COIL)
    png(ITEM_DIR / "aetherium.png", AETHERIUM, P_AETHERIUM)
    for i in (1, 2, 3, 4):
        png(ITEM_DIR / f"ships_log_{i}.png", SHIPS_LOG, P_LOG)
    png(BLOCK_DIR / "aetherium_block.png", AETHERIUM_BLOCK, P_AETHERIUM_BLOCK)


if __name__ == "__main__":
    main()
