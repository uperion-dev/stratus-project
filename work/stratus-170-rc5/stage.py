from pathlib import Path
import hashlib,json,shutil
root=Path.cwd(); work=root/'work/stratus-170-rc5'; batch=root/'work/Custom instructions/IN-PROGRESS/c3ec7834-5d1e-403e-9eb7-7a12a3226909'
paths=['work/Custom instructions/TASK.md','work/Custom instructions/CHANGES.md',str(batch.relative_to(root)/'CHANGES.md')]
records={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in paths}
(work/'initial-fingerprints.json').write_text(json.dumps(records,indent=2)+'\n')
for name in ['TASK.md','CHANGES.md']:
 shutil.copy2(batch/name,work/('batch-'+name))
shutil.copytree(root/'outputs/Stratus/shaders',work/'baseline-shaders',dirs_exist_ok=True)
p=batch/'CHANGES.md'; text=p.read_text(); head=text.split('## Pending changes')[0]
p.write_text(head+'''## Pending changes

- [ ] Extend temporal optimisation to active reflection and refraction paths. Preserve sharp current-frame colour, all controls and selected sampling/resolution. Start with validated prior-frame intersection/shoreline hints; always reject stale history and validate current geometry. Check water/scenery/sky and transparent-solid paths, motion, disocclusion, reload, viewport and waterline cases. Keep any unsupported or unverified coverage pending rather than claiming all optics are finished.
- [ ] Run matched, focused active-game FPS/frame-time comparisons after the stable chunk-readiness gate, recording hardware, exact options/framebuffer/camera/time/weather, Dynamic FPS and inactivity limiter state. The user has explicitly resumed this test and intends to keep Minecraft focused. Preserve quality; do not claim an improvement from unmatched or throttled samples.

## Staging notes

- Frozen TASK delta contains already completed rc4 material/default/evidence reconciliation. No additional material implementation is staged.
- Shared CHANGES.md is protected as the next unsent queue. This active batch alone is being processed.
''')
(batch/'PROGRESS.md').write_text('''# Batch progress

Status: staged; implementation in progress

## Resume here
- Work directory: `work/stratus-170-rc5/` (rc5 is a candidate name, not a packaged release).
- Baseline shader snapshot and initial document fingerprints saved there.
- Next action: implement and test current-geometry-validated temporal optical hints, then check the live Main world/focus before benchmarking.
- Frozen delta repeats completed rc4 changes; active optics/FPS requests only. Shared next queue untouched.

## Evidence and remaining work
- Running Java PID6833 inspected; guarded read confirms player present, pause menu class433, HUD visible, pause-on-focus-loss true. Focus not yet measured.
- All implementation, compile/GPU, runtime, visual and focused FPS checks remain pending.
''')
