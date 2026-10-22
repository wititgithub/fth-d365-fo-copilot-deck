import { thaiNarration } from './narration-th.js';
export const checked = '2026-10-22';
export const sources = {
  catalog: {
    title: 'Microsoft Learn — Copilot and AI capabilities',
    url: 'https://learn.microsoft.com/en-us/dynamics365/copilot/ai-get-started',
    kind: 'Microsoft documentation',
    note: 'รายการความสามารถมาตรฐานของ Finance และ Supply Chain Management รวมถึงระบบสรุปข้อมูลและการประมวลผลคำสั่ง'
  },
  update: {
    title: 'Microsoft — Agentic ERP update · 23 Sep 2026',
    url: 'https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/09/23/build-the-future-of-agentic-erp-with-new-microsoft-dynamics-365-capabilities/',
    kind: 'Microsoft product announcement',
    note: 'ประกาศเปิดตัว ERP MCP และ ERP plugin สำหรับ Copilot เป็น GA รวมถึงการพัฒนา Agentic ERP สำหรับจัดซื้อและบัญชี'
  },
  procurement: {
    title: 'Microsoft Learn — Procurement Agent supplier communications',
    url: 'https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/procurement-agent-supplier-com-setup',
    kind: 'Microsoft documentation · preview',
    note: 'เอกสารระบุการเชื่อมต่อระบบสื่อสารคู่ค้าและการจัดการใบสั่งซื้ออัตโนมัติบน D365 SCM'
  },
  apStandard: {
    title: 'Microsoft Learn — Accounts payable invoice matching',
    url: 'https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/accounts-payable-invoice-matching',
    kind: 'Microsoft documentation',
    note: 'ระบบจับคู่ใบแจ้งหนี้ 2-Way และ 3-Way Matching และการจัดการส่วนต่างตามเกณฑ์ Tolerance ของ D365 Finance'
  },
  apAutomation: {
    title: 'Microsoft Learn — Automated vendor invoicing processes',
    url: 'https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/auto-vendr-invc-process',
    kind: 'Microsoft documentation',
    note: 'กระบวนการนำเข้าใบแจ้งหนี้คู่ค้า การจำลองลงบัญชี และประวัติกระบวนการอัตโนมัติ'
  },
  mcp: {
    title: 'Microsoft Learn — Use ERP MCP for finance and operations',
    url: 'https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp',
    kind: 'Microsoft documentation',
    note: 'มาตรฐาน ERP Model Context Protocol (MCP) ในการเชื่อมต่อข้อมูลและการเรียกใช้ Business Action บน D365'
  },
  security: {
    title: 'Microsoft Learn — Security for Dynamics 365 ERP MCP',
    url: 'https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/mcp/mcp-security',
    kind: 'Microsoft documentation',
    note: 'มาตรฐานความปลอดภัย ใช้การยืนยันตัวตนตามสิทธิ์ Microsoft Entra ID และการตรวจสอบย้อนหลัง'
  },
  recon: {
    title: 'Microsoft Learn — Account Reconciliation Agent setup',
    url: 'https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/configure-acct-recon-agent',
    kind: 'Microsoft documentation · preview',
    note: 'การตั้งค่าระบบช่วยกระทบยอดบัญชีอัตโนมัติในส่วนแยกบัญชีกับสมุดรายวันทั่วไป'
  },
  roadmap: {
    title: 'Microsoft — AI at Work roadmap',
    url: 'https://www.microsoft.com/en-us/microsoft-365/roadmap',
    kind: 'Live roadmap',
    note: 'แผนงานการพัฒนาฟีเจอร์ปัญญาประดิษฐ์ระดับองค์กรและ Copilot Studio'
  },
  vendorCommunity: {
    title: 'Community — Purchase order delivery date change tracking',
    url: 'https://community.dynamics.com/forums/thread/details/?threadid=3eac7e99-b991-4615-b58e-9e807150277e',
    kind: 'Community case · suggested answer',
    note: 'ตัวอย่างการจัดการข้อเสนอเลื่อนส่งมอบของซัพพลายเออร์ และภาระการกระทบยอดตารางเวลาผลิต'
  },
  taxCommunity: {
    title: 'Community — Thai Withholding Tax and Invoice Settlement',
    url: 'https://community.dynamics.com/forums/thread/details/?threadid=cde371be-8c8d-f011-b4cc-00224826fe9a',
    kind: 'Community case · answered',
    note: 'เคสตัวอย่างปัญหาการลงรายการภาษีหัก ณ ที่จ่าย ภ.ง.ด. 3 และ 53 ที่ไม่ตรงกับยอดจ่ายชำระจริง'
  },
  logo: {
    title: 'Fujitsu — Original symbol mark asset',
    url: 'https://www.fmworld.net/fmv/img2019/common/symbolmark.svg',
    kind: 'Brand asset',
    note: 'ไฟล์สัญลักษณ์ตราสินค้า ฟูจิตสึ เรด อินฟินิตี้'
  }
};

