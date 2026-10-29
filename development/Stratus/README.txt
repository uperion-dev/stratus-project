STRATUS1.7.0-rc7 — CLASSIC REFLECTIONS, WET SHEEN AND INDEPENDENT BLOOM
Original Iris shader pack, MIT licensed. Restoration candidate; not full1.7
milestone acceptance or a claim that all historical issues are fixed.

Reflection renderer: Classic1.3.1(default) restores the original16/28 perspective
samples and4/5 bisections, with current medium-side validation. It omits the
added20-step reflected volumetric-mist integration and unused receiver-normal
cache output. Current camera atmosphere, sky/clouds, refraction, native water,
underwater and transparent composition stay. Detailed geometry retains the
current receiver-plane tracer plus reflected mist. Both honour selected effect
resolution/range/quality modes. Classic can miss thin scenery and does not add
mist along the reflected path; this is an explicit requested algorithm restore,
not identical output to Detailed. Higher/manual choices remain available.

Wet sheen style: Classic1.3.1(default) restores the dielectric sky film and GGX
sun response, saturating moisture/exposure and world-face drainage. Uniform
material roughness is retained. Current restrained keeps the rc5 response.
Both preserve independent film amount/sheen, all-weather/rain-only, dry zeros,
back/depth guards and optional separate Original dampness. Classic does not
silently restore coupled pore darkening or material-dependent film roughness.
Native textures/colours/exposure/angle still affect perceived brightness.

Bloom strength/radius were present but bypassed by vanilla lighting. They now
work independently. Strength0 truly contributes zero; radius keeps its existing
range and image-height scaling. Native fractional-emitter coverage now reaches
the bloom threshold without an artistic HDR boost; only the bloom target is
mip-prefiltered to avoid widely spaced sampling boxes at large radii.
Original lightmap/AO and bypass of unrelated
artistic grading remain in vanilla lighting; ordinary white geometry does not
pass the non-emissive bright threshold in the targeted GPU check.

All68 existing controls/defaults/ranges/preset assignments retained; two new
selectors give70. Four presets explicitly default to Classic choices. No reset
of saved overrides, no old archive/preference overwrite. Existing new-release
preferences win. Temporal sky reuse and default-off optics hints retained;
geometry history targets are unused in Classic, shoreline hints stay optional.
No changes to sky/cloud/mist fields, view quality, buffer resolution or draw
distance. Compare actual settings:1.3.1's own saved tuning and algorithms differ
from the current sky and are not a constant-quality performance baseline.

Use install.py to install/migrate. Technical snapshots:VALIDATION.txt/CHECKS.json.
Final ZIP/load/visual/FPS evidence and remaining work are recorded separately
in the external install receipt and work/stratus-170-rc6. Do not infer FPS from
compile checks or background GPU queries. Pending full-optics temporal and
historical waterline/leaf acceptance are not solved by this restoration.
