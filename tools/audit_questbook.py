"""Quest book flow audit (review-pass tool): reward-policy violations,
overlapping quest coordinates per chapter, dependency cycles."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
issues = []
all_deps = {}

for ch in sorted((ROOT / "config/ftbquests/quests/chapters").glob("*.snbt")):
    text = ch.read_text(encoding="utf-8")
    coords = re.findall(r"x: (-?[\d.]+)d\s+y: (-?[\d.]+)d", text)
    dups = {c for c in coords if coords.count(c) > 1}
    if dups:
        issues.append(f"{ch.name}: overlapping quest positions {sorted(dups)}")
    for rb in re.findall(r"rewards: \[(.*?)\]\n", text, re.S):
        for item in re.findall(r'item: "([a-z_]+:[a-z0-9_/]+)"', rb):
            if not item.startswith(("numismatics:", "minecraft:")):
                issues.append(f"{ch.name}: reward outside policy: {item}")
    # quest blocks: id + optional dependencies (deps listed before id in our style)
    for m in re.finditer(r'dependencies: \[([^\]]*)\][^{]*?id: "([0-9A-F]{16})"', text, re.S):
        all_deps[m.group(2)] = re.findall(r'"([0-9A-F]{16})"', m.group(1))

WHITE, GRAY, BLACK = 0, 1, 2
color = {k: WHITE for k in all_deps}


def visit(n):
    color[n] = GRAY
    for d in all_deps.get(n, []):
        if color.get(d) == GRAY:
            issues.append(f"dependency cycle involving {d} and {n}")
        elif color.get(d, BLACK) == WHITE:
            visit(d)
    color[n] = BLACK


for k in list(all_deps):
    if color[k] == WHITE:
        visit(k)

print(f"{len(all_deps)} quests with dependencies audited")
print("\n".join(issues) if issues else "ALL CLEAN: rewards in policy, no overlaps, no cycles")
raise SystemExit(1 if issues else 0)
