import { slides, sources, checked } from './content.js';
import { visual } from './visuals.js';

const $ = id => document.getElementById(id);
const total = slides.reduce((n, s) => n + s.duration, 0);
const offsets = slides.map((_, i) => slides.slice(0, i).reduce((n, s) => n + s.duration, 0));

let lang = localStorage.getItem('fth_presentation_lang') || 'en';
let fxEnabled = localStorage.getItem('fth_presentation_fx') !== 'false';
let index = 0, elapsed = 0, playing = false, voiceEnabled = true, speaking = false;
let lastTick = 0, speechEpoch = 0, chosenVoice = 'neural', toastTimer, panel = '';
let pauseTimer = null, transitioning = false;

const synth = window.speechSynthesis;
const recorded = $('narration-audio');

const ui = {
  th: {
    play: 'เล่น',
    pause: 'หยุดชั่วคราว',
    notes: 'บทพูด',
    evidence: 'หลักฐาน',
    voiceOn: 'เสียง: เปิด',
    voiceOff: 'เสียง: ปิด',
    fxOn: 'เอฟเฟกต์: เปิด',
    fxOff: 'เอฟเฟกต์: ปิด',
    overview: `ภาพรวม ${slides.length} สไลด์`,
    sourceTitle: 'หลักฐานและขอบเขตข้อเสนอ',
    scriptTitle: 'บทบรรยาย',
    back: 'ก่อนหน้า',
    next: 'ถัดไป',
    voiceHelp: 'เสียง Neural สตูดิโอความคมชัดสูง • พัก 2 วินาทีระหว่างสไลด์ • ปรับเปลี่ยนภาษาได้ทันที',
    voiceLabel: 'เลือกเสียงบรรยาย',
    defaultVoice: 'เสียงเริ่มต้นของระบบ',
    full: 'เต็มจอ',
    draft: 'DISCUSSION DRAFT · ข้อเสนอนำร่อง',
    illustrative: 'ภาพแสดงแนวคิด ไม่ใช่ข้อมูลลูกค้า',
    checked: 'ตรวจแหล่งข้อมูล',
    research: 'บันทึก research',
    download: 'ดาวน์โหลดบทพูด TH / EN',
    motion: 'พัก / เล่น motion',
    done: 'จบการนำเสนอ ขอบคุณครับ',
    missing: 'ยังไม่พบเสียงสำหรับภาษานี้ กรุณาเลือกเสียงหรือติดตั้งเสียงในระบบ',
    speechError: 'เสียงอ่านไม่พร้อมใช้งาน — เล่นต่อแบบไม่มีเสียงได้',
    security: 'แนวคิด workflow ที่เสนอต้องทดสอบเทียบ standard ใน tenant เป้าหมาย ข้อมูล Community เป็นเคสตัวอย่าง ไม่ใช่สถิติความแพร่หลาย และไม่ใช่หลักฐานว่า standard ไม่มีความสามารถนั้น',
    navHint: '← → เปลี่ยนหน้า · Space เล่น/หยุด · T สลับเอฟเฟกต์ · N บทพูด · E หลักฐาน · F เต็มจอ · M พัก motion',
    duration: 'วินาที'
  },
  en: {
    play: 'Play',
    pause: 'Pause',
    notes: 'Script',
    evidence: 'Evidence',
    voiceOn: 'Voice: on',
    voiceOff: 'Voice: off',
    fxOn: 'FX: ON',
    fxOff: 'FX: OFF',
    overview: `${slides.length}-slide overview`,
    sourceTitle: 'Evidence & proposal boundaries',
    scriptTitle: 'Narration',
    back: 'Previous',
    next: 'Next',
    voiceHelp: 'Studio neural audio playback • 2-second natural pacing buffer • Instant EN/TH track toggle',
    voiceLabel: 'Narration voice',
    defaultVoice: 'System default voice',
    full: 'Fullscreen',
    draft: 'DISCUSSION DRAFT · Pilot proposal',
    illustrative: 'Conceptual illustration · No customer data',
    checked: 'Sources checked',
    research: 'Research notes',
    download: 'Download TH / EN script',
    motion: 'Pause / resume motion',
    done: 'Presentation complete. Thank you.',
    missing: 'No voice found for this language. Choose a voice or install one in your system.',
    speechError: 'Narration is unavailable. You can continue without voice.',
    security: 'These proposed workflows require a standard-capability benchmark in the target tenant. Community cases demonstrate reported friction, not prevalence or proof that a capability is absent from standard.',
    navHint: '← → Navigate · Space Play/pause · T Toggle FX · N Script · E Evidence · F Fullscreen · M Motion',
    duration: 'seconds'
  }
};

