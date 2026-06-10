"""Cross-reference validator.

1. Builds the known-item universe from the jar lang dumps (docs/audit/jars/*_items.txt)
   plus kubejs items registered in startup_scripts/items.js.
2. Validates quest SNBT files: brace balance, unique quest IDs, dependencies resolve,
   every item/icon reference exists.
3. Validates server scripts: every modded item ID string exists.

Exit code 1 on any failure.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

RECIPE_TYPES = {
    "create:mixing", "create:compacting", "create:filling", "create:deploying",
    "create:cutting", "create:pressing", "create:sequenced_assembly",
    "create:mechanical_crafting", "create:crushing", "create:splashing",
    "create:milling", "create:emptying", "create:haunting", "create:item_application",
}
CHECK_NS = {"create", "aeronautics", "simulated", "aeroworks", "offroad",
            "numismatics", "kubejs"}


def known_items():
    items = set()
    for f in (ROOT / "docs/audit/jars").glob("*_items.txt"):
        for line in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^(item|block)\.([a-z_]+)\.([a-z0-9_]+)$", line.strip())
            if m:
                items.add(f"{m.group(2)}:{m.group(3)}")
    js = (ROOT / "kubejs/startup_scripts/items.js").read_text(encoding="utf-8")
    for m in re.finditer(r"event\.create\('([a-z0-9_]+)'\)", js):
        items.add(f"kubejs:{m.group(1)}")
    return items


def main():
    items = known_items()
    print(f"known item universe: {len(items)} ids")
    errors = []

    # --- quest files ---
    quest_ids = {}
    chapters = sorted((ROOT / "config/ftbquests/quests/chapters").glob("*.snbt"))
    all_refs = []  # (file, dep_or_item, value)
    for ch in chapters:
        text = ch.read_text(encoding="utf-8")
        if text.count("{") != text.count("}") or text.count("[") != text.count("]"):
            errors.append(f"{ch.name}: unbalanced braces/brackets")
        for m in re.finditer(r'\bid: "([0-9A-F]{16})"', text):
            qid = m.group(1)
            if qid in quest_ids:
                errors.append(f"{ch.name}: duplicate id {qid} (also in {quest_ids[qid]})")
            quest_ids[qid] = ch.name
        for m in re.finditer(r'"([0-9A-F]{16})"', text):
            pass  # collected below via dependencies blocks
        for m in re.finditer(r'dependencies: \[([^\]]*)\]', text):
            for d in re.findall(r'"([0-9A-F]{16})"', m.group(1)):
                all_refs.append((ch.name, "dep", d))
        for m in re.finditer(r'\b(?:item|icon): "([a-z_]+:[a-z0-9_/]+)"', text):
            all_refs.append((ch.name, "item", m.group(1)))

    for fname, kind, val in all_refs:
        if kind == "dep":
            if val not in quest_ids:
                errors.append(f"{fname}: dependency {val} does not exist")
        else:
            ns = val.split(":")[0]
            if ns in CHECK_NS and val not in items:
                errors.append(f"{fname}: unknown item {val}")

    # quest ids that only appear as task/reward subids start with 1/2 prefix; deps must
    # point at quest ids starting 0A-0F — sanity: warn if dep targets a task id
    for fname, kind, val in all_refs:
        if kind == "dep" and val[0] in "12":
            errors.append(f"{fname}: dependency {val} points at a task/reward id")

    # --- server + startup scripts ---
    for js in sorted(list((ROOT / "kubejs/server_scripts").glob("*.js"))
                     + list((ROOT / "kubejs/startup_scripts").glob("*.js"))):
        text = js.read_text(encoding="utf-8")
        for m in re.finditer(r"(?<!id: )'([a-z_]+:[a-z0-9_/]+)'", text):
            val = m.group(1)
            ns = val.split(":")[0]
            if ns not in CHECK_NS or "/" in val or val in RECIPE_TYPES:
                continue
            if val not in items:
                errors.append(f"{js.name}: unknown item {val}")
        # template-literal envelope ids
        if "envelope" in text:
            for color in ["white", "orange", "magenta", "light_blue", "yellow", "lime",
                          "pink", "gray", "light_gray", "cyan", "purple", "blue",
                          "brown", "green", "red", "black"]:
                if f"aeronautics:{color}_envelope" not in items:
                    errors.append(f"{js.name}: unknown envelope aeronautics:{color}_envelope")

    if errors:
        print("\nFAILURES:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print(f"OK: {len(chapters)} chapters, {len(quest_ids)} unique ids, "
          f"{sum(1 for r in all_refs if r[1] == 'dep')} deps, "
          f"{sum(1 for r in all_refs if r[1] == 'item')} item refs — all valid")


if __name__ == "__main__":
    main()
