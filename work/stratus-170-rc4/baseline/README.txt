STRATUS 1.7.0-rc3 — EXPOSED FOLIAGE AND GUARDED TEMPORAL SKY REUSE
Original Iris shader pack, MIT licensed. Implementation candidate, not full1.7 milestone acceptance.

Exposed front-facing leaf/plant material4113 receives restrained film again.
Back-facing surfaces remain excluded; ordinary opaque depth occlusion, sky
exposure, drainage/weather and independent amount/sheen-zero controls remain.
This is raster face orientation, not voxel-neighbour occupancy: a front-facing
leaf face glimpsed through other leaves may still receive film. See remaining
live acceptance in the batch; no claim every internal cluster face is removed.

Temporal sky reuse (Performance menu) uses the existing atmosphere ping-pong
target. At most one previous fresh frame is reused, only for sky with a static
camera/projection and consecutive matching time/weather/status/viewport.
Terrain, water, moving/rotating/bobbing views, FOV changes, status changes,
missing/reloaded history and frames over50ms evaluate freshly at full selected
quality. No reuse chains, frame presentation changes, added pass or history
buffer. Cloud animation may be delayed one frame. Off disables reuse. Two
history-header pixels use the existing exact atmosphere reconstruction fallback.

All previous65 controls/defaults/ranges/menu access and preset quality values
remain; new TEMPORAL_ATMOSPHERE [0 1] defaults1 in all presets, giving66 controls.
Previous native water/entity fixes and all quality choices remain. No release-
related override reset; unrelated/latest/manual preferences carry. Missing new
option uses source default; an explicit new-option override wins. Existing
new-version preferences and older archives are never overwritten.

Install with install.py --profile PATH --previous-settings OLD.zip.txt.
Installation, selection, loading, visual review and FPS are separate states.
CHECKS.json records technical scope; external install receipt/gallery records
actual runtime evidence. Focused gameplay performance is unverified while the
Mac is locked. Synthetic GPU timer results are not gameplay FPS. The known
waterline band and older pending acceptance remain separate, unresolved work.