function copy() { return ui[lang]; }
function stamp(value) {
  const m = Math.floor(value / 60).toString().padStart(2, '0');
  const s = Math.floor(value % 60).toString().padStart(2, '0');
  return `${m}:${s}`;
}

function toast(message) {
  $('status').textContent = message;
  $('status').classList.add('visible');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => $('status').classList.remove('visible'), 5000);
}

function stopSpeech(reset = true) {
  speechEpoch++;
  speaking = false;
  clearTimeout(pauseTimer);
  pauseTimer = null;
  synth?.cancel();
  recorded.pause();
  if (reset) recorded.currentTime = 0;
}

function onSlideFinished() {
  if (!playing) return;
  speaking = false;
  clearTimeout(pauseTimer);
  // User requested: exactly 2s pause before advancing slides
  pauseTimer = setTimeout(() => {
    if (!playing) return;
    if (index < slides.length - 1) {
      navigate(index + 1);
    } else {
      elapsed = slides[index].duration;
      setPlaying(false);
      updateControls();
      toast(copy().done);
    }
  }, 2000);
}

function updateControls() {
  const c = copy();
  const durMin = Math.ceil(total / 60);
  $('play').innerHTML = `${playing ? 'Ⅱ' : '▶'} <span>${playing ? c.pause : `${c.play} ${durMin} min`}</span>`;
  $('play').setAttribute('aria-label', playing ? c.pause : `${c.play} ${durMin} min`);
  $('voice').innerHTML = `♬ <span>${voiceEnabled ? c.voiceOn : c.voiceOff}</span>`;
  $('voice').setAttribute('aria-pressed', String(voiceEnabled));
  $('voice').setAttribute('aria-label', voiceEnabled ? c.voiceOn : c.voiceOff);
  $('notes').textContent = c.notes;
  $('evidence').textContent = c.evidence;

  // Language buttons
  if ($('lang-en')) {
    $('lang-en').classList.toggle('active', lang === 'en');
    $('lang-en').setAttribute('aria-pressed', String(lang === 'en'));
  }
  if ($('lang-th')) {
    $('lang-th').classList.toggle('active', lang === 'th');
    $('lang-th').setAttribute('aria-pressed', String(lang === 'th'));
  }

  // FX Toggle button
  if ($('fx-toggle')) {
    $('fx-toggle').classList.toggle('active', fxEnabled);
    $('fx-toggle').setAttribute('aria-pressed', String(fxEnabled));
    $('fx-toggle').innerHTML = `⚡ <span>${fxEnabled ? c.fxOn : c.fxOff}</span>`;
  }

  $('fullscreen').setAttribute('aria-label', c.full);
  $('page').textContent = `${String(index + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')}`;
  $('prev').disabled = index === 0;
  $('next').disabled = index === slides.length - 1;

  const position = offsets[index] + Math.min(elapsed, slides[index].duration);
  $('clock').textContent = `${stamp(position)} / ${stamp(total)}`;

  const bar = document.querySelector('.progress');
  if (bar) {
    bar.setAttribute('aria-valuemax', String(Math.floor(total)));
    bar.setAttribute('aria-valuenow', String(Math.floor(position)));
    bar.querySelector('i').style.width = `${Math.min(100, (position / total) * 100)}%`;
  }

  $('dots').querySelectorAll('button').forEach((button, i) => {
    button.setAttribute('aria-current', String(i === index));
  });
}