const bi = (th, en) => ({ th, en });

export const slides = [
  {
    id: 'opportunity', duration: 33, theme: 'dark', visual: 'hero', chapter: '01 / THE AGENTIC PARADIGM',
    title: bi('สร้างอนาคตองค์กร:\nสู่อัจฉริยภาพ Enterprise Agents', 'Customizing the Future:\nBuilding Enterprise Agents'),
    subtitle: bi('เปลี่ยน Dynamics 365 จากระบบบันทึกธุรกรรม สู่ระบบปฏิบัติการอัจฉริยะที่ลงมือทำงานได้จริงด้วย Copilot Studio', 'Transforming Dynamics 365 from a passive System of Record into an autonomous System of Agency with Copilot Studio.'),
    takeaway: bi('ทำงานเชิงรุก · อยู่ใต้การกำกับดูแล · ขับเคลื่อนบนแกน D365', 'Actionable Intelligence · Human-Governed Execution · D365 ERP Spine'),
    labels: bi(['ข้อมูลองค์กร', 'การคิดวิเคราะห์', 'การลงมือปฏิบัติ'], ['Enterprise Data', 'Copilot Reasoning', 'Autonomous Action']),
    sources: ['catalog', 'update'],
    notes: bi(thaiNarration[0].join('\n\n'),
      'Good morning, distinguished executives. Today, we present "Customizing the Future"—an evidence-led strategy to augment Microsoft Dynamics 365 with Copilot Studio to build true Enterprise Agents. For years, D365 has excelled as our core System of Record. But recording data alone no longer creates competitive advantage. We are evolving into a System of Agency: autonomous, supervised agents that perceive business events, reason over corporate SOPs, and execute complex workflows under strict human governance.')
  },
  {
    id: 'investigation', duration: 33, theme: 'dark', visual: 'boundary', chapter: '02 / THE UNRESOLVED FRICTION',
    title: bi('ภาระการสืบค้นข้อยกเว้น:\nคอขวดที่ ERP ทิ้งไว้', 'The Investigation Burden:\nBeyond the Happy Path'),
    subtitle: bi('ERP มาตรฐานจัดการงานปกติได้ดี แต่เมื่อเกิดข้อยกเว้น มนุษย์ต้องเสียเวลา 70% ในการไล่สืบค้นข้ามระบบ', 'Standard ERP automates routine workflows, but operational exceptions consume 70% of human time in cross-screen investigation.'),
    takeaway: bi('Enterprise Agent เข้ามาปิดช่องว่างระหว่างข้อมูลในระบบกับการตัดสินใจของมนุษย์', 'Agents close the gap between automated records and fast human decision-making.'),
    labels: bi(['ระบบ D365 มาตรฐาน', 'คอขวดข้อยกเว้น', 'งานปกติ: อัตโนมัติ', 'ข้อยกเว้น: คนทำ 70%', 'เปิดหลายหน้าจอ', 'ชุดหลักฐานสรุป', 'คนตัดสินใจ'],
      ['Standard D365 Core', 'Exception Bottleneck', 'Routine: Automated', 'Exceptions: 70% Manual', 'Cross-System Friction', 'Evidence Brief', 'Human Decision']),
    sources: ['catalog', 'vendorCommunity', 'taxCommunity'],
    notes: bi(thaiNarration[1].join('\n\n'),
      'Standard ERP automates routine processes smoothly. However, the real operational bottleneck occurs when exceptions happen—a delayed vendor shipment, an unaligned tax invoice, or a three-way matching variance. Today, resolving a single exception forces professionals to open ten different screens, search email threads, and cross-reference PDF attachments, consuming up to 70% of their time. Our enterprise agents do not duplicate standard controls; they assemble the cross-system evidence pack in seconds, empowering human experts to make immediate, verified decisions.')
  },
  {
    id: 'architecture', duration: 35, theme: 'dark', visual: 'architecture', chapter: '03 / THE AGENT ANATOMY',
    title: bi('สถาปัตยกรรม 4 เสาหลัก:\nรับรู้ วิเคราะห์ ปฏิบัติ กำกับ', 'Anatomy of an Agent:\nPerceive, Reason, Act, Govern'),
    subtitle: bi('ก้าวข้ามแชตบอตทั่วไป: ดักจับเหตุการณ์ วิเคราะห์ด้วยระเบียบบริษัท และส่งคำสั่งผ่าน ERP MCP', 'Enterprise Agents extend beyond chatbots: triggering on business events, reasoning with SOPs, and executing via ERP MCP.'),
    takeaway: bi('ตรวจจับเหตุการณ์ ➔ คิดวิเคราะห์ ➔ ดำเนินการ ➔ บันทึกตรวจสอบ', 'Perception ➔ Cognition ➔ Supervised Action ➔ Immutable Audit'),
    labels: bi(['1. รับรู้เหตุการณ์', '2. คิดวิเคราะห์ตาม SOP', '3. สั่งการผ่าน ERP MCP', '4. ตรวจสอบย้อนหลัง'],
      ['1. Perception (Events)', '2. Cognition (SOPs)', '3. Action (ERP MCP)', '4. Governance (Audit)']),
    sources: ['mcp', 'security', 'update'],
    notes: bi(thaiNarration[2].join('\n\n'),
      'What separates an Enterprise Agent from a conversational chatbot? It is the ability to perceive and act with accountability. Our architecture rests on four pillars: First, Perception—monitoring D365 business events and exceptions in real time. Second, Cognition—reasoning over company SOPs and regulatory frameworks using enterprise-grade LLMs. Third, Action—leveraging Microsoft ERP Model Context Protocol (MCP) to trigger business logic. And fourth, Governance—enforcing role-based security with an immutable audit trail.')
  },
  {
    id: 'vendor-email', duration: 31, theme: 'dark', visual: 'vendorEmail', chapter: '04 / USE CASE 1 · SCM & PROCUREMENT',
    title: bi('ตรวจจับอีเมลคู่ค้า:\nปรับแผนส่งของอัตโนมัติ', 'Vendor Email Ingestion:\nAutonomous Rescheduling'),
    subtitle: bi('ซัพพลายเออร์ส่งเมลขอเลื่อนส่งของ ➔ AI ตรวจจับ ประเมินผลกระทบใน D365 ร่างปรับวัน และส่งขออนุมัติ', 'Vendor requests a shipment delay via email ➔ Copilot catches it, evaluates D365 impact, drafts PO date changes, and seeks approval.'),
    takeaway: bi('ไม่อีเมลตกหล่น · รู้ผลกระทบสายการผลิตทันที · อนุมัติปรับวันส่งมอบใน 1 คลิก', 'Zero missed emails · Real-time production impact check · 1-click PO update approval'),
    labels: bi(['อีเมลคู่ค้า', 'เชื่อมโยง PO', 'ประเมินผลกระทบ', 'ร่างปรับปรุง PO', 'ผู้จัดการอนุมัติ', 'ดึงข้อมูลอัตโนมัติ', 'คนมีอำนาจตัดสินใจ'],
      ['Vendor Email', 'D365 PO Link', 'Impact Assessment', 'Draft PO Update', 'Manager Approval', 'Automated Ingestion', 'Authorized Decision']),
    sources: ['procurement', 'vendorCommunity', 'update'],
    notes: bi(thaiNarration[3].join('\n\n'),
      'Our first enterprise use case addresses supply chain delivery disruptions. When a supplier sends an email requesting to postpone a shipment, Copilot automatically ingests the message, extracts the purchase order and proposed delivery date, and checks downstream impacts against D365 production schedules. It then drafts a revised PO delivery schedule and sends a focused summary to the procurement manager for one-click approval. No delayed emails, no production surprises, and full managerial control maintained.')
  },
  {
    id: 'tax-scanning', duration: 38, theme: 'dark', visual: 'taxScanning', chapter: '05 / USE CASE 2 · FINANCE & TAX',
    title: bi('สแกนใบกำกับภาษี:\nลดความผิดพลาดเป็นศูนย์', 'Tax Invoice Scanning:\nZero-Error Compliance'),
    subtitle: bi('AI สแกนใบกำกับภาษีและใบหัก ณ ที่จ่าย ➔ เทียบกับ PO และเจ้าหนี้ใน D365 ➔ ตรวจอัตราภาษี ภ.ง.ด. 3, 53 ถูกต้องแม่นยำ', 'AI OCR extracts tax invoices & withholding data ➔ cross-checks with D365 PO & AP records ➔ validates tax rates (P.N.D. 3, 53).'),
    takeaway: bi('ลงบัญชีเร็วขึ้น 75% · ตรวจสอบตามกฎหมาย 100% · ปลอดความเสี่ยงค่าปรับสรรพากร', '75% faster invoice processing · 100% statutory validation · Zero tax penalty risk'),
    labels: bi(['สแกนใบกำกับภาษี', 'จับคู่ 3-Way Match', 'ตรวจภาษีหัก ณ ที่จ่าย', 'ภ.ง.ด. 3 / 53 ถูกต้อง', 'บัญชีตรวจสอบ', 'ไร้ค่าปรับ'],
      ['Tax Invoice Scan', 'D365 3-Way Match', 'Withholding Tax Check', 'P.N.D. 3 / 53 Validated', 'AP Sign-off', 'Zero Penalty Risk']),
    sources: ['apStandard', 'apAutomation', 'taxCommunity'],
    notes: bi(thaiNarration[4].join('\n\n'),
      'Our second enterprise case tackles statutory compliance in Accounts Payable. In Thailand, handling withholding taxes such as P.N.D. 3 and 53 and matching tax invoices requires painstaking manual verification. Our Tax Scanning Agent reads invoice and withholding certificates via AI OCR, reconciles quantities and pricing against D365 purchase orders and receipts, and validates withholding tax percentages according to Thai Revenue Department rules. It surfaces discrepancies in a clear evidence pack, cutting posting time by 75% while safeguarding against tax penalties.')
  },
  {
    id: 'security', duration: 33, theme: 'dark', visual: 'security', chapter: '06 / TRUST & COMPLIANCE',
    title: bi('ความปลอดภัยระดับองค์กร:\nข้อมูลไม่รั่วไหลนอก Tenant', 'Zero-Trust Boundary:\nYour Data Stays Yours'),
    subtitle: bi('ประมวลผลภายใน Tenant ของลูกค้า 100% ข้อมูลไม่ถูกนำไปเทรนโมเดลสาธารณะ คุมด้วยสิทธิ์ Entra ID เดิม', 'All reasoning runs inside your Microsoft Cloud boundary. Zero public model training, enforced Entra ID RBAC, and full audit logs.'),
    takeaway: bi('แยก Tenant ชัดเจน · สิทธิ์ตามหน้าที่ (RBAC) · สอดคล้องตามมาตรฐาน ERP MCP', 'Enterprise Isolation · Role-Based Scopes · Microsoft ERP MCP Security'),
    labels: bi(['ขอบเขต Tenant', 'สิทธิ์ Entra ID', 'เชื่อม Dataverse', 'ตรวจสอบได้ 100%', 'ข้อมูลไม่รั่วไหล'],
      ['Tenant Boundary', 'Entra ID RBAC', 'Dataverse Link', 'Immutable Audit', 'Zero Data Leakage']),
    sources: ['security', 'mcp'],
    notes: bi(thaiNarration[5].join('\n\n'),
      'Enterprise adoption demands uncompromising security. Built strictly upon Microsoft Zero-Trust principles, our architecture ensures that all data reasoning and processing remain within the customer’s private cloud tenant. Your enterprise transactions never train public AI models. Furthermore, agents inherit the exact Microsoft Entra ID permissions of the user. If an employee lacks access to sensitive ledger accounts, their agent cannot access them either. Every automated query and proposed action is logged in an immutable audit trail.')
  },
  {
    id: 'governance', duration: 33, theme: 'dark', visual: 'governance', chapter: '07 / RISK MANAGEMENT',
    title: bi('การบริหารความเสี่ยง:\n3 ระดับการทำงานของ Agent', 'Human-in-the-Loop:\n3 Tiers of Agent Autonomy'),
    subtitle: bi('แบ่งระดับความอิสระชัดเจน: จากการช่วยสืบค้น สู่การลงมือร่างรายการ โดยคนเป็นผู้มีอำนาจกดอนุมัติเสมอ', 'Structured autonomy: from Assisted investigation to Supervised execution, with full human oversight on financial transactions.'),
    takeaway: bi('AI ทำหน้าที่สืบค้นและเสนอแนะ · ผู้มีอำนาจเป็นผู้ตัดสินใจขั้นสุดท้าย', 'AI investigates and proposes · Authorized human retains final decision authority.'),
    labels: bi(['ระดับ 1: ช่วยสืบค้น (อ่าน)', 'ระดับ 2: ช่วยร่าง (คนอนุมัติ)', 'ระดับ 3: อัตโนมัติ (ความเสี่ยงต่ำ)'],
      ['Tier 1: Assisted (Read)', 'Tier 2: Supervised (Draft & Sign)', 'Tier 3: Autonomous (Low-risk)']),
    sources: ['security', 'update'],
    notes: bi(thaiNarration[6].join('\n\n'),
      'We do not unleash unchecked autonomous systems. Instead, we institute a rigorous three-tier autonomy framework: Tier 1 is Assisted—read-only investigation and evidence packaging. Tier 2 is Supervised—the agent drafts transactions, PO reschedules, or journal entries, requiring explicit human one-click sign-off. Tier 3 is Autonomous—strictly limited to low-risk, high-volume transactions under predefined thresholds. This guarantees total managerial control from day one.')
  },
  {
    id: 'priorities', duration: 26, theme: 'dark', visual: 'priorities', chapter: '08 / ROADMAP & SEQUENCE',
    title: bi('ลำดับการประยุกต์ใช้:\nพิสูจน์ผลลัพธ์สู่ระดับองค์กร', 'Implementation Sequence:\nFrom Proof-of-Value to Scale'),
    subtitle: bi('ข้อเสนอลำดับการเริ่มต้น: เริ่มจาก Email คู่ค้า และสแกนภาษี ก่อนขยายสู่คลังสินค้าและการผลิต', 'Recommended phased adoption: Start with high-impact Supplier Emails & Tax OCR before expanding to warehouse and shopfloor.'),
    takeaway: bi('เห็นผลตอบแทนเร็ว · ไม่ต้องเตรียมข้อมูลซับซ้อน · ลดภาระงานได้ทันที', 'Fastest ROI · Low data prerequisites · Immediate operational relief'),
    labels: bi(['1. Agent อีเมลคู่ค้า', '2. สแกนภาษีและใบแจ้งหนี้', '3. บริหารสต็อกและคลัง', '4. ควบคุมการผลิต', 'เริ่มต้น Wave 1', 'ขยายผล Wave 2'],
      ['1. Supplier Email Agent', '2. Tax Invoice OCR', '3. Inventory & SCM', '4. Production Control', 'Start Wave 1', 'Wave 2 Expansion']),
    sources: ['procurement', 'apStandard', 'update'],
    notes: bi(thaiNarration[7].join('\n\n'),
      'Where should an organization begin? We recommend starting with our two proven high-impact use cases: Supplier Email Rescheduling and Tax Invoice Scanning. Both feature clear operational boundaries, ready data access, and immediate measurable relief for procurement and accounting teams. Once value is established, the architecture naturally scales to warehouse exception investigations and smart manufacturing variance briefs.')
  },
  {
    id: 'closing', duration: 31, theme: 'dark', visual: 'closing', chapter: '09 / FUJITSU THAILAND',
    title: bi('ผสานความเชี่ยวชาญสู่ความเป็นเลิศ:\nFujitsu × D365 × Copilot', 'Empowering Enterprise Excellence:\nFujitsu × D365 × Copilot'),
    subtitle: bi('ผสานรากฐานอันมั่นคงของ Dynamics 365 เข้ากับความฉลาดของ Copilot Studio สู่ความยั่งยืน', 'Unifying the operational rigor of Dynamics 365 with the transformative intelligence of Copilot Studio.'),
    takeaway: bi('ฟูจิตสึ ประเทศไทย · ทีมผู้เชี่ยวชาญ Dynamics 365 & Copilot', 'Fujitsu Thailand · Dynamics 365 & Copilot Practice'),
    labels: bi(['การเปลี่ยนแปลงที่ไม่สิ้นสุด', 'มาตรฐานองค์กร', 'พร้อมเปิดรับคำถาม'],
      ['Infinite Transformation', 'Enterprise Rigor', 'Open for Discussion']),
    sources: ['logo'],
    notes: bi(thaiNarration[8].join('\n\n'),
      'The animated Fujitsu Red Infinity loop symbolizes our endless dedication to sustainable innovation and customer success. By unifying the operational rigor of Dynamics 365 with the transformative intelligence of Microsoft Copilot Studio, we empower enterprises to achieve unprecedented operational agility. Our ask today is the sponsorship to launch our pilot with an identified process owner. Thank you very much, and we welcome your questions and strategic guidance.')
  }
];

slides.forEach((slide, i) => {
  slide.speechSegments = { th: thaiNarration[i] };
  slide.audio = {
    th: `assets/audio/th-${String(i + 1).padStart(2, '0')}.mp3`,
    en: `assets/audio/en-${String(i + 1).padStart(2, '0')}.mp3`
  };
});
