STRATUS1.7.0-rc4 — UNIFORM MATERIAL FILM AND OPTIONAL ORIGINAL DAMPNESS
Original Iris shader pack, MIT licensed. Candidate; not full1.7 acceptance.

All eligible exposed solid/leaf materials use the same film roughness/lobe and
reflectance. Underlying texture, native diffuse colour, face orientation,
lighting/exposure and drainage still change apparent brightness. Interior/back
face guards remain; no whole-material exclusions added. Water keeps its own
optics controls. Optional original dampness affects absorption, not sheen parity.

New Materials slider: Original dampness, default0/off. Restores the project's
original1.6.7 porous absorption darkening, clear/rain humidity, partial-shelter
and world-face drainage shape with a separate amount. Nonporous material does
not absorb; sealed caves stay dry. This local retained-dampness approximation
stores no wetness over time. It is independent of film amount and sheen, so
turn all three to zero for a completely dry result. WET_DARKENING remains its
clearly labelled retired no-op and existing saved values retain that meaning.

Every previous66 control/default/range/menu/preset quality assignment remains.
ORIGINAL_DAMPNESS has12 choices0..2, default0 in all presets, giving67 controls.
No release override reset. Latest/manual unrelated settings and prior archives
preserved; existing new-version settings win. Missing new control uses0.

Temporal sky reuse/native water/entity fixes remain. Resolution, draw distance,
quality options, sampling and passes are unchanged. FocusedFPS was explicitly
skipped; no new measured game-performance gain is claimed. Primary lightweight
shader framework research is recorded externally; no third-party shader source
was copied or imported. Known older waterline/leaf/temporal gates remain pending.

Use install.py --profile PATH --previous-settings OLD.zip.txt (or --dry-run).
Source/compile/GPU/package/install/load/visual/FPS are separate evidence states.
See CHECKS.json and the external versioned install receipt/visual gallery/log.
