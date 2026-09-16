"""Create browser-ready copies of the owner-supplied videos. Requires imageio-ffmpeg."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess,json
import imageio_ffmpeg
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'assets'/'video';DEST.mkdir(exist_ok=True)
HOME=Path.home();MOVIES=HOME/'Movies';HORIZONTAL=HOME/'Desktop'/'Video pion '
VIDEOS=[
 ('showreel',MOVIES/'show reel 2025 09 .mov','scale=540:960',24),
 ('nespresso-kinoteka',MOVIES/'Nesspresso x Kinoteka - K.Pakiela - Video .mov','scale=1280:720',24),
 ('spedz-dzien',MOVIES/'spedz dzien.mov','scale=540:960',24),
 ('oddychanie',MOVIES/'oddychanie .mov','scale=540:960',24),
 ('przepis-na-ciastka',MOVIES/'Przepis na Ciasstka - IG SONG - driving by lofi muspace-.mov','scale=540:960',24),
 ('foremki',MOVIES/'Foremki - kolorowe - song name for IG - Eric Godlow - Peace.mov','scale=540:960',24),
 ('czarek',HORIZONTAL/'CZAREK 1 .mov','scale=1280:-2:flags=lanczos,fps=30',25),
 ('greenmax',HORIZONTAL/'GreenMax_prev_08092025.MP4','scale=1280:-2:flags=lanczos,fps=30',25),
 ('niunia-kas',HORIZONTAL/'Niunia kas .mov','scale=1280:-2:flags=lanczos,fps=30',25),
 ('rozlewnia-metali',HORIZONTAL/'ROZLEWNIA METALI_V3.mp4','scale=1280:-2:flags=lanczos,fps=30',25),
 ('bigram',HORIZONTAL/'poprawki ver 5.mov','scale=1280:-2:flags=lanczos,fps=30',25),
 ('gobrain',HORIZONTAL/'wersja 2.mov','scale=1280:-2:flags=lanczos,fps=30',25),
]
ff=imageio_ffmpeg.get_ffmpeg_exe()
def encode(item):
 slug,src,video_filter,quality=item
 out=DEST/f'{slug}.mp4'
 cmd=[ff,'-hide_banner','-loglevel','error','-y','-i',str(src),'-map','0:v:0','-map','0:a:0?','-vf',video_filter,'-c:v','libx264','-preset','fast','-crf',str(quality),'-maxrate','2200k','-bufsize','4400k','-pix_fmt','yuv420p','-threads','3','-c:a','aac','-b:a','96k','-movflags','+faststart','-map_metadata','-1',str(out)]
 subprocess.run(cmd,check=True)
 subprocess.run([ff,'-hide_banner','-loglevel','error','-y','-ss','2','-i',str(out),'-frames:v','1','-q:v','3',str(DEST/f'{slug}.jpg')],check=True)
 print(slug,round(out.stat().st_size/1e6,2),'MB',flush=True)
 return {'slug':slug,'original':str(src.relative_to(HOME)),'file':f'assets/video/{slug}.mp4','poster':f'assets/video/{slug}.jpg','bytes':out.stat().st_size}
with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(encode,VIDEOS))
(ROOT/'references'/'video-sources.json').write_text(json.dumps(results,indent=2))
