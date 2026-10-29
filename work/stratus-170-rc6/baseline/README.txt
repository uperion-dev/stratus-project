STRATUS 1.7.0-rc5 — EXPERIMENTAL TEMPORAL OPTICS HINTS
Original Iris shader pack, MIT licensed. Candidate; not full 1.7 acceptance.

New optional Temporal optics hints switch in Reflections/Performance, default
Off in all four presets. This extends temporal work beyond sky atmosphere:
- Water and thin transparent-solid scenery reflection searches try the preceding
  frame's intersection distance as a current-plane search seed. Current depth,
  normals, medium-side tests, foreground traversal and current colour remain.
- Water refraction tries the previously rejected shoreline guard first, using
  current depth. Every accepted ray still runs the full selected guard set.

These are geometry/search hints, not colour accumulation or renderer frame
skipping. Waves, animated textures and reflected colours evaluate freshly.
Cheap sky/environment lookup, single-guard thin-glass refraction and the
unbent underwater exit remain fresh. This candidate does not claim temporal
radiance reuse across all optics or a measured gameplay FPS improvement.

All 67 previous controls/defaults/choices/preset assignments remain, including
optional Original dampness and retired WET_DARKENING. New switch gives 68
controls. No existing override resets; existing new-release preferences win.
Quality, resolution, ray budgets and draw distance are preserved. On uses up
to three extra RG16F history pairs in existing passes (no new pass); storage
and invalid hints can cost performance. Off removes those history outputs.
At 1440x842 with full scenery reflections and half water, raw paired history
storage is about 21.8 MB (20.8 MiB), excluding driver alignment/overhead.
Sky-only/quality-zero branches omit their unused hint attachments.

Install: use install.py with this release ZIP to preserve latest saved settings.
Earlier release archives/settings remain intact. Technical checks and finite
QA are described in VALIDATION.txt/CHECKS.json. Actual final-release loading,
visual and performance acceptance are recorded separately in the external
install receipt and work/stratus-170-rc5 evidence. Pending work stays pending.
