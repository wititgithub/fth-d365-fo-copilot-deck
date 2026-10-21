const photoScenes = {
  hero: { file: 'hero', alt: 'Cinematic 3D crimson ribbon connecting business, logistics and manufacturing around an intelligence core' },
  boundary: { file: 'workflow', alt: 'Cinematic 3D enterprise workflow split-stage connecting standard ERP foundation with crystalline Copilot extension platform' },
  invoice: { file: 'ap', alt: 'Three floating glass documents: two validated and one unresolved, connected by a broken crimson link' },
  cost: { file: 'inventory', alt: 'An empty crystal inventory cube with a residual value sphere linked to a chain of containers' },
  warehouse: { file: 'warehouse', alt: 'A futuristic warehouse digital twin with a clearly highlighted empty shelf and scanning plane' },
  production: { file: 'production', alt: 'Robotic manufacturing cell with exploded material layers, a timing wheel and evidence threads' },
  architecture: { file: 'architecture', alt: 'High-tech enterprise AI cloud architecture with central Copilot Studio neural core and secure ERP data conduits' },
  priorities: { file: 'priorities', alt: 'Sleek four-stage sequential implementation priority runway with illuminated plinths and laser filaments' },
  pilot: { file: 'pilot', alt: 'Six-week pilot framework and dual-perspective ROI impact with holographic phase pillars and balanced value prisms' }
};

