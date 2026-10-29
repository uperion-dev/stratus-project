from pathlib import Path
import json,sys
sys.path.insert(0,str(Path('work/stratus-check').resolve()));from prepare import profiles
p=Path('outputs/Stratus');w=Path(__file__).parent;policy=json.loads((p/'RELEASE-POLICY.json').read_text());policy.update({'version':'1.7.0-rc6','reset_related_overrides':[],'visual_defaults':profiles((p/'shaders').resolve())['REFERENCE'],'notes':'Requested classic1.3.1 reflection and sheen defaults; current algorithms retained as new selectors. Bloom independent of realistic lighting. Existing68 option values/defaults/ranges/preset assignments preserved,70 total. No saved override reset. Live performance acceptance tracked externally.'});(p/'RELEASE-POLICY.json').write_text(json.dumps(policy,indent=2)+'\n')
f=p/'package.py';f.write_text(f.read_text().replace("'Stratus-1.7.0-rc5.zip'","'Stratus-1.7.0-rc6.zip'"))
(p/'README.txt').write_text('''STRATUS1.7.0-rc6 — CLASSIC REFLECTIONS, WET SHEEN AND INDEPENDENT BLOOM
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
range and image-height scaling. Original lightmap/AO and bypass of unrelated
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
''')
(p/'VALIDATION.txt').write_text('''Stratus1.7.0-rc6 candidate. Evidence:work/stratus-170-rc6.
768 native program pairs passed across8 variants (compatibility shim, not Iris).
1152 material GPU cases preserve equal material film and separate absorption;
96 wet/exposure/weather/zero cases pass.288 classic reflection comparisons
against actual1.3.1 GLSL have RGBA error0 in the tested receivers/quality modes.
Bloom GPU:radius0.5 vs4 second moments10.684 vs642.156; ordinary white geometry
bloom0; vanilla lighting output shows bloom delta0.2165; strength0 preserves
native transfer. Zero GL errors/failures.70 options reachable; all original68
defaults/ranges/preset values and620 block tokens retained.33 real installer
checks preserve old/manual/new-version preferences. Sky/mist/ripple/refraction/
underwater composition modules byte-identical to rc5. Prior unrelated release
checks do not certify this code. Source/package/install bytes checked at build.

Development QA source loaded in actual Main/Iris. Matched normal-world before/
restored river views inspected, plus actual1.3.1 saved-reference view; original
sky/settings differ and are labelled. Detailed material/bloom fixture review,
exact final release loading, profile matching, restoration and focused FPS
are recorded after packaging in external evidence/receipt. Initial game probe
unfocused1440x842,DynamicFPS1FPS, LONG_AFK15; no accepted FPS at this snapshot.
Background six-second GPU draw queries suggest reflection-pass cost reduction
but are not focused whole-game FPS evidence. Some pass readings are zero;
use them as limited diagnostics only. All-optics temporal implementation,
broad motion/edge coverage and60FPS goal remain pending until actual evidence.
''')
(p/'IN-GAME-TEST.txt').write_text('''Main/Stratus Terrain Lab:compare rc5 and final rc6 at the exact latest saved
settings, framebuffer, distance, camera, time and weather. Record actual70-option
Iris state and all four profiles. Check Classic and Detailed reflection modes,
water depth/shore/glass/particles/underside and current sky. Compare original
1.3.1 separately with its saved tuning; do not label it constant-quality.

Compare Classic/Current/dry wet styles on matched materials and grazing/top
faces, nonporous/porous surfaces, rain/caves and zero controls. Optional Original
dampness remains independent. Bloom zero/small/wide:verify visible halo radius
around emitters and clean white blocks with vanilla lighting selected. Confirm
all sliders in the actual Bloom/Reflection/Materials UI and retained ranges.

Focused FPS only:real focus, active DynamicFPS/noAFK limit, matched user quality,
fresh stable5-second loaded-column/zero-mesh gate and continued camera/focus/
size/loading guards. Bound activity resets to test duration, stop afterwards.
Never improve benchmark numbers by silently lowering quality. Restore exact
snapshot fixture blocks and original time/weather/camera/HUD/pause/flight,
preserve newer user edits, and remove only unchanged owned QA files. Final
release selection and remaining acceptance must be explicit in external receipt.
''')
checks={'version':'1.7.0-rc6','batch':'6d616ef5-4067-4c24-afdc-c69e622af1c9','native_pairs':768,'native_failures':0,'compile_log':str(w/'compile.log'),'material_GPU':json.loads((w/'material-checks.json').read_text()),'wet_GPU':json.loads((w/'wet-checks.json').read_text()),'classic_bloom_GPU':json.loads((w/'restoration-gpu-checks.json').read_text()),'controls':json.loads((w/'control-checks.json').read_text()),'migration':json.loads((w/'migration-checks.json').read_text()),'preserved_modules':json.loads((w/'preserved-sky-water-checks.json').read_text()),'prepackage_runtime_scope':'QA source loaded, finite matched river captures and actual131 reference inspected; final load/profiles/material-bloom/FPS/restoration tracked externally','focused_FPS_samples_at_snapshot':0,'notes':'This immutable package records pre-final-live checks. External receipt/log carry later evidence and pending acceptance.'};(p/'CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n')
