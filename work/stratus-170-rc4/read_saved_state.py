from pathlib import Path
import gzip,struct,json,io
w=Path(__file__).resolve().parent;path=Path.home()/'Library/Application Support/ModrinthApp/profiles/Minecraft (1)/saves/StratusTerrainLab/level.dat';stream=io.BytesIO(gzip.decompress(path.read_bytes()))
def num(fmt):return struct.unpack('>'+fmt,stream.read(struct.calcsize('>'+fmt)))[0]
def string():return stream.read(num('H')).decode('utf8')
def value(tag):
 if tag in [1,2,3,4,5,6]:return num({1:'b',2:'h',3:'i',4:'q',5:'f',6:'d'}[tag])
 if tag==7:return stream.read(num('i'))
 if tag==8:return string()
 if tag==9:
  subtype=num('B');return [value(subtype) for _ in range(num('i'))]
 if tag==10:
  d={}
  while (subtype:=num('B'))!=0:
   name=string();d[name]=value(subtype)
  return d
 if tag in [11,12]:return [num('i' if tag==11 else 'q') for _ in range(num('i'))]
 raise ValueError(tag)
tag=num('B');string();root=value(tag);data=root.get('Data',root);player=data.get('Player',{})
result={'source':'Persisted level.dat after the test world logged out; read-only bounded field extraction','position':player.get('Pos'),'rotation':player.get('Rotation'),'flying':player.get('abilities',{}).get('flying'),'daytime':data.get('DayTime'),'raining':data.get('raining'),'rainTime':data.get('rainTime')};(w/'final-saved-player-state.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
