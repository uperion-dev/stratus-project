# Shader context — generated locally

Navigation and fingerprints only; this file does not certify a release or authorise additional work.
Project: /Users/william.lei/Documents/ChatGPT/MC Shader Making
Active brief: work/Custom instructions/IN-PROGRESS/35e4400d-e968-4a39-891a-a8101d519c45/CHANGES.md
Target snapshot: work/Custom instructions/IN-PROGRESS/35e4400d-e968-4a39-891a-a8101d519c45/TASK.md
Brief SHA256: 95f1e4ab62fb2a0816edaa182142c2c2875d2c42315bd55dd090bf01757854b8
Target SHA256: f8fc3d8acefab329e65a18385189af9b01fd89c9914cb3b0a36d1280813c1983
Current shared TASK SHA256: 2e8d1f4cd2071c19f2ee06f757e4e156c079c38b708ec5b10c6fab9f10de8f25
Current shader tree SHA256: 094a8c6fc290863c0b2ce2e49a90f016f51fb2d0a3f0e533bb56225a4456c214 (243 files)

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
- outputs/Stratus/shaders/core/water-surface.glsl
- outputs/Stratus/shaders/core/classic-reflection.glsl
- outputs/Stratus/shaders/core/entity-lighting.glsl
- outputs/Stratus/shaders/core/temporal-optics.glsl
- outputs/Stratus/shaders/core/transparent-optics.glsl
- outputs/Stratus/shaders/core/water-interface.glsl
- outputs/Stratus/shaders/core/water-optics.glsl
- outputs/Stratus/shaders/core/water-path.glsl
- outputs/Stratus/shaders/core/water-reflection.frag.glsl
- outputs/Stratus/shaders/block.properties
- outputs/Stratus/shaders/core/options.glsl
- outputs/Stratus/shaders/shaders.properties
- outputs/Stratus/package.py and outputs/Stratus/install.py: existing release tooling.
Hints are filename matches only, not a diagnosis or a complete dependency list.

## Latest recorded release summary — reported evidence, not a live check
## 30 October 2026 — Stratus 1.7.0-rc8 — technical candidate, live checks deferred

### At a glance

- Restored actual1.3.1 RGB face-light response, retained independent controls, and enabled native model lighting for block entities and player hand/held items. Added nonnegative extended-contrast guards.
- Added selectable Classic fused water composition using the same current optics in the full-resolution resolve; Layered remains available. Existing native atlas, transparent ordering and nearest-exit underwater fog protections retained.
- [Candidate ZIP](../../outputs/Stratus-1.7.0-rc8.zip):252files,7,787,770bytes;SHA256 `77da8afdce004277a0cbc04290bbafeb7cb49f65ece6fc67bd34548d57b830e3`. Final source/archive/manifest integrity verified. **Final archive not installed or live-loaded.**
-768 native program pairs, targeted face/water/underwater GPU checks,35 actual installer cases and71 reachable controls pass. **User deferred live visuals and FPS; no speedup,1.3.1 parity or60FPS claim. All five requests remain pending acceptance.**

Active batch: [35e4400d brief](IN-PROGRESS/35e4400d-e968-4a39-891a-a8101d519c45/CHANGES.md). Frozen rc7 delta already implemented and preserved; no whole-target audit. Shared unsent CHANGES.md and immutable snapshots preserved. Shared TASK reconciled to approved face-design change and honest candidate/evidence state after confirming unchanged starting hashes; no newer-edit conflict.


For earlier evidence, search the exact version or issue in CHANGE-LOG.md; do not dump its entire history.
