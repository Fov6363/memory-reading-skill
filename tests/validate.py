#!/usr/bin/env python3
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "memory-reading"
SKILL = PLUGIN / "skills" / "find-next-book"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
frontmatter = re.match(r"^---\n(.*?)\n---\n", skill_text, re.DOTALL)
require(frontmatter is not None, "SKILL.md must start with YAML frontmatter")
require("name: find-next-book" in frontmatter.group(1), "Unexpected skill name")
require("description:" in frontmatter.group(1), "Skill description is required")
require("TODO" not in skill_text, "Skill contains a TODO placeholder")

for relative in re.findall(r"\((references/[^)]+)\)", skill_text):
    require((SKILL / relative).is_file(), f"Missing referenced file: {relative}")

plugin = json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
require(plugin["name"] == "memory-reading", "Unexpected plugin name")
require(re.fullmatch(r"\d+\.\d+\.\d+", plugin["version"]) is not None, "Invalid plugin version")
require((PLUGIN / plugin["skills"]).is_dir(), "Plugin skills path does not exist")

marketplace_path = ROOT / ".agents" / "plugins" / "marketplace.json"
marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
require(marketplace["name"] == "memory-reading", "Unexpected marketplace name")
entries = [entry for entry in marketplace["plugins"] if entry["name"] == plugin["name"]]
require(len(entries) == 1, "Marketplace must contain exactly one memory-reading entry")
entry = entries[0]
require(entry["policy"]["installation"] == "AVAILABLE", "Unexpected install policy")
require(entry["policy"]["authentication"] == "ON_INSTALL", "Unexpected auth policy")
source = (ROOT / entry["source"]["path"]).resolve()
require(source == PLUGIN.resolve(), "Marketplace source path does not resolve to the plugin")

cases = json.loads((ROOT / "tests" / "cases.json").read_text(encoding="utf-8"))
require(len(cases["positive"]) == 5, "Expected exactly five positive cases")
require(len(cases["negative"]) == 3, "Expected exactly three negative cases")

print("Validated memory-reading plugin, find-next-book skill, marketplace, and 8 trigger cases.")