function render() {
  const s = slides[index], c = copy();
  document.documentElement.lang = lang;
  $('stage').innerHTML = `<section class="slide ${s.id} ${s.theme} enter" aria-labelledby="slide-title"><div class="slide-copy"><div class="chapter">${s.chapter}</div><h1 id="slide-title">${s.title[lang]}</h1><p class="subtitle">${s.subtitle[lang]}</p><div class="takeaway">${s.takeaway[lang]}</div></div><div class="slide-art">${visual(s, lang)}</div><div class="slide-meta"><span>${c.draft}</span><span>${c.illustrative}</span></div></section>`;
  $('dots').innerHTML = slides.map((s, i) => `<button data-slide="${i}" aria-label="${i + 1}: ${s.title[lang].replaceAll('\n', ' ')}" aria-current="${i === index}"></button>`).join('');
  updateControls();
}

function navigate(next, { hash = true } = {}) {
  const targetIndex = Math.max(0, Math.min(slides.length - 1, next));
  if (targetIndex === index && document.querySelector('.slide')) return;

  stopSpeech();
  elapsed = 0;

  if (fxEnabled && targetIndex !== index && !transitioning) {
    transitioning = true;
    const sNext = slides[targetIndex];
    const transEl = $('slide-transition');
    const badgeEl = $('transition-badge');
    const titleEl = $('transition-title');

    if (badgeEl) badgeEl.textContent = lang === 'en' ? 'SYSTEM DISPATCH' : 'กำลังเปลี่ยนสไลด์';
    if (titleEl) titleEl.textContent = `${sNext.chapter} · ${sNext.title[lang].replaceAll('\n', ' ')}`;

    if (transEl) transEl.classList.add('active');

    setTimeout(() => {
      index = targetIndex;
      if (hash) history.replaceState(null, '', `#${index + 1}`);
      render();
      if (playing && voiceEnabled) speak();
    }, 360);

    setTimeout(() => {
      if (transEl) transEl.classList.remove('active');
      transitioning = false;
    }, 760);
    return;
  }

  index = targetIndex;
  if (hash) history.replaceState(null, '', `#${index + 1}`);
  render();
  if (playing && voiceEnabled) speak();
}

function setPlaying(value) {
  playing = value;
  lastTick = performance.now();
  if (!playing) stopSpeech(false);
  else if (voiceEnabled) speak();
  updateControls();
}

function setLang(newLang) {
  if (newLang !== 'en' && newLang !== 'th') return;
  stopSpeech();
  lang = newLang;
  localStorage.setItem('fth_presentation_lang', lang);
  chosenVoice = 'neural';
  render();
  if ($('drawer').open) drawPanel();
  if (playing && voiceEnabled) speak();
}

function toggleFx() {
  fxEnabled = !fxEnabled;
  localStorage.setItem('fth_presentation_fx', String(fxEnabled));
  updateControls();
  toast(fxEnabled ? (lang === 'th' ? 'เปิดเอฟเฟกต์คั่นเปลี่ยนสไลด์แล้ว' : 'Transition motion graphics enabled') : (lang === 'th' ? 'ปิดเอฟเฟกต์คั่นเปลี่ยนสไลด์แล้ว' : 'Transition motion graphics disabled'));
}

function voices() {
  return synth ? synth.getVoices().filter(v => v.lang.toLowerCase().startsWith(lang === 'th' ? 'th' : 'en')) : [];
}

function speechChunks(text) {
  if (lang === 'th') return text.split(/\n\s*\n/).map(p => p.trim()).filter(Boolean);
  return text.split(/(?<=[.!?])\s+/).map(p => p.trim()).filter(Boolean);
}

