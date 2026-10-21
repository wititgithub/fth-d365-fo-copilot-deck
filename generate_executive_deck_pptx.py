"""
generate_executive_deck_pptx.py
Builds the 10-slide C-Level Executive Presentation Deck (.pptx):
"Augmenting Microsoft Dynamics 365 with Copilot AI: Real Pains, Pragmatic Use Cases & ROI"
With bilingual (Thai/English) speaker notes on every slide, and animated Slide 10.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

def create_deck():
    prs = Presentation()
    # 16:9 Widescreen
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette
    C_NAVY = RGBColor(15, 23, 42)
    C_WHITE = RGBColor(255, 255, 255)
    C_RED = RGBColor(230, 0, 18)
    C_BLUE = RGBColor(0, 120, 212)
    C_PURPLE = RGBColor(121, 40, 202)
    C_SLATE_BG = RGBColor(248, 250, 252)
    C_DARK_BG = RGBColor(15, 23, 42)
    C_TEXT_DARK = RGBColor(15, 23, 42)
    C_TEXT_MUTED = RGBColor(100, 116, 139)
    C_CARD_BORDER = RGBColor(226, 232, 240)

    slides_data = [
        # SLIDE 1: Title
        {
            "num": 1,
            "title": "THE AUTONOMOUS ENTERPRISE",
            "subtitle": "Augmenting Microsoft Dynamics 365 with Copilot AI",
            "desc": "ยกระดับระบบ ERP จาก 'ระบบบันทึกข้อมูลแบบดั้งเดิม' สู่ 'ระบบอัจฉริยะที่ตัดสินใจและทำงานเชิงรุก' (System of Intelligence)",
            "script_th": "สวัสดีท่านผู้บริหารทุกท่านครับ วันนี้ผมขออนุญาตนำเสนอวิสัยทัศน์ที่จะเปลี่ยนวิธีที่องค์กรของเราขับเคลื่อนธุรกิจด้วย Microsoft Dynamics 365 และ Copilot AI... ตลอดหลายปีที่ผ่านมา ERP คือหัวใจในการบันทึกข้อมูลธุรกรรม แต่ในยุคปี 2026 นี้ แค่บันทึกอย่างเดียวไม่เพียงพอแล้วครับ สิ่งที่เราต้องการคือระบบที่สามารถคิด วิเคราะห์ และช่วยทีมงานตัดสินใจเชิงรุกได้ทันทีในทุกโมดูลครับ",
            "script_en": "Good morning, executive leaders. Today, I am excited to share a transformative vision for how our organization can elevate Microsoft Dynamics 365 using Copilot AI. For years, ERP has served as our robust system of record. But in 2026, mere record-keeping is no longer enough. We need an intelligent, autonomous ERP that actively reasons, predicts, and empowers our teams to act proactively.",
            "is_title": True
        },
        # SLIDE 2: The Enterprise Reality Gap
        {
            "num": 2,
            "title": "The Enterprise Reality Gap: Where Standard D365 Stops",
            "subtitle": "ทำไม ERP ชั้นนำระดับโลก ถึงยังเหลือภาระงาน Manual ให้ทีมงานกว่า 60%?",
            "cards": [
                {"title": "1. Unstructured Data Blindspot", "detail": "Standard D365 ประมวลผลได้เฉพาะข้อมูลตาราง (SQL/Structured) แต่เอกสารจริง 80% คือ PDF ใบแจ้งหนี้, สัญญา, แชท, และอีเมล ที่ระบบอ่านไม่ออก ต้องใช้คนคีย์ซ้ำ"},
                {"title": "2. Reactive & Deterministic Rules", "detail": "ระบบบอกได้แค่ว่า 'เกิดอะไรขึ้นแล้วในอดีต' และทำตามกฎตายตัว (Static Rules) ไม่สามารถคาดการณ์ความเสี่ยงซัพพลายเออร์ หรือความผันผวนของตลาดล่วงหน้าได้"},
                {"title": "3. High Cognitive Load & Complexity", "detail": "งานกระทบยอดภาษีไทย (หัก ณ ที่จ่าย ภ.ง.ด., e-Tax), 3-Way Matching ที่ไม่ตรงกัน และการแกะข้อผิดพลาด ยังต้องพึ่งพาผู้เชี่ยวชาญนั่งตรวจสอบทีละบรรทัด"}
            ],
            "script_th": "ก่อนอื่นเราต้องยอมรับความจริงข้อหนึ่งครับ... แม้ว่า Dynamics 365 จะเป็นระบบ ERP ชั้นยอด แต่ทำไมทีมบัญชี จัดซื้อ และซัพพลายเชนของเรายังต้องเสียเวลาส่วนใหญ่ไปกับ Excel และงานคีย์ข้อมูลมือ? นั่นเป็นเพราะ Standard D365 มีจุดบอด 3 ประการ: มันอ่านเอกสารที่ไม่เป็นโครงสร้างไม่ออก, มันทำงานแบบรอให้เรื่องเกิดก่อน (Reactive), และกฎหมายภาษีของไทยมีความซับซ้อนเกินกว่าระบบสำเร็จรูปจะจัดการได้อัตโนมัติครับ",
            "script_en": "Let's begin with an honest reality check. While Dynamics 365 is a world-class platform, why do our finance, procurement, and operations teams still spend over 60% of their time trapped in Excel and manual reconciliation? Because standard ERP has three inherent blind spots: it cannot understand unstructured documents like PDFs or emails, it only tells us what happened in the past, and complex local requirements like Thai tax reconciliation require heavy human intervention."
        },
        # SLIDE 3: Strategic Blueprint
        {
            "num": 3,
            "title": "Strategic Blueprint: The Copilot AI Augmentation Layer",
            "subtitle": "สถาปัตยกรรมอัจฉริยะที่ผสานเข้ากับ D365 Dataverse ภายใต้ความปลอดภัยระดับสูงสุด",
            "cards": [
                {"title": "Multi-Modal Cognitive Ingestion", "detail": "Copilot ถอดรหัสเอกสารทุกรูปแบบ (PDF, รูปถ่าย, เอกสารภาษี) แปลงเป็นตรรกะทางธุรกิจอัตโนมัติ"},
                {"title": "Enterprise Isolated Tenant Security", "detail": "ข้อมูลองค์กร 100% อยู่ใน Tenant ส่วนตัว ข้อมูลไม่ถูกนำไปเทรนโมเดลสาธารณะ พร้อมการเข้ารหัส AES-256"},
                {"title": "Human-in-the-Loop Governance", "detail": "AI เสนอแนวทางและร่างเอกสาร แต่การอนุมัติขั้นสุดท้าย (Sign-off) ยังคงอยู่ในการควบคุมของผู้บริหาร 100%"}
            ],
            "script_th": "นี่คือจุดที่ Copilot AI เข้ามาเสริมครับ เราไม่ได้มารื้อระบบ D365 เดิม แต่เรานำเลเยอร์ปัญญาประดิษฐ์มาสวมทับบน Dataverse ที่มีอยู่เดิม โดยมีหัวใจสำคัญคือความปลอดภัยระดับ Enterprise ข้อมูลของเราจะไม่รั่วไหลออกนอก Tenant และทุกการตัดสินใจสำคัญยังคงมี 'Human-in-the-Loop' คือให้ AI เตรียมงานและวิเคราะห์ แล้วให้พนักงานเป็นผู้อนุมัติครับ",
            "script_en": "Here is our strategic architecture. We are not replacing or overhauling Dynamics 365; we are augmenting it with an intelligent cognitive layer powered by Azure OpenAI and Copilot Studio. Crucially for our leadership, this operates inside our isolated enterprise tenant with zero data leakage, and always maintains a Human-in-the-Loop governance model where AI assists and humans approve."
        },
        # SLIDE 4: Module 1 Finance
        {
            "num": 4,
            "title": "Module 1: Finance & Thai Tax Modernization",
            "subtitle": "แก้ Pain Point งานบัญชีและการกระทบยอดภาษีไทยที่ Standard D365 ทำไม่ได้",
            "cards": [
                {"title": "Pain ใน Standard D365", "detail": "• ใบแจ้งหนี้ไม่ตรง PO (เช่น มีค่าธรรมเนียมแฝง, ส่วนลดพิเศษ) ทำให้ระบบ 3-Way Matching ค้าง\n• การกระทบยอด ภ.ง.ด. 3, 53 และ e-Tax Invoice XML ต้องใช้คนตรวจคู่มือภาษี"},
                {"title": "Use Case 1: Autonomous 3-Way Audit", "detail": "Copilot อ่านเอกสารเทียบกับ PO และ GRN หากพบส่วนต่าง ระบบจะอธิบายเหตุผลเป็นภาษาไทย และร่าง Adjustment Voucher ให้อัตโนมัติ"},
                {"title": "Use Case 2: Thai Tax Auto-Reconciliation", "detail": "ตรวจสอบเลขอ้างอิงและลายมือชื่อดิจิทัลกับกรมสรรพากรอัตโนมัติ ลดเวลาปิดงวดบัญชีจาก 5 วันเหลือ 4 ชั่วโมง"}
            ],
            "script_th": "ในโมดูลการเงินครับ Pain ที่พบบ่อยที่สุดคือเมื่อใบแจ้งหนี้จากคู่ค้ามีค่าขนส่งหรือส่วนลดที่ไม่ได้ระบุใน PO ระบบ D365 มาตรฐานจะติดล็อก 3-Way Matching ทันที ต้องรอคนไปไล่ถามอีเมล... ด้วย Copilot AI ระบบจะอ่านและเข้าใจเงื่อนไข ทำการอธิบายสาเหตุเป็นภาษาไทย และร่างใบปรับปรุงบัญชีให้เสร็จสรรพ พร้อมตรวจกระทบยอด e-Tax ภาษีหัก ณ ที่จ่ายกับกรมสรรพากรแบบไร้รอยต่อครับ",
            "script_en": "In Finance, our biggest bottleneck is 3-way matching exceptions. When a vendor adds freight surcharges or off-invoice discounts, standard D365 simply halts processing, requiring accountants to manually chase emails. With Copilot, the AI understands the discrepancies in plain context, drafts adjustment journals, and validates Thai e-Tax and withholding tax digital signatures automatically, slashing month-end closing from five days down to four hours."
        },
        # SLIDE 5: Module 2 Procurement
        {
            "num": 5,
            "title": "Module 2: Procurement & Sourcing Intelligence",
            "subtitle": "จากงานจัดซื้อเชิงรับ สู่การคัดเลือกและเจรจาต่อรองคู่ค้าด้วยปัญญาประดิษฐ์",
            "cards": [
                {"title": "Pain ใน Standard D365", "detail": "• การประเมินคู่ค้าดูได้แค่วันที่ส่งของในอดีต (Lagging KPI) ไม่รู้สถานะการเงินจริงหรือความเสี่ยงภายนอก\n• การตรวจสัญญาและ RFQ เปรียบเทียบราคาหลายเจ้าทำได้ช้า"},
                {"title": "Use Case 1: Predictive AI Vendor Selection", "detail": "วิเคราะห์ประวัติคุณภาพใน D365 ร่วมกับแนวโน้มราคาสินค้าโภคภัณฑ์โลกและข่าวความเสี่ยง แนะนำสัดส่วนการสั่งซื้อที่คุ้มค่าที่สุด"},
                {"title": "Use Case 2: Contract Risk & Negotiation Copilot", "detail": "สแกนข้อสัญญาที่อาจเสียเปรียบ สรุปข้อเบี่ยงเบน และร่างแนวทางเจรจาต่อรองราคาช่วยทีมจัดซื้อ"}
            ],
            "script_th": "ถัดมาคือฝ่ายจัดซื้อครับ ปกติ D365 จะให้คะแนนคู่ค้าจากประวัติการส่งของในอดีตเท่านั้น ซึ่งไม่ช่วยเตือนภัยล่วงหน้าเลยครับ... Copilot จะดึงข้อมูลต้นทุนโภคภัณฑ์โลก ข่าวความเสี่ยง และผลงานในอดีตมารวมกัน เพื่อแนะนำว่าควรซื้อจากเจ้าไหนในสัดส่วนเท่าไร พร้อมสแกนเงื่อนไขสัญญาว่ามีข้อผูกมัดหรือเบี้ยปรับใดที่องค์กรเราเสียเปรียบหรือไม่ ช่วยให้เราประหยัดต้นทุนจัดซื้อได้ทันที 15% ครับ",
            "script_en": "In Procurement, standard D365 evaluates vendors purely on historical delivery timestamps. It cannot see impending supplier insolvency or global raw material inflation. Copilot synthesizes internal purchase history with live global commodity trends and news sentiment to recommend optimal vendor allocations. It even reviews supplier contracts to flag high-risk liability clauses and draft data-backed negotiation strategies."
        },
        # SLIDE 6: Module 3 Supply Chain
        {
            "num": 6,
            "title": "Module 3: Autonomous Supply Chain Resiliency",
            "subtitle": "พลิกโฉมการวางแผนคลังสินค้า รับมือวิกฤตโลจิสติกส์ได้ล่วงหน้า",
            "cards": [
                {"title": "Pain ใน Standard D365", "detail": "• Master Planning (MRP) คำนวณแบบคงที่ ไม่รู้ข้อมูลพายุ ท่าเรือปิด หรือตู้คอนเทนเนอร์ตกค้าง\n• คลังสินค้าต้องถือ Safety Stock สูงเพื่อกันของขาด ทำให้จมทุนมหาศาล"},
                {"title": "Use Case 1: Proactive Disruption Rerouting", "detail": "ตรวจจับความล่าช้าของการขนส่งทั่วโลก และเสนอแผนสลับ PO หรือโอนย้ายสินค้าข้ามคลัง (Cross-docking) ล่วงหน้า 2 สัปดาห์"},
                {"title": "Use Case 2: Contextual Demand Sensing", "detail": "พยากรณ์ความต้องการสินค้าแม่นยำขึ้น ลดต้นทุนการถือครองสินค้า (Carrying Cost) ลงได้ถึง 25%"}
            ],
            "script_th": "ในด้านห่วงโซ่อุปทาน การคำนวณ MRP ของระบบทั่วไปไม่เคยรู้ว่าเส้นทางขนส่งทางทะเลติดขัดหรือมีพายุเข้า ทำให้เกิดปัญหาของขาดสต็อก หรือเราต้องถือสินค้าเผื่อไว้จนเงินจม... Copilot เชื่อมโยงข้อมูลโลจิสติกส์ภายนอก แจ้งเตือนความเสี่ยงล่วงหน้า 2 สัปดาห์ และเสนอทางเลือกให้โอนย้ายสินค้าระหว่างสาขาได้ทันที ทำให้เราลดมูลค่าสต็อกจมลงได้ถึง 25% ครับ",
            "script_en": "In Supply Chain, conventional MRP calculations are blind to external disruptions such as port congestions or adverse weather, forcing us to hold excessive safety stock. Copilot injects external logistics telemetry into D365, predicting stockout risks two weeks in advance and suggesting cross-warehouse transfers. This predictive demand sensing enables us to cut inventory carrying costs by up to 25%."
        },
        # SLIDE 7: Module 4 Manufacturing
        {
            "num": 7,
            "title": "Module 4: Smart Manufacturing & Shopfloor AI",
            "subtitle": "ยกระดับสายการผลิตด้วยการเชื่อมโยงข้อมูลหน้างานและการวินิจฉัยของเสียแบบเรียลไทม์",
            "cards": [
                {"title": "Pain ใน Standard D365", "detail": "• ตารางการผลิตไม่ปรับเปลี่ยนอัตโนมัติเมื่อเครื่องจักรขัดข้อง หรือมีอัตราของเสีย (Scrap) พุ่งสูง\n• การหาสาเหตุของเสียต้องอาศัยวิศวกรไล่ดูบันทึกย้อนหลังหลายวัน"},
                {"title": "Use Case 1: Real-time Telemetry Dispatching", "detail": "เมื่อเซนเซอร์แจ้งเตือนความร้อนหรือแรงสั่นสะเทือน ระบบจะจัดลำดับ Work Order ใหม่ไปยังเครื่องจักรสำรองทันที"},
                {"title": "Use Case 2: Automated Scrap Root-Cause Diagnostics", "detail": "ประมวลผลข้อมูลล็อตวัตถุดิบ อุณหภูมิ และกะการทำงาน เพื่อสรุปสาเหตุของเสียให้หัวหน้างานใน 3 นาที"}
            ],
            "script_th": "สำหรับสายการผลิตในโรงงานครับ เมื่อเครื่องจักรเกิดอาการสั่นผิดปกติหรือของเสียสูงขึ้นในกะดึก ระบบ D365 ปกติจะไม่ปรับตารางงานให้เอง... ด้วย Copilot ที่เชื่อมกับ IoT หน้างาน ระบบจะจัดลำดับคิวงานใหม่ไปยังเครื่องสำรองทันที และวินิจฉัยหาสาเหตุของเสียจากล็อตวัตถุดิบและสภาพแวดล้อมได้ภายใน 3 นาที แทนที่จะต้องรอวิศวกรสอบสวนเป็นสัปดาห์ครับ",
            "script_en": "On the Manufacturing shopfloor, standard production scheduling fails to dynamically adapt when machines experience telemetry anomalies or sudden defect spikes. Copilot integrates IoT sensor alerts with work orders, re-routing production to backup machines before catastrophic failure occurs, and diagnosing scrap root causes across material batches and shift conditions in minutes rather than days."
        },
        # SLIDE 8: Module 5 Project Operations
        {
            "num": 8,
            "title": "Module 5: Project Operations & Governance",
            "subtitle": "ควบคุมกำไรของโครงการแบบเรียลไทม์ ป้องกันต้นทุนบานปลายก่อนสายเกินไป",
            "cards": [
                {"title": "Pain ใน Standard D365", "detail": "• การจัดสรรบุคลากรดูแค่ปฏิทินว่าง ไม่รู้ทักษะเชิงลึกหรือภาระงานจริง\n• รับรู้ว่าโครงการขาดทุน (Margin Slippage) เมื่อปิดบัญชีสิ้นงวด ซึ่งสายเกินแก้"},
                {"title": "Use Case 1: Predictive Margin Bleed Early Warning", "detail": "วิเคราะห์อัตราการเบิกจ่าย Timesheet เทียบกับผลงานจริง แจ้งเตือนความเสี่ยงงบบานปลายล่วงหน้า 4 สัปดาห์"},
                {"title": "Use Case 2: Automated SOW & Change Order Synthesis", "detail": "แปลงบทสนทนาและมติในที่ประชุมให้เป็นเอกสาร Change Request พร้อมประเมินผลกระทบต่อกำไร"}
            ],
            "script_th": "ในส่วนของการบริหารโครงการครับ ผู้บริหารมักจะทราบว่างบประมาณบานปลายก็ต่อเมื่อสิ้นเดือนไปแล้ว... Copilot จะคอยจับตาดูอัตราการใช้ชั่วโมงการทำงานเทียบกับความคืบหน้าจริง เพื่อส่งสัญญาณเตือนล่วงหน้า 4 สัปดาห์ก่อนที่กำไรจะติดลบ และยังช่วยร่างเอกสาร Change Order จากบันทึกการประชุมเพื่อเรียกเก็บเงินลูกค้าได้อย่างแม่นยำครับ",
            "script_en": "For Project Operations, executives typically discover budget overruns weeks after the damage is done. Copilot monitors milestone burn rates and timesheet velocity against deliverables, issuing margin erosion alerts four weeks in advance. It also converts meeting transcripts and client emails directly into formal Scope of Work change orders, safeguarding our project profitability."
        },
        # SLIDE 9: Business Case & Roadmap
        {
            "num": 9,
            "title": "Business Case & 90-Day Enterprise Roadmap",
            "subtitle": "ความคุ้มค่าที่วัดผลได้ และแผนงานทดสอบสู่การใช้งานจริงใน 3 เดือน",
            "cards": [
                {"title": "Key Tangible ROI Metrics", "detail": "• ลดเวลาปิดงวดบัญชีและภาษี 70% (จาก 5 วันเหลือ 4 ชม.)\n• ลดต้นทุนจัดซื้อ 15% จากการต่อรองด้วยข้อมูล AI\n• ลดต้นทุนสต็อกจม 25% ด้วย Predictive SCM"},
                {"title": "Phase 1: Proof of Value (Days 1-30)", "detail": "โฟกัสที่ AP Matching & Thai Tax Automation วัดผลความแม่นยำและประหยัดเวลา"},
                {"title": "Phase 2 & 3: Scale (Days 31-90)", "detail": "ขยายผลสู่ Procurement Intelligence และ Supply Chain พร้อมฝึกอบรมทีมงาน 100%"}
            ],
            "script_th": "หากพิจารณาด้านความคุ้มค่าในการลงทุน (ROI) ครับ การเสริมศักยภาพนี้จะช่วยคืนทุนอย่างรวดเร็ว: ปิดงวดเร็วขึ้น 70%, ประหยัดต้นทุนจัดซื้อ 15%, และลดสต็อกจม 25%... โดยเราวางแผนการทำงานเป็น 3 ระยะอย่างรัดกุม เริ่มต้นด้วย Proof of Value ใน 30 วันแรกกับงานภาษีและบัญชีเจ้าหนี้ จากนั้นจึงขยายสู่โมดูลอื่นๆ จนใช้งานได้เต็มรูปแบบภายใน 90 วันครับ",
            "script_en": "To summarize the business case: we are targeting hard, quantifiable returns: a 70% reduction in financial closing cycle times, a 15% procurement cost avoidance, and a 25% reduction in dead inventory. We recommend a structured 90-day roadmap, beginning with a 30-day Proof of Value focused on Accounts Payable and Thai tax automation before enterprise-wide scaling."
        },
        # SLIDE 10: Executive Finale (Motion Graphic)
        {
            "num": 10,
            "title": "Pioneering the Intelligent Enterprise Ecosystem",
            "subtitle": "Fujitsu Thailand × Microsoft Copilot: พันธมิตรที่จะขับเคลื่อนองค์กรสู่อนาคต",
            "cards": [
                {"title": "The Infinite Synergy", "detail": "การผสานรวมระหว่างความเชี่ยวชาญระดับองค์กรของ Fujitsu Red Infinity เข้ากับขุมพลังปัญญาประดิษฐ์ Microsoft Copilot"},
                {"title": "Tailored for Thailand Enterprise", "detail": "เข้าใจระบบภาษี ระเบียบปฏิบัติ และวัฒนธรรมการทำงานขององค์กรไทยอย่างแท้จริง"},
                {"title": "Next Steps for Executive Action", "detail": "อนุมัติเปิดโครงการ 30-Day Executive POC เพื่อสัมผัสผลลัพธ์จริงบนข้อมูลจำลองขององค์กร"}
            ],
            "script_th": "และในสไลด์สุดท้ายนี้ครับ สัญลักษณ์ Fujitsu Red Infinity ที่โอบล้อม Microsoft Dynamics 365 และ Copilot คือความมุ่งมั่นของ Fujitsu Thailand ในการเป็นพันธมิตรที่นำความเชี่ยวชาญระดับโลกและโซลูชันที่ตอบโจทย์ประเทศไทย มาช่วยให้องค์กรของท่านก้าวสู่การเป็น Autonomous Enterprise อย่างแท้จริง... ขอขอบคุณทุกท่าน และยินดีตอบทุกข้อซักถามครับ",
            "script_en": "In closing, the Fujitsu Red Infinity ribbon seamlessly uniting Microsoft Dynamics 365 and Copilot symbolizes our shared commitment to empowering your leadership. Fujitsu Thailand brings deep localization expertise, world-class enterprise delivery, and unmatched AI engineering to make your autonomous enterprise a reality. Thank you for your time, and I welcome any questions."
        }
    ]

    for data in slides_data:
        slide = prs.slides.add_slide(blank_layout)

        # Background
        bg_shape = slide.shapes.add_shape(1, 0, 0, Inches(13.333), Inches(7.5)) # Rectangle
        if data.get("is_title"):
            bg_shape.fill.solid()
            bg_shape.fill.fore_color.rgb = C_DARK_BG
            bg_shape.line.fill.background()
        elif data["num"] == 10:
            bg_shape.fill.solid()
            bg_shape.fill.fore_color.rgb = C_WHITE
            bg_shape.line.fill.background()
        else:
            bg_shape.fill.solid()
            bg_shape.fill.fore_color.rgb = C_SLATE_BG
            bg_shape.line.fill.background()

        # Header Pill
        pill_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(8), Inches(0.4))
        tf_pill = pill_box.text_frame
        p_pill = tf_pill.paragraphs[0]
        if data.get("is_title"):
            p_pill.text = f"FUJITSU THAILAND  //  EXECUTIVE PRESENTATION  //  SLIDE {data['num']}"
            p_pill.font.color.rgb = C_RED
        elif data["num"] == 10:
            p_pill.text = f"FUJITSU RED INFINITY  ✕  MICROSOFT COPILOT  //  SLIDE {data['num']} OF 10"
            p_pill.font.color.rgb = C_RED
        else:
            p_pill.text = f"D365 & COPILOT AI MODERNIZATION  //  SLIDE {data['num']} OF 10"
            p_pill.font.color.rgb = C_RED
        p_pill.font.size = Pt(11)
        p_pill.font.bold = True

        # Slide Title
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.5), Inches(0.8))
        tf_t = t_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = data["title"]
        p_t.font.bold = True
        p_t.font.size = Pt(28)
        p_t.font.color.rgb = C_WHITE if data.get("is_title") else C_TEXT_DARK

        # Slide Subtitle
        st_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(11.5), Inches(0.5))
        tf_st = st_box.text_frame
        tf_st.word_wrap = True
        p_st = tf_st.paragraphs[0]
        p_st.text = data["subtitle"]
        p_st.font.size = Pt(15)
        p_st.font.color.rgb = RGBColor(148, 163, 184) if data.get("is_title") else C_TEXT_MUTED

        # Content Rendering
        if data.get("is_title"):
            desc_box = slide.shapes.add_textbox(Inches(0.8), Inches(2.4), Inches(11.5), Inches(1.2))
            p_desc = desc_box.text_frame.paragraphs[0]
            p_desc.text = data["desc"]
            p_desc.font.size = Pt(18)
            p_desc.font.color.rgb = RGBColor(226, 232, 240)

            # Metadata chips
            meta_box = slide.shapes.add_textbox(Inches(0.8), Inches(5.8), Inches(11.5), Inches(0.8))
            p_meta = meta_box.text_frame.paragraphs[0]
            p_meta.text = "Target Audience: C-Level Executives (CEO, CFO, CIO, COO)  |  Presentation Length: 8 Minutes  |  Prepared by: Fujitsu Thailand"
            p_meta.font.size = Pt(12)
            p_meta.font.color.rgb = RGBColor(148, 163, 184)

        elif data["num"] == 10:
            # SLIDE 10: Features the exact uploaded image / motion graphic loop!
            # Insert Image on Right or Center
            img_path = "assets/slide10_fujitsu_red_infinity_motion.gif"
            if not os.path.exists(img_path):
                img_path = "assets/fujitsu_red_ribbon_d365_copilot_clean_white.png"
            
            # Place image center-left or prominent
            slide.shapes.add_picture(img_path, Inches(0.8), Inches(2.1), width=Inches(7.2))

            # Right Column: 3 Takeaways
            col_left = Inches(8.3)
            cards = data["cards"]
            for i, card in enumerate(cards):
                card_y = Inches(2.1 + i * 1.6)
                card_shape = slide.shapes.add_shape(1, col_left, card_y, Inches(4.3), Inches(1.4))
                card_shape.fill.solid()
                card_shape.fill.fore_color.rgb = RGBColor(241, 245, 249)
                card_shape.line.color.rgb = RGBColor(203, 213, 225)
                card_shape.line.width = Pt(1)

                tf = card_shape.text_frame
                tf.word_wrap = True
                p1 = tf.paragraphs[0]
                p1.text = card["title"]
                p1.font.bold = True
                p1.font.size = Pt(14)
                p1.font.color.rgb = C_RED if i == 0 else C_BLUE

                p2 = tf.add_paragraph()
                p2.text = card["detail"]
                p2.font.size = Pt(11)
                p2.font.color.rgb = C_TEXT_DARK

        else:
            # 3 Cards Layout (Horizontal)
            cards = data["cards"]
            col_w = Inches(3.65)
            col_gap = Inches(0.4)
            left_margin = Inches(0.8)

            for i, card in enumerate(cards):
                card_x = left_margin + i * (col_w + col_gap)
                card_y = Inches(2.2)
                card_h = Inches(4.5)

                card_shape = slide.shapes.add_shape(1, card_x, card_y, col_w, card_h)
                card_shape.fill.solid()
                card_shape.fill.fore_color.rgb = C_WHITE
                card_shape.line.color.rgb = C_CARD_BORDER
                card_shape.line.width = Pt(1.5)

                tf = card_shape.text_frame
                tf.word_wrap = True
                
                # Card Title
                p1 = tf.paragraphs[0]
                p1.text = card["title"]
                p1.font.bold = True
                p1.font.size = Pt(15)
                if "Pain" in card["title"]:
                    p1.font.color.rgb = C_RED
                elif "Use Case" in card["title"] or "Metrics" in card["title"]:
                    p1.font.color.rgb = C_BLUE
                else:
                    p1.font.color.rgb = C_TEXT_DARK

                # Card Body
                p2 = tf.add_paragraph()
                p2.text = card["detail"]
                p2.font.size = Pt(12)
                p2.font.color.rgb = C_TEXT_DARK

        # Populate Notes Slide (Speaker Script TH/EN)
        notes_slide = slide.notes_slide
        tf_notes = notes_slide.notes_text_frame
        tf_notes.text = f"[บทพูดภาษาไทย - Slide {data['num']} (~45-50 วินาที)]\n" + data["script_th"] + "\n\n" + f"[ENGLISH SCRIPT - Slide {data['num']} (~45-50 seconds)]\n" + data["script_en"]

    output_path = "FTH_D365_Copilot_AI_Executive_Presentation.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    create_deck()
