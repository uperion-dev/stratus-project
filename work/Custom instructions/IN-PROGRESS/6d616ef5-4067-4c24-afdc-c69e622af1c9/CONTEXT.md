# Shader context — generated locally

Navigation and fingerprints only; this file does not certify a release or authorise additional work.
Project: /Users/william.lei/Documents/ChatGPT/MC Shader Making
Active brief: work/Custom instructions/IN-PROGRESS/6d616ef5-4067-4c24-afdc-c69e622af1c9/CHANGES.md
Target snapshot: work/Custom instructions/IN-PROGRESS/6d616ef5-4067-4c24-afdc-c69e622af1c9/TASK.md
Brief SHA256: ea2f4bcb885196e2ac3a04ee49e7b59b14e46617bffa2c7426f13fd7f7a8785a
Target SHA256: 7eb37fc7a4cf6f30111490c72eedb4acc52142559853565e220d1b9a67ae3347
Current shared TASK SHA256: f8fc3d8acefab329e65a18385189af9b01fd89c9914cb3b0a36d1280813c1983
Current shader tree SHA256: 26802b40ade03b68332751b256a7185f05bb31c570514b8196c80cbf3b54a8c4 (242 files)

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
- Line 88: Packaging, testing and evidence

## Current source navigation hints
- outputs/Stratus/shaders/core/classic-reflection.glsl
- outputs/Stratus/shaders/core/submerged-reflection.glsl
- outputs/Stratus/shaders/core/temporal-atmosphere.glsl
- outputs/Stratus/shaders/block.properties
- outputs/Stratus/shaders/core/air.glsl
- outputs/Stratus/shaders/core/atmosphere-resolve.frag.glsl
- outputs/Stratus/shaders/core/atmosphere.frag.glsl
- outputs/Stratus/shaders/core/bloom-horizontal.frag.glsl
- outputs/Stratus/shaders/core/bloom-vertical.frag.glsl
- outputs/Stratus/shaders/core/options.glsl
- outputs/Stratus/shaders/shaders.properties
- outputs/Stratus/package.py and outputs/Stratus/install.py: existing release tooling.
Hints are filename matches only, not a diagnosis or a complete dependency list.

## Latest recorded release summary — reported evidence, not a live check
## 27 October 2026 — Stratus 1.7.0-rc7 — classic restoration and independent bloom

### At a glance

- Restored selectable **Classic1.3.1 reflection** and **Classic wet sheen** defaults, retaining Detailed geometry/Current film and every prior control. Current sky, cloud/mist producer, water/refraction/underwater modules preserved. Bloom now works in vanilla lighting; fractional native emitters and visibly adjustable smooth radius repaired.
- [Final ZIP](../../outputs/Stratus-1.7.0-rc7.zip) · [Actual visual checks](../../outputs/Stratus-1.7.0-rc7-visual-checks/index.html) · [Install/load receipt](../../outputs/Stratus-1.7.0-rc7-install.json).251 entries,7,789,615bytes;SHA256 `cc0fd043e8f96d415d7376aba0f0835596971e28a2155cccda1458c78d986d9b`. Exact source/archive/installed bytes match; final ZIP loaded and left selected/enabled in Main.
-768 native pairs,1152 material cases,96 wet cases,288 original1.3.1 trace comparisons, targeted bloom GPU checks,33 installer cases,70 reachable options and four actual70-option Iris profiles pass. All prior68 defaults/ranges/preset assignments and620 block tokens retained.
- **Focused development pair30.51→48.59FPS (~59.2%) predates final bloom corrections. Final rc7 FPS and valid1.3.1 comparison remain pending after the Mac locked.** No final60FPS/max-FPS or full temporal completion claim.

Batch: [6d616ef5 active brief](IN-PROGRESS/6d616ef5-4067-4c24-afdc-c69e622af1c9/CHANGES.md). Shared next queue and immutable snapshots preserved; no newer document conflict before reconciliation. Frozen delta’s unfinished all-optics temporal target is staged and retained, not treated as completed by classic restoration. Old chat was read only (three recent turns); no handoff/message/revival. Actual own1.3.1 archive source is the restoration reference.


For earlier evidence, search the exact version or issue in CHANGE-LOG.md; do not dump its entire history.
