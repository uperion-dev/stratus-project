# Shader context — generated locally

Navigation and fingerprints only; this file does not certify a release or authorise additional work.
Project: /Users/william.lei/Documents/ChatGPT/MC Shader Making
Active brief: work/Custom instructions/IN-PROGRESS/c3ec7834-5d1e-403e-9eb7-7a12a3226909/CHANGES.md
Target snapshot: work/Custom instructions/IN-PROGRESS/c3ec7834-5d1e-403e-9eb7-7a12a3226909/TASK.md
Brief SHA256: f3c9d2a6f260e5dc1ebb7d9e4decc8bb1e0d92b3591c54457c359fbc2c937bbd
Target SHA256: c4deb00fbe7fa9b84148da3c00d418dfb3734c2f95aea3e1eb719fc0b61352f7
Current shared TASK SHA256: 7eb37fc7a4cf6f30111490c72eedb4acc52142559853565e220d1b9a67ae3347
Current shader tree SHA256: aa21d87ed3601eaa364801964a2d3708b83146365f4102db8877b6a6439bf471 (241 files)

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
- outputs/Stratus/shaders/core/temporal-optics.glsl
- outputs/Stratus/shaders/core/water-path.glsl
- outputs/Stratus/shaders/block.properties
- outputs/Stratus/shaders/core/air.glsl
- outputs/Stratus/shaders/core/frame.glsl
- outputs/Stratus/shaders/core/options.glsl
- outputs/Stratus/shaders/core/temporal-atmosphere.glsl
- outputs/Stratus/shaders/core/transparent-optics.glsl
- outputs/Stratus/shaders/core/water-buffer.glsl
- outputs/Stratus/shaders/shaders.properties
- outputs/Stratus/package.py and outputs/Stratus/install.py: existing release tooling.
Hints are filename matches only, not a diagnosis or a complete dependency list.

## Latest recorded release summary — reported evidence, not a live check
## 26 October 2026 — Stratus 1.7.0-rc5 — experimental temporal optics hints

### At a glance

- Optional **Temporal optics hints**, default **Off**, adds prior-frame geometry/search hints for water/glass scenery reflections and water shoreline refraction checks. Fresh depth, occlusion and colour remain; no renderer frame skipping or colour accumulation. **The full all-reflections/refractions optimisation request remains pending.**
- [Candidate ZIP](../../outputs/Stratus-1.7.0-rc5.zip), [install/load receipt](../../outputs/Stratus-1.7.0-rc5-install.json), [nine reviewed finite river captures](../../outputs/Stratus-1.7.0-rc5-visual-checks/index.html). Exact final source/archive/install bytes match;250 entries,7,785,718bytes;SHA256 `4424a2f229ffca4519e0b619264b933de44b3f365532246492ad6b2fa68632d0`.
-768 native pairs, targeted GPU comparisons at all three refraction qualities,17 installer checks,68 reachable options and four actual68-option Iris profiles pass. All previous67 option defaults/ranges/preset assignments and620 block tokens retained. **Six valid focused FPS samples now recorded; no speedup.** Keep this experiment disabled. Net optimisation, approximately60FPS Reference goal and broad motion/glass/waterline acceptance remain pending.

Batch: [c3ec7834 active brief](IN-PROGRESS/c3ec7834-5d1e-403e-9eb7-7a12a3226909/CHANGES.md). Frozen delta repeats completed rc4 material reconciliation, so no duplicate material work. Shared next queue, immutable batch target and frozen snapshots are preserved. Only this batch's brief is staged/reconciled; earlier pending batches remain untouched. No newer document conflict was found before reconciliation.


For earlier evidence, search the exact version or issue in CHANGE-LOG.md; do not dump its entire history.
