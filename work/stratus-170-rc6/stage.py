from pathlib import Path
import hashlib,json,shutil
from zipfile import ZipFile
r=Path.cwd();w=r/'work/stratus-170-rc6';b=r/'work/Custom instructions/IN-PROGRESS/6d616ef5-4067-4c24-afdc-c69e622af1c9';d=r/'work/Custom instructions'
paths=[d/'TASK.md',d/'CHANGES.md',d/'CHANGE-LOG.md',d/'COMPLETED-CHANGES.md',b/'CHANGES.md',b/'TASK.md']
(w/'initial-fingerprints.json').write_text(json.dumps({str(p.relative_to(r)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},indent=2)+'\n')
for n in ['TASK.md','CHANGES.md']:shutil.copy2(b/n,w/('batch-'+n))
shutil.copytree(r/'outputs/Stratus',w/'baseline',dirs_exist_ok=True)
with ZipFile(r/'outputs/Stratus-1.3.1.zip') as z:
 for name in z.namelist():
  if name.startswith('shaders/') and not name.endswith('/'):
   p=w/'reference-131'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(z.read(name))
p=b/'CHANGES.md';head=p.read_text().split('## Pending changes')[0]
p.write_text(head+'''## Pending changes

- [ ] Investigate and repair the performance regression against the actual1.3.1 archive. Compare actual source and matched active-game behaviour; identify added expensive work, preserve the current sky and existing controls. Restore a clearly labelled classic1.3.1 reflection implementation while retaining the current geometry path as a selectable option; keep selected resolution and other quality controls. Do not claim speedup from old/new settings that differ.
- [ ] Restore the1.3.1 wet-sheen character: its dielectric sky-film response and GGX sun highlight, exposure and drainage. Preserve uniform material response, all-weather/rain-only choices, zero controls, native diffuse colour, optional separate Original dampness and existing inward/back-face guards. Keep the current sheen style selectable rather than deleting it.
- [ ] Repair bloom/radius usability. Both controls exist but are bypassed by vanilla lighting; restore independent bloom with a true zero strength and meaningful radius, without enabling unrelated artistic lighting/grading or making ordinary white blocks glow. Keep menu access, saved identifiers and full ranges.
- [ ] Package and verify the restoration at preserved settings: compile/GPU, control/menu/preset/migration audit, actual Iris load, finite wet/bloom/water/sky review and focused gated FPS comparison where live access permits. Preserve old archives, newer user edits, settings and the shared next queue. Unverified parts stay pending.

## Staging notes

- The frozen TASK delta repeats rc5 implementation/evidence reconciliation. It creates no duplicate optics-hint or material task. Earlier pending batches are preserved.
- The explicit request to bring bloom back supersedes only the old requirement that vanilla lighting bypass bloom; native lightmap/AO and bypass of artistic grading remain.
-1.3.1 is the user's restoration/performance reference. This authorises focused restoration, not an entire pack rollback or removal of newer working sky/water/controls. New classic modes will be labelled; previous algorithms remain available.
''')
(b/'PROGRESS.md').write_text('''# Batch progress

Status: staged; source diagnosis in progress

## Resume here
- Work/evidence: `work/stratus-170-rc6/`; initial document hashes, exact current pack backup and extracted immutable1.3.1 reference saved.
- Next action: restore selectable classic reflection and wet response, repair lighting-independent bloom, and test concrete bottlenecks against baseline. No source edit yet.
- Findings: current scenery tracing uses receiver-plane reconstruction/bilinear gathers and up to192 steps vs1.3.1's16/28 samples with4/5 bisections. Current mist also has more sampling/self-light integration than1.3.1; preserve the approved sky and measure before changing it. Bloom/radius controls exist but are completely bypassed with default vanilla lighting.

## Evidence and remaining work
- Source/instruction/target/brief/frozen delta inspected. Frozen delta only repeats completed rc5 reconciliation.
- Java PID6833 still exists; actual current profile/world/focus/options not refreshed yet.
- All implementation, new compilation/GPU, live visual and focused performance checks remain pending.
- Shared CHANGES.md and immutable snapshots untouched. No extra agents/handoff.
''')
print('Staged four concrete restoration/verification items; saved rc5 and1.3.1 source references.')
