# -*- coding: utf-8 -*-
"""
build_static_web_deck.py
Generates Executive_D365_Copilot_Deck.html with ALL 10 SLIDES PRE-RENDERED as pure HTML.
Zero blank screen possible on load.
"""

import json

slides_data = [
    # SLIDE 1
    {
        "num": 1,
        "tag": "FUJITSU THAILAND // EXECUTIVE PRESENTATION // SLIDE 1",
        "title": "The Autonomous Enterprise: Augmenting Microsoft Dynamics 365 with Copilot AI",
        "subtitle": "ยกระดับระบบ ERP จาก 'ระบบบันทึกธุรกรรมดั้งเดิม' (System of Record) สู่ 'ระบบอัจฉริยะที่คิด วิเคราะห์ และเตือนภัยล่วงหน้า' (System of Intelligence)",
        "is_title": True,
        "script_th": "กราบเรียนท่านประธาน และคณะกรรมการบริหารทุกท่านครับ วันนี้ผมขออนุญาตนำเสนอทิศทางเชิงกลยุทธ์ในการยกระดับ Microsoft Dynamics 365 ด้วย Copilot AI... ตลอดหลายปีที่ผ่านมา ERP ทำหน้าที่เป็น 'System of Record' ที่บันทึกข้อมูลอย่างแม่นยำ แต่วันนี้ข้อมูลที่บันทึกไว้เฉยๆ ไม่เพียงพอที่จะสร้างความได้เปรียบทางธุรกิจ สิ่งที่เราต้องการคือ 'System of Intelligence' ที่สามารถคิด วิเคราะห์ ช่วยตัดสินใจ และทำงานเชิงรุกได้ครอบคลุมทุกโมดูลหลักขององค์กรครับ",
        "script_en": "Good morning, members of the Board and Executive Committee. Today, I present our strategic roadmap for augmenting Microsoft Dynamics 365 with Copilot AI. While D365 has long served as our reliable System of Record, recorded data alone is no longer enough to outpace market volatility. We must evolve into a System of Intelligence—an autonomous enterprise where AI reasons, predicts, and empowers human decision-making across all core business modules.",
        "time": "0:00 - 0:45"
    },
    # SLIDE 2
    {
        "num": 2,
        "tag": "MODULE 1: FINANCE & THAI TAX // SLIDE 2 OF 10",
        "title": "Module 1: Finance & Thai Tax Localization",
        "subtitle": "แก้ Pain Point งานบัญชีเจ้าหนี้ และภาษีไทยที่ Standard D365 ไม่ยืดหยุ่นพอ",
        "cards": [
            {
                "title": "ภาพความเป็นจริง & Pain Point",
                "detail": "• Standard 3-Way Match แข็งตัวเกินไป: ถ้าใบแจ้งหนี้มีค่าขนส่งรวมมา หรือเศษทศนิยมต่าง 5 สตางค์ ระบบจะสั่ง Hold ทันที ต้องใช้คนไปไล่สืบอีเมล\n• ความซับซ้อนของภาษีไทย: การตรวจใบหัก ณ ที่จ่าย ภ.ง.ด. 3, 53 และการกระทบยอด e-Tax Invoice ต้องใช้แรงงานคนตรวจทีละบรรทัด สิ้นเดือนทำงานหามรุ่งหามค่ำ",
                "color": "border-red-500/40 text-red-400"
            },
            {
                "title": "Copilot AI เข้ามาช่วยอย่างไร",
                "detail": "• เสมือน 'ผู้ช่วยนักบัญชีอาวุโส': อ่านเอกสาร PDF หลากหลายรูปแบบ ดึงข้อมูลอัตโนมัติ (Document Intelligence)\n• เมื่อพบราคาคลาดเคลื่อน Copilot จะตรวจสอบประวัติสัญญา และวิเคราะห์ว่าอยู่ในเกณฑ์ยอมรับได้หรือไม่ พร้อมร่าง Adjustment Voucher ให้กดอนุมัติในคลิกเดียว\n• จับคู่กระทบยอดภาษีหัก ณ ที่จ่ายกับระบบสรรพากรอัตโนมัติ",
                "color": "border-blue-500/40 text-blue-400"
            },
            {
                "title": "ผลลัพธ์ที่จับต้องได้ (Impact)",
                "detail": "⚡ ปิดงวดบัญชีเร็วขึ้น 70% (จาก 5 วัน เหลือไม่กี่ชั่วโมง)\n📉 ลดปัญหายอดค้างจ่ายในระบบ (Blocked Invoices) ได้กว่า 85%\n🛡️ ขจัดความเสี่ยงจากการถูกสรรพากรปรับเรื่องภาษีหัก ณ ที่จ่าย 100%",
                "color": "border-emerald-500/40 text-emerald-400"
            }
        ],
        "script_th": "ในโมดูลแรก คือการเงินและบัญชีครับ Pain Point จริงที่พบบ่อยมากคือ Standard 3-Way Match ใน D365 มีตรรกะที่แข็งตัวมากครับ หากใบแจ้งหนี้จากคู่ค้ามีค่าขนส่งเพิ่มมา หรือเศษสตางค์ไม่ตรงกับ PO ระบบจะสั่ง Hold การจ่ายเงินทันที ทำให้เกิดการค้างจ่ายและนักบัญชีต้องไปไล่สืบเอกสารทีละใบ ยิ่งไปกว่านั้น ภาษีหัก ณ ที่จ่าย ภ.ง.ด. 3, 53 และ e-Tax ของไทย ต้องใช้คนตรวจทีละบรรทัด... Copilot AI เข้ามาเป็นเสมือนผู้ช่วยนักบัญชีอาวุโส อ่าน PDF สแกน ตรวจสอบบริบทสัญญา หากอยู่ในเกณฑ์จะร่างใบปรับปรุงยอดให้อนุมัติในคลิกเดียว พร้อมกระทบยอดภาษีกับสรรพากรอัตโนมัติ ช่วยให้ปิดงบเร็วขึ้นถึง 70% ครับ",
        "script_en": "In our first module, Finance & Thai Tax, standard D365's 3-way matching logic is strictly deterministic. If an invoice diverges by even a few pennies or includes an off-PO delivery fee, processing halts instantly, creating manual bottlenecks. Compounding this, reconciling Thai withholding tax forms ภ.ง.ด. 3, 53 and e-Tax requires tedious line-by-line checks. Copilot AI functions like a seasoned senior accountant: it reads unstructured PDFs, understands contract tolerance, drafts one-click adjustment journals, and auto-reconciles statutory taxes, cutting closing time by 70%.",
        "time": "0:45 - 1:35"
    },
    # SLIDE 3
    {
        "num": 3,
        "tag": "MODULE 2: SOURCING & PROCUREMENT // SLIDE 3 OF 10",
        "title": "Module 2: Sourcing & Procurement Intelligence",
        "subtitle": "เปลี่ยนจัดซื้อจากการตั้งรับ สู่การรู้ทันแนวโน้มราคาตลาดและป้องกันความเสี่ยงสัญญา",
        "cards": [
            {
                "title": "ภาพความเป็นจริง & Pain Point",
                "detail": "• ซื้อตามราคากลางเดิม: Standard D365 อิงราคาจาก Trade Agreement เก่า ตาบอดต่อความผันผวนของราคาตลาดโลก (น้ำมัน, เหล็ก, ค่าระวางเรือ)\n• สัญญาคู่ค้าแฝงความเสี่ยง: เวลาเปิดประมูล (RFQ) ฝ่ายจัดซื้อไม่มีเวลาอ่านสัญญาละเอียดยิบ มักมองข้ามเงื่อนไขค่าปรับหรือการรับประกันที่เสียเปรียบ",
                "color": "border-red-500/40 text-red-400"
            },
            {
                "title": "Copilot AI เข้ามาช่วยอย่างไร",
                "detail": "• เสมือน 'ที่ปรึกษาจัดซื้อเชิงกลยุทธ์': เชื่อมโยงดัชนีราคาสินค้าโภคภัณฑ์โลก ผสานกับประวัติคุณภาพคู่ค้าใน D365\n• สแกนร่างสัญญาคู่ค้าอัตโนมัติ ทำการ Redline ไฮไลต์ข้อความที่เป็นความเสี่ยงทางกฎหมาย\n• สรุปจุดแข็ง-จุดอ่อนของแต่ละใบเสนอราคา และร่างบทเจรจาต่อรองให้ผู้จัดซื้อนำไปใช้คุยกับคู่ค้าได้ทันที",
                "color": "border-blue-500/40 text-blue-400"
            },
            {
                "title": "ผลลัพธ์ที่จับต้องได้ (Impact)",
                "detail": "💰 ประหยัดต้นทุนจัดซื้อ (Cost Avoidance) เฉลี่ย 10 - 15%\n⏱️ ลดเวลาการเปรียบเทียบ RFQ จาก 3 วัน เหลือ 30 นาที\n🔒 ป้องกันข้อพิพาททางสัญญาและค่าปรับแฝงได้ล่วงหน้า 100%",
                "color": "border-emerald-500/40 text-emerald-400"
            }
        ],
        "script_th": "โมดูลที่สอง ฝ่ายจัดซื้อครับ ปัจจุบัน D365 ทำงานโดยอิงจากราคากลางในอดีต แต่ราคาวัตถุดิบและค่าระวางเรือในตลาดโลกผันผวนตลอดเวลา ทำให้เราอาจซื้อของแพงกว่าราคาตลาดโดยไม่รู้ตัว นอกจากนี้ สัญญาคู่ค้าที่มีข้อความทางกฎหมายซับซ้อน ฝ่ายจัดซื้อมักไม่มีเวลาตรวจละเอียด... Copilot AI ทำหน้าที่เป็นที่ปรึกษาจัดซื้อเชิงกลยุทธ์ คอยมอนิเตอร์ราคาตลาดโลก เปรียบเทียบใบเสนอราคาหลายเจ้าพร้อมกัน และตรวจจับข้อสัญญาที่อาจทำให้เราเสียเปรียบ พร้อมแนะนำข้อเจรจาต่อรอง ช่วยให้เราประหยัดต้นทุนจัดซื้อได้ทันที 10 ถึง 15% ครับ",
        "script_en": "Moving to Procurement: standard D365 relies on static price catalogs and historical purchase agreements, blind to real-time global commodity swings. Furthermore, reviewing lengthy vendor contracts often leads to overlooked legal risks or unfavorable penalty terms. Copilot acts as a strategic procurement advisor: it cross-references global commodity price trends with internal vendor scorecards, automatically redlines high-risk clauses in contracts, and prepares negotiation scripts—yielding an estimated 10 to 15% in direct cost avoidance.",
        "time": "1:35 - 2:25"
    },
    # SLIDE 4
    {
        "num": 4,
        "tag": "MODULE 3: SUPPLY CHAIN & INVENTORY // SLIDE 4 OF 10",
        "title": "Module 3: Supply Chain Resiliency & Inventory",
        "subtitle": "เรดาร์ตรวจจับวิกฤตโลจิสติกส์ล่วงหน้า ป้องกันสินค้าขาดมือโดยไม่ต้องจมสต็อก",
        "cards": [
            {
                "title": "ภาพความเป็นจริง & Pain Point",
                "detail": "• Standard MRP ทำงานแบบตาบอด: คำนวณจากตัวเลขใน ERP เท่านั้น ไม่รู้ว่าท่าเรือปลายทางหยุดงาน เรือติดพายุ หรือโรงงานต้นทางสะดุด\n• รู้ตัวเมื่อสายเกินแก้: กว่าจะรู้ว่าวัตถุดิบมาไม่ทัน ก็ตอนเลยกำหนดส่งแล้ว ผลคือสายการผลิตหยุด หรือต้องแบก Safety Stock มหาศาลจนจมกระแสเงินสด",
                "color": "border-red-500/40 text-red-400"
            },
            {
                "title": "Copilot AI เข้ามาช่วยอย่างไร",
                "detail": "• เสมือน 'เรดาร์ตรวจจับวิกฤตซัพพลายเชน 24/7': เชื่อมโยงข้อมูลสภาพอากาศ การจราจรทางเรือ และข่าวสารท่าเรือ เข้ากับใบสั่งซื้อใน D365\n• แจ้งเตือนความล่าช้าล่วงหน้า 10-14 วัน ก่อนเกิดปัญหาจริง\n• จำลองทางเลือกแก้ไขปัญหา (Scenario Simulation) เช่น แนะนำคลังสำรองที่สามารถสลับของ หรือแนะนำซัพพลายเออร์ใกล้เคียงที่ส่งทดแทนได้",
                "color": "border-blue-500/40 text-blue-400"
            },
            {
                "title": "ผลลัพธ์ที่จับต้องได้ (Impact)",
                "detail": "📦 ลดปริมาณสต็อกสำรอง (Safety Stock) ลง 20 - 25% โดยไม่กระทบยอดขาย\n🚨 ลดความเสี่ยงสายการผลิตหยุดชะงัก (Downtime) จากของขาดได้ 80%\n💵 ปลดล็อกเงินทุนหมุนเวียน (Working Capital) คืนสู่กระแสเงินสดองค์กร",
                "color": "border-emerald-500/40 text-emerald-400"
            }
        ],
        "script_th": "ในโมดูลที่สาม ซัพพลายเชนและคลังสินค้าครับ ปัญหาคลาสสิกของ Standard MRP คือมันมองไม่เห็นโลกภายนอก มันไม่รู้ว่ามีมรสุมเข้า หรือท่าเรือแหลมฉบังกำลังติดขัด กว่าที่ระบบจะรู้ว่าของไม่มาส่ง ก็คือเลยวันนัดไปแล้ว ทำให้โรงงานผลิตต่อไม่ได้ หรือเราต้องแก้ปัญหาด้วยการสต็อกของไว้เยอะๆ จนเงินจม... Copilot AI เข้ามาเป็นเรดาร์ตรวจจับวิกฤต แจ้งเตือนล่วงหน้า 10 ถึง 14 วัน พร้อมจำลองแผนแก้ไขให้ทันที เช่น สลับของจากคลังอื่น ช่วยให้เราลดเงินจมใน Safety Stock ได้ถึง 20-25% ครับ",
        "script_en": "In Supply Chain and Inventory, standard MRP plans blindly using only internal database timestamps. It has zero awareness of external port congestion, strikes, or typhoons. Delays are discovered only after missing customer dock dates, forcing companies to carry bloated safety stock. Copilot acts as a 24/7 disruption radar: ingesting external maritime telematics and weather feeds, anticipating shortages 10 to 14 days ahead, and simulating rerouting options. This allows us to cut safety inventory holding by 20 to 25%.",
        "time": "2:25 - 3:15"
    },
    # SLIDE 5
    {
        "num": 5,
        "tag": "MODULE 4: MANUFACTURING // SLIDE 5 OF 10",
        "title": "Module 4: Smart Manufacturing & Operations",
        "subtitle": "วิเคราะห์หาสาเหตุของเสีย (Scrap) ในไม่กี่นาที และจัดตารางผลิตแบบยืดหยุ่น",
        "cards": [
            {
                "title": "ภาพความเป็นจริง & Pain Point",
                "detail": "• สืบหาสาเหตุของเสียล่าช้า: เมื่อชิ้นงานตกเกณฑ์ (Scrap Spike) ข้อมูลกระจัดกระจายอยู่ในเครื่องจักร IoT, สภาพแวดล้อม และล็อตวัตถุดิบ\n• วิศวกรต้องใช้เวลาครึ่งวันเปิดดูหลายระบบเพื่อหาสาเหตุ ทำให้เสียเวลาและผลิตของเสียเพิ่มขึ้นเรื่อยๆ",
                "color": "border-red-500/40 text-red-400"
            },
            {
                "title": "Copilot AI เข้ามาช่วยอย่างไร",
                "detail": "• เสมือน 'หัวหน้าวิศวกรโรงงานอัจฉริยะ': นำข้อมูลเซนเซอร์ IoT, อุณหภูมิโรงงาน และประวัติล็อตวัตถุดิบ (Lot Genealogy) มาวิเคราะห์ร่วมกัน\n• สรุปรายงานหาสาเหตุต้นตอ (Root Cause Analysis) ให้วิศวกรได้ภายในไม่กี่นาที\n• ปรับเปลี่ยนคิวงานผลิต (Dynamic Dispatching) ไปยังเครื่องสำรองใน D365 โดยอัตโนมัติ",
                "color": "border-blue-500/40 text-blue-400"
            },
            {
                "title": "ผลลัพธ์ที่จับต้องได้ (Impact)",
                "detail": "⏱️ ลดเวลาการวินิจฉัยปัญหาของเสียจาก 4 ชั่วโมง เหลือไม่เกิน 15 นาที\n📉 ลดอัตราของเสีย (Scrap Rate) ในสายการผลิตลง 18 - 25%\n⚙️ ยกระดับ Overall Equipment Effectiveness (OEE) ของเครื่องจักรหลัก",
                "color": "border-emerald-500/40 text-emerald-400"
            }
        ],
        "script_th": "โมดูลที่สี่ ฝ่ายผลิตและควบคุมคุณภาพครับ เมื่อเกิดของเสียในสายการผลิต หรือเครื่องจักรเริ่มมีอาการสะดุด ปัญหาคือข้อมูลอยู่กระจัดกระจายมากครับ ทั้งเซนเซอร์ความร้อน สภาพอากาศ และล็อตวัตถุดิบ วิศวกรต้องเสียเวลาหลายชั่วโมงในการสืบหาต้นตอ... Copilot AI จะเชื่อมโยงข้อมูล IoT และประวัติใน D365 เข้าด้วยกัน สรุป Root Cause ให้วิศวกรได้ในเวลาไม่กี่นาที พร้อมปรับลำดับงานผลิตไปยังเครื่องจักรสำรองได้ทันที ช่วยลดอัตราของเสียลงได้ถึง 18-25% ครับ",
        "script_en": "On the Manufacturing shop floor, diagnosing quality drift and equipment failures requires cross-referencing disparate IoT logs, factory ambient humidity, and batch genealogy. Engineers often spend half a day investigating the cause while defective parts accumulate. Copilot correlates real-time IoT telemetry with D365 batch records, generating root-cause diagnostics within minutes and dynamically adjusting production schedules to alternative work centers, reducing scrap rates by 18 to 25%.",
        "time": "3:15 - 4:05"
    },
    # SLIDE 6
    {
        "num": 6,
        "tag": "MODULE 5: PROJECT OPERATIONS // SLIDE 6 OF 10",
        "title": "Module 5: Project Operations & Professional Services",
        "subtitle": "เตือนภัยกำไรรั่วไหล (Margin Bleed) และแปลงข้อสรุปประชุมเป็น Change Order",
        "cards": [
            {
                "title": "ภาพความเป็นจริง & Pain Point",
                "detail": "• กำไรรั่วไหลแบบเงียบๆ (Silent Margin Bleed): ลูกค้าขอแก้งานหรือเพิ่มงานเล็กๆ ในที่ประชุม (Scope Creep) แต่ทีมหน้างานไม่ได้บันทึกหรือออกบิล\n• รู้ตัวว่าขาดทุนเมื่อจบโปรเจกต์: เสียเวลาในการสรุปเอกสารเพื่อขออนุมัติงานเพิ่ม ทำให้ไม่ได้เรียกเก็บเงินตามจริง",
                "color": "border-red-500/40 text-red-400"
            },
            {
                "title": "Copilot AI เข้ามาช่วยอย่างไร",
                "detail": "• เสมือน 'ผู้ช่วยผู้จัดการโครงการ': มอนิเตอร์อัตราการใช้ชั่วโมงงานและงบประมาณเทียบกับ Milestone แบบ Real-time\n• เตือนภัยล่วงหน้า 3-4 สัปดาห์ ก่อนที่งบประมาณจะบานปลายเกินกำไรที่ตั้งไว้\n• ถอดบันทึกการประชุม แปลงเป็นร่างเอกสาร Change Order พร้อมคำนวณมูลค่างานเพิ่มให้อัตโนมัติ เพื่อส่งให้ลูกค้าอนุมัติก่อนเริ่มทำ",
                "color": "border-blue-500/40 text-blue-400"
            },
            {
                "title": "ผลลัพธ์ที่จับต้องได้ (Impact)",
                "detail": "📈 ปกป้องอัตรากำไรโครงการ (Project Profit Margin) เพิ่มขึ้น 12 - 18%\n📝 เก็บเงินค่างานเพิ่ม (Unbilled Scope Creep) ได้ครบถ้วน 100%\n⚡ ลดเวลาจัดทำเอกสาร Change Order และ SOW ลง 80%",
                "color": "border-emerald-500/40 text-emerald-400"
            }
        ],
        "script_th": "โมดูลที่ห้า งานบริหารโครงการและบริการครับ ปัญหาคลาสสิกที่ทำให้โครงการขาดทุนคือ 'Margin Bleed' หรือกำไรที่รั่วไหลจากงานงอกในที่ประชุม ลูกค้าขอให้ช่วยทำเพิ่มนิดหน่อย ทีมงานก็ทำให้โดยไม่ได้ออกเอกสารขอแก้งาน กว่าผู้บริหารจะรู้ว่าขาดทุนก็คือตอนปิดโครงการแล้ว... Copilot AI ทำหน้าที่เป็นเรดาร์ตรวจจับอัตราการใช้งบ เตือนล่วงหน้า 4 สัปดาห์ก่อนกำไรติดลบ และสามารถถอดเทปการประชุม แปลงเป็นร่าง Change Order พร้อมคิดราคาค่างานเพิ่มให้ลูกค้าเซ็นอนุมัติได้ทันทีครับ",
        "script_en": "In Project Operations and Professional Services, unbilled scope creep is the primary driver of silent margin erosion. Client requests made during meetings are executed by engineers without formal change orders, only discovering project losses at final review. Copilot monitors labor burn rates against project milestones, alerting management 4 weeks before margin bleed occurs, and translates meeting transcripts into billable Change Orders ready for client sign-off, protecting project profitability by 12 to 18%.",
        "time": "4:05 - 4:55"
    },
    # SLIDE 7
    {
        "num": 7,
        "tag": "TOOLS & ARCHITECTURE // SLIDE 7 OF 10",
        "title": "Enterprise Technology Stack & Architecture",
        "subtitle": "สรุปเครื่องมือหลักที่ใช้ขับเคลื่อนระบบ ภายใต้ความปลอดภัยระดับ Enterprise",
        "cards": [
            {
                "title": "1. Cognitive & AI Engine",
                "detail": "• Microsoft Copilot Studio: เครื่องมือสร้างและปรับแต่ง AI Agents ให้เข้าใจขั้นตอนเฉพาะขององค์กร\n• Dynamics 365 Copilot: ฟังก์ชัน AI พื้นฐานที่ฝังมาในแต่ละโมดูลของ D365\n• Azure OpenAI Service: โมเดล GPT-4o รันบน Private Tenant ไม่แชร์ข้อมูลกับภายนอก",
                "color": "border-purple-500/40 text-purple-400"
            },
            {
                "title": "2. Data Integration Layer",
                "detail": "• Microsoft Dataverse: ฐานข้อมูลกลางที่เก็บ Transaction และโครงสร้างของ D365\n• Azure Document Intelligence: แปลงเอกสารสแกน PDF ใบกำกับภาษี และสัญญา เป็นข้อมูลเชิงโครงสร้าง\n• Power Platform: เชื่อมต่อ API ภายนอก (กรมสรรพากร, อัตราแลกเปลี่ยน, ข้อมูลท่าเรือ)",
                "color": "border-blue-500/40 text-blue-400"
            },
            {
                "title": "3. Security & Governance",
                "detail": "• Isolated Tenant: ข้อมูลองค์กรถูกจำกัดอยู่ภายใน Tenant เรา 100% ไม่ถูกนำไปเทรนโมเดลสาธารณะ\n• AES-256 Encryption: เข้ารหัสข้อมูลทั้งในขณะพักและขณะรับส่ง\n• Human-in-the-Loop: AI มีหน้าที่วิเคราะห์และร่างข้อเสนอ แต่ผู้มีอำนาจตัดสินใจอนุมัติขั้นสุดท้ายคือผู้บริหาร",
                "color": "border-emerald-500/40 text-emerald-400"
            }
        ],
        "script_th": "สำหรับเครื่องมือและเทคโนโลยีที่ใช้ครับ เราใช้เทคโนโลยีมาตรฐานระดับ Enterprise ของ Microsoft ที่ทำงานร่วมกันอย่างไร้รอยต่อ: 1. ด้าน AI เราใช้ Copilot Studio และ Azure OpenAI Service รันโมเดลบน Private Tenant ของเราเอง 2. ด้านข้อมูล เราใช้ Dataverse และ Azure Document Intelligence ในการสกัดเอกสาร PDF และสัญญา 3. ที่สำคัญที่สุดคือความปลอดภัย ข้อมูลองค์กร 100% จะไม่มีวันรั่วไหลไปเทรน AI สาธารณะ และใช้หลักการ Human-in-the-Loop โดยผู้บริหารและพนักงานของเรายังคงมีอำนาจตัดสินใจอนุมัติขั้นสุดท้ายเสมอครับ",
        "script_en": "Regarding the technology stack, we leverage Microsoft's enterprise-grade architecture: 1. The AI engine combines Copilot Studio, embedded D365 Copilot, and Azure OpenAI Service operating within a private tenant. 2. Data integration is managed via Dataverse and Azure Document Intelligence for robust unstructured document extraction. 3. Most importantly, enterprise security is paramount: zero data leakage, AES-256 encryption, and a strict Human-in-the-Loop governance model where AI proposes, but humans always retain ultimate approval authority.",
        "time": "4:55 - 5:45"
    },
    # SLIDE 8
    {
        "num": 8,
        "tag": "FRAMEWORK & TIMELINE // SLIDE 8 OF 10",
        "title": "Implementation Framework & Timeline",
        "subtitle": "ขั้นตอนการดำเนินงานมาตรฐาน 4 เฟส ในกรอบเวลา 8 - 12 สัปดาห์ (เปิดกว้าง ยังไม่ผูกมัดเลือกข้อใด)",
        "is_timeline": True,
        "cards": [
            {
                "title": "Phase 1: Readiness & Discovery\n(สัปดาห์ที่ 1 - 2)",
                "detail": "• สำรวจกระบวนการทำงานและคุณภาพข้อมูลในแต่ละโมดูล\n• ประเมินความพร้อมด้านความปลอดภัยและสิทธิ์การเข้าถึง\n• นำเสนอผลการประเมินเพื่อให้ผู้บริหารพิจารณาคัดเลือกโมดูลที่เหมาะสมที่สุดสำหรับเริ่มต้น",
                "color": "border-blue-500/40 text-blue-400"
            },
            {
                "title": "Phase 2: Foundation & Setup\n(สัปดาห์ที่ 3 - 4)",
                "detail": "• ติดตั้งสภาพแวดล้อม Copilot Studio และ Azure OpenAI บน Private Tenant\n• กำหนดนโยบายความปลอดภัยและ Data Governance\n• เชื่อมต่อ Dataverse และระบบเอกสารที่เกี่ยวข้อง",
                "color": "border-purple-500/40 text-purple-400"
            },
            {
                "title": "Phase 3: Pilot & Iteration\n(สัปดาห์ที่ 5 - 8)",
                "detail": "• เริ่มต้นทดลองใช้งานในขอบเขตที่คัดเลือก\n• ปรับจูน Prompt และ Knowledge Base ตามบริบทธุรกิจจริง\n• ทดสอบความแม่นยำร่วมกับ Key Users ในสภาพแวดล้อมควบคุม",
                "color": "border-amber-500/40 text-amber-400"
            },
            {
                "title": "Phase 4: Scale & Evaluation\n(สัปดาห์ที่ 9 - 12)",
                "detail": "• อบรมผู้ใช้งาน (Upskilling) และจัดการการเปลี่ยนแปลง (Change Management)\n• วัดผลสัมฤทธิ์ทางธุรกิจและ ROI จริงเทียบกับเป้าหมาย\n• วางแผนขยายผล (Rollout) สู่โมดูลอื่นๆ ตามลำดับความสำคัญ",
                "color": "border-emerald-500/40 text-emerald-400"
            }
        ],
        "script_th": "ในด้านขั้นตอนและระยะเวลา เราวางกรอบการทำงานมาตรฐานไว้ 4 เฟส รวมระยะเวลาประมาณ 8 ถึง 12 สัปดาห์ โดยในจุดนี้ เรายังไม่ได้เจาะจงว่าจะเลือกโมดูลไหนมาทำก่อนครับ แต่เราจะเริ่มที่ Phase 1 คือการทำ Discovery ร่วมกันเพื่อประเมินความพร้อมของข้อมูลในแต่ละโมดูล แล้วให้ผู้บริหารเป็นผู้เลือกจุดที่สร้าง Impact สูงสุด จากนั้นใน Phase 2 จะเป็นการวางระบบความปลอดภัย Phase 3 คือการทดลองใช้และปรับจูนความแม่นยำ และ Phase 4 คือการขยายผลพร้อมวัดผลตอบแทน ROI จริง เพื่อให้การลงทุนมีความเสี่ยงต่ำและคุ้มค่าที่สุดครับ",
        "script_en": "Our implementation approach follows a proven 4-phase enterprise framework spanning 8 to 12 weeks. Importantly, we do not pre-select a specific POC module today. Instead, Phase 1 conducts a thorough readiness assessment across all modules, empowering leadership to prioritize the highest-impact opportunity. Phase 2 establishes our secure foundation. Phase 3 executes the pilot and prompt tuning with key users, and Phase 4 scales adoption while measuring tangible business ROI. This ensures a controlled, agile, and low-risk journey.",
        "time": "5:45 - 6:30"
    },
    # SLIDE 9
    {
        "num": 9,
        "tag": "DUAL ROI ANALYSIS // SLIDE 9 OF 10",
        "title": "Dual-Perspective ROI: Value for Customer & Value for Our Organization",
        "subtitle": "ความคุ้มค่าที่ชัดเจนทั้งในมุมมองของลูกค้าผู้ใช้งาน และในมุมมองขององค์กรเรา (Fujitsu)",
        "is_dual_roi": True,
        "cards": [
            {
                "title": "🎯 ความคุ้มค่าสำหรับลูกค้า (Client Enterprise ROI)",
                "detail": "• ปิดบัญชีเร็วขึ้น 70%: ปลดล็อกเวลาของทีมนักบัญชีสู่การวางแผนการเงิน\n• ประหยัดต้นทุนจัดซื้อ 10-15%: จากการรู้ทันแนวโน้มราคาตลาดและการเจรจาต่อรอง\n• ลดเงินจมใน Safety Stock 20-25%: กระแสเงินสดหมุนเวียนเพิ่มขึ้นทันที\n• ลดความเสี่ยงทางภาษีและสัญญา 100%: ป้องกันเบี้ยปรับและข้อพิพาททางกฎหมาย\n• ยกระดับพนักงาน: ลดงานคีย์ข้อมูลซ้ำซาก เพิ่มความพึงพอใจในการทำงานของบุคลากร",
                "color": "border-blue-500/50 text-blue-400"
            },
            {
                "title": "🏆 ความคุ้มค่าสำหรับองค์กรของเรา (Fujitsu Partner ROI)",
                "detail": "• ก้าวสู่ Strategic AI Transformation Partner: ขยับจากผู้ติดตั้ง ERP ดั้งเดิม สู่ที่ปรึกษา AI ระดับสูงที่มี Margin มากขึ้น\n• ส่งมอบโครงการเร็วขึ้น 30-40%: ใช้ AI ช่วยทดสอบและ Migrate ข้อมูล ลดภาระ Man-days ของทีมงานเรา\n• สร้างกระแสรายได้ใหม่ต่อเนื่อง (Recurring Revenue): จากบริการ AI Advisory, Knowledge Tuning, และ AI Managed Services\n• เพิ่มขีดความสามารถในการแข่งขัน (Win Rate สูงขึ้น): ข้อเสนอโครงการของเราโดดเด่นและเหนือกว่าคู่แข่งในตลาดอย่างชัดเจน",
                "color": "border-red-500/50 text-red-400"
            }
        ],
        "script_th": "สไลด์นี้คือหัวใจสำคัญครับ คือผลตอบแทนที่คุ้มค่าทั้ง 2 ด้าน: ฝั่งลูกค้า ได้ประโยชน์โดยตรงทั้งการปิดบัญชีเร็วขึ้น 70%, ประหยัดต้นทุนจัดซื้อ 10-15%, ลดเงินจมในสต็อก 20-25% และลดความเสี่ยงข้อผิดพลาด... ขณะเดียวกัน ฝั่งองค์กรของเรา (Fujitsu) เรายกระดับจากการเป็นเพียงผู้ติดตั้งระบบ ERP ธรรมดา สู่การเป็น 'Strategic AI Transformation Partner' ซึ่งมีกำไรต่อโครงการสูงขึ้น ส่งมอบงานได้เร็วขึ้น ลด Man-days ของทีมงานเรา และเปิดช่องทางรายได้ใหม่จากการดูแลระบบ AI อย่างต่อเนื่อง เป็นผลประโยชน์ร่วมกันแบบ Win-Win อย่างแท้จริงครับ",
        "script_en": "Slide 9 presents our business justification from a dual-perspective ROI. For the customer, the value is immediate: 70% faster financial close, 10 to 15% procurement cost avoidance, 20 to 25% lower inventory carrying costs, and total compliance safeguard. Simultaneously, for Fujitsu as their trusted partner, this elevates us from a traditional ERP system integrator into a high-margin Strategic AI Transformation Partner, reducing delivery man-days by up to 40%, increasing our win-rate in competitive tenders, and generating sustainable recurring AI advisory revenue.",
        "time": "6:30 - 7:15"
    },
    # SLIDE 10
    {
        "num": 10,
        "tag": "FUJITSU RED INFINITY ✕ MICROSOFT COPILOT // SLIDE 10 OF 10",
        "title": "The Executive Finale: Partnership Synergy",
        "subtitle": "Fujitsu Red Infinity × Dynamics 365 & Copilot AI",
        "is_finale": True,
        "cards": [
            {"title": "1. Infinite Transformation", "detail": "สัญลักษณ์ Fujitsu Red Infinity สะท้อนความมุ่งมั่นที่ไม่สิ้นสุดในการส่งมอบคุณค่าและขับเคลื่อนธุรกิจสู่อนาคต"},
            {"title": "2. Seamless Augmentation", "detail": "ผสานความมั่นคงของระบบ D365 เข้ากับพลังปัญญาประดิษฐ์ Copilot AI ได้อย่างสมบูรณ์แบบโดยไม่ต้องรื้อระบบเดิม"},
            {"title": "3. Readiness for Action", "detail": "พร้อมเริ่มต้นขั้นตอนประเมินความพร้อมและนำเสนอผลลัพธ์ที่เป็นรูปธรรมต่อผู้บริหารในทุกโมดูล"}
        ],
        "script_th": "ทุกท่านครับ บนหน้าจอสุดท้ายนี้ คือภาพเคลื่อนไหวของสัญลักษณ์ 'Fujitsu Red Infinity' ที่สะท้อนถึงคำมั่นสัญญาที่ไม่สิ้นสุดในการขับเคลื่อนนวัตกรรมสู่ความยั่งยืน... เมื่อเราผสานรากฐานที่แข็งแกร่งของ Dynamics 365 เข้ากับพลังการเรียนรู้และคาดการณ์ของ Copilot AI เราไม่ได้เพียงแค่อัปเกรดระบบ ERP แต่เรากำลังสร้างองค์กรที่พร้อมรับมือกับทุกความท้าทาย ดำเนินการได้อย่างชาญฉลาด และก้าวขึ้นเป็นผู้นำในอุตสาหกรรมอย่างแท้จริง ขอขอบคุณท่านคณะกรรมการบริหารทุกท่าน และยินดีตอบทุกข้อซักถามครับ",
        "script_en": "Distinguished board members, our final slide presents the animated Fujitsu Red Infinity loop—representing our infinite commitment to sustainable transformation and customer success. By unifying the structured operational rigor of Dynamics 365 with the predictive intelligence of Copilot AI, we empower both our clients and ourselves to achieve unprecedented agility and market leadership. Thank you very much for your time, and I welcome your strategic questions and guidance.",
        "time": "7:15 - 8:00"
    }
]