function speak() {
  stopSpeech(false);
  if (!voiceEnabled) return;

  // Use Neural Studio recorded audio for both EN and TH
  if (chosenVoice === 'neural' && slides[index].audio?.[lang]) {
    const epoch = speechEpoch, path = slides[index].audio[lang];
    if (recorded.getAttribute('src') !== path) {
      recorded.src = path;
      recorded.currentTime = 0;
    }
    speaking = true;
    recorded.onended = () => {
      if (epoch === speechEpoch) {
        speaking = false;
        onSlideFinished();
      }
    };
    const failed = () => {
      if (epoch !== speechEpoch) return;
      speaking = false;
      voiceEnabled = false;
      updateControls();
      toast(copy().speechError);
    };
    recorded.onerror = failed;
    recorded.play().catch(failed);
    return;
  }

  // Fallback to browser Web Speech API
  if (!synth) {
    voiceEnabled = false;
    updateControls();
    toast(copy().speechError);
    return;
  }
  const available = voices();
  if (!available.length) {
    voiceEnabled = false;
    updateControls();
    toast(copy().missing);
    return;
  }

  const epoch = speechEpoch;
  const voice = available.find(v => v.voiceURI === chosenVoice) || available.find(v => v.localService) || available[0];
  const chunks = speechChunks(slides[index].notes[lang]);
  let cursor = 0;
  speaking = true;

  function queue() {
    if (epoch !== speechEpoch || !playing || !voiceEnabled) { speaking = false; return; }
    if (cursor >= chunks.length) {
      speaking = false;
      onSlideFinished();
      return;
    }
    const u = new SpeechSynthesisUtterance(chunks[cursor++]);
    u.voice = voice;
    u.lang = voice.lang;
    u.rate = lang === 'th' ? 0.97 : 1;
    u.pitch = 1;
    u.onend = queue;
    u.onerror = e => {
      if (epoch !== speechEpoch) return;
      speaking = false;
      if (e.error !== 'canceled' && e.error !== 'interrupted') {
        voiceEnabled = false;
        updateControls();
        toast(copy().speechError);
      }
    };
    synth.speak(u);
  }
  queue();
}

function drawPanel() {
  const s = slides[index], c = copy(), title = s.title[lang].replaceAll('\n', ' ');
  if (panel === 'overview') {
    $('drawer-title').textContent = c.overview;
    $('drawer-body').innerHTML = `<p class="hint">${c.navHint}</p><div class="slide-list">${slides.map((s, i) => `<button data-jump="${i}"><b>${String(i + 1).padStart(2, '0')}</b><span>${s.title[lang]}</span><small>${s.duration}s</small></button>`).join('')}</div><div class="panel-nav"><button data-motion>${c.motion}</button><a class="download" href="docs/research.md" target="_blank" rel="noopener">${c.research} ↗</a></div>`;
  } else if (panel === 'notes') {
    $('drawer-title').textContent = `${c.scriptTitle} · ${String(index + 1).padStart(2, '0')}`;
    $('drawer-body').innerHTML = `<h3>${title}</h3><p class="hint">${s.duration} ${c.duration} · ${c.voiceHelp}</p><p class="narration-text">${s.notes[lang]}</p><div class="audio-preview"><label>${lang === 'th' ? 'ฟังบทพูดเฉพาะหน้านี้' : 'Listen to narration for this slide'}</label><audio controls preload="metadata" src="${s.audio?.[lang]}"></audio></div><div class="voice-settings"><label for="voice-choice">${c.voiceLabel}</label><select id="voice-choice"><option value="neural" ${chosenVoice === 'neural' ? 'selected' : ''}>${lang === 'th' ? 'Microsoft Niwat Neural · ไทย (แนะนำ)' : 'Microsoft Andrew Neural · English (Recommended)'}</option><option value="" ${chosenVoice === '' ? 'selected' : ''}>${c.defaultVoice}</option>${voices().map(v => `<option value="${encodeURIComponent(v.voiceURI)}" ${v.voiceURI === chosenVoice ? 'selected' : ''}>${v.name.replaceAll('<', '&lt;')} (${v.lang})</option>`).join('')}</select></div><div class="panel-nav"><button data-panel-prev ${index === 0 ? 'disabled' : ''}>← ${c.back}</button><a class="download" href="docs/narration.md" download>${c.download}</a><button data-panel-next ${index === slides.length - 1 ? 'disabled' : ''}>${c.next} →</button></div>`;
  } else {
    $('drawer-title').textContent = c.sourceTitle;
    $('drawer-body').innerHTML = `<h3>${title}</h3><p class="hint">${c.security}<br>${c.checked}: ${checked}</p>${s.sources.map(key => {
      const src = sources[key];
      return `<article class="source"><a href="${src.url}" target="_blank" rel="noopener noreferrer">${src.title} ↗</a><small>${src.kind}</small><p>${lang === 'th' ? src.note : englishEvidence[key] || 'See the linked primary source. Specific applicability must be checked in the target tenant.'}</p></article>`;
    }).join('')}<div class="panel-nav"><button data-panel-prev ${index === 0 ? 'disabled' : ''}>← ${c.back}</button><a class="download" href="docs/research.md" target="_blank" rel="noopener">${c.research} ↗</a><button data-panel-next ${index === slides.length - 1 ? 'disabled' : ''}>${c.next} →</button></div>`;
  }
}

