import http from 'node:http';
import { readFile,stat } from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.dirname(fileURLToPath(import.meta.url));
const types={'.html':'text/html; charset=utf-8','.js':'text/javascript; charset=utf-8','.css':'text/css; charset=utf-8','.png':'image/png','.svg':'image/svg+xml','.mp3':'audio/mpeg','.md':'text/plain; charset=utf-8','.json':'application/json'};
const port=Number(process.env.PORT||4173);
http.createServer(async(req,res)=>{
  try{
    const pathname=decodeURIComponent(new URL(req.url,'http://localhost').pathname);
    const relative=pathname==='/'?'index.html':pathname.replace(/^\/+/, '');
    const target=path.resolve(root,relative);
    if(!target.startsWith(root+path.sep)||relative.split('/').some(p=>p.startsWith('.'))){res.writeHead(403);res.end('Forbidden');return;}
    if(!(await stat(target)).isFile())throw new Error('Not a file');
    const bytes=await readFile(target);
    const headers={'Content-Type':types[path.extname(target)]||'application/octet-stream','Cache-Control':'no-cache','X-Content-Type-Options':'nosniff','Accept-Ranges':'bytes'};
    const range=req.headers.range;
    if(range){
      const match=/^bytes=(\d*)-(\d*)$/.exec(range);
      let start=0,end=bytes.length-1;
      if(match){
        if(match[1]){start=Number(match[1]);if(match[2])end=Number(match[2]);}
        else if(match[2])start=Math.max(0,bytes.length-Number(match[2]));
      }
      if(!match||(!match[1]&&!match[2])||start>end||start>=bytes.length){res.writeHead(416,{'Content-Range':`bytes */${bytes.length}`});res.end();return;}
      end=Math.min(end,bytes.length-1);
      res.writeHead(206,{...headers,'Content-Length':end-start+1,'Content-Range':`bytes ${start}-${end}/${bytes.length}`});
      res.end(req.method==='HEAD'?undefined:bytes.subarray(start,end+1));return;
    }
    res.writeHead(200,{...headers,'Content-Length':bytes.length});res.end(req.method==='HEAD'?undefined:bytes);
  }catch{res.writeHead(404);res.end('Not found');}
}).listen(port,'127.0.0.1',()=>console.log(`Local: http://127.0.0.1:${port}`));
