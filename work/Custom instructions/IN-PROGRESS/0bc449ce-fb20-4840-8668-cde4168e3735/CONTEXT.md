# Shader context — generated locally

Navigation and fingerprints only; this file does not certify a release or authorise additional work.
Project: /Users/william.lei/Documents/ChatGPT/MC Shader Making
Active brief: /Users/william.lei/Documents/ChatGPT/MC Shader Making/work/Custom instructions/IN-PROGRESS/0bc449ce-fb20-4840-8668-cde4168e3735/CHANGES.md
Target snapshot: /Users/william.lei/Documents/ChatGPT/MC Shader Making/work/Custom instructions/IN-PROGRESS/0bc449ce-fb20-4840-8668-cde4168e3735/TASK.md
Brief SHA256: c34166a1618f4a1ba40e3ae1028cb75d2bffe78fe71d96b2ae28be1dc7089b8d
Target SHA256: b8d0719b52758cf4e1402fe02ddec320944f5fa262b62f6b0d9553b2ae28accb
Current shared TASK SHA256: b8d0719b52758cf4e1402fe02ddec320944f5fa262b62f6b0d9553b2ae28accb
Current shader tree SHA256: 22791013348c7a1500e2d7ebc3c558467b48646fc10834ea1478b407dd8c19c6 (240 files)

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
- Line 87: Packaging, testing and evidence

## Current source navigation hints
- outputs/Stratus/shaders/shaders.properties
- outputs/Stratus/shaders/core/frame.glsl
- outputs/Stratus/shaders/core/medium.glsl
- outputs/Stratus/shaders/core/options.glsl
- outputs/Stratus/package.py and outputs/Stratus/install.py: existing release tooling.
Hints are filename matches only, not a diagnosis or a complete dependency list.

## Latest recorded release summary — reported evidence, not a live check
## 25 October 2026 — Stratus 1.7.0-rc3 — exposed foliage and temporal sky candidate

### At a glance

- Restored film on exposed front-facing foliage; backward leaf planes stay dry. Added guarded one-frame stationary-sky atmosphere reuse and an off switch. All previous65 controls/defaults/ranges/menu access and preset assignments retained, now66 options.
- **[Candidate ZIP](../../outputs/Stratus-1.7.0-rc3.zip)** installed and actually test-loaded in Main. [Install/load receipt](../../outputs/Stratus-1.7.0-rc3-install.json), [11 individually reviewed stills](../../outputs/Stratus-1.7.0-rc3-visual-checks/index.html), including one rejected reload diagnostic. Final exact ZIP capture passed the stable loaded-chunk gate. Existing user overrides carried, not reset to Reference.
-768 final native pairs,17 temporal history cases,4 compositor cases,14 raster/entity/underside samples,12 migration checks and actual four66-option Iris profile matching pass. Broader leaf-interior/motion/transition and focusedFPS acceptance remains pending. Dynamic FPS was temporarily disabled through its runtime switch and automatically restored; original session/config restored and checked.

Batch: [b9a03cf9 active brief](IN-PROGRESS/b9a03cf9-f681-4a16-8115-d8b44fd3525a/CHANGES.md). Frozen delta repeats rc2 reconciliation; no duplicate entity/water rebuild. The explicit leaf correction supersedes its whole-material matte wording. Shared next queue, batch target and frozen snapshots untouched. Current TASK/log/archive/next queue matched initial fingerprints before reconciliation; active brief differed only by this run's staging. No newer-edit conflict found. Earlier pending batches untouched.


For earlier evidence, search the exact version or issue in CHANGE-LOG.md; do not dump its entire history.
