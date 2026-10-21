import { slides, sources, checked } from './content.js';
import { visual } from './visuals.js';

const $=id=>document.getElementById(id);
const total=slides.reduce((n,s)=>n+s.duration,0);
const offsets=slides.map((_,i)=>slides.slice(0,i).reduce((n,s)=>n+s.duration,0));
let lang='th', index=0, elapsed=0, playing=false, voiceEnabled=true, speaking=false;
let lastTick=0, speechEpoch=0, chosenVoice='neural', toastTimer, panel='';
const synth=window.speechSynthesis;
const recorded=$('narration-audio');
const ui={
  th:{play:'เล่น 8 นาที',pause:'หยุดชั่วคราว',notes:'บทพูด',evidence:'หลักฐาน',voiceOn:'เสียง: เปิด',voiceOff:'เสียง: ปิด',overview:'ภาพรวม 10 สไลด์',sourceTitle:'หลักฐานและขอบเขตข้อเสนอ',scriptTitle:'บทบรรยาย',back:'ก่อนหน้า',next:'ถัดไป',voiceHelp:'เสียงไทย Neural ที่สร้างเป็นไฟล์แล้ว • หยุดและเล่นต่อได้จากจุดเดิม • ภาษาอังกฤษใช้เสียงจากเบราว์เซอร์ • ระบบรอเสียงจบก่อนเปลี่ยนหน้า',voiceLabel:'เลือกเสียงบรรยาย',defaultVoice:'เสียงเริ่มต้นของระบบ',full:'เต็มจอ',draft:'DISCUSSION DRAFT · ข้อเสนอนำร่อง',illustrative:'ภาพแสดงแนวคิด ไม่ใช่ข้อมูลลูกค้า',checked:'ตรวจแหล่งข้อมูล',research:'บันทึก research',download:'ดาวน์โหลดบทพูด TH / EN',motion:'พัก / เล่น motion',done:'จบการนำเสนอ ขอบคุณครับ',missing:'ยังไม่พบเสียงสำหรับภาษานี้ กรุณาเลือกเสียงหรือติดตั้งเสียงในระบบ',speechError:'เสียงอ่านไม่พร้อมใช้งาน — เล่นต่อแบบไม่มีเสียงได้',security:'แนวคิด workflow ที่เสนอต้องทดสอบเทียบ standard ใน tenant เป้าหมาย ข้อมูล Community เป็นเคสตัวอย่าง ไม่ใช่สถิติความแพร่หลาย และไม่ใช่หลักฐานว่า standard ไม่มีความสามารถนั้น',navHint:'← → เปลี่ยนหน้า · Space เล่น/หยุด · N บทพูด · E หลักฐาน · F เต็มจอ · M พัก motion',duration:'วินาที'},
  en:{play:'Play 8 min',pause:'Pause',notes:'Script',evidence:'Evidence',voiceOn:'Voice: on',voiceOff:'Voice: off',overview:'10-slide overview',sourceTitle:'Evidence & proposal boundaries',scriptTitle:'Narration',back:'Previous',next:'Next',voiceHelp:'Thai uses a pre-generated neural voice. English uses installed browser voices. Silent playback is 8 minutes; each slide waits for narration to finish.',voiceLabel:'Narration voice',defaultVoice:'System default voice',full:'Fullscreen',draft:'DISCUSSION DRAFT · Pilot proposal',illustrative:'Conceptual illustration · No customer data',checked:'Sources checked',research:'Research notes',download:'Download TH / EN script',motion:'Pause / resume motion',done:'Presentation complete. Thank you.',missing:'No voice found for this language. Choose a voice or install one in your system.',speechError:'Narration is unavailable. You can continue without voice.',security:'These proposed workflows require a standard-capability benchmark in the target tenant. Community cases demonstrate reported friction, not prevalence or proof that a capability is absent from standard.',navHint:'← → Navigate · Space Play/pause · N Script · E Evidence · F Fullscreen · M Motion',duration:'seconds'}
};
function copy(){return ui[lang];}
function stamp(value){return `${Math.floor(value/60).toString().padStart(2,'0')}:${Math.floor(value%60).toString().padStart(2,'0')}`;}
function toast(message){$('status').textContent=message;$('status').classList.add('visible');clearTimeout(toastTimer);toastTimer=setTimeout(()=>$('status').classList.remove('visible'),5000);}
function stopSpeech(reset=true){speechEpoch++;speaking=false;synth?.cancel();recorded.pause();if(reset)recorded.currentTime=0;}
function updateControls(){
  const c=copy();
  $('play').innerHTML=`${playing?'Ⅱ':'▶'} <span>${playing?c.pause:c.play}</span>`;
  $('play').setAttribute('aria-label',playing?c.pause:c.play);
  $('voice').innerHTML=`♬ <span>${voiceEnabled?c.voiceOn:c.voiceOff}</span>`;
  $('voice').setAttribute('aria-pressed',String(voiceEnabled));
  $('voice').setAttribute('aria-label',voiceEnabled?c.voiceOn:c.voiceOff);
  $('notes').textContent=c.notes;$('evidence').textContent=c.evidence;
  $('lang').innerHTML=lang==='th'?'TH <span>/ EN</span>':'EN <span>/ TH</span>';
  $('lang').setAttribute('aria-label',lang==='th'?'Switch to English':'เปลี่ยนเป็นภาษาไทย');
  $('fullscreen').setAttribute('aria-label',c.full);
  $('page').textContent=`${String(index+1).padStart(2,'0')} / 10`;
  $('prev').disabled=index===0;$('next').disabled=index===slides.length-1;
  const position=offsets[index]+Math.min(elapsed,slides[index].duration);
  $('clock').textContent=`${stamp(position)} / 08:00`;
  const bar=document.querySelector('.progress');bar.setAttribute('aria-valuenow',String(Math.floor(position)));bar.querySelector('i').style.width=`${position/total*100}%`;
  $('dots').querySelectorAll('button').forEach((button,i)=>button.setAttribute('aria-current',String(i===index)));
}
function render(){
  const s=slides[index],c=copy();document.documentElement.lang=lang;
  $('stage').innerHTML=`<section class="slide ${s.id} ${s.theme} enter" aria-labelledby="slide-title"><div class="slide-copy"><div class="chapter">${s.chapter}</div><h1 id="slide-title">${s.title[lang]}</h1><p class="subtitle">${s.subtitle[lang]}</p><div class="takeaway">${s.takeaway[lang]}</div></div><div class="slide-art">${visual(s,lang)}</div><div class="slide-meta"><span>${c.draft}</span><span>${c.illustrative}</span></div></section>`;
  $('dots').innerHTML=slides.map((s,i)=>`<button data-slide="${i}" aria-label="${i+1}: ${s.title[lang].replaceAll('\n',' ')}" aria-current="${i===index}"></button>`).join('');
  updateControls();
}
function navigate(next,{hash=true}={}){
  stopSpeech();index=Math.max(0,Math.min(slides.length-1,next));elapsed=0;
  if(hash)history.replaceState(null,'',`#${index+1}`);
  render();if(playing&&voiceEnabled)speak();
}
function setPlaying(value){
  playing=value;lastTick=performance.now();
  if(!playing)stopSpeech(false);else if(voiceEnabled)speak();
  updateControls();
}
function voices(){return synth?synth.getVoices().filter(v=>v.lang.toLowerCase().startsWith(lang==='th'?'th':'en')):[];}
function speechChunks(text){
  // Never split Thai mid-thought just to satisfy a character count.
  if(lang==='th')return text.split(/\n\s*\n/).map(p=>p.trim()).filter(Boolean);
  return text.split(/(?<=[.!?])\s+/).map(p=>p.trim()).filter(Boolean);
}
function speak(){
  stopSpeech(false);if(!voiceEnabled)return;
  if(lang==='th'&&chosenVoice==='neural'&&slides[index].audio?.th){
    const epoch=speechEpoch,path=slides[index].audio.th;
    if(recorded.getAttribute('src')!==path){recorded.src=path;recorded.currentTime=0;}
    speaking=true;
    recorded.onended=()=>{if(epoch===speechEpoch)speaking=false;};
    const failed=()=>{if(epoch!==speechEpoch)return;speaking=false;voiceEnabled=false;updateControls();toast(copy().speechError);};
    recorded.onerror=failed;
    recorded.play().catch(failed);
    return;
  }
  if(!synth){voiceEnabled=false;updateControls();toast(copy().speechError);return;}
  const available=voices();
  if(!available.length){voiceEnabled=false;updateControls();toast(copy().missing);return;}
  const epoch=speechEpoch;
  const voice=available.find(v=>v.voiceURI===chosenVoice)||available.find(v=>v.localService)||available[0];
  const chunks=speechChunks(slides[index].notes[lang]);let cursor=0;speaking=true;
  function queue(){
    if(epoch!==speechEpoch||!playing||!voiceEnabled){speaking=false;return;}
    if(cursor>=chunks.length){speaking=false;return;}
    const u=new SpeechSynthesisUtterance(chunks[cursor++]);u.voice=voice;u.lang=voice.lang;u.rate=lang==='th'?.97:1;u.pitch=1;
    u.onend=queue;u.onerror=e=>{if(epoch!==speechEpoch)return;speaking=false;if(e.error!=='canceled'&&e.error!=='interrupted'){voiceEnabled=false;updateControls();toast(copy().speechError);}};
    synth.speak(u);
  }
  queue();
}
function drawPanel(){
  const s=slides[index],c=copy(),title=s.title[lang].replaceAll('\n',' ');
  if(panel==='overview'){
    $('drawer-title').textContent=c.overview;
    $('drawer-body').innerHTML=`<p class="hint">${c.navHint}</p><div class="slide-list">${slides.map((s,i)=>`<button data-jump="${i}"><b>${String(i+1).padStart(2,'0')}</b><span>${s.title[lang]}</span><small>${s.duration}s</small></button>`).join('')}</div><div class="panel-nav"><button data-motion>${c.motion}</button><a class="download" href="docs/research.md" target="_blank" rel="noopener">${c.research} ↗</a></div>`;
  }else if(panel==='notes'){
    $('drawer-title').textContent=`${c.scriptTitle} · ${String(index+1).padStart(2,'0')}`;
    $('drawer-body').innerHTML=`<h3>${title}</h3><p class="hint">${s.duration} ${c.duration} · ${c.voiceHelp}</p><p class="narration-text">${s.notes[lang]}</p>${lang==='th'?`<div class="audio-preview"><label>ฟังบทพูดเฉพาะหน้านี้</label><audio controls preload="metadata" src="${s.audio.th}"></audio></div>`:''}<div class="voice-settings"><label for="voice-choice">${c.voiceLabel}</label><select id="voice-choice">${lang==='th'?`<option value="neural" ${chosenVoice==='neural'?'selected':''}>Microsoft Niwat Neural · ไทย (แนะนำ)</option>`:''}<option value="" ${chosenVoice===''?'selected':''}>${c.defaultVoice}</option>${voices().map(v=>`<option value="${encodeURIComponent(v.voiceURI)}" ${v.voiceURI===chosenVoice?'selected':''}>${v.name.replaceAll('<','&lt;')} (${v.lang})</option>`).join('')}</select></div><div class="panel-nav"><button data-panel-prev ${index===0?'disabled':''}>← ${c.back}</button><a class="download" href="docs/narration.md" download>${c.download}</a><button data-panel-next ${index===9?'disabled':''}>${c.next} →</button></div>`;
  }else{
    $('drawer-title').textContent=c.sourceTitle;
    $('drawer-body').innerHTML=`<h3>${title}</h3><p class="hint">${c.security}<br>${c.checked}: ${checked}</p>${s.sources.map(key=>{const src=sources[key];return `<article class="source"><a href="${src.url}" target="_blank" rel="noopener noreferrer">${src.title} ↗</a><small>${src.kind}</small><p>${lang==='th'?src.note:englishEvidence[key]||'See the linked primary source. Specific applicability must be checked in the target tenant.'}</p></article>`;}).join('')}<div class="panel-nav"><button data-panel-prev ${index===0?'disabled':''}>← ${c.back}</button><a class="download" href="docs/research.md" target="_blank" rel="noopener">${c.research} ↗</a><button data-panel-next ${index===9?'disabled':''}>${c.next} →</button></div>`;
  }
}
const englishEvidence={
  catalog:'Documents existing Finance and SCM experiences, including summaries, collections, demand planning and warehouse workload insights. Check each detailed feature page for availability.',
  update:'Microsoft announces ERP MCP and ERP plugin for Copilot Cowork as GA, Procurement impact analysis in public preview, and further AP and Finance Agent investments. This is a mix of available and upcoming functionality.',
  roadmap:'The live roadmap was opened, but the text extraction does not expose every dynamic feature listing. A missing search result is not proof of absence. Check individual entries and the target tenant before investing.',
  recon:'The setup page labels Account Reconciliation as production-ready preview and requires Finance 10.0.46 or later. It is an existing subledger-to-GL scenario, not a new opportunity to rebuild.',
  procurement:'Supplier communications are documented as production-ready preview with prerequisites including SCM 10.0.44 or later. Availability in a particular tenant is not assumed.',
  apCommunity:'A user reports posting blocked by product-receipt quantity after discrepancy approval. Suggested answers discuss validations and receipt completeness. It demonstrates investigation friction, not a missing matching engine. Posting date was not exposed in the readable page.',
  apStandard:'Two-way, three-way, tolerance and charges matching already exist. The proposed extension is a company-specific evidence and handoff workflow.',
  apAutomation:'Standard automation already supports matching, workflow submission, posting simulation and history. Do not rebuild invoice capture or matching.',
  costCommunity:'A reported zero-quantity residual-value case was resolved around main/transit warehouse site setup. It is one case, not a universal cause. Posting date was not exposed in the readable page.',
  costStandard:'Inventory close already includes settlements, open-quantity checks and warnings. The original engine remains responsible for cost calculations.',
  whCommunity:'A customer wanted investigation before stock write-off. The moderator described standard short-pick limitations and open work exceptions. The proposal adds evidence preparation; it does not assume AI can relocate stock.',
  whCase2:'The discussion points to open counting work and worker configuration. Treat it as multi-step investigation, not a confirmed software defect. Posting date was not exposed in the readable page.',
  whStandard:'Standard work exceptions, item reallocation and adjustment configuration are available. Use the existing counting and stock-control process.',
  prodCommunity:'A disabled variance option was resolved by the costing-model prerequisite. This is standard configuration knowledge, not a missing AI feature. The proposed shop-floor evidence workflow remains a hypothesis.',
  prodStandard:'Production variance analysis and reports already exist for standard-cost items after order ending. Figures must come from the system.',
  prodCauses:'Microsoft lists material, time, version and cost-category causes. The extension would relate those facts to authorized factory notes and require expert confirmation.',
  mcp:'ERP MCP supports data and business actions, including secured custom APIs. Verify available tools, entities, versions and integration needs in the target environment.',
  security:'MCP preserves F&O identity, permissions and validation. Agent-client data retention and onward data movement need a separate review.',
  logo:'Original Fujitsu symbol mark from a Fujitsu domain. The closing infinity artwork was supplied by the user; its motion is a presentation effect, not an animated 3D model.'
};
function openPanel(type){setPlaying(false);panel=type;drawPanel();$('drawer').showModal();}
$('drawer-body').addEventListener('click',e=>{
  const jump=e.target.closest('[data-jump]');if(jump){navigate(Number(jump.dataset.jump));$('drawer').close();return;}
  if(e.target.closest('[data-panel-prev]')){navigate(index-1);drawPanel();}
  if(e.target.closest('[data-panel-next]')){navigate(index+1);drawPanel();}
  if(e.target.closest('[data-motion]'))document.body.classList.toggle('motion-paused');
});
$('drawer-body').addEventListener('change',e=>{if(e.target.id==='voice-choice')chosenVoice=decodeURIComponent(e.target.value);});
$('close-drawer').onclick=()=>$('drawer').close();
$('drawer').addEventListener('close',()=>{$('drawer-body').querySelectorAll('audio').forEach(a=>a.pause());});
$('drawer').addEventListener('click',e=>{if(e.target===$('drawer')){const r=$('drawer').getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)$('drawer').close();}});
$('notes').onclick=()=>openPanel('notes');$('evidence').onclick=()=>openPanel('evidence');$('menu').onclick=()=>openPanel('overview');
$('next').onclick=()=>navigate(index+1);$('prev').onclick=()=>navigate(index-1);
$('dots').onclick=e=>{const button=e.target.closest('[data-slide]');if(button)navigate(Number(button.dataset.slide));};
$('lang').onclick=()=>{stopSpeech();lang=lang==='th'?'en':'th';chosenVoice=lang==='th'?'neural':'';render();if($('drawer').open)drawPanel();if(playing&&voiceEnabled)speak();};
$('play').onclick=()=>{if(!playing&&index===9&&elapsed>=slides[index].duration)navigate(0);setPlaying(!playing);};
$('voice').onclick=()=>{const hasRecorded=lang==='th'&&chosenVoice==='neural'&&slides[index].audio?.th;if(!synth&&!hasRecorded){toast(copy().speechError);return;}voiceEnabled=!voiceEnabled;if(voiceEnabled&&!hasRecorded&&!voices().length){voiceEnabled=false;toast(copy().missing);}if(playing&&voiceEnabled)speak();else stopSpeech();updateControls();};
async function fullscreen(){try{if(document.fullscreenElement)await document.exitFullscreen();else await document.documentElement.requestFullscreen();}catch{toast(lang==='th'?'ใช้ปุ่มเต็มจอของเบราว์เซอร์ได้เช่นกัน':'You can also use your browser’s fullscreen command.');}}
$('fullscreen').onclick=fullscreen;
document.addEventListener('keydown',e=>{
  if($('drawer').open||e.ctrlKey||e.metaKey||e.altKey||/INPUT|SELECT|TEXTAREA/.test(e.target.tagName))return;
  if(e.code==='Space'&&!/BUTTON|A/.test(e.target.tagName)){e.preventDefault();$('play').click();}
  else if(e.key==='ArrowRight'){e.preventDefault();if(index<9)navigate(index+1);}
  else if(e.key==='ArrowLeft'){e.preventDefault();if(index>0)navigate(index-1);}
  else if(e.key.toLowerCase()==='n')openPanel('notes');else if(e.key.toLowerCase()==='e')openPanel('evidence');else if(e.key.toLowerCase()==='f')fullscreen();else if(e.key.toLowerCase()==='m')document.body.classList.toggle('motion-paused');
});
let touchStart=null;$('stage').addEventListener('touchstart',e=>{touchStart={x:e.changedTouches[0].clientX,y:e.changedTouches[0].clientY};},{passive:true});
$('stage').addEventListener('touchend',e=>{if(!touchStart)return;const dx=e.changedTouches[0].clientX-touchStart.x,dy=e.changedTouches[0].clientY-touchStart.y;if(Math.abs(dx)>70&&Math.abs(dx)>Math.abs(dy)*1.5)navigate(index+(dx<0?1:-1));touchStart=null;},{passive:true});
window.addEventListener('hashchange',()=>{const n=Number(location.hash.slice(1));if(Number.isInteger(n)&&n>=1&&n<=10)navigate(n-1,{hash:false});});
document.addEventListener('visibilitychange',()=>{if(document.hidden&&playing)setPlaying(false);});
window.addEventListener('pagehide',stopSpeech);
if(synth)synth.addEventListener('voiceschanged',()=>{if($('drawer').open&&panel==='notes')drawPanel();});
function tick(now){if(playing){elapsed+=(now-lastTick)/1000;if(elapsed>=slides[index].duration&&!speaking){if(index<9)navigate(index+1);else{elapsed=slides[index].duration;setPlaying(false);toast(copy().done);}}updateControls();}lastTick=now;requestAnimationFrame(tick);}
const initial=Number(location.hash.slice(1));if(Number.isInteger(initial)&&initial>=1&&initial<=10)index=initial-1;
render();requestAnimationFrame(tick);
