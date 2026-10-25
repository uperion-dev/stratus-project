# Shader context — generated locally

Navigation and fingerprints only; this file does not certify a release or authorise additional work.
Project: /Users/william.lei/Documents/ChatGPT/MC Shader Making
Active brief: /Users/william.lei/Documents/ChatGPT/MC Shader Making/work/Custom instructions/IN-PROGRESS/b9a03cf9-f681-4a16-8115-d8b44fd3525a/CHANGES.md
Target snapshot: /Users/william.lei/Documents/ChatGPT/MC Shader Making/work/Custom instructions/IN-PROGRESS/b9a03cf9-f681-4a16-8115-d8b44fd3525a/TASK.md
Brief SHA256: 042ef608d6ae6b1a3f3f080639c7d60953652e1fbb4833a582f69f60e48e60bc
Target SHA256: 71d69fbb75c4773616aed62f88b607cfb56f599e37c20e881dd6b7537266191a
Current shared TASK SHA256: 71d69fbb75c4773616aed62f88b607cfb56f599e37c20e881dd6b7537266191a
Current shader tree SHA256: f658e4ce29a551c7c2bb66fc5aaa252f58b92f3bd06e7ec36b2d453c11c27a3d (239 files)

## Read first
- Project AGENTS.md, work/Custom instructions/AGENTS.md, GOALS.md and WORKFLOW.md.
- RELEASE-ROADMAP.md guides release numbering; planned milestones are not extra implementation scope.
- Active brief and applicable TASK.md. Read unchanged documents once per context; use hashes to detect changes.
- PROGRESS.md, if resuming this batch. Recheck changed files and relevant runtime state before reusing evidence.
- Relative links copied into a batch brief resolve from work/Custom instructions, their original location.

## Target section index
- Line 1: Stratus — editable shader specification
- Line 5: Quick edit — major design choices
- Line 20: Full shader specification
- Line 22: Identity and reference
- Line 33: Terrain, lighting, sun and materials
- Line 48: Water
- Line 58: Lower clouds, cirrus and mist
- Line 72: Controls, presets and rendering
- Line 86: Packaging, testing and evidence

## Current source navigation hints
- outputs/Stratus/shaders/block.properties
- outputs/Stratus/shaders/shaders.properties
- outputs/Stratus/shaders/core/options.glsl
- outputs/Stratus/package.py and outputs/Stratus/install.py: existing release tooling.
Hints are filename matches only, not a diagnosis or a complete dependency list.

## Latest recorded release summary — reported evidence, not a live check
## 24 October 2026 — Stratus 1.7.0-rc2 — targeted repair candidate

### At a glance

- Repaired pale cave-water strips and native entity face shading; restored adjustable native underwater atlas; made foliage matte and reduced the excessive solar film lobe. All65 controls/defaults/ranges/menu paths and preset assignments preserved.
- **[Candidate ZIP](../../outputs/Stratus-1.7.0-rc2.zip)** installed and actually test-loaded in Main, with exact source/archive/install bytes and all65 Reference values verified. [Install/load receipt](../../outputs/Stratus-1.7.0-rc2-install.json), [24 reviewed comparisons](../../outputs/Stratus-1.7.0-rc2-visual-checks/index.html).
-768 final native pairs, targeted GPU checks and13 migration checks pass. Finite visual acceptance only; additional solid-occluder, solar-angle and waterline/glass checks remain pending. Focused FPS explicitly skipped; no sustained-lag fix or60FPS claim. Original session and temporary test world edits restored and verified.

Batch: [1af89474 active brief](IN-PROGRESS/1af89474-f56a-4419-bc73-7f12d4950cfa/CHANGES.md). Frozen delta only reiterated the recorded stable/candidate reference distinction; no extra shader behaviour staged. Shared next queue and immutable target snapshot unchanged. TASK, shared queue, change log and completed archive matched initial fingerprints before reconciliation; the active brief differed only by this run's staging. No newer-edit conflict found. Earlier pending batches remain separate.


For earlier evidence, search the exact version or issue in CHANGE-LOG.md; do not dump its entire history.
