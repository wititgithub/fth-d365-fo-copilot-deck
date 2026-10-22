const photoScenes = {
  hero: { file: 'hero', alt: 'Cinematic 3D crimson ribbon connecting business, logistics and manufacturing around an intelligence core' },
  boundary: { file: 'investigation', alt: '3D architectural concept visual of scattered fragmented enterprise screens synthesized by an AI analytical beam into an evidence brief' },
  architecture: { file: 'architecture', alt: 'High-tech enterprise AI cloud architecture with central Copilot Studio neural core and secure ERP data conduits' },
  vendorEmail: { file: 'email-vendor', alt: 'Futuristic supplier email origami envelope unfurling into delivery calendar streams under crimson approval seal' },
  taxScanning: { file: 'tax-scan', alt: '3D visualization of automated Thai tax invoice and withholding certificate scanning with holographic OCR laser grid, 3-way match and D365 AP plinth' },
  security: { file: 'security', alt: 'Enterprise zero-trust cybersecurity enclave with crystalline data vault, hexagonal forcefield barrier, Entra ID RBAC, and zero data leakage' },
  governance: { file: 'governance', alt: 'Executive 3D command console with three tiered autonomy podiums: Assisted inspection, Supervised human sign-off seal, and Autonomous threshold' },
  priorities: { file: 'priorities', alt: 'Sleek four-stage sequential implementation priority runway with illuminated plinths and laser filaments' },
  pilot: { file: 'roadmap-roi', alt: '10-week implementation bridge with four progressive milestone pedestals connected to a dual-perspective ROI balance scale plinth' }
};