const englishEvidence = {
  catalog: 'Documents existing Finance and SCM experiences, including summaries, collections, demand planning and warehouse workload insights. Check each detailed feature page for availability.',
  update: 'Microsoft announces ERP MCP and ERP plugin for Copilot Cowork as GA, Procurement impact analysis in public preview, and further AP and Finance Agent investments. This is a mix of available and upcoming functionality.',
  roadmap: 'The live roadmap was opened, but the text extraction does not expose every dynamic feature listing. A missing search result is not proof of absence. Check individual entries and the target tenant before investing.',
  recon: 'The setup page labels Account Reconciliation as production-ready preview and requires Finance 10.0.46 or later. It is an existing subledger-to-GL scenario, not a new opportunity to rebuild.',
  procurement: 'Supplier communications are documented as production-ready preview with prerequisites including SCM 10.0.44 or later. Availability in a particular tenant is not assumed.',
  vendorCommunity: 'A supplier postponement request requires checking downstream production impact and updating PO delivery dates under human sign-off.',
  taxCommunity: 'Thai withholding tax (P.N.D. 3/53) and 7% VAT invoice settlement require exact statutory validation against D365 vendor ledger journals.',
  apStandard: 'Two-way, three-way, tolerance and charges matching already exist. The proposed extension is a company-specific evidence and handoff workflow.',
  apAutomation: 'Standard automation already supports matching, workflow submission, posting simulation and history. Do not rebuild invoice capture or matching.',
  mcp: 'ERP MCP supports data and business actions, including secured custom APIs. Verify available tools, entities, versions and integration needs in the target environment.',
  security: 'MCP preserves F&O identity, permissions and validation. Agent-client data retention and onward data movement need a separate review.',
  logo: 'Fujitsu Red Infinity symbol mark unified on dark executive theme with Dynamics 365 and Microsoft Copilot.'
};

function openPanel(type) {
  setPlaying(false);
  panel = type;
  drawPanel();
  $('drawer').showModal();
}

$('drawer-body').addEventListener('click', e => {
  const jump = e.target.closest('[data-jump]');
  if (jump) { navigate(Number(jump.dataset.jump)); $('drawer').close(); return; }
  if (e.target.closest('[data-panel-prev]')) { navigate(index - 1); drawPanel(); }
  if (e.target.closest('[data-panel-next]')) { navigate(index + 1); drawPanel(); }
  if (e.target.closest('[data-motion]')) document.body.classList.toggle('motion-paused');
});

$('drawer-body').addEventListener('change', e => {
  if (e.target.id === 'voice-choice') chosenVoice = decodeURIComponent(e.target.value);
});

$('close-drawer').onclick = () => $('drawer').close();
$('drawer').addEventListener('close', () => { $('drawer-body').querySelectorAll('audio').forEach(a => a.pause()); });
$('drawer').addEventListener('click', e => {
  if (e.target === $('drawer')) {
    const r = $('drawer').getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) $('drawer').close();
  }
});

$('notes').onclick = () => openPanel('notes');
$('evidence').onclick = () => openPanel('evidence');
$('menu').onclick = () => openPanel('overview');
$('next').onclick = () => navigate(index + 1);
$('prev').onclick = () => navigate(index - 1);
$('dots').onclick = e => {
  const button = e.target.closest('[data-slide]');
  if (button) navigate(Number(button.dataset.slide));
};

