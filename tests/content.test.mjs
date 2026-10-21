import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile,access} from 'node:fs/promises';
import {slides,sources} from '../content.js';
import {visual} from '../visuals.js';

test('Exactly ten slides, unique routes, and eight-minute silent timeline',()=>{
  assert.equal(slides.length,10);assert.equal(new Set(slides.map(s=>s.id)).size,10);
  assert.equal(slides.reduce((n,s)=>n+s.duration,0),480);
});
test('Every slide has both complete language tracks and traceable sources',()=>{
  for(const s of slides){
    for(const lang of ['th','en']){
      assert.ok(s.title[lang]);assert.ok(s.subtitle[lang]);assert.ok(s.notes[lang].length>200);
      const scene=visual(s,lang);assert.ok(scene.includes('<svg')||scene.includes('<img'));
      assert.ok(!scene.includes('undefined'));
    }
    assert.ok(s.sources.length);
    for(const key of s.sources){assert.ok(sources[key],key);assert.equal(new URL(sources[key].url).protocol,'https:');}
  }
});
test('Thai neural narration assets are complete and fit each presentation cue',async()=>{
  const manifest=JSON.parse(await readFile(new URL('../assets/audio/manifest.json',import.meta.url),'utf8'));
  assert.equal(manifest.length,10);
  for(const [i,s] of slides.entries()){
    assert.equal(s.audio.th,manifest[i].path);
    assert.ok(manifest[i].duration>20);
    assert.ok(manifest[i].duration<=s.duration,`${s.id}: narration exceeds its cue`);
    assert.ok(!/[A-Za-z]/.test(s.notes.th),'Thai listening track uses pronounceable Thai terms');
    await access(new URL('../'+s.audio.th,import.meta.url));
  }
  assert.ok(manifest.reduce((n,s)=>n+s.duration,0)<480);
});
test('Every conceptual image exists locally and has an accessible description',async()=>{
  for(const s of slides){
    const markup=visual(s,'th');
    const images=[...markup.matchAll(/<img[^>]*src="([^"]+)"[^>]*alt="([^"]+)"/g)];
    for(const match of images){await access(new URL('../'+match[1],import.meta.url));assert.ok(match[2].length>20);}
  }
});
test('Case proposals include community evidence and Microsoft standard baseline',()=>{
  for(const id of ['accounts-payable','inventory-cost','warehouse','production']){
    const s=slides.find(s=>s.id===id);
    assert.ok(s.sources.some(key=>sources[key].kind.includes('Community')));
    assert.ok(s.sources.some(key=>sources[key].kind.includes('Microsoft documentation')));
  }
});
test('Closing uses the exact supplied image and local links exist',async()=>{
  assert.equal(slides.at(-1).visual,'closing');
  for(const file of ['assets/closing-original.png','assets/fujitsu-red.png','app.js','styles.css','docs/research.md','docs/narration.md'])await access(new URL('../'+file,import.meta.url));
  const html=await readFile(new URL('../index.html',import.meta.url),'utf8');
  for(const id of ['stage','play','voice','lang','notes','evidence','prev','next','drawer','drawer-body','dots','status'])assert.ok(html.includes(`id="${id}"`));
});
test('Presentation remains portable under a GitHub Pages repository subpath',async()=>{
  for(const file of ['index.html','app.js','styles.css','visuals.js']){
    const text=await readFile(new URL('../'+file,import.meta.url),'utf8');
    assert.ok(!/(?:src|href)=["']\/(?!\/)/.test(text));
    assert.ok(!text.includes('http://127.0.0.1'));
  }
});
