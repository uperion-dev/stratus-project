# Stratus — changes for the next coding pass

Put only the changes you want worked on now under **Pending changes**. `TASK.md` is the complete shader target and remains in force for everything else. A saved file does not start work; tell the coding chat **“Apply the pending changes.”** After implementation and verification, move completed requests to [COMPLETED-CHANGES.md](COMPLETED-CHANGES.md) with the release/evidence reference. If none remain pending, leave **“No pending changes.”** Partial or unverified work stays pending. Studio run actions save the submitted brief as a separate `IN-PROGRESS/<request-id>/CHANGES.md` batch and clear this pending section for your next requests. The coder works on that saved batch; queued work is not completed work.

## Pending changes

- [ ] Extend temporal optimisation to active reflection and refraction paths. Preserve sharp current-frame colour, all controls and selected sampling/resolution. Start with validated prior-frame intersection/shoreline hints; always reject stale history and validate current geometry. Check water/scenery/sky and transparent-solid paths, motion, disocclusion, reload, viewport and waterline cases. Keep any unsupported or unverified coverage pending rather than claiming all optics are finished.
- [ ] Run matched, focused active-game FPS/frame-time comparisons after the stable chunk-readiness gate, recording hardware, exact options/framebuffer/camera/time/weather, Dynamic FPS and inactivity limiter state. The user has explicitly resumed this test and intends to keep Minecraft focused. Preserve quality; do not claim an improvement from unmatched or throttled samples.

## Staging notes

- Frozen TASK delta contains already completed rc4 material/default/evidence reconciliation. No additional material implementation is staged.
- Shared CHANGES.md is protected as the next unsent queue. This active batch alone is being processed.
