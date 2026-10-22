const photoScenes = {
  hero: { file: 'hero', alt: 'Cinematic 3D crimson ribbon connecting business, logistics and manufacturing around an intelligence core' },
  boundary: { file: 'workflow', alt: 'Cinematic 3D enterprise workflow split-stage connecting standard ERP foundation with crystalline Copilot extension platform' },
  architecture: { file: 'architecture', alt: 'High-tech enterprise AI cloud architecture with central Copilot Studio neural core and secure ERP data conduits' },
  vendorEmail: { file: 'email-vendor', alt: 'Futuristic supplier email origami envelope unfurling into delivery calendar streams under crimson approval seal' },
  taxScanning: { file: 'ap', alt: 'Three floating glass documents on a verification plinth with red inspection lens validating tax compliance and 3-way match' },
  security: { file: 'warehouse', alt: 'Enterprise zero-trust cloud boundary with protected tenant isolation, role-based access, and immutable audit trails' },
  governance: { file: 'production', alt: 'Human-in-the-loop governance console with three structured tiers of agent autonomy from assisted to supervised execution' },
  priorities: { file: 'priorities', alt: 'Sleek four-stage sequential implementation priority runway with illuminated plinths and laser filaments' },
  pilot: { file: 'pilot', alt: 'Ten-week pilot framework and dual-perspective ROI impact with holographic phase pillars and balanced value prisms' }
};

function cinematic(slide, lang) {
  const scene = photoScenes[slide.visual], l = slide.labels[lang];
  const sparks = Array.from({ length: 9 }, (_, i) => `<i class="scene-spark" style="--x:${12 + (i * 17) % 77}%;--y:${15 + (i * 23) % 67}%;--delay:${i * 0.63}s"></i>`).join('');
  let annotations = '', caption = '';

  if (slide.visual === 'hero') {
    annotations = `<div class="core-orbit"><i></i><i></i></div><div class="hero-data-trail"></div>`;
    caption = `<div class="cinema-caption hero-caption"><span>Dynamics 365</span><i>+</i><span>Copilot Studio</span></div>`;
  } else if (slide.visual === 'boundary') {
    annotations = `<div class="workflow-laser-bridge"></div><div class="workflow-pulse-gate"></div><div class="workflow-badges"><div class="badge-std"><b>D365 STANDARD</b><span>${l[0]}</span></div><div class="badge-ext"><b>COPILOT AGENTS</b><span>${l[1]}</span></div></div>`;
    caption = `<div class="cinema-caption"><span>${l[2]}</span><i class="caption-trace"></i><span>${l[3]}</span><i class="caption-trace"></i><span>${l[5]}</span><i class="caption-trace"></i><strong>${l[6]}</strong></div>`;
  } else if (slide.visual === 'architecture') {
    annotations = `<div class="arch-core-orbit"><i></i><i></i></div><div class="arch-laser-grid"></div><div class="arch-hud-left"><b>1. PERCEPTION</b><span>${l[0]}</span></div><div class="arch-hud-right"><b>3. ACTION & 4. GOVERN</b><span>${l[2]} · ${l[3]}</span></div>`;
    caption = `<div class="cinema-caption"><span>${l[0]}</span><i class="caption-trace"></i><strong>${l[1]}</strong><i class="caption-trace"></i><span>${l[2]}</span><i class="caption-trace"></i><span>${l[3]}</span></div>`;
  } else if (slide.visual === 'vendorEmail') {
    annotations = `<div class="workflow-laser-bridge"></div><div class="email-clock-gear"></div><div class="vendor-badges"><div class="badge-email"><b>INCOMING EMAIL</b><span>${l[0]}</span></div><div class="badge-d365"><b>D365 PO DRAFT</b><span>${l[3]}</span></div></div>`;
    caption = `<div class="cinema-caption"><span class="caption-index">01</span><span>${l[0]}</span><i class="caption-trace"></i><span>${l[2]}</span><i class="caption-trace"></i><strong>${l[4]}</strong></div>`;
  } else if (slide.visual === 'taxScanning') {
    annotations = `<div class="verification-sweep"></div><div class="link-pulse"></div><div class="document-labels"><span>${l[0]}</span><span>${l[1]}</span><span>${l[2]}</span></div><div class="tax-badge-hud"><b>STATUTORY COMPLIANCE</b><span>${l[3]}</span></div>`;
    caption = `<div class="cinema-caption"><span class="caption-index">02</span><span>${l[0]}</span><i class="caption-trace"></i><span>${l[1]}</span><i class="caption-trace"></i><strong>${l[5]}</strong></div>`;
  } else if (slide.visual === 'security') {
    annotations = `<div class="arch-core-orbit"><i></i><i></i></div><div class="arch-laser-grid"></div><div class="arch-hud-left"><b>TENANT ISOLATION</b><span>${l[0]}</span></div><div class="arch-hud-right"><b>ZERO RETENTION</b><span>${l[4]}</span></div>`;
    caption = `<div class="cinema-caption"><span>${l[0]}</span><i class="caption-trace"></i><strong>${l[1]}</strong><i class="caption-trace"></i><span>${l[3]}</span></div>`;
  } else if (slide.visual === 'governance') {
    annotations = `<div class="priorities-radar"></div><div class="governance-tiers"><span class="g-tier1">${l[0]}</span><span class="g-tier2">${l[1]}</span><span class="g-tier3">${l[2]}</span></div>`;
    caption = `<div class="cinema-caption"><span>${l[0]}</span><i class="caption-trace"></i><strong style="color:var(--red)">${l[1]}</strong><i class="caption-trace"></i><span>${l[2]}</span></div>`;
  } else if (slide.visual === 'priorities') {
    annotations = `<div class="priorities-beacon-pulse"></div><div class="priorities-radar"></div><div class="priorities-tier-badge"><b>WAVE 1</b><span>${l[0]} · ${l[4]}</span></div><div class="priorities-stepper"><span>01</span><span>02</span><span>03</span><span>04</span></div>`;
    caption = `<div class="cinema-caption"><strong style="color:var(--red)">01 ${l[0]}</strong><i class="caption-trace"></i><strong>02 ${l[1]}</strong><i class="caption-trace"></i><span>03 ${l[2]}</span><i class="caption-trace"></i><span>04 ${l[3]}</span></div>`;
  } else if (slide.visual === 'pilot') {
    annotations = `<div class="pilot-laser-rail"></div><div class="pilot-phase-badges"><span>${l[0]}</span><span>${l[1]}</span><span>${l[2]}</span></div><div class="pilot-roi-hud"><b>DUAL ROI</b><span>${lang === 'en' ? 'Client: 70% Faster · FTH Strategic IP' : 'ลูกค้าลดเวลา 70% · FTH AI Advisory'}</span></div>`;
    caption = `<div class="cinema-caption"><span>${l[0]}</span><i class="caption-trace"></i><span>${l[1]}</span><i class="caption-trace"></i><span>${l[2]}</span><i class="caption-trace"></i><strong style="color:var(--red)">${l[5]}</strong></div>`;
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
