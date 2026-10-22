# 🎙️ FTH x D365 x Copilot Studio: Executive Presentation Script & NotebookLM Pack (EN / TH)

**Topic:** Customizing the Future: Building Enterprise Agents with Dynamics 365 and Copilot Studio  
**Organization:** Fujitsu Thailand (FTH) · Dynamics 365 Practice  
**Date:** 22 October 2026  

---

## 🎧 ส่วนที่ 1: คำสั่ง Custom Prompt สำหรับ Google NotebookLM (Audio Overview)

> [!TIP]
> **วิธีใช้งานใน Google NotebookLM:**
> 1. อัปโหลดไฟล์นี้และเอกสารในโฟลเดอร์ `docs/` เข้าสู่ [notebooklm.google.com](https://notebooklm.google.com)
> 2. ในส่วน **Audio Overview (Deep Dive Conversation)** กดปุ่ม **Customize**
> 3. ก๊อปปี้ Prompt ด้านล่างนี้ไปใส่ แล้วกด **Generate** เพื่อสร้าง Podcast ผู้ดำเนินรายการคู่

### 🇬🇧 NotebookLM Prompt (English Version)
```text
Act as two sharp, inspiring, and executive-level technology innovation hosts presenting an executive briefing to Fujitsu Thailand (FTH) leadership.
Keep the dialogue engaging, clear, punchy, and confident. Avoid unnecessary tech buzzwords without substance.
Walk through our 10-slide strategy: "Customizing the Future: Building Enterprise Agents with Dynamics 365 and Copilot Studio":
1. The Paradigm Shift: Transforming D365 from a passive System of Record into an autonomous System of Agency.
2. The Real Friction: Routine is already automated; 70% of human time is wasted sifting 10 screens and emails for operational exceptions.
3. The 4-Pillar Agent Anatomy: Perception (Events) -> Cognition (SOPs) -> Action (ERP MCP) -> Governance (Audit).
4. Use Case 1 (SCM/Procurement): Supplier Email Ingestion for autonomous delivery rescheduling and 1-click PO updates.
5. Use Case 2 (Finance/Tax): Thai Tax Invoice and Withholding (P.N.D. 3/53) Scanning with AI OCR, 3-way matching, and zero tax penalty risk.
6. Zero-Trust Security: 100% inside client tenant, Entra ID RBAC enforced, zero public model training, and Dataverse Customer Lockbox.
7. Human-in-the-Loop Governance: 3 Tiers of Autonomy (Assisted -> Supervised 1-Click Approval -> Guardrailed Autonomous).
8. Implementation Sequence: Wave 1 (Supplier Emails & Tax OCR) before scaling to warehouse and shopfloor.
9. 10-Week Pilot Journey & Dual ROI: 70% cycle time reduction for clients; reusable proprietary AI IP for Fujitsu Thailand.
10. Finale: Unifying Fujitsu Red Infinity with Microsoft Copilot Studio to lead Thailand's enterprise agent modernization.
```

### 🇹🇭 NotebookLM Prompt (เวอร์ชันภาษาไทย)
```text
ดำเนินรายการแบบคู่หูผู้เชี่ยวชาญเทคโนโลยีระดับองค์กร ด้วยน้ำเสียงมั่นใจ ทันสมัย น่าเชื่อถือ และกระชับ สำหรับนำเสนอต่อคณะกรรมการบริหาร Fujitsu Thailand (FTH)
เล่าเรื่องตามโครงสร้าง 10 สไลด์ของยุทธศาสตร์ "Customizing the Future: สร้าง Enterprise Agents ด้วย D365 และ Copilot Studio":
1. จุดเปลี่ยนสำคัญ: เปลี่ยน D365 จากระบบบันทึกธุรกรรมย้อนหลัง (System of Record) สู่ระบบปฏิบัติการอัจฉริยะเชิงรุก (System of Agency)
2. ปัญหาจริงหน้างาน: งานปกติระบบจัดการได้ดี แต่เมื่อเกิดข้อยกเว้น คนต้องเสียเวลา 70% เปิด 10 หน้าจอดึงเมลและเอกสารแนบ
3. สถาปัตยกรรม 4 เสาหลัก: รับรู้เหตุการณ์ (Perceive) -> วิเคราะห์ตาม SOP (Reason) -> สั่งการผ่าน ERP MCP (Act) -> ตรวจสอบย้อนหลัง (Govern)
4. Use Case 1 จัดซื้อ: ดักจับอีเมลคู่ค้าขอเลื่อนส่งมอบ ประเมินผลกระทบสายการผลิต และร่างปรับวันส่งใน D365 ให้คนกดอนุมัติในคลิกเดียว
5. Use Case 2 บัญชีภาษี: สแกนใบกำกับภาษีและใบหัก ณ ที่จ่าย (ภ.ง.ด. 3/53) ตรวจสอบ 3-Way Match และ VAT 7% ปลอดความเสี่ยงเบี้ยปรับสรรพากร
6. ความปลอดภัย Zero-Trust: ประมวลผลใน Tenant ลูกค้า 100%, ไม่นำข้อมูลไปเทรนโมเดลสาธารณะ, คุมด้วย Entra ID เดิม
7. การกำกับดูแล Human-in-the-Loop: โมเดล 3 ระดับ (ช่วยอ่าน -> ร่างรอคนอนุมัติ -> อัตโนมัติในกรอบเข้มงวด) คนคุมอำนาจตัดสินใจเสมอ
8. ลำดับการเริ่ม: เริ่มจาก 2 Use Cases แรกที่เห็นผลเร็ว ข้อมูลพร้อม แล้วจึงขยายผลสู่คลังสินค้าและการผลิต
9. แผนนำร่อง 10 สัปดาห์ & ROI สองมิติ: ลูกค้าลดเวลา 70% ไร้ค่าปรับ; ฟูจิตสึได้ทรัพย์สินทางปัญญา AI เชิงกลยุทธ์
10. บทสรุป: พลังของ Fujitsu Red Infinity ผสาน Copilot Studio สู่การเป็นผู้นำที่ปรึกษา AI ยุคใหม่
```

---

## 🎤 ส่วนที่ 2: บทพูดนำเสนอรายสไลด์ (10-Slide Dual Track)

### Slide 1: Customizing the Future / สร้างอนาคตองค์กร
* **🇬🇧 EN:** "Good morning, distinguished executives. Today, we present 'Customizing the Future'—an evidence-led strategy by Fujitsu Thailand to build Enterprise Agents with Dynamics 365 and Microsoft Copilot Studio. For years, ERP has served as a passive System of Record. We are now evolving into an autonomous System of Agency: deploying intelligent, supervised agents that perceive business events, reason over corporate SOPs, and execute complex workflows under strict human governance."
* **🇹🇭 TH:** "สวัสดีครับ ท่านคณะผู้บริหารทุกท่าน วันนี้ฟูจิตสึ ประเทศไทย ขอเสนอแนวคิด สร้างอนาคตองค์กร ด้วยการสร้างเอนเทอร์ไพรส์ เอเจนต์ บนไดนามิกส์ สามหกห้า ร่วมกับ โคไพลอต สตูดิโอ ครับ ตลอดเวลาที่ผ่านมา ระบบอีอาร์พีทำหน้าที่เป็นเพียงระบบบันทึกธุรกรรมย้อนหลัง แต่วันนี้เรากำลังยกระดับสู่ระบบปฏิบัติการอัจฉริยะเชิงรุก ที่รับรู้เหตุการณ์ทางธุรกิจ วิเคราะห์ตามระเบียบองค์กร และลงมือปฏิบัติงานร่วมกับคนได้อย่างแม่นยำ โดยหัวใจสำคัญคือการช่วยให้ธุรกิจขับเคลื่อนได้รวดเร็วขึ้น ภายใต้กรอบธรรมาภิบาลและความปลอดภัยระดับองค์กรครับ"

### Slide 2: The Investigation Burden / ภาระการสืบค้นข้อยกเว้น
* **🇬🇧 EN:** "Standard ERP automates routine processes smoothly. However, the real operational bottleneck occurs when exceptions happen—such as a delayed shipment, an unaligned invoice, or a three-way matching variance. Today, resolving a single exception forces professionals to open up to ten different screens, search email threads, and cross-reference PDF attachments, consuming up to 70% of human time. Our enterprise agents assemble cross-system evidence in seconds, empowering human experts to make immediate, verified decisions."
* **🇹🇭 TH:** "ระบบไดนามิกส์มาตรฐานจัดการงานตามขั้นตอนปกติได้อย่างราบรื่น แต่คอขวดที่แท้จริงเกิดขึ้นเมื่อมีข้อยกเว้นในกระบวนการทำงานครับ ในปัจจุบัน เมื่อเกิดปัญหาสินค้าส่งล่าช้า หรือยอดเงินไม่ตรง พนักงานต้องเสียเวลาเฉลี่ยถึงร้อยละเจ็ดสิบ ในการเปิดถึงสิบหน้าจอ ไล่ค้นหาอีเมล และเปิดเอกสารแนบ เพื่อตามหาต้นตอของปัญหา เอเจนต์ระดับองค์กรจะเข้ามาปิดช่องว่างนี้ โดยดึงข้อมูลข้ามระบบมารวบรวมเป็นชุดหลักฐานสรุปที่แม่นยำ ช่วยให้ผู้มีอำนาจตัดสินใจได้ทันทีในคลิกเดียวครับ"

### Slide 3: Anatomy of an Agent / สถาปัตยกรรม 4 เสาหลัก
* **🇬🇧 EN:** "What separates an Enterprise Agent from a conversational chatbot? It is the ability to perceive and act with accountability. Our architecture rests on four pillars: First, Perception—monitoring D365 business events and exceptions in real time. Second, Cognition—reasoning over company SOPs and regulatory frameworks using enterprise AI. Third, Action—leveraging Microsoft ERP Model Context Protocol to execute business logic. And fourth, Governance—enforcing role-based security with an immutable audit trail."
* **🇹🇭 TH:** "สิ่งที่ทำให้เอเจนต์ระดับองค์กรแตกต่างจากแชตบอตทั่วไป คือความสามารถในการรับรู้และลงมือปฏิบัติการอย่างรับผิดชอบครับ สถาปัตยกรรมของเราประกอบด้วยสี่เสาหลัก เสาแรกคือ การรับรู้เหตุการณ์และความผิดปกติในระบบไดนามิกส์แบบเรียลไทม์ เสาสองคือ การคิดวิเคราะห์โดยเทียบเคียงกับระเบียบปฏิบัติและนโยบายขององค์กร เสาสามคือ การลงมือปฏิบัติการสั่งงานผ่านช่องทางเชื่อมต่อมาตรฐานของไมโครซอฟท์ และเสาสี่คือ ธรรมาภิบาลที่มีบันทึกตรวจสอบย้อนหลังได้ทุกขั้นตอนครับ"

### Slide 4: Use Case 1: Vendor Email Ingestion / ตรวจจับอีเมลคู่ค้า
* **🇬🇧 EN:** "Our first enterprise use case addresses supply chain delivery disruptions. When a supplier sends an email requesting to postpone a shipment, Copilot automatically ingests the message, extracts the purchase order and proposed delivery date, and checks downstream impacts against D365 production schedules. It then drafts a revised PO delivery schedule and sends a focused summary to the procurement manager for one-click approval. No delayed emails, no production surprises, and full managerial control maintained."
* **🇹🇭 TH:** "กรณีศึกษาแรก คืองานจัดซื้อและห่วงโซ่อุปทาน กับปัญหาการขอเลื่อนส่งมอบสินค้าของคู่ค้าครับ เมื่อคู่ค้าส่งอีเมลมาแจ้งขอเลื่อนวันส่งมอบ โคไพลอตจะตรวจจับอีเมล ดึงเลขที่ใบสั่งซื้อ และตรวจสอบผลกระทบต่อแผนการผลิตในระบบไดนามิกส์ทันที จากนั้นจะจัดเตรียมแบบร่างปรับปรุงวันส่งมอบ พร้อมสรุปผลกระทบส่งให้ผู้จัดการฝ่ายจัดซื้ออนุมัติในคลิกเดียว หมดปัญหาอีเมลตกหล่น และป้องกันสายการผลิตสะดุดได้อย่างมั่นใจครับ"

### Slide 5: Use Case 2: Tax Invoice Scanning / สแกนใบกำกับภาษี
* **🇬🇧 EN:** "Our second enterprise case tackles statutory compliance in Accounts Payable. In Thailand, handling withholding taxes such as P.N.D. 3 and 53 and matching tax invoices requires painstaking manual verification. Our Tax Scanning Agent reads invoice and withholding certificates via AI OCR, reconciles quantities and pricing against D365 purchase orders and receipts, and validates withholding tax percentages according to Thai Revenue Department rules. It surfaces discrepancies in a clear evidence pack, cutting posting time by 75% while safeguarding against tax penalties."
* **🇹🇭 TH:** "กรณีศึกษาที่สอง คืองานสแกนใบกำกับภาษีและใบหัก ณ ที่จ่าย เพื่อขจัดความผิดพลาดทางภาษีให้เป็นศูนย์ครับ ระบบปัญญาประดิษฐ์จะสแกนเอกสารใบกำกับภาษีและหนังสือรับรองการหัก ณ ที่จ่าย ดึงเลขประจำตัวผู้เสียภาษีสิบสามหลัก และทำการจับคู่สามทางกับใบสั่งซื้อและใบรับสินค้าในระบบไดนามิกส์โดยอัตโนมัติ พร้อมตรวจสอบอัตราภาษีตามเกณฑ์สรรพากร เช่น ภาษีมูลค่าเพิ่มร้อยละเจ็ด และ ภ.ง.ด. สาม หรือ ห้าสิบสาม ช่วยลดเวลาทำงานลงร้อยละเจ็ดสิบห้า และปลอดความเสี่ยงจากค่าปรับครับ"

### Slide 6: Zero-Trust Boundary / ความปลอดภัยระดับองค์กร
* **🇬🇧 EN:** "Enterprise adoption demands uncompromising security. Built strictly upon Microsoft Zero-Trust principles, our architecture ensures that all data reasoning and processing remain within the customer's private cloud tenant. Your enterprise transactions never train public AI models. Furthermore, agents inherit the exact Microsoft Entra ID permissions of the user. If an employee lacks access to sensitive ledger accounts, their agent cannot access them either. Every automated query and proposed action is logged in an immutable audit trail."
* **🇹🇭 TH:** "ความปลอดภัยของข้อมูลองค์กรเป็นสิ่งที่ผู้บริหารให้ความสำคัญสูงสุด สถาปัตยกรรมนี้จึงยึดหลักความปลอดภัยสูงสุดตามมาตรฐานไมโครซอฟท์ครับ การประมวลผลทั้งหมดเกิดขึ้นภายในขอบเขตเทแนนต์คลาวด์ของลูกค้าเท่านั้น ข้อมูลธุรกิจจะไม่ถูกนำไปฝึกฝนโมเดลสาธารณะภายนอกอย่างเด็ดขาด นอกจากนี้ เอเจนต์ยังทำงานภายใต้สิทธิ์เดิมของผู้ใช้งานผ่านระบบเอนทรา ไอดี ทำให้ข้อมูลสำคัญปลอดภัย และมีบันทึกตรวจสอบย้อนหลังได้อย่างโปร่งใสครับ"

### Slide 7: Human-in-the-Loop Governance / 3 ระดับการทำงาน
* **🇬🇧 EN:** "We do not unleash unchecked autonomous systems. Instead, we institute a rigorous three-tier autonomy framework: Tier 1 is Assisted—read-only investigation and evidence packaging. Tier 2 is Supervised—the core tier where the agent drafts transactions, PO reschedules, or journal entries, requiring explicit human one-click sign-off. Tier 3 is Autonomous—strictly limited to low-risk, high-volume transactions under predefined thresholds. This guarantees total managerial control from day one."
* **🇹🇭 TH:** "เราบริหารความเสี่ยงด้วยการกำหนดระดับความเป็นอิสระของเอเจนต์อย่างรัดกุมเป็นสามระดับครับ ระดับหนึ่ง คือ การช่วยสืบค้นและรวบรวมหลักฐานแบบอ่านอย่างเดียว ระดับสอง ซึ่งเป็นหัวใจหลัก คือ การช่วยร่างรายการธุรกรรม โดยต้องมีผู้มีอำนาจกดอนุมัติเสมอ และระดับสาม คือ การทำงานอัตโนมัติเฉพาะรายการความเสี่ยงต่ำที่มีส่วนต่างน้อยกว่าร้อยละสอง โครงสร้างนี้ทำให้มั่นใจได้ว่า เอเจนต์ทำหน้าที่เตรียมข้อมูลและเสนอแนะ แต่มนุษย์เป็นผู้ถืออำนาจตัดสินใจขั้นสุดท้ายเสมอครับ"

### Slide 8: Implementation Sequence / ลำดับการประยุกต์ใช้
* **🇬🇧 EN:** "Where should an organization begin? We recommend starting with our two proven high-impact use cases: Supplier Email Rescheduling and Tax Invoice Scanning. Both feature clear operational boundaries, ready data access, and immediate measurable relief for procurement and accounting teams. Once value is established, the architecture naturally scales to warehouse exception investigations and smart manufacturing variance briefs."
* **🇹🇭 TH:** "สำหรับการเริ่มต้นจริง เราแนะนำให้จัดลำดับโดยเริ่มจากสองกรณีศึกษาแรก คือ การจัดการอีเมลคู่ค้า และการสแกนใบกำกับภาษีครับ เนื่องจากเป็นจุดที่มีขอบเขตงานชัดเจน ข้อมูลในระบบมีความพร้อม และปลดล็อกภาระงานของทีมจัดซื้อและบัญชีได้ทันที เมื่อพิสูจน์ผลลัพธ์สำเร็จแล้ว สถาปัตยกรรมนี้จะสามารถต่อยอดขยายผลไปสู่การจัดการคลังสินค้า และการวิเคราะห์ต้นทุนการผลิตในระยะถัดไปได้อย่างมั่นใจครับ"

### Slide 9: 10-Week Pilot Journey / แผนนำร่อง 10 สัปดาห์ & Dual ROI
* **🇬🇧 EN:** "Our proposed engagement is a disciplined 10-week Proof-of-Value journey. In Weeks 1 and 2, we establish baseline metrics on standard D365. In Weeks 3 through 5, we build the supervised agent in Copilot Studio. In Weeks 6 through 8, we pilot with real business users. The return on investment is immediate and dual-perspective: Clients experience a 70% reduction in cycle time and total tax compliance. For Fujitsu Thailand, it solidifies our leadership as a premier Strategic AI Transformation Partner with proprietary enterprise assets."
* **🇹🇭 TH:** "แผนงานนำร่องสิบสัปดาห์ได้รับการออกแบบให้พิสูจน์ความคุ้มค่าอย่างเป็นรูปธรรมครับ เริ่มต้นจากการวัดเกณฑ์มาตรฐานในสัปดาห์ที่หนึ่งถึงสอง สร้างเอเจนต์ในสัปดาห์ที่สามถึงห้า และทดสอบนำร่องกับผู้ใช้งานจริงในสัปดาห์ที่หกถึงแปด ก่อนวางแผนขยายผล ผลตอบแทนที่ได้เกิดขึ้นทั้งสองมิติ ลูกค้าประหยัดเวลาลงร้อยละเจ็ดสิบและขจัดเบี้ยปรับภาษี ขณะที่ฟูจิตสึ ประเทศไทย ได้ยกระดับสู่การเป็นพันธมิตรเชิงกลยุทธ์ด้านปัญญาประดิษฐ์ระดับองค์กรครับ"

### Slide 10: Empowering Enterprise Excellence / Fujitsu Red Infinity × Copilot
* **🇬🇧 EN:** "The animated Fujitsu Red Infinity loop symbolizes our endless dedication to sustainable innovation and customer success. By unifying the operational rigor of Dynamics 365 with the transformative intelligence of Microsoft Copilot Studio, we empower enterprises to achieve unprecedented operational agility. Our ask today is the sponsorship to launch our 10-week proof-of-value with an identified process owner. Thank you very much, and we welcome your questions and strategic guidance."
* **🇹🇭 TH:** "สัญลักษณ์ ฟูจิตสึ เรด อินฟินิตี้ บนหน้าจอนี้ สะท้อนถึงคำมั่นสัญญาที่ไม่สิ้นสุดในการขับเคลื่อนนวัตกรรมเพื่อความยั่งยืนของลูกค้าครับ ด้วยการผสานความแข็งแกร่งของระบบไดนามิกส์ สามหกห้า เข้ากับความฉลาดของ โคไพลอต สตูดิโอ ฟูจิตสึ ประเทศไทย พร้อมสนับสนุนให้องค์กรของท่านก้าวสู่ยุคใหม่อย่างมั่นคง เราขอรับการสนับสนุนจากท่านผู้บริหารเพื่อเริ่มโครงการนำร่องสิบสัปดาห์ ขอขอบพระคุณทุกท่าน และพร้อมตอบข้อซักถามครับ"