def render_slide_html(s):
    num = s["num"]
    hidden_class = "" if num == 1 else "hidden"

    if s.get("is_title"):
        return f"""
    <!-- SLIDE {num} -->
    <div id="slide-{num}" class="slide-item {hidden_class} w-full h-full flex flex-col justify-between p-6 md:p-10 bg-gradient-to-br from-slate-950 via-slate-900 to-red-950/40 rounded-3xl border border-red-500/30 shadow-2xl">
      <div>
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-red-600/20 border border-red-500/40 text-red-400 text-xs font-mono font-bold mb-4">
          <span class="w-2 h-2 rounded-full bg-red-500 animate-ping"></span>
          <span>{s['tag']}</span>
        </div>
        <h2 class="text-2xl md:text-4xl lg:text-5xl font-black text-white tracking-tight leading-tight max-w-4xl">
          {s['title']}
        </h2>
        <p class="text-sm md:text-lg text-slate-300 font-semibold mt-3 max-w-3xl leading-relaxed">
          {s['subtitle']}
        </p>
      </div>

      <div class="border-t border-slate-800 pt-4 flex items-center justify-between text-xs text-slate-400 font-mono">
        <div>Target Audience: C-Level Executives (CEO, CFO, CIO, COO)</div>
        <div>Speech: ~8 Minutes // Prepared by Fujitsu Thailand</div>
      </div>
    </div>
"""
    elif s.get("is_finale"):
        cards_html = ""
        for i, c in enumerate(s["cards"]):
            c_color = "text-red-600" if i == 0 else "text-blue-600"
            cards_html += f"""
          <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 shadow-sm">
            <div class="font-extrabold text-sm {c_color} mb-1">{c['title']}</div>
            <div class="text-xs text-slate-600 leading-relaxed">{c['detail']}</div>
          </div>
"""
        return f"""
    <!-- SLIDE {num} (FINALE WITH MOTION GRAPHIC) -->
    <div id="slide-{num}" class="slide-item {hidden_class} w-full h-full flex flex-col justify-between p-6 md:p-8 bg-white rounded-3xl border border-slate-200 shadow-2xl text-slate-900">
      <div>
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-red-100 border border-red-300 text-red-600 text-xs font-mono font-bold mb-1.5">
          <span class="w-2 h-2 rounded-full bg-red-600 animate-ping"></span>
          <span>{s['tag']}</span>
        </div>
        <h2 class="text-xl md:text-3xl font-black text-slate-950 tracking-tight">
          {s['title']}
        </h2>
        <p class="text-xs md:text-sm text-slate-600 font-semibold">
          {s['subtitle']}
        </p>
      </div>

      <!-- SPLIT: MOTION GRAPHIC IMAGE + 3 TAKEAWAYS -->
      <div class="grid grid-cols-1 md:grid-cols-12 gap-5 items-center flex-1 my-2 min-h-0 overflow-hidden">
        <!-- Motion Graphic Render of Exact Uploaded Image -->
        <div class="md:col-span-7 rounded-2xl overflow-hidden border border-slate-200 bg-slate-50 shadow-lg relative h-full max-h-[340px] flex items-center justify-center">
          <img src="assets/slide10_fujitsu_red_infinity_motion.gif" alt="Fujitsu Red Infinity Motion" class="w-full h-full object-contain">
          <div class="absolute bottom-2 left-2 px-2.5 py-1 rounded-md bg-black/75 backdrop-blur-md text-[10px] font-mono text-white flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-red-500 animate-pulse"></span>
            <span>Active 3D Motion Graphic // Fujitsu Red Infinity × D365 & Copilot</span>
          </div>
        </div>

        <!-- 3 Executive Key Takeaways -->
        <div class="md:col-span-5 flex flex-col gap-2.5">
          {cards_html}
        </div>
      </div>

      <div class="border-t border-slate-200 pt-2 flex items-center justify-between text-xs text-slate-500 font-mono">
        <div>Fujitsu Thailand (FTH) × Microsoft Copilot AI Partnership</div>
        <div>Slide 10 of 10 // Open for Executive Q&A</div>
      </div>
    </div>
"""
    elif s.get("is_dual_roi"):
        cards_html = ""
        for c in s["cards"]:
            color = c.get("color", "border-slate-800")
            cards_html += f"""
        <div class="bg-slate-950/80 border {color} rounded-2xl p-5 flex flex-col justify-between shadow-xl">
          <div>
            <h3 class="font-black text-sm md:text-base text-white mb-2.5 pb-2.5 border-b border-slate-800 flex items-center gap-2">
              {c['title']}
            </h3>
            <div class="text-xs md:text-sm text-slate-300 leading-relaxed whitespace-pre-line font-normal space-y-1.5">
              {c['detail']}
            </div>
          </div>
        </div>
"""
        return f"""
    <!-- SLIDE {num} (DUAL ROI) -->
    <div id="slide-{num}" class="slide-item {hidden_class} w-full h-full flex flex-col justify-between p-6 md:p-8 bg-slate-900 rounded-3xl border border-slate-800 shadow-2xl text-white">
      <div>
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-800 border border-slate-700 text-slate-300 text-xs font-mono font-bold mb-1.5">
          <span class="w-2 h-2 rounded-full bg-red-500"></span>
          <span>{s['tag']}</span>
        </div>
        <h2 class="text-xl md:text-3xl font-black text-white tracking-tight">
          {s['title']}
        </h2>
        <p class="text-xs md:text-sm text-slate-400 font-semibold">
          {s['subtitle']}
        </p>
      </div>

      <!-- 2 Columns -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-5 my-auto">
        {cards_html}
      </div>

      <div class="border-t border-slate-800 pt-2 flex items-center justify-between text-[11px] text-slate-500 font-mono">
        <div>Win-Win Value Proposition: Customer & Partner</div>
        <div>Slide {num} of 10</div>
      </div>
    </div>
"""
    elif s.get("is_timeline"):
        cards_html = ""
        for c in s["cards"]:
            color = c.get("color", "border-slate-800")
            cards_html += f"""
        <div class="bg-slate-950/80 border {color} rounded-2xl p-3.5 flex flex-col justify-between shadow-xl">
          <div>
            <h3 class="font-black text-xs md:text-sm text-white mb-2 pb-2 border-b border-slate-800/80 flex items-center gap-1 whitespace-pre-line">
              {c['title']}
            </h3>
            <div class="text-[11px] md:text-xs text-slate-300 leading-relaxed whitespace-pre-line font-normal">
              {c['detail']}
            </div>
          </div>
        </div>
"""
        return f"""
    <!-- SLIDE {num} (TIMELINE) -->
    <div id="slide-{num}" class="slide-item {hidden_class} w-full h-full flex flex-col justify-between p-6 md:p-8 bg-slate-900 rounded-3xl border border-slate-800 shadow-2xl text-white">
      <div>
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-800 border border-slate-700 text-slate-300 text-xs font-mono font-bold mb-1.5">
          <span class="w-2 h-2 rounded-full bg-red-500"></span>
          <span>{s['tag']}</span>
        </div>
        <h2 class="text-xl md:text-3xl font-black text-white tracking-tight">
          {s['title']}
        </h2>
        <p class="text-xs md:text-sm text-slate-400 font-semibold">
          {s['subtitle']}
        </p>
      </div>

      <!-- 4 Columns -->
      <div class="grid grid-cols-1 md:grid-cols-4 gap-3 my-auto">
        {cards_html}
      </div>

      <div class="border-t border-slate-800 pt-2 flex items-center justify-between text-[11px] text-slate-500 font-mono">
        <div>Agile & Scalable Implementation Framework</div>
        <div>Slide {num} of 10</div>
      </div>
    </div>
"""
    else:
        # Standard 3-Card Layout
        cards_html = ""
        for c in s["cards"]:
            color = c.get("color", "border-slate-800")
            cards_html += f"""
        <div class="bg-slate-950/80 border {color} rounded-2xl p-4 flex flex-col justify-between shadow-xl">
          <div>
            <h3 class="font-black text-sm text-white mb-2 pb-2 border-b border-slate-800/80 flex items-center gap-1.5">
              {c['title']}
            </h3>
            <div class="text-xs text-slate-300 leading-relaxed whitespace-pre-line font-normal">
              {c['detail']}
            </div>
          </div>
        </div>
"""
        return f"""
    <!-- SLIDE {num} -->
    <div id="slide-{num}" class="slide-item {hidden_class} w-full h-full flex flex-col justify-between p-6 md:p-8 bg-slate-900 rounded-3xl border border-slate-800 shadow-2xl text-white">
      <div>
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-800 border border-slate-700 text-slate-300 text-xs font-mono font-bold mb-1.5">
          <span class="w-2 h-2 rounded-full bg-red-500"></span>
          <span>{s['tag']}</span>
        </div>
        <h2 class="text-xl md:text-3xl font-black text-white tracking-tight">
          {s['title']}
        </h2>
        <p class="text-xs md:text-sm text-slate-400 font-semibold">
          {s['subtitle']}
        </p>
      </div>

      <!-- 3 Columns -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-auto">
        {cards_html}
      </div>

      <div class="border-t border-slate-800 pt-2 flex items-center justify-between text-[11px] text-slate-500 font-mono">
        <div>D365 & Copilot AI Augmentation Layer</div>
        <div>Slide {num} of 10</div>
      </div>
    </div>
"""

