"""Create browser-ready copies of the six owner-supplied videos. Requires imageio-ffmpeg."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess,json
import imageio_ffmpeg
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'assets'/'video';DEST.mkdir(exist_ok=True)
VIDEOS=[('showreel','show reel 2025 09 .mov',False),('nespresso-kinoteka','Nesspresso x Kinoteka - K.Pakiela - Video .mov',True),('spedz-dzien','spedz dzien.mov',False),('oddychanie','oddychanie .mov',False),('przepis-na-ciastka','Przepis na Ciasstka - IG SONG - driving by lofi muspace-.mov',False),('foremki','Foremki - kolorowe - song name for IG - Eric Godlow - Peace.mov',False)]
ff=imageio_ffmpeg.get_ffmpeg_exe()
def encode(item):
 slug,name,wide=item;src=Path('/Users/krystianpakiela/Movies')/name
 out=DEST/f'{slug}.mp4'
 cmd=[ff,'-hide_banner','-loglevel','error','-y','-i',str(src),'-map','0:v:0','-map','0:a:0?','-vf','scale=1280:720' if wide else 'scale=540:960','-c:v','libx264','-preset','fast','-crf','24','-maxrate','2200k','-bufsize','4400k','-pix_fmt','yuv420p','-threads','3','-c:a','aac','-b:a','96k','-movflags','+faststart','-map_metadata','-1',str(out)]
 subprocess.run(cmd,check=True)
 subprocess.run([ff,'-hide_banner','-loglevel','error','-y','-ss','2','-i',str(out),'-frames:v','1','-q:v','3',str(DEST/f'{slug}.jpg')],check=True)
 print(slug,round(out.stat().st_size/1e6,2),'MB',flush=True)
 return {'slug':slug,'original':name,'file':f'assets/video/{slug}.mp4','poster':f'assets/video/{slug}.jpg','bytes':out.stat().st_size}
with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(encode,VIDEOS))
(ROOT/'references'/'video-sources.json').write_text(json.dumps(results,indent=2))
