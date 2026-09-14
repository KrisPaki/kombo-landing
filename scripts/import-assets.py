from html.parser import HTMLParser
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request,json
ROOT=Path(__file__).resolve().parents[1]
class P(HTMLParser):
 def __init__(self):super().__init__();self.urls=[]
 def handle_starttag(self,t,a):
  d=dict(a);u=d.get('data-src','')
  if t=='img' and u.startswith('https://cdn.myportfolio.com/') and u not in self.urls:self.urls.append(u)
p=P();p.feed(Path('/tmp/kombo-food-source.html').read_text())
def get(item):
 i,u=item;dest=ROOT/'assets'/f'food-{i:02}.jpg'
 if not dest.exists():urllib.request.urlretrieve(u,dest)
 return {'id':i,'source':u,'file':str(dest.relative_to(ROOT))}
with ThreadPoolExecutor(max_workers=8) as pool:r=list(pool.map(get,enumerate(p.urls,1)))
(ROOT/'references'/'image-sources.json').write_text(json.dumps(r,indent=2))
print('Downloaded',len(r),'photos')
