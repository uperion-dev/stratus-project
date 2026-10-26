# Shader context — generated locally

Navigation and fingerprints only; this file does not certify a release or authorise additional work.
Project: /Users/william.lei/Documents/ChatGPT/MC Shader Making
Active brief: work/Custom instructions/IN-PROGRESS/c3ec7834-5d1e-403e-9eb7-7a12a3226909/CHANGES.md
Target snapshot: work/Custom instructions/IN-PROGRESS/c3ec7834-5d1e-403e-9eb7-7a12a3226909/TASK.md
Brief SHA256: 87772243f12b010b6ddc7501bbc119e29c9b538b629c1410fc39292d4458ebac
Target SHA256: c4deb00fbe7fa9b84148da3c00d418dfb3734c2f95aea3e1eb719fc0b61352f7
Current shared TASK SHA256: c4deb00fbe7fa9b84148da3c00d418dfb3734c2f95aea3e1eb719fc0b61352f7
Current shader tree SHA256: ab379c84c62a57007f1a9ca22ec2c243a08ef1a87a60e0eb5360d51e910513ad (240 files)

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
- outputs/Stratus/shaders/core/refraction.glsl
- outputs/Stratus/shaders/core/submerged-reflection.glsl
- outputs/Stratus/shaders/core/temporal-atmosphere.glsl
- outputs/Stratus/shaders/core/water-reflection.frag.glsl
- outputs/Stratus/shaders/shaders.properties
- outputs/Stratus/shaders/core/options.glsl
- outputs/Stratus/package.py and outputs/Stratus/install.py: existing release tooling.
Hints are filename matches only, not a diagnosis or a complete dependency list.

## Latest recorded release summary — reported evidence, not a live check
## 26 October 2026 — Stratus 1.7.0-rc4 — uniform material film and original dampness

### At a glance

- Eligible material classes now use one film reflectance/roughness response. New **Original dampness** Materials slider restores porous absorption/retained-dampness shape, default0/off, independent of film/sheens. Retired WET_DARKENING remains a no-op. Prior66 controls/defaults/ranges/preset quality retained;67 total.
- **[Candidate ZIP](../../outputs/Stratus-1.7.0-rc4.zip)** installed and actually test-loaded with all saved overrides preserved. [Install/load receipt](../../outputs/Stratus-1.7.0-rc4-install.json), [11 reviewed material-panel comparisons](../../outputs/Stratus-1.7.0-rc4-visual-checks/index.html). Resolution remains854×480 and saved quality choices unchanged.
-768 native pairs,1152 material GPU cases,96 wet-film cases,4 compositor cases,15 migration checks and actual four67-option Iris profile matching pass. **Focused FPS explicitly skipped by user; performance optimisation remains pending, no game-speedup claim.** Test fixture removed and helpers stopped. Original shader/config restored; newer world exit/saved pose preserved.

Batch: [0bc449ce active brief](IN-PROGRESS/0bc449ce-fb20-4840-8668-cde4168e3735/CHANGES.md). Frozen delta repeats rc3 reconciliation; no duplicate temporal/native-water rebuild. Explicit requests supersede material-dependent film roughness and unconditional absorption removal. Shared next queue, immutable target and frozen snapshots untouched. Shared TASK/log/archive/queue matched initial fingerprints before reconciliation; only this run's staging changed the batch brief. No newer document conflict found. Earlier pending batches unchanged.


For earlier evidence, search the exact version or issue in CHANGE-LOG.md; do not dump its entire history.
