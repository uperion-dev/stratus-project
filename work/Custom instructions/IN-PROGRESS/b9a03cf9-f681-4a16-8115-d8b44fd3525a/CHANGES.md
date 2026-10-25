# Stratus — changes for the next coding pass

Put only the changes you want worked on now under **Pending changes**. `TASK.md` is the complete shader target and remains in force for everything else. A saved file does not start work; tell the coding chat **“Apply the pending changes.”** After implementation and verification, move completed requests to [COMPLETED-CHANGES.md](COMPLETED-CHANGES.md) with the release/evidence reference. If none remain pending, leave **“No pending changes.”** Partial or unverified work stays pending. Studio run actions save the submitted brief as a separate `IN-PROGRESS/<request-id>/CHANGES.md` batch and clear this pending section for your next requests. The coder works on that saved batch; queued work is not completed work.

## Pending changes

Frozen delta repeats rc2 implementation/reconciliation already recorded. Do not reimplement entity/native-water fixes. The explicit leaf correction below supersedes the delta's whole-material matte wording. Shared next queue and frozen snapshots stay untouched.

- [ ] Restore restrained sheen on exposed leaf/plant faces. Remove the blanket4113 exclusion; reject inward/back-facing leaf surfaces and preserve opaque depth occlusion, exposure/drainage/weather and zero controls. Review front/back, holes and sheltered/blocked cases; document limits of screen-space/material classification rather than claiming voxel visibility.
- [ ] Implement guarded temporal optimisation: reuse eligible previous-frame sky atmosphere under stable camera/projection, dimensions, time/weather/status and consecutive-frame history. Retain fresh terrain/water/disocclusions and invalid history, full selected fresh-sample quality and all existing controls. Provide an off switch. Verify history invalidation, reload, movement and appearance, plus matched timing; no unfinished-frame presentation claim.
- [ ] Live-test access: user authorises temporary disabling of mods that demonstrably prevent testing. First inspect actual runtime; avoid unnecessary mod changes. Back up and restore each changed file/mod and record any restart/config restoration. This is authorisation, not a requirement to disable mods or proof of FPS.
