# Memory Reading

Memory Reading recommends the next book from what matters to the user now—not only from what they read before.

The `find-next-book` skill combines the current request, relevant conversation context, available long-term memory, optional reading history, and verified book information. It returns one primary recommendation with a transparent “why now” explanation and a practical reading approach.

## Principles

- Current user intent overrides remembered preferences.
- Only memory relevant to choosing a book may be used.
- Book titles, authors, premises, and availability must be verified.
- The workflow must degrade honestly when memory or reading integrations are unavailable.
- Persistent memory is not updated without explicit user intent or host confirmation.

## Install as a Codex plugin

Add this repository as a plugin marketplace:

```bash
codex plugin marketplace add Fov6363/memory-reading-skill
```

Then open the plugin directory in the ChatGPT desktop app and install **Memory Reading**. Start a new task after installation.

## Install only the skill

Ask Codex:

```text
Use $skill-installer to install this GitHub skill:
https://github.com/Fov6363/memory-reading-skill/tree/main/plugins/memory-reading/skills/find-next-book
```

## Example prompts

- 根据你对我的相关记忆，推荐我现在最值得读的一本书。
- 我最近一直在处理团队沟通问题，下一本该读什么？
- 结合我的长期目标和微信读书记录，给我一个稳妥选择和一个探索选择。
- 不要给长书单，只推荐一本，并说明为什么是现在。

## Repository layout

```text
.agents/plugins/marketplace.json       Codex marketplace catalog
plugins/memory-reading/                Installable skills-only plugin
  .codex-plugin/plugin.json            Plugin manifest
  skills/find-next-book/               Portable Agent Skill
tests/                                 Trigger and structure checks
```

## Validate

```bash
python3 tests/validate.py
```

## License

MIT-0