function cinematic(slide, lang) {
  const scene = photoScenes[slide.visual], l = slide.labels[lang];
  const sparks = Array.from({ length: 9 }, (_, i) => `<i class="scene-spark" style="--x:${12 + (i * 17) % 77}%;--y:${15 + (i * 23) % 67}%;--delay:${i * 0.63}s"></i>`).join('');
  let annotations = '', caption = '';

  if (slide.visual === 'hero') {
    annotations = `<div class="core-orbit"><i></i><i></i></div><div class="hero-data-trail"></div>`;
    caption = `<div class="cinema-caption hero-caption"><span>Dynamics 365</span><i>+</i><span>Copilot</span></div>`;
  } else if (slide.visual === 'boundary') {
    annotations = `<div class="workflow-laser-bridge"></div><div class="workflow-pulse-gate"></div><div class="workflow-badges"><div class="badge-std"><b>D365 STANDARD</b><span>${l[0]}</span></div><div class="badge-ext"><b>COPILOT EXTENSION</b><span>${l[1]}</span></div></div>`;
    caption = `<div class="cinema-caption"><span>${l[2]}</span><i class="caption-trace"></i><span>${l[3]}</span><i class="caption-trace"></i><span>${l[5]}</span><i class="caption-trace"></i><strong>${l[7]}</strong></div>`;
  } else if (slide.visual === 'invoice') {
    annotations = `<div class="verification-sweep"></div><div class="link-pulse"></div><div class="document-labels"><span>${l[0]}</span><span>${l[1]}</span><span>${l[2]}</span></div>`;
    caption = `<div class="cinema-caption"><span class="caption-index">01</span><strong>${l[5]}</strong><span class="caption-end">${l[6]}</span></div>`;
  } else if (slide.visual === 'cost') {
    annotations = `<div class="value-orbit"></div><div class="residual-label"><b>0</b><span>${l[0]}</span></div><div class="value-label"><b>฿ ?</b><span>${l[1]}</span></div>`;
    caption = `<div class="cinema-caption"><span>${l[2]}</span><i class="caption-trace"></i><span>${l[3]}</span><i class="caption-trace"></i><span>${l[4]}</span></div>`;
  } else if (slide.visual === 'warehouse') {
    annotations = `<div class="warehouse-sweep"></div><div class="stock-target"><i></i><i></i><i></i><i></i></div><div class="stock-callout"><span>SHORT PICK</span><b>${lang === 'th' ? 'จุดที่ต้องตรวจสอบ' : 'Investigate this location'}</b></div>`;
    caption = `<div class="cinema-caption"><span>${l[3]}</span><i class="caption-trace"></i><span>${l[4]}</span><i class="caption-trace"></i><span>${l[5]}</span></div>`;
  } else if (slide.visual === 'production') {
    annotations = `<div class="production-radar"></div><svg class="evidence-threads" viewBox="0 0 780 520" aria-hidden="true"><path d="M180 410Q240 300 385 170Q520 80 645 110M390 420Q385 270 385 170M630 420Q580 280 645 110"/></svg>`;
    caption = `<div class="cinema-caption"><span>${l[2]}</span><i class="caption-trace"></i><span>${l[3]}</span><i class="caption-trace"></i><span>${l[4]}</span></div>`;
  } else if (slide.visual === 'architecture') {
    annotations = `<div class="arch-core-orbit"><i></i><i></i></div><div class="arch-laser-grid"></div><div class="arch-hud-left"><b>D365 ERP & DATA</b><span>${l[0]} · ${l[1]}</span></div><div class="arch-hud-right"><b>GOVERNANCE</b><span>${l[4]} · ${l[6]}</span></div>`;
    caption = `<div class="cinema-caption"><span>${l[0]}</span><i class="caption-trace"></i><strong>${l[2]} + ${l[5]}</strong><i class="caption-trace"></i><span>${l[4]}</span></div>`;
  } else if (slide.visual === 'priorities') {
    annotations = `<div class="priorities-beacon-pulse"></div><div class="priorities-radar"></div><div class="priorities-tier-badge"><b>WAVE 1</b><span>${l[0]} · ${l[4]}</span></div><div class="priorities-stepper"><span>01</span><span>02</span><span>03</span><span>04</span></div>`;
    caption = `<div class="cinema-caption"><strong style="color:var(--red)">01 ${l[0]}</strong><i class="caption-trace"></i><span>02 ${l[1]}</span><i class="caption-trace"></i><span>03 ${l[2]}</span><i class="caption-trace"></i><span>04 ${l[3]}</span></div>`;
  } else if (slide.visual === 'pilot') {
    annotations = `<div class="pilot-laser-rail"></div><div class="pilot-phase-badges"><span>W1–2 ${l[3]}</span><span>W3–4 ${l[4]}</span><span>W5–6 ${l[5]}</span></div><div class="pilot-roi-hud"><b>DUAL ROI</b><span>${lang === 'th' ? 'ลูกค้าลดเวลา 70% · FTH AI Advisory Partner' : 'Customer 70% Time Saved · FTH AI Practice'}</span></div>`;
    caption = `<div class="cinema-caption"><span>${l[0]} ${l[3]}</span><i class="caption-trace"></i><span>${l[1]} ${l[4]}</span><i class="caption-trace"></i><span>${l[2]} ${l[5]}</span></div>`;
  }

  return `<div class="cinema-composition composition-${slide.visual}"><figure class="cinematic cinematic-${slide.visual}"><img class="cinema-image" src="assets/${scene.file}-3d-v2.png" alt="${scene.alt}" ${slide.visual === 'hero' ? 'fetchpriority="high"' : 'loading="eager"'}><div class="cinema-atmosphere" aria-hidden="true">${sparks}</div><div class="cinema-overlay">${annotations}</div><figcaption class="scene-credit">CONCEPT VISUAL · AI + MOTION DESIGN</figcaption></figure>${caption}</div>`;
}

export function visual(slide, lang) {
  if (photoScenes[slide.visual]) return cinematic(slide, lang);
  if (slide.visual === 'closing') {
    return `<div class="closing-art"><div class="closing-halo"></div><img src="assets/slide10_fujitsu_red_infinity_motion.gif" alt="User-supplied 3D red infinity ribbon motion graphic connecting Dynamics 365 and Copilot" class="closing-image"><div class="closing-orbit"></div><div class="closing-badge"><span>FUJITSU RED INFINITY ✕ DYNAMICS 365 & COPILOT</span></div></div>`;
  }
  return '';
}