// Language switcher clicks
if ($('lang-en')) $('lang-en').onclick = () => setLang('en');
if ($('lang-th')) $('lang-th').onclick = () => setLang('th');
if ($('fx-toggle')) $('fx-toggle').onclick = toggleFx;

$('play').onclick = () => {
  if (!playing && index === slides.length - 1 && elapsed >= slides[index].duration) navigate(0);
  setPlaying(!playing);
};

$('voice').onclick = () => {
  const hasRecorded = chosenVoice === 'neural' && slides[index].audio?.[lang];
  if (!synth && !hasRecorded) { toast(copy().speechError); return; }
  voiceEnabled = !voiceEnabled;
  if (voiceEnabled && !hasRecorded && !voices().length) {
    voiceEnabled = false;
    toast(copy().missing);
  }
  if (playing && voiceEnabled) speak(); else stopSpeech();
  updateControls();
};

async function fullscreen() {
  try {
    if (document.fullscreenElement) await document.exitFullscreen();
    else await document.documentElement.requestFullscreen();
  } catch {
    toast(lang === 'th' ? 'ใช้ปุ่มเต็มจอของเบราว์เซอร์ได้เช่นกัน' : 'You can also use your browser’s fullscreen command.');
  }
}
$('fullscreen').onclick = fullscreen;

document.addEventListener('keydown', e => {
  if ($('drawer').open || e.ctrlKey || e.metaKey || e.altKey || /INPUT|SELECT|TEXTAREA/.test(e.target.tagName)) return;
  if (e.code === 'Space' && !/BUTTON|A/.test(e.target.tagName)) { e.preventDefault(); $('play').click(); }
  else if (e.key === 'ArrowRight') { e.preventDefault(); if (index < slides.length - 1) navigate(index + 1); }
  else if (e.key === 'ArrowLeft') { e.preventDefault(); if (index > 0) navigate(index - 1); }
  else if (e.key.toLowerCase() === 't') toggleFx();
  else if (e.key.toLowerCase() === 'n') openPanel('notes');
  else if (e.key.toLowerCase() === 'e') openPanel('evidence');
  else if (e.key.toLowerCase() === 'f') fullscreen();
  else if (e.key.toLowerCase() === 'm') document.body.classList.toggle('motion-paused');
});

let touchStart = null;
$('stage').addEventListener('touchstart', e => {
  touchStart = { x: e.changedTouches[0].clientX, y: e.changedTouches[0].clientY };
}, { passive: true });

$('stage').addEventListener('touchend', e => {
  if (!touchStart) return;
  const dx = e.changedTouches[0].clientX - touchStart.x, dy = e.changedTouches[0].clientY - touchStart.y;
  if (Math.abs(dx) > 70 && Math.abs(dx) > Math.abs(dy) * 1.5) navigate(index + (dx < 0 ? 1 : -1));
  touchStart = null;
}, { passive: true });

window.addEventListener('hashchange', () => {
  const n = Number(location.hash.slice(1));
  if (Number.isInteger(n) && n >= 1 && n <= slides.length) navigate(n - 1, { hash: false });
});

document.addEventListener('visibilitychange', () => { if (document.hidden && playing) setPlaying(false); });
window.addEventListener('pagehide', stopSpeech);
if (synth) synth.addEventListener('voiceschanged', () => { if ($('drawer').open && panel === 'notes') drawPanel(); });

function tick(now) {
  if (playing) {
    elapsed += (now - lastTick) / 1000;
    // If playing in silent mode (no voice) and elapsed reached slide duration, trigger 2s pause
    if (!voiceEnabled && elapsed >= slides[index].duration && !pauseTimer) {
      onSlideFinished();
    }
    updateControls();
  }
  lastTick = now;
  requestAnimationFrame(tick);
}

const initial = Number(location.hash.slice(1));
if (Number.isInteger(initial) && initial >= 1 && initial <= slides.length) index = initial - 1;

render();
requestAnimationFrame(tick);