def generate_full_html():
    all_slides_html = "\n".join([render_slide_html(s) for s in slides_data])
    slides_json = json.dumps(slides_data, ensure_ascii=False)

    html_template = f"""<!DOCTYPE html>
<html lang="th" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>D365 & Copilot AI Modernization — Executive Deck (10 Slides)</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&family=Sarabun:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    body {{
      font-family: 'Plus Jakarta Sans', Sarabun, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}
    .slide-enter {{ animation: fadeIn 0.25s cubic-bezier(0.16, 1, 0.3, 1) forwards; }}
    @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(4px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
    ::-webkit-scrollbar-track {{ background: rgba(15, 23, 42, 0.6); }}
    ::-webkit-scrollbar-thumb {{ background: rgba(100, 116, 139, 0.5); border-radius: 9999px; }}
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col justify-between selection:bg-red-600 selection:text-white">

  <!-- TOP BAR -->
  <header class="border-b border-slate-800 bg-slate-900/90 backdrop-blur-xl sticky top-0 z-50 px-4 py-2.5">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-3 flex-wrap">
      <!-- Brand & Title -->
      <div class="flex items-center gap-3">
        <a href="index.html" class="flex items-center gap-2 group">
          <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-red-600 to-red-800 flex items-center justify-center font-black text-white text-base shadow-md shadow-red-900/40">
            ∞
          </div>
          <div>
            <div class="text-[10px] font-extrabold uppercase tracking-widest text-red-400">Fujitsu Thailand (FTH)</div>
            <h1 class="text-sm md:text-base font-black text-white flex items-center gap-1.5">
              <span>Executive Deck: D365 & Copilot AI</span>
              <span class="px-2 py-0.5 rounded-full bg-red-600/20 border border-red-500/40 text-[11px] font-bold text-red-300">10 Slides</span>
            </h1>
          </div>
        </a>
      </div>

      <!-- Controls & Download -->
      <div class="flex items-center gap-2 flex-wrap text-xs font-bold">
        <!-- Presentation Timer -->
        <div class="px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-800 text-slate-300 font-mono flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
          <span>เวลาพูด:</span>
          <span id="speechTimer" class="text-emerald-400 font-bold">08:00</span>
        </div>

        <!-- Language Script Toggle -->
        <button onclick="toggleScriptLang()" id="btnLangToggle" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 flex items-center gap-1 transition-all">
          <span>🌐 บทพูด:</span>
          <span id="langLabel" class="text-red-400 font-bold">ภาษาไทย</span>
        </button>

        <!-- AI Voice Narrator -->
        <button onclick="toggleSpeech()" id="btnVoiceToggle" class="px-3 py-1.5 rounded-lg bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white flex items-center gap-1 shadow-md shadow-purple-950/40 transition-all">
          <span id="voiceIcon">🎙️</span>
          <span id="voiceLabel">ฟังเสียงบรรยาย</span>
        </button>

        <!-- Fullscreen -->
        <button onclick="toggleFullscreen()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 flex items-center gap-1 transition-all" title="สลับโหมดเต็มจอ">
          <span>⛶</span>
          <span class="hidden sm:inline">เต็มจอ</span>
        </button>

        <!-- PPTX Download -->
        <a href="FTH_D365_Copilot_AI_Executive_Presentation.pptx" download class="px-3 py-1.5 rounded-lg bg-red-600 hover:bg-red-500 text-white flex items-center gap-1 shadow-md shadow-red-900/40 transition-all">
          <span>📥 ดาวน์โหลด PPTX</span>
        </a>

        <!-- Link back to Hub -->
        <a href="index.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white border border-slate-700 flex items-center gap-1 transition-all" title="กลับหน้าหลัก">
          <span>🏠</span>
        </a>
      </div>
    </div>
  </header>

  <!-- MAIN SLIDE VIEWER -->
  <main class="max-w-7xl mx-auto px-4 py-4 w-full flex-1 flex flex-col gap-4">

    <!-- SLIDE VIEWPORT CONTAINER (Pre-rendered static HTML - Never Blank) -->
    <div class="w-full h-[520px] md:h-[560px] relative" id="slideViewport">
{all_slides_html}
    </div>

    <!-- SLIDE CONTROLS & THUMBNAIL TRACK -->
    <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-3 flex items-center justify-between gap-4 flex-wrap">
      <!-- Prev / Next Buttons -->
      <div class="flex items-center gap-2">
        <button onclick="prevSlide()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs flex items-center gap-1 border border-slate-700 transition-all">
          <span>⬅️ ย้อนกลับ</span>
        </button>
        <span class="text-xs font-mono text-slate-300 font-bold px-2" id="slideCounter">
          Slide 1 / 10
        </span>
        <button onclick="nextSlide()" class="px-4 py-2 rounded-xl bg-red-600 hover:bg-red-500 text-white font-bold text-xs flex items-center gap-1 shadow-md shadow-red-900/30 transition-all">
          <span>ถัดไป ➡️</span>
        </button>
      </div>

      <!-- Quick Slide Dots -->
      <div class="flex items-center gap-1.5 flex-wrap" id="dotsContainer">
        <!-- Dots rendered by JS -->
      </div>

      <!-- Fullscreen & Help -->
      <div class="text-[11px] font-mono text-slate-400 hidden sm:block">
        กดปุ่ม <kbd class="px-1.5 py-0.5 bg-slate-800 rounded border border-slate-700">←</kbd> <kbd class="px-1.5 py-0.5 bg-slate-800 rounded border border-slate-700">→</kbd> บนคีย์บอร์ดเพื่อเลื่อนสไลด์
      </div>
    </div>

    <!-- SPEAKER NOTES / SCRIPT DRAWER (บทพูด 8 นาที) -->
    <section class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 space-y-2">
      <div class="flex items-center justify-between border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-red-500"></span>
          <h3 class="text-xs font-black uppercase tracking-widest text-red-400">
            SPEAKER SCRIPT FOR THIS SLIDE (บทพูดสำหรับสไลด์นี้ ~45-50 วินาที)
          </h3>
        </div>
        <span class="text-[11px] font-mono text-slate-400" id="scriptTimeEstimate">0:00 - 0:45</span>
      </div>

      <!-- Thai Script -->
      <div id="scriptContentTh" class="text-sm text-slate-200 leading-relaxed font-normal bg-slate-950/60 p-3.5 rounded-xl border border-slate-800/80">
        {slides_data[0]['script_th']}
      </div>

      <!-- English Script -->
      <div id="scriptContentEn" class="text-sm text-slate-300 leading-relaxed font-normal bg-slate-950/60 p-3.5 rounded-xl border border-slate-800/80 hidden">
        {slides_data[0]['script_en']}
      </div>
    </section>

  </main>

  <!-- FOOTER -->
  <footer class="border-t border-slate-800 bg-slate-900/60 py-2.5 px-4 text-center text-xs text-slate-500">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-2 flex-wrap">
      <div>Fujitsu Thailand (FTH) — Microsoft Dynamics 365 & Copilot AI Modernization</div>
      <div class="font-mono text-[11px]">10-Slide C-Level Executive Presentation // 8-Minute Speech</div>
    </div>
  </footer>

  <!-- SCRIPT ENGINE -->
  <script>
    const slides = {slides_json};
    let currentSlide = 0;
    let isThaiScript = true;
    let isSpeaking = false;

    function showSlide(index) {{
      if (index < 0) index = 0;
      if (index >= slides.length) index = slides.length - 1;
      currentSlide = index;

      const s = slides[currentSlide];

      // Hide all slides, show current
      for (let i = 1; i <= slides.length; i++) {{
        const el = document.getElementById('slide-' + i);
        if (el) {{
          if (i === currentSlide + 1) {{
            el.classList.remove('hidden');
            el.classList.add('slide-enter');
          }} else {{
            el.classList.add('hidden');
            el.classList.remove('slide-enter');
          }}
        }}
      }}

      // Update counters & scripts
      const counterEl = document.getElementById('slideCounter');
      if (counterEl) counterEl.textContent = `Slide ${{s.num}} / ${{slides.length}}`;

      const timeEl = document.getElementById('scriptTimeEstimate');
      if (timeEl) timeEl.textContent = s.time;

      const thEl = document.getElementById('scriptContentTh');
      if (thEl) thEl.textContent = s.script_th;

      const enEl = document.getElementById('scriptContentEn');
      if (enEl) enEl.textContent = s.script_en;

      // Stop previous audio voice if speaking
      if (window.speechSynthesis && isSpeaking) {{
        window.speechSynthesis.cancel();
        isSpeaking = false;
        updateVoiceButtonState();
      }}

      renderDots();
    }}

    function renderDots() {{
      const container = document.getElementById('dotsContainer');
      if (!container) return;
      container.innerHTML = slides.map((s, i) => `
        <button onclick="showSlide(${{i}})" class="w-6 h-6 rounded-lg text-[10px] font-mono font-bold transition-all ${{i === currentSlide ? 'bg-red-600 text-white shadow-md shadow-red-900/40 ring-2 ring-red-400' : 'bg-slate-800 text-slate-400 hover:bg-slate-700'}}">
          ${{s.num}}
        </button>
      `).join('');
    }}

    function nextSlide() {{
      if (currentSlide < slides.length - 1) showSlide(currentSlide + 1);
    }}

    function prevSlide() {{
      if (currentSlide > 0) showSlide(currentSlide - 1);
    }}

    function toggleScriptLang() {{
      isThaiScript = !isThaiScript;
      const label = document.getElementById('langLabel');
      if (label) label.textContent = isThaiScript ? "ภาษาไทย" : "English";

      const thEl = document.getElementById('scriptContentTh');
      const enEl = document.getElementById('scriptContentEn');

      if (isThaiScript) {{
        if (thEl) thEl.classList.remove('hidden');
        if (enEl) enEl.classList.add('hidden');
      }} else {{
        if (thEl) thEl.classList.add('hidden');
        if (enEl) enEl.classList.remove('hidden');
      }}

      if (isSpeaking) {{
        window.speechSynthesis.cancel();
        isSpeaking = false;
        updateVoiceButtonState();
      }}
    }}

    // AI Voice Synthesis (Web Speech API)
    function toggleSpeech() {{
      if (!('speechSynthesis' in window)) {{
        alert("เบราว์เซอร์นี้ไม่รองรับ Web Speech API");
        return;
      }}
      if (isSpeaking) {{
        window.speechSynthesis.cancel();
        isSpeaking = false;
        updateVoiceButtonState();
        return;
      }}

      const s = slides[currentSlide];
      const text = isThaiScript ? s.script_th : s.script_en;
      const lang = isThaiScript ? 'th-TH' : 'en-US';

      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = lang;
      utterance.rate = isThaiScript ? 1.05 : 1.0;
      utterance.pitch = 1.0;

      utterance.onstart = () => {{
        isSpeaking = true;
        updateVoiceButtonState();
      }};
      utterance.onend = () => {{
        isSpeaking = false;
        updateVoiceButtonState();
      }};
      utterance.onerror = () => {{
        isSpeaking = false;
        updateVoiceButtonState();
      }};

      window.speechSynthesis.speak(utterance);
    }}

    function updateVoiceButtonState() {{
      const btn = document.getElementById('btnVoiceToggle');
      const icon = document.getElementById('voiceIcon');
      const label = document.getElementById('voiceLabel');
      if (!btn) return;
      if (isSpeaking) {{
        btn.classList.add('animate-pulse', 'ring-2', 'ring-red-400');
        if (icon) icon.textContent = '⏹️';
        if (label) label.textContent = 'หยุดเสียง';
      }} else {{
        btn.classList.remove('animate-pulse', 'ring-2', 'ring-red-400');
        if (icon) icon.textContent = '🎙️';
        if (label) label.textContent = 'ฟังเสียงบรรยาย';
      }}
    }}

    // Fullscreen Toggle
    function toggleFullscreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(err => console.log(err));
      }} else {{
        if (document.exitFullscreen) document.exitFullscreen();
      }}
    }}

    // Keyboard navigation
    window.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === ' ') {{
        nextSlide();
      }} else if (e.key === 'ArrowLeft') {{
        prevSlide();
      }} else if (e.key.toLowerCase() === 'f') {{
        toggleFullscreen();
      }}
    }});

    // Initialize dots on load
    renderDots();
  </script>
</body>
</html>"""
    return html_template

if __name__ == "__main__":
    html_content = generate_full_html()
    with open("Executive_D365_Copilot_Deck.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated Executive_D365_Copilot_Deck.html with {len(html_content)} bytes.")
