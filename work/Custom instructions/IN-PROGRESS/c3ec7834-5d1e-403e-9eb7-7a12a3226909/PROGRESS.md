# Batch progress

Status: staged; implementation in progress

## Resume here
- Work directory: `work/stratus-170-rc5/` (rc5 is a candidate name, not a packaged release).
- Baseline shader snapshot and initial document fingerprints saved there.
- Next action: implement and test current-geometry-validated temporal optical hints, then check the live Main world/focus before benchmarking.
- Frozen delta repeats completed rc4 changes; active optics/FPS requests only. Shared next queue untouched.

## Evidence and remaining work
- Running Java PID6833 inspected; guarded read confirms player present, pause menu class433, HUD visible, pause-on-focus-loss true. Focus not yet measured.
- All implementation, compile/GPU, runtime, visual and focused FPS checks remain pending.
