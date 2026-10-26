# Batch progress

Status: partial — candidate built/tested; effective all-optics optimisation remains pending

## Resume here
- Active brief: this batch's CHANGES.md only. Shared CHANGES.md is protected next unsent work.
- Source/package: `outputs/Stratus`, immutable `outputs/Stratus-1.7.0-rc5.zip`, SHA2564424a2f229ffca4519e0b619264b933de44b3f365532246492ad6b2fa68632d0.250 entries,7,785,718bytes. Source/archive/install match.
- Current shader selection restored to rc3 enabled. Final HUD/pause/menu/flight/options unchanged, newer user camera yaw−67.70922/pitch10.483427 preserved. Helpers stopped; all owned QA files cleaned up. No world-block mutation.
- Next concrete work: develop an effective all-optics temporal design with correct motion/disocclusion and fresh fallback, or obtain supported pass profiling; current hint approach is not faster. Keep TEMPORAL_OPTICS0/default Off. No lowering quality or claiming60FPS.

## Evidence and remaining work
-768 native compile/link pairs pass: `work/stratus-170-rc5/compile-final.log`.
- GPU:960 reflection comparisons,1344 refraction comparisons for each quality0/1/2,8 RG16F history cases per run; no failures/API errors or tested colour/UV mismatch. `optics-checks-final.json`.
- All old67 defaults/ranges/presets and620 block tokens retained;68 controls reachable.17 actual installer checks pass. Exact final ZIP loaded; four actual68-option Iris profiles match, saved overrides retained. `control-checks.json`, `migration-checks.json`, `final-release-runtime.json`, `final-audit.json`.
- Six primary focused20s samples,1440×842, Apple M1, render distance12, time1000/rain0, real focus, stable441-column/zero-mesh gates. Manual A31.42Off/30.42On; manual B30.93Off/30.03On. Strict Reference50.24Off/49.91On with zero limiter/DynamicFPS violations, cap70. SavedVSync=true, DynamicFPS reportsVSyncfalse; effective swap interval not independently checked. No supported gain. `performance-results.json`, raw `benchmarks/`, `activity-monitor.txt`.
- Nine finite river captures inspected. Continuous motion/glass/waterline/reload/resize/full temporal optics coverage remain pending. Earlier unrelated batches untouched.
- Four-second per-pass query helper failed Fabric class-loader visibility check before registering any transformer; no accepted pass timings/hook. `gpu-profiling-blocker.json`.
- Shared TASK reconciled carefully; focused comparison archived separately from pending optimisation. Package CHECKS/VALIDATION are pre-live-test snapshots; external receipt/log contain subsequent evidence. No newer document conflict found.