function cinematic(slide, lang) {
  const scene = photoScenes[slide.visual], l = slide.labels[lang];
  const sparks = Array.from({ length: 9 }, (_, i) => `<i class="scene-spark" style="--x:${12 + (i * 17) % 77}%;--y:${15 + (i * 23) % 67}%;--delay:${i * 0.63}s"></i>`).join('');
  let annotations = '', caption = '';

  if (slide.visual === 'hero') {
    annotations = `<div class="core-orbit"><i></i><i></i></div><div class="hero-data-trail"></div>`;
    caption = `<div class="cinema-caption hero-caption"><span>Dynamics 365</span><i>+</i><span>Copilot Studio</span></div>`;
  } else if (slide.visual === 'boundary') {
    annotations = `<div class="investigation-rays"></div><div class="investigation-target"></div><div class="investigation-badges"><div class="badge-silos"><b>FRAGMENTED SILOS</b><span>${lang === 'en' ? '10 Screens · Outlook · PDFs' : '10 หน้าจอ · อีเมล · PDF'}</span></div><div class="badge-brief"><b>EVIDENCE BRIEF</b><span>${lang === 'en' ? '1-Click Decision Ready' : 'พร้อมตัดสินใจใน 1 คลิก'}</span></div></div><div class="investigation-hud-center"><b>COPILOT REASONING CORE</b><span>${lang === 'en' ? 'Sifting Exceptions & Assembling Proof' : 'สืบค้นข้อยกเว้น & รวบรวมหลักฐาน'}</span></div>`;
    caption = `<div class="cinema-caption"><span class="caption-index">02</span><span>${l[4]}</span><i class="caption-trace"></i><span>${l[1]}</span><i class="caption-trace"></i><strong>${l[5]}</strong><i class="caption-trace"></i><strong style="color:var(--red)">${l[6]}</strong></div>`;
  } else if (slide.visual === 'architecture') {
    annotations = `<div class="arch-core-orbit"><i></i><i></i></div><div class="arch-laser-grid"></div><div class="arch-hud-left"><b>1. PERCEPTION</b><span>${l[0]}</span></div><div class="arch-hud-right"><b>3. ACTION & 4. GOVERN</b><span>${l[2]} · ${l[3]}</span></div>`;
    caption = `<div class="cinema-caption"><span>${l[0]}</span><i class="caption-trace"></i><strong>${l[1]}</strong><i class="caption-trace"></i><span>${l[2]}</span><i class="caption-trace"></i><span>${l[3]}</span></div>`;
  } else if (slide.visual === 'vendorEmail') {
    annotations = `<div class="workflow-laser-bridge"></div><div class="email-clock-gear"></div><div class="vendor-badges"><div class="badge-email"><b>INCOMING EMAIL</b><span>${l[0]}</span></div><div class="badge-d365"><b>D365 PO DRAFT</b><span>${l[3]}</span></div></div>`;
    caption = `<div class="cinema-caption"><span class="caption-index">01</span><span>${l[0]}</span><i class="caption-trace"></i><span>${l[2]}</span><i class="caption-trace"></i><strong>${l[4]}</strong></div>`;
  } else if (slide.visual === 'taxScanning') {
    annotations = `<div class="tax-ocr-grid"></div><div class="tax-scan-beam"></div><div class="tax-doc-badges"><div class="badge-doc-invoice"><b>TAX INVOICE (ใบกำกับภาษี)</b><span>${lang === 'en' ? '7% VAT & 13-Digit Tax ID ✓' : 'ภาษีมูลค่าเพิ่ม 7% & เลข 13 หลัก ✓'}</span></div><div class="badge-doc-wht"><b>WHT CERT (ภ.ง.ด. 3/53)</b><span>${lang === 'en' ? 'Withholding Rate Validated' : 'อัตราหัก ณ ที่จ่ายถูกต้อง'}</span></div></div><div class="tax-match-hud"><b>3-WAY MATCHING VERIFIED</b><span>${lang === 'en' ? 'PO #48201 = Receipt = Invoice (100% Match)' : 'PO = ใบรับสินค้า = ใบกำกับภาษี (ตรงกัน 100%)'}</span></div><div class="tax-badge-hud"><b>STATUTORY COMPLIANCE</b><span>${lang === 'en' ? 'D365 AP Journal Draft · Zero Penalty Risk' : 'ร่างสมุดรายวันเจ้าหนี้ D365 · ไร้ค่าปรับ'}</span></div>`;
    caption = `<div class="cinema-caption"><span class="caption-index">05</span><span>${l[0]}</span><i class="caption-trace"></i><span>${l[1]}</span><i class="caption-trace"></i><strong>${l[2]}</strong><i class="caption-trace"></i><strong style="color:var(--green)">${l[5]}</strong></div>`;
  } else if (slide.visual === 'security') {
    annotations = `<div class="security-hex-field"></div><div class="security-deflect-pulse"></div><div class="security-badges"><div class="badge-tenant"><b>TENANT BOUNDARY</b><span>${lang === 'en' ? 'Customer Cloud Enclave · Zero Leakage' : 'คลาวด์แยกเฉพาะลูกค้า · ข้อมูลไม่รั่วไหล'}</span></div><div class="badge-entra"><b>MICROSOFT ENTRA ID</b><span>${lang === 'en' ? 'Role-Based Access (RBAC) Enforced' : 'ควบคุมสิทธิ์ตามบทบาทผู้ใช้ (RBAC)'}</span></div></div><div class="security-hud-center"><b>ZERO PUBLIC MODEL TRAINING</b><span>${lang === 'en' ? 'Enterprise Data Never Leaves Your Tenant' : 'ข้อมูลองค์กรไม่ถูกนำไปเทรนโมเดลสาธารณะ 100%'}</span></div><div class="security-hud-bottom"><b>DATAVERSE PRIVATE LINK</b><span>${lang === 'en' ? 'Customer Lockbox · Immutable Audit Log' : 'ลิงก์ส่วนตัว Dataverse · บันทึกตรวจสอบย้อนหลัง'}</span></div>`;
    caption = `<div class="cinema-caption"><span class="caption-index">06</span><span>${l[0]}</span><i class="caption-trace"></i><strong>${l[1]}</strong><i class="caption-trace"></i><span>${l[2]}</span><i class="caption-trace"></i><strong style="color:var(--green)">${l[4]}</strong></div>`;
  } else if (slide.visual === 'governance') {
    annotations = `<div class="gov-radar-sweep"></div><div class="gov-tier-pillars"><div class="gov-pillar p-tier1"><b>TIER 1 · ASSISTED</b><span>${lang === 'en' ? 'Read-Only Evidence Sifting' : 'ช่วยสืบค้น & รวบรวมหลักฐาน'}</span></div><div class="gov-pillar p-tier2 active"><div class="gov-seal-pulse"></div><b>TIER 2 · SUPERVISED (CORE)</b><span>${lang === 'en' ? '1-Click Human Sign-Off Stamp' : 'คนเป็นผู้อนุมัติใน 1 คลิก'}</span></div><div class="gov-pillar p-tier3"><b>TIER 3 · AUTONOMOUS</b><span>${lang === 'en' ? 'Strict Tolerance (<2% Variance)' : 'อัตโนมัติเฉพาะส่วนต่าง < 2%'}</span></div></div><div class="gov-hud-bottom"><b>EXECUTIVE GOVERNANCE CONTROL</b><span>${lang === 'en' ? 'Full Traceability in D365 Action Center & Audit Trail' : 'ตรวจสอบย้อนหลังได้ 100% บน D365 Action Center'}</span></div>`;
    caption = `<div class="cinema-caption"><span class="caption-index">07</span><span>${l[0]}</span><i class="caption-trace"></i><strong style="color:var(--red)">★ ${l[1]}</strong><i class="caption-trace"></i><span>${l[2]}</span></div>`;
  } else if (slide.visual === 'priorities') {
    annotations = `<div class="priorities-beacon-pulse"></div><div class="priorities-radar"></div><div class="priorities-tier-badge"><b>WAVE 1</b><span>${l[0]} · ${l[4]}</span></div><div class="priorities-stepper"><span>01</span><span>02</span><span>03</span><span>04</span></div>`;
    caption = `<div class="cinema-caption"><strong style="color:var(--red)">01 ${l[0]}</strong><i class="caption-trace"></i><strong>02 ${l[1]}</strong><i class="caption-trace"></i><span>03 ${l[2]}</span><i class="caption-trace"></i><span>04 ${l[3]}</span></div>`;
  } else if (slide.visual === 'pilot') {
    annotations = `<div class="pilot-laser-rail"></div><div class="pilot-timeline-stepper"><div class="p-step active"><b>W1–2</b><span>${lang === 'en' ? 'Benchmark' : 'วัดเกณฑ์'}</span></div><div class="p-step-arrow">➔</div><div class="p-step"><b>W3–5</b><span>${lang === 'en' ? 'Build' : 'พัฒนา'}</span></div><div class="p-step-arrow">➔</div><div class="p-step"><b>W6–8</b><span>${lang === 'en' ? 'Pilot UAT' : 'ทดสอบ'}</span></div><div class="p-step-arrow">➔</div><div class="p-step"><b>W9–10</b><span>${lang === 'en' ? 'Scale' : 'ขยายผล'}</span></div></div><div class="pilot-dual-roi-cards"><div class="roi-card-client"><b>CLIENT ROI (ผลลัพธ์ลูกค้า)</b><span>${lang === 'en' ? '⚡ 70% Faster Cycle Time · Zero Tax Penalties' : '⚡ ลดเวลา 70% · ปลอดค่าปรับสรรพากร'}</span></div><div class="roi-card-fth"><b>FUJITSU PARTNER ROI (ผลลัพธ์พาร์ทเนอร์)</b><span>${lang === 'en' ? '🏆 Strategic Copilot IP · Repeatable Practice Lead' : '🏆 ทรัพย์สินทางปัญญา AI · ผู้นำที่ปรึกษาองค์กร'}</span></div></div>`;
    caption = `<div class="cinema-caption"><span class="caption-index">09</span><span>${l[0]}</span><i class="caption-trace"></i><span>${l[1]}</span><i class="caption-trace"></i><span>${l[2]}</span><i class="caption-trace"></i><strong style="color:var(--red)">${l[3]} · ${l[4]}</strong></div>`;
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
