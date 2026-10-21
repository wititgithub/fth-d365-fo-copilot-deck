"""
generate_executive_deck_pptx_v2.py
Builds the refined 10-slide C-Level Executive Presentation Deck (.pptx):
- Focuses directly on the 5 Core Modules from the Research Table with vivid, visual explanations.
- Synthesizes Technology Stack (Tools).
- Outlines a 4-Phase, 8-12 Week Framework & Timeline WITHOUT pre-selecting a POC module.
- Highlights Dual-Perspective ROI (Value for Customer & Value for Fujitsu/Partner).
- Features the Fujitsu Red Infinity Motion Graphic GIF on Slide 10 with bilingual 8-minute speaker notes.
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
    C_EMERALD = RGBColor(16, 185, 129)
    C_AMBER = RGBColor(217, 119, 6)
    C_SLATE_BG = RGBColor(248, 250, 252)
    C_DARK_BG = RGBColor(15, 23, 42)
    C_TEXT_DARK = RGBColor(15, 23, 42)
    C_TEXT_MUTED = RGBColor(100, 116, 139)
    C_CARD_BORDER = RGBColor(226, 232, 240)

    slides_data = [
        # SLIDE 1: Executive Title & Vision
        {
            "num": 1,
            "title": "THE AUTONOMOUS ENTERPRISE",
            "subtitle": "Augmenting Microsoft Dynamics 365 with Copilot AI",
            "desc": "ยกระดับระบบ ERP จาก 'ระบบบันทึกธุรกรรมดั้งเดิม' (System of Record) สู่ 'ระบบอัจฉริยะที่คิด วิเคราะห์ และเตือนภัยล่วงหน้า' (System of Intelligence)",
            "script_th": "กราบเรียนท่านประธาน และคณะกรรมการบริหารทุกท่านครับ วันนี้ผมขออนุญาตนำเสนอทิศทางเชิงกลยุทธ์ในการยกระดับ Microsoft Dynamics 365 ด้วย Copilot AI... ตลอดหลายปีที่ผ่านมา ERP ทำหน้าที่เป็น 'System of Record' ที่บันทึกข้อมูลอย่างแม่นยำ แต่วันนี้ข้อมูลที่บันทึกไว้เฉยๆ ไม่เพียงพอที่จะสร้างความได้เปรียบทางธุรกิจ สิ่งที่เราต้องการคือ 'System of Intelligence' ที่สามารถคิด วิเคราะห์ ช่วยตัดสินใจ และทำงานเชิงรุกได้ครอบคลุมทุกโมดูลหลักขององค์กรครับ",
            "script_en": "Good morning, members of the Board and Executive Committee. Today, I present our strategic roadmap for augmenting Microsoft Dynamics 365 with Copilot AI. While D365 has long served as our reliable System of Record, recorded data alone is no longer enough to outpace market volatility. We must evolve into a System of Intelligence—an autonomous enterprise where AI reasons, predicts, and empowers human decision-making across all core business modules.",
            "is_title": True
        },
        # SLIDE 2: Module 1 - Finance & Thai Tax Localization
        {
            "num": 2,
            "title": "Module 1: Finance & Thai Tax Localization",
            "subtitle": "แก้ Pain Point งานบัญชีเจ้าหนี้ และภาษีไทยที่ Standard D365 ไม่ยืดหยุ่นพอ",
            "tag": "D365 FINANCE",
            "cards": [
                {
                    "title": "ภาพความเป็นจริง & Pain Point",
                    "detail": "• Standard 3-Way Match แข็งตัวเกินไป: ถ้าใบแจ้งหนี้มีค่าขนส่งรวมมา หรือเศษทศนิยมต่าง 5 สตางค์ ระบบจะสั่ง Hold ทันที ต้องใช้คนไปไล่สืบอีเมล\n• ความซับซ้อนของภาษีไทย: การตรวจใบหัก ณ ที่จ่าย ภ.ง.ด. 3, 53 และการกระทบยอด e-Tax Invoice ต้องใช้แรงงานคนตรวจทีละบรรทัด สิ้นเดือนทำงานหามรุ่งหามค่ำ"
                },
                {
                    "title": "Copilot AI เข้ามาช่วยอย่างไร",
                    "detail": "• เสมือน 'ผู้ช่วยนักบัญชีอาวุโส': อ่านเอกสาร PDF หลากหลายรูปแบบ ดึงข้อมูลอัตโนมัติ (Document Intelligence)\n• เมื่อพบราคาคลาดเคลื่อน Copilot จะตรวจสอบประวัติสัญญา และวิเคราะห์ว่าอยู่ในเกณฑ์ยอมรับได้หรือไม่ พร้อมร่าง Adjustment Voucher ให้กดอนุมัติในคลิกเดียว\n• จับคู่กระทบยอดภาษีหัก ณ ที่จ่ายกับระบบสรรพากรอัตโนมัติ"
                },
                {
                    "title": "ผลลัพธ์ที่จับต้องได้ (Impact)",
                    "detail": "⚡ ปิดงวดบัญชีเร็วขึ้น 70% (จาก 5 วัน เหลือไม่กี่ชั่วโมง)\n📉 ลดปัญหายอดค้างจ่ายในระบบ (Blocked Invoices) ได้กว่า 85%\n🛡️ ขจัดความเสี่ยงจากการถูกสรรพากรปรับเรื่องภาษีหัก ณ ที่จ่าย 100%"
                }
            ],
            "script_th": "ในโมดูลแรก คือการเงินและบัญชีครับ Pain Point จริงที่พบบ่อยมากคือ Standard 3-Way Match ใน D365 มีตรรกะที่แข็งตัวมากครับ หากใบแจ้งหนี้จากคู่ค้ามีค่าขนส่งเพิ่มมา หรือเศษสตางค์ไม่ตรงกับ PO ระบบจะสั่ง Hold การจ่ายเงินทันที ทำให้เกิดการค้างจ่ายและนักบัญชีต้องไปไล่สืบเอกสารทีละใบ ยิ่งไปกว่านั้น ภาษีหัก ณ ที่จ่าย ภ.ง.ด. 3, 53 และ e-Tax ของไทย ต้องใช้คนตรวจทีละบรรทัด... Copilot AI เข้ามาเป็นเสมือนผู้ช่วยนักบัญชีอาวุโส อ่าน PDF สแกน ตรวจสอบบริบทสัญญา หากอยู่ในเกณฑ์จะร่างใบปรับปรุงยอดให้อนุมัติในคลิกเดียว พร้อมกระทบยอดภาษีกับสรรพากรอัตโนมัติ ช่วยให้ปิดงบเร็วขึ้นถึง 70% ครับ",
            "script_en": "In our first module, Finance & Thai Tax, standard D365's 3-way matching logic is strictly deterministic. If an invoice diverges by even a few pennies or includes an off-PO delivery fee, processing halts instantly, creating manual bottlenecks. Compounding this, reconciling Thai withholding tax forms ภ.ง.ด. 3, 53 and e-Tax requires tedious line-by-line checks. Copilot AI functions like a seasoned senior accountant: it reads unstructured PDFs, understands contract tolerance, drafts one-click adjustment journals, and auto-reconciles statutory taxes, cutting closing time by 70%."
        },
        # SLIDE 3: Module 2 - Sourcing & Procurement Intelligence
        {
            "num": 3,
            "title": "Module 2: Sourcing & Procurement Intelligence",
            "subtitle": "เปลี่ยนจัดซื้อจากการตั้งรับ สู่การรู้ทันแนวโน้มราคาตลาดและป้องกันความเสี่ยงสัญญา",
            "tag": "D365 SCM — PROCUREMENT",
            "cards": [
                {
                    "title": "ภาพความเป็นจริง & Pain Point",
                    "detail": "• ซื้อตามราคากลางเดิม: Standard D365 อิงราคาจาก Trade Agreement เก่า ตาบอดต่อความผันผวนของราคาตลาดโลก (น้ำมัน, เหล็ก, ค่าระวางเรือ)\n• สัญญาคู่ค้าแฝงความเสี่ยง: เวลาเปิดประมูล (RFQ) ฝ่ายจัดซื้อไม่มีเวลาอ่านสัญญาละเอียดยิบ มักมองข้ามเงื่อนไขค่าปรับหรือการรับประกันที่เสียเปรียบ"
                },
                {
                    "title": "Copilot AI เข้ามาช่วยอย่างไร",
                    "detail": "• เสมือน 'ที่ปรึกษาจัดซื้อเชิงกลยุทธ์': เชื่อมโยงดัชนีราคาสินค้าโภคภัณฑ์โลก ผสานกับประวัติคุณภาพคู่ค้าใน D365\n• สแกนร่างสัญญาคู่ค้าอัตโนมัติ ทำการ Redline ไฮไลต์ข้อความที่เป็นความเสี่ยงทางกฎหมาย\n• สรุปจุดแข็ง-จุดอ่อนของแต่ละใบเสนอราคา และร่างบทเจรจาต่อรองให้ผู้จัดซื้อนำไปใช้คุยกับคู่ค้าได้ทันที"
                },
                {
                    "title": "ผลลัพธ์ที่จับต้องได้ (Impact)",
                    "detail": "💰 ประหยัดต้นทุนจัดซื้อ (Cost Avoidance) เฉลี่ย 10 - 15%\n⏱️ ลดเวลาการเปรียบเทียบ RFQ จาก 3 วัน เหลือ 30 นาที\n🔒 ป้องกันข้อพิพาททางสัญญาและค่าปรับแฝงได้ล่วงหน้า 100%"
                }
            ],
            "script_th": "โมดูลที่สอง ฝ่ายจัดซื้อครับ ปัจจุบัน D365 ทำงานโดยอิงจากราคากลางในอดีต แต่ราคาวัตถุดิบและค่าระวางเรือในตลาดโลกผันผวนตลอดเวลา ทำให้เราอาจซื้อของแพงกว่าราคาตลาดโดยไม่รู้ตัว นอกจากนี้ สัญญาคู่ค้าที่มีข้อความทางกฎหมายซับซ้อน ฝ่ายจัดซื้อมักไม่มีเวลาตรวจละเอียด... Copilot AI ทำหน้าที่เป็นที่ปรึกษาจัดซื้อเชิงกลยุทธ์ คอยมอนิเตอร์ราคาตลาดโลก เปรียบเทียบใบเสนอราคาหลายเจ้าพร้อมกัน และตรวจจับข้อสัญญาที่อาจทำให้เราเสียเปรียบ พร้อมแนะนำข้อเจรจาต่อรอง ช่วยให้เราประหยัดต้นทุนจัดซื้อได้ทันที 10 ถึง 15% ครับ",
            "script_en": "Moving to Procurement: standard D365 relies on static price catalogs and historical purchase agreements, blind to real-time global commodity swings. Furthermore, reviewing lengthy vendor contracts often leads to overlooked legal risks or unfavorable penalty terms. Copilot acts as a strategic procurement advisor: it cross-references global commodity price trends with internal vendor scorecards, automatically redlines high-risk clauses in contracts, and prepares negotiation scripts—yielding an estimated 10 to 15% in direct cost avoidance."
        },
        # SLIDE 4: Module 3 - Supply Chain Resiliency & Inventory
        {
            "num": 4,
            "title": "Module 3: Supply Chain Resiliency & Inventory",
            "subtitle": "เรดาร์ตรวจจับวิกฤตโลจิสติกส์ล่วงหน้า ป้องกันสินค้าขาดมือโดยไม่ต้องจมสต็อก",
            "tag": "D365 SCM — INVENTORY",
            "cards": [
                {
                    "title": "ภาพความเป็นจริง & Pain Point",
                    "detail": "• Standard MRP ทำงานแบบตาบอด: คำนวณจากตัวเลขใน ERP เท่านั้น ไม่รู้ว่าท่าเรือปลายทางหยุดงาน เรือติดพายุ หรือโรงงานต้นทางสะดุด\n• รู้ตัวเมื่อสายเกินแก้: กว่าจะรู้ว่าวัตถุดิบมาไม่ทัน ก็ตอนเลยกำหนดส่งแล้ว ผลคือสายการผลิตหยุด หรือต้องแบก Safety Stock มหาศาลจนจมกระแสเงินสด"
                },
                {
                    "title": "Copilot AI เข้ามาช่วยอย่างไร",
                    "detail": "• เสมือน 'เรดาร์ตรวจจับวิกฤตซัพพลายเชน 24/7': เชื่อมโยงข้อมูลสภาพอากาศ การจราจรทางเรือ และข่าวสารท่าเรือ เข้ากับใบสั่งซื้อใน D365\n• แจ้งเตือนความล่าช้าล่วงหน้า 10-14 วัน ก่อนเกิดปัญหาจริง\n• จำลองทางเลือกแก้ไขปัญหา (Scenario Simulation) เช่น แนะนำคลังสำรองที่สามารถสลับของ หรือแนะนำซัพพลายเออร์ใกล้เคียงที่ส่งทดแทนได้"
                },
                {
                    "title": "ผลลัพธ์ที่จับต้องได้ (Impact)",
                    "detail": "📦 ลดปริมาณสต็อกสำรอง (Safety Stock) ลง 20 - 25% โดยไม่กระทบยอดขาย\n🚨 ลดความเสี่ยงสายการผลิตหยุดชะงัก (Downtime) จากของขาดได้ 80%\n💵 ปลดล็อกเงินทุนหมุนเวียน (Working Capital) คืนสู่กระแสเงินสดองค์กร"
                }
            ],
            "script_th": "ในโมดูลที่สาม ซัพพลายเชนและคลังสินค้าครับ ปัญหาคลาสสิกของ Standard MRP คือมันมองไม่เห็นโลกภายนอก มันไม่รู้ว่ามีมรสุมเข้า หรือท่าเรือแหลมฉบังกำลังติดขัด กว่าที่ระบบจะรู้ว่าของไม่มาส่ง ก็คือเลยวันนัดไปแล้ว ทำให้โรงงานผลิตต่อไม่ได้ หรือเราต้องแก้ปัญหาด้วยการสต็อกของไว้เยอะๆ จนเงินจม... Copilot AI เข้ามาเป็นเรดาร์ตรวจจับวิกฤต แจ้งเตือนล่วงหน้า 10 ถึง 14 วัน พร้อมจำลองแผนแก้ไขให้ทันที เช่น สลับของจากคลังอื่น ช่วยให้เราลดเงินจมใน Safety Stock ได้ถึง 20-25% ครับ",
            "script_en": "In Supply Chain and Inventory, standard MRP plans blindly using only internal database timestamps. It has zero awareness of external port congestion, strikes, or typhoons. Delays are discovered only after missing customer dock dates, forcing companies to carry bloated safety stock. Copilot acts as a 24/7 disruption radar: ingesting external maritime telematics and weather feeds, anticipating shortages 10 to 14 days ahead, and simulating rerouting options. This allows us to cut safety inventory holding by 20 to 25%."
        },
        # SLIDE 5: Module 4 - Smart Manufacturing & Operations
        {
            "num": 5,
            "title": "Module 4: Smart Manufacturing & Operations",
            "subtitle": "วิเคราะห์หาสาเหตุของเสีย (Scrap) ในไม่กี่นาที และจัดตารางผลิตแบบยืดหยุ่น",
            "tag": "D365 SCM — MANUFACTURING",
            "cards": [
                {
                    "title": "ภาพความเป็นจริง & Pain Point",
                    "detail": "• สืบหาสาเหตุของเสียล่าช้า: เมื่อชิ้นงานตกเกณฑ์ (Scrap Spike) ข้อมูลกระจัดกระจายอยู่ในเครื่องจักร IoT, สภาพแวดล้อม และล็อตวัตถุดิบ\n• วิศวกรต้องใช้เวลาครึ่งวันเปิดดูหลายระบบเพื่อหาสาเหตุ ทำให้เสียเวลาและผลิตของเสียเพิ่มขึ้นเรื่อยๆ"
                },
                {
                    "title": "Copilot AI เข้ามาช่วยอย่างไร",
                    "detail": "• เสมือน 'หัวหน้าวิศวกรโรงงานอัจฉริยะ': นำข้อมูลเซนเซอร์ IoT, อุณหภูมิโรงงาน และประวัติล็อตวัตถุดิบ (Lot Genealogy) มาวิเคราะห์ร่วมกัน\n• สรุปรายงานหาสาเหตุต้นตอ (Root Cause Analysis) ให้วิศวกรได้ภายในไม่กี่นาที\n• ปรับเปลี่ยนคิวงานผลิต (Dynamic Dispatching) ไปยังเครื่องสำรองใน D365 โดยอัตโนมัติ"
                },
                {
                    "title": "ผลลัพธ์ที่จับต้องได้ (Impact)",
                    "detail": "⏱️ ลดเวลาการวินิจฉัยปัญหาของเสียจาก 4 ชั่วโมง เหลือไม่เกิน 15 นาที\n📉 ลดอัตราของเสีย (Scrap Rate) ในสายการผลิตลง 18 - 25%\n⚙️ ยกระดับ Overall Equipment Effectiveness (OEE) ของเครื่องจักรหลัก"
                }
            ],
            "script_th": "โมดูลที่สี่ ฝ่ายผลิตและควบคุมคุณภาพครับ เมื่อเกิดของเสียในสายการผลิต หรือเครื่องจักรเริ่มมีอาการสะดุด ปัญหาคือข้อมูลอยู่กระจัดกระจายมากครับ ทั้งเซนเซอร์ความร้อน สภาพอากาศ และล็อตวัตถุดิบ วิศวกรต้องเสียเวลาหลายชั่วโมงในการสืบหาต้นตอ... Copilot AI จะเชื่อมโยงข้อมูล IoT และประวัติใน D365 เข้าด้วยกัน สรุป Root Cause ให้วิศวกรได้ในเวลาไม่กี่นาที พร้อมปรับลำดับงานผลิตไปยังเครื่องจักรสำรองได้ทันที ช่วยลดอัตราของเสียลงได้ถึง 18-25% ครับ",
            "script_en": "On the Manufacturing shop floor, diagnosing quality drift and equipment failures requires cross-referencing disparate IoT logs, factory ambient humidity, and batch genealogy. Engineers often spend half a day investigating the cause while defective parts accumulate. Copilot correlates real-time IoT telemetry with D365 batch records, generating root-cause diagnostics within minutes and dynamically adjusting production schedules to alternative work centers, reducing scrap rates by 18 to 25%."
        },
        # SLIDE 6: Module 5 - Project Operations & Services
        {
            "num": 6,
            "title": "Module 5: Project Operations & Professional Services",
            "subtitle": "เตือนภัยกำไรรั่วไหล (Margin Bleed) และแปลงข้อสรุปประชุมเป็น Change Order",
            "tag": "D365 PROJECT OPERATIONS",
            "cards": [
                {
                    "title": "ภาพความเป็นจริง & Pain Point",
                    "detail": "• กำไรรั่วไหลแบบเงียบๆ (Silent Margin Bleed): ลูกค้าขอแก้งานหรือเพิ่มงานเล็กๆ ในที่ประชุม (Scope Creep) แต่ทีมหน้างานไม่ได้บันทึกหรือออกบิล\n• รู้ตัวว่าขาดทุนเมื่อจบโปรเจกต์: เสียเวลาในการสรุปเอกสารเพื่อขออนุมัติงานเพิ่ม ทำให้ไม่ได้เรียกเก็บเงินตามจริง"
                },
                {
                    "title": "Copilot AI เข้ามาช่วยอย่างไร",
                    "detail": "• เสมือน 'ผู้ช่วยผู้จัดการโครงการ': มอนิเตอร์อัตราการใช้ชั่วโมงงานและงบประมาณเทียบกับ Milestone แบบ Real-time\n• เตือนภัยล่วงหน้า 3-4 สัปดาห์ ก่อนที่งบประมาณจะบานปลายเกินกำไรที่ตั้งไว้\n• ถอดบันทึกการประชุม แปลงเป็นร่างเอกสาร Change Order พร้อมคำนวณมูลค่างานเพิ่มให้อัตโนมัติ เพื่อส่งให้ลูกค้าอนุมัติก่อนเริ่มทำ"
                },
                {
                    "title": "ผลลัพธ์ที่จับต้องได้ (Impact)",
                    "detail": "📈 ปกป้องอัตรากำไรโครงการ (Project Profit Margin) เพิ่มขึ้น 12 - 18%\n📝 เก็บเงินค่างานเพิ่ม (Unbilled Scope Creep) ได้ครบถ้วน 100%\n⚡ ลดเวลาจัดทำเอกสาร Change Order และ SOW ลง 80%"
                }
            ],
            "script_th": "โมดูลที่ห้า งานบริหารโครงการและบริการครับ ปัญหาคลาสสิกที่ทำให้โครงการขาดทุนคือ 'Margin Bleed' หรือกำไรที่รั่วไหลจากงานงอกในที่ประชุม ลูกค้าขอให้ช่วยทำเพิ่มนิดหน่อย ทีมงานก็ทำให้โดยไม่ได้ออกเอกสารขอแก้งาน กว่าผู้บริหารจะรู้ว่าขาดทุนก็คือตอนปิดโครงการแล้ว... Copilot AI ทำหน้าที่เป็นเรดาร์ตรวจจับอัตราการใช้งบ เตือนล่วงหน้า 4 สัปดาห์ก่อนกำไรติดลบ และสามารถถอดเทปการประชุม แปลงเป็นร่าง Change Order พร้อมคิดราคาค่างานเพิ่มให้ลูกค้าเซ็นอนุมัติได้ทันทีครับ",
            "script_en": "In Project Operations and Professional Services, unbilled scope creep is the primary driver of silent margin erosion. Client requests made during meetings are executed by engineers without formal change orders, only discovering project losses at final review. Copilot monitors labor burn rates against project milestones, alerting management 4 weeks before margin bleed occurs, and translates meeting transcripts into billable Change Orders ready for client sign-off, protecting project profitability by 12 to 18%."
        },
        # SLIDE 7: Technology Stack & Security Architecture (สรุปเครื่องมือ)
        {
            "num": 7,
            "title": "Enterprise Technology Stack & Architecture",
            "subtitle": "สรุปเครื่องมือหลักที่ใช้ขับเคลื่อนระบบ ภายใต้ความปลอดภัยระดับ Enterprise",
            "tag": "TOOLS & ARCHITECTURE",
            "cards": [
                {
                    "title": "1. Cognitive & AI Engine",
                    "detail": "• Microsoft Copilot Studio: เครื่องมือสร้างและปรับแต่ง AI Agents ให้เข้าใจขั้นตอนเฉพาะขององค์กร\n• Dynamics 365 Copilot: ฟังก์ชัน AI พื้นฐานที่ฝังมาในแต่ละโมดูลของ D365\n• Azure OpenAI Service: โมเดล GPT-4o รันบน Private Tenant ไม่แชร์ข้อมูลกับภายนอก"
                },
                {
                    "title": "2. Data Integration Layer",
                    "detail": "• Microsoft Dataverse: ฐานข้อมูลกลางที่เก็บ Transaction และโครงสร้างของ D365\n• Azure Document Intelligence: แปลงเอกสารสแกน PDF ใบกำกับภาษี และสัญญา เป็นข้อมูลเชิงโครงสร้าง\n• Power Platform: เชื่อมต่อ API ภายนอก (กรมสรรพากร, อัตราแลกเปลี่ยน, ข้อมูลท่าเรือ)"
                },
                {
                    "title": "3. Security & Governance",
                    "detail": "• Isolated Tenant: ข้อมูลองค์กรถูกจำกัดอยู่ภายใน Tenant เรา 100% ไม่ถูกนำไปเทรนโมเดลสาธารณะ\n• AES-256 Encryption: เข้ารหัสข้อมูลทั้งในขณะพักและขณะรับส่ง\n• Human-in-the-Loop: AI มีหน้าที่วิเคราะห์และร่างข้อเสนอ แต่ผู้มีอำนาจตัดสินใจอนุมัติขั้นสุดท้ายคือผู้บริหาร"
                }
            ],
            "script_th": "สำหรับเครื่องมือและเทคโนโลยีที่ใช้ครับ เราใช้เทคโนโลยีมาตรฐานระดับ Enterprise ของ Microsoft ที่ทำงานร่วมกันอย่างไร้รอยต่อ: 1. ด้าน AI เราใช้ Copilot Studio และ Azure OpenAI Service รันโมเดลบน Private Tenant ของเราเอง 2. ด้านข้อมูล เราใช้ Dataverse และ Azure Document Intelligence ในการสกัดเอกสาร PDF และสัญญา 3. ที่สำคัญที่สุดคือความปลอดภัย ข้อมูลองค์กร 100% จะไม่มีวันรั่วไหลไปเทรน AI สาธารณะ และใช้หลักการ Human-in-the-Loop โดยผู้บริหารและพนักงานของเรายังคงมีอำนาจตัดสินใจอนุมัติขั้นสุดท้ายเสมอครับ",
            "script_en": "Regarding the technology stack, we leverage Microsoft's enterprise-grade architecture: 1. The AI engine combines Copilot Studio, embedded D365 Copilot, and Azure OpenAI Service operating within a private tenant. 2. Data integration is managed via Dataverse and Azure Document Intelligence for robust unstructured document extraction. 3. Most importantly, enterprise security is paramount: zero data leakage, AES-256 encryption, and a strict Human-in-the-Loop governance model where AI proposes, but humans always retain ultimate approval authority."
        },
        # SLIDE 8: Framework & Implementation Timeline (สรุปขั้นตอน & ระยะเวลา)
        {
            "num": 8,
            "title": "Implementation Framework & Timeline",
            "subtitle": "ขั้นตอนการดำเนินงานมาตรฐาน 4 เฟส ในกรอบเวลา 8 - 12 สัปดาห์ (เปิดกว้าง ยังไม่ผูกมัดเลือกข้อใด)",
            "tag": "FRAMEWORK & TIMELINE",
            "cards": [
                {
                    "title": "Phase 1: Readiness & Discovery\n(สัปดาห์ที่ 1 - 2)",
                    "detail": "• สำรวจกระบวนการทำงานและคุณภาพข้อมูลในแต่ละโมดูล\n• ประเมินความพร้อมด้านความปลอดภัยและสิทธิ์การเข้าถึง\n• นำเสนอผลการประเมินเพื่อให้ผู้บริหารพิจารณาคัดเลือกโมดูลที่เหมาะสมที่สุดสำหรับเริ่มต้น"
                },
                {
                    "title": "Phase 2: Foundation & Setup\n(สัปดาห์ที่ 3 - 4)",
                    "detail": "• ติดตั้งสภาพแวดล้อม Copilot Studio และ Azure OpenAI บน Private Tenant\n• กำหนดนโยบายความปลอดภัยและ Data Governance\n• เชื่อมต่อ Dataverse และระบบเอกสารที่เกี่ยวข้อง"
                },
                {
                    "title": "Phase 3: Pilot & Iteration\n(สัปดาห์ที่ 5 - 8)",
                    "detail": "• เริ่มต้นทดลองใช้งานในขอบเขตที่คัดเลือก\n• ปรับจูน Prompt และ Knowledge Base ตามบริบทธุรกิจจริง\n• ทดสอบความแม่นยำร่วมกับ Key Users ในสภาพแวดล้อมควบคุม"
                },
                {
                    "title": "Phase 4: Scale & Evaluation\n(สัปดาห์ที่ 9 - 12)",
                    "detail": "• อบรมผู้ใช้งาน (Upskilling) และจัดการการเปลี่ยนแปลง (Change Management)\n• วัดผลสัมฤทธิ์ทางธุรกิจและ ROI จริงเทียบกับเป้าหมาย\n• วางแผนขยายผล (Rollout) สู่โมดูลอื่นๆ ตามลำดับความสำคัญ"
                }
            ],
            "script_th": "ในด้านขั้นตอนและระยะเวลา เราวางกรอบการทำงานมาตรฐานไว้ 4 เฟส รวมระยะเวลาประมาณ 8 ถึง 12 สัปดาห์ โดยในจุดนี้ เรายังไม่ได้เจาะจงว่าจะเลือกโมดูลไหนมาทำก่อนครับ แต่เราจะเริ่มที่ Phase 1 คือการทำ Discovery ร่วมกันเพื่อประเมินความพร้อมของข้อมูลในแต่ละโมดูล แล้วให้ผู้บริหารเป็นผู้เลือกจุดที่สร้าง Impact สูงสุด จากนั้นใน Phase 2 จะเป็นการวางระบบความปลอดภัย Phase 3 คือการทดลองใช้และปรับจูนความแม่นยำ และ Phase 4 คือการขยายผลพร้อมวัดผลตอบแทน ROI จริง เพื่อให้การลงทุนมีความเสี่ยงต่ำและคุ้มค่าที่สุดครับ",
            "script_en": "Our implementation approach follows a proven 4-phase enterprise framework spanning 8 to 12 weeks. Importantly, we do not pre-select a specific POC module today. Instead, Phase 1 conducts a thorough readiness assessment across all modules, empowering leadership to prioritize the highest-impact opportunity. Phase 2 establishes our secure foundation. Phase 3 executes the pilot and prompt tuning with key users, and Phase 4 scales adoption while measuring tangible business ROI. This ensures a controlled, agile, and low-risk journey."
        },
        # SLIDE 9: Dual-Perspective ROI
        {
            "num": 9,
            "title": "Dual-Perspective ROI: Value for Customer & Value for Our Organization",
            "subtitle": "ความคุ้มค่าที่ชัดเจนทั้งในมุมมองของลูกค้าผู้ใช้งาน และในมุมมองขององค์กรเรา (Fujitsu)",
            "tag": "DUAL ROI ANALYSIS",
            "cards": [
                {
                    "title": "🎯 ความคุ้มค่าสำหรับลูกค้า (Client Enterprise ROI)",
                    "detail": "• ปิดบัญชีเร็วขึ้น 70%: ปลดล็อกเวลาของทีมนักบัญชีสู่การวางแผนการเงิน\n• ประหยัดต้นทุนจัดซื้อ 10-15%: จากการรู้ทันแนวโน้มราคาตลาดและการเจรจาต่อรอง\n• ลดเงินจมใน Safety Stock 20-25%: กระแสเงินสดหมุนเวียนเพิ่มขึ้นทันที\n• ลดความเสี่ยงทางภาษีและสัญญา 100%: ป้องกันเบี้ยปรับและข้อพิพาททางกฎหมาย\n• ยกระดับพนักงาน: ลดงานคีย์ข้อมูลซ้ำซาก เพิ่มความพึงพอใจในการทำงานของบุคลากร"
                },
                {
                    "title": "🏆 ความคุ้มค่าสำหรับองค์กรของเรา (Fujitsu Partner ROI)",
                    "detail": "• ก้าวสู่ Strategic AI Transformation Partner: ขยับจากผู้ติดตั้ง ERP ดั้งเดิม สู่ที่ปรึกษา AI ระดับสูงที่มี Margin มากขึ้น\n• ส่งมอบโครงการเร็วขึ้น 30-40%: ใช้ AI ช่วยทดสอบและ Migrate ข้อมูล ลดภาระ Man-days ของทีมงานเรา\n• สร้างกระแสรายได้ใหม่ต่อเนื่อง (Recurring Revenue): จากบริการ AI Advisory, Knowledge Tuning, และ AI Managed Services\n• เพิ่มขีดความสามารถในการแข่งขัน (Win Rate สูงขึ้น): ข้อเสนอโครงการของเราโดดเด่นและเหนือกว่าคู่แข่งในตลาดอย่างชัดเจน"
                }
            ],
            "script_th": "สไลด์นี้คือหัวใจสำคัญครับ คือผลตอบแทนที่คุ้มค่าทั้ง 2 ด้าน: ฝั่งลูกค้า ได้ประโยชน์โดยตรงทั้งการปิดบัญชีเร็วขึ้น 70%, ประหยัดต้นทุนจัดซื้อ 10-15%, ลดเงินจมในสต็อก 20-25% และลดความเสี่ยงข้อผิดพลาด... ขณะเดียวกัน ฝั่งองค์กรของเรา (Fujitsu) เรายกระดับจากการเป็นเพียงผู้ติดตั้งระบบ ERP ธรรมดา สู่การเป็น 'Strategic AI Transformation Partner' ซึ่งมีกำไรต่อโครงการสูงขึ้น ส่งมอบงานได้เร็วขึ้น ลด Man-days ของทีมงานเรา และเปิดช่องทางรายได้ใหม่จากการดูแลระบบ AI อย่างต่อเนื่อง เป็นผลประโยชน์ร่วมกันแบบ Win-Win อย่างแท้จริงครับ",
            "script_en": "Slide 9 presents our business justification from a dual-perspective ROI. For the customer, the value is immediate: 70% faster financial close, 10 to 15% procurement cost avoidance, 20 to 25% lower inventory carrying costs, and total compliance safeguard. Simultaneously, for Fujitsu as their trusted partner, this elevates us from a traditional ERP system integrator into a high-margin Strategic AI Transformation Partner, reducing delivery man-days by up to 40%, increasing our win-rate in competitive tenders, and generating sustainable recurring AI advisory revenue."
        },
        # SLIDE 10: Executive Finale with Motion Graphic
        {
            "num": 10,
            "title": "THE EXECUTIVE FINALE: PARTNERSHIP SYNERGY",
            "subtitle": "Fujitsu Red Infinity × Dynamics 365 & Copilot AI",
            "tag": "EXECUTIVE FINALE",
            "is_finale": True,
            "cards": [
                {"title": "1. Infinite Transformation", "detail": "สัญลักษณ์ Fujitsu Red Infinity สะท้อนความมุ่งมั่นที่ไม่สิ้นสุดในการส่งมอบคุณค่าและขับเคลื่อนธุรกิจสู่อนาคต"},
                {"title": "2. Seamless Augmentation", "detail": "ผสานความมั่นคงของระบบ D365 เข้ากับพลังปัญญาประดิษฐ์ Copilot AI ได้อย่างสมบูรณ์แบบโดยไม่ต้องรื้อระบบเดิม"},
                {"title": "3. Readiness for Action", "detail": "พร้อมเริ่มต้นขั้นตอนประเมินความพร้อมและนำเสนอผลลัพธ์ที่เป็นรูปธรรมต่อผู้บริหารในทุกโมดูล"}
            ],
            "script_th": "ทุกท่านครับ บนหน้าจอสุดท้ายนี้ คือภาพเคลื่อนไหวของสัญลักษณ์ 'Fujitsu Red Infinity' ที่สะท้อนถึงคำมั่นสัญญาที่ไม่สิ้นสุดในการขับเคลื่อนนวัตกรรมสู่ความยั่งยืน... เมื่อเราผสานรากฐานที่แข็งแกร่งของ Dynamics 365 เข้ากับพลังการเรียนรู้และคาดการณ์ของ Copilot AI เราไม่ได้เพียงแค่อัปเกรดระบบ ERP แต่เรากำลังสร้างองค์กรที่พร้อมรับมือกับทุกความท้าทาย ดำเนินการได้อย่างชาญฉลาด และก้าวขึ้นเป็นผู้นำในอุตสาหกรรมอย่างแท้จริง ขอขอบคุณท่านคณะกรรมการบริหารทุกท่าน และยินดีตอบทุกข้อซักถามครับ",
            "script_en": "Distinguished board members, our final slide presents the animated Fujitsu Red Infinity loop—representing our infinite commitment to sustainable transformation and customer success. By unifying the structured operational rigor of Dynamics 365 with the predictive intelligence of Copilot AI, we empower both our clients and ourselves to achieve unprecedented agility and market leadership. Thank you very much for your time, and I welcome your strategic questions and guidance."
        }
    ]

    for s_idx, s in enumerate(slides_data):
        slide = prs.slides.add_slide(blank_layout)

        # Background
        bg_shape = slide.shapes.add_shape(1, 0, 0, prs.slide_width, prs.slide_height)
        bg_shape.line.fill.background()

        if s.get("is_title"):
            bg_shape.fill.solid()
            bg_shape.fill.fore_color.rgb = C_NAVY

            # Red accent stripe
            stripe = slide.shapes.add_shape(1, Inches(0.8), Inches(1.8), Inches(0.12), Inches(3.8))
            stripe.fill.solid()
            stripe.fill.fore_color.rgb = C_RED
            stripe.line.fill.background()

            # Text box
            tb = slide.shapes.add_textbox(Inches(1.2), Inches(1.6), Inches(11.0), Inches(4.5))
            tf = tb.text_frame
            tf.word_wrap = True

            p0 = tf.paragraphs[0]
            p0.text = "FUJITSU THAILAND (FTH) — EXECUTIVE STRATEGIC BRIEFING"
            p0.font.bold = True
            p0.font.size = Pt(13)
            p0.font.color.rgb = C_RED

            p1 = tf.add_paragraph()
            p1.text = s["title"]
            p1.font.bold = True
            p1.font.size = Pt(38)
            p1.font.color.rgb = C_WHITE
            p1.space_before = Pt(12)

            p2 = tf.add_paragraph()
            p2.text = s["subtitle"]
            p2.font.bold = True
            p2.font.size = Pt(22)
            p2.font.color.rgb = RGBColor(56, 189, 248) # Sky blue
            p2.space_before = Pt(10)

            p3 = tf.add_paragraph()
            p3.text = s["desc"]
            p3.font.size = Pt(14)
            p3.font.color.rgb = RGBColor(203, 213, 225)
            p3.space_before = Pt(18)

            # Metadata Footer
            p4 = tf.add_paragraph()
            p4.text = "10-Slide Executive Overview | Presentation Time: ~8 Minutes (Bilingual TH/EN)"
            p4.font.size = Pt(11)
            p4.font.color.rgb = RGBColor(148, 163, 184)
            p4.space_before = Pt(28)

        elif s.get("is_finale"):
            # Finale Slide with Motion Graphic GIF
            bg_shape.fill.solid()
            bg_shape.fill.fore_color.rgb = C_NAVY

            # Header
            tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
            tf = tb.text_frame
            tf.word_wrap = True
            p0 = tf.paragraphs[0]
            p0.text = f"SLIDE {s['num']} // {s['tag']}"
            p0.font.bold = True
            p0.font.size = Pt(11)
            p0.font.color.rgb = C_RED

            p1 = tf.add_paragraph()
            p1.text = s["title"]
            p1.font.bold = True
            p1.font.size = Pt(24)
            p1.font.color.rgb = C_WHITE

            # Left side: Animated GIF of Motion Graphic
            gif_path = "assets/slide10_fujitsu_red_infinity_motion.gif"
            if os.path.exists(gif_path):
                slide.shapes.add_picture(gif_path, Inches(0.8), Inches(1.6), width=Inches(6.8), height=Inches(5.0))

            # Right side: 3 Executive Takeaway Cards
            card_top = Inches(1.6)
            card_h = Inches(1.5)
            card_gap = Inches(0.2)
            card_w = Inches(4.7)
            card_left = Inches(7.8)

            for c_i, c in enumerate(s["cards"]):
                top_pos = card_top + (c_i * (card_h + card_gap))
                card_bg = slide.shapes.add_shape(1, card_left, top_pos, card_w, card_h)
                card_bg.fill.solid()
                card_bg.fill.fore_color.rgb = RGBColor(30, 41, 59)
                card_bg.line.color.rgb = RGBColor(51, 65, 85)

                tb_c = slide.shapes.add_textbox(card_left + Inches(0.15), top_pos + Inches(0.1), card_w - Inches(0.3), card_h - Inches(0.2))
                tf_c = tb_c.text_frame
                tf_c.word_wrap = True

                p_t = tf_c.paragraphs[0]
                p_t.text = c["title"]
                p_t.font.bold = True
                p_t.font.size = Pt(13)
                p_t.font.color.rgb = C_RED if c_i == 0 else RGBColor(56, 189, 248)

                p_d = tf_c.add_paragraph()
                p_d.text = c["detail"]
                p_d.font.size = Pt(11)
                p_d.font.color.rgb = RGBColor(226, 232, 240)
                p_d.space_before = Pt(4)

        elif s.get("num") == 9:
            # Dual ROI Slide (Side-by-side 2 large cards)
            bg_shape.fill.solid()
            bg_shape.fill.fore_color.rgb = C_SLATE_BG

            # Header
            tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.2))
            tf = tb.text_frame
            tf.word_wrap = True
            p0 = tf.paragraphs[0]
            p0.text = f"SLIDE {s['num']} // {s['tag']}"
            p0.font.bold = True
            p0.font.size = Pt(11)
            p0.font.color.rgb = C_RED

            p1 = tf.add_paragraph()
            p1.text = s["title"]
            p1.font.bold = True
            p1.font.size = Pt(22)
            p1.font.color.rgb = C_NAVY

            p2 = tf.add_paragraph()
            p2.text = s["subtitle"]
            p2.font.size = Pt(12)
            p2.font.color.rgb = C_TEXT_MUTED

            # 2 Columns for Dual ROI
            card_w = Inches(5.7)
            card_h = Inches(5.0)
            card_y = Inches(1.8)

            for c_i, c in enumerate(s["cards"]):
                card_x = Inches(0.8) + (c_i * Inches(6.0))
                card_bg = slide.shapes.add_shape(1, card_x, card_y, card_w, card_h)
                card_bg.fill.solid()
                card_bg.fill.fore_color.rgb = C_WHITE
                card_bg.line.color.rgb = RGBColor(0, 120, 212) if c_i == 0 else C_RED
                card_bg.line.width = Pt(1.5)

                tb_c = slide.shapes.add_textbox(card_x + Inches(0.25), card_y + Inches(0.2), card_w - Inches(0.5), card_h - Inches(0.4))
                tf_c = tb_c.text_frame
                tf_c.word_wrap = True

                p_t = tf_c.paragraphs[0]
                p_t.text = c["title"]
                p_t.font.bold = True
                p_t.font.size = Pt(14)
                p_t.font.color.rgb = RGBColor(0, 120, 212) if c_i == 0 else C_RED

                p_d = tf_c.add_paragraph()
                p_d.text = c["detail"]
                p_d.font.size = Pt(11.5)
                p_d.font.color.rgb = C_TEXT_DARK
                p_d.space_before = Pt(10)

        elif s.get("num") == 8:
            # 4 Phases Framework & Timeline (4 Columns)
            bg_shape.fill.solid()
            bg_shape.fill.fore_color.rgb = C_SLATE_BG

            # Header
            tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.2))
            tf = tb.text_frame
            tf.word_wrap = True
            p0 = tf.paragraphs[0]
            p0.text = f"SLIDE {s['num']} // {s['tag']}"
            p0.font.bold = True
            p0.font.size = Pt(11)
            p0.font.color.rgb = C_RED

            p1 = tf.add_paragraph()
            p1.text = s["title"]
            p1.font.bold = True
            p1.font.size = Pt(22)
            p1.font.color.rgb = C_NAVY

            p2 = tf.add_paragraph()
            p2.text = s["subtitle"]
            p2.font.size = Pt(12)
            p2.font.color.rgb = C_TEXT_MUTED

            # 4 Columns for 4 Phases
            col_w = Inches(2.75)
            col_h = Inches(5.0)
            col_gap = Inches(0.2)
            col_y = Inches(1.8)

            for c_i, c in enumerate(s["cards"]):
                col_x = Inches(0.8) + (c_i * (col_w + col_gap))
                card_bg = slide.shapes.add_shape(1, col_x, col_y, col_w, col_h)
                card_bg.fill.solid()
                card_bg.fill.fore_color.rgb = C_WHITE
                card_bg.line.color.rgb = C_CARD_BORDER

                tb_c = slide.shapes.add_textbox(col_x + Inches(0.15), col_y + Inches(0.15), col_w - Inches(0.3), col_h - Inches(0.3))
                tf_c = tb_c.text_frame
                tf_c.word_wrap = True

                p_t = tf_c.paragraphs[0]
                p_t.text = c["title"]
                p_t.font.bold = True
                p_t.font.size = Pt(12)
                p_t.font.color.rgb = C_RED if c_i == 0 else RGBColor(0, 120, 212)

                p_d = tf_c.add_paragraph()
                p_d.text = c["detail"]
                p_d.font.size = Pt(10.5)
                p_d.font.color.rgb = C_TEXT_DARK
                p_d.space_before = Pt(8)

        else:
            # Standard 3-Card Layout for Modules & Tools (Slides 2, 3, 4, 5, 6, 7)
            bg_shape.fill.solid()
            bg_shape.fill.fore_color.rgb = C_SLATE_BG

            # Header
            tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.2))
            tf = tb.text_frame
            tf.word_wrap = True
            p0 = tf.paragraphs[0]
            p0.text = f"SLIDE {s['num']} // {s.get('tag', 'OVERVIEW')}"
            p0.font.bold = True
            p0.font.size = Pt(11)
            p0.font.color.rgb = C_RED

            p1 = tf.add_paragraph()
            p1.text = s["title"]
            p1.font.bold = True
            p1.font.size = Pt(22)
            p1.font.color.rgb = C_NAVY

            p2 = tf.add_paragraph()
            p2.text = s["subtitle"]
            p2.font.size = Pt(12)
            p2.font.color.rgb = C_TEXT_MUTED

            # 3 Columns
            col_w = Inches(3.7)
            col_h = Inches(5.0)
            col_gap = Inches(0.3)
            col_y = Inches(1.8)

            for c_i, c in enumerate(s["cards"]):
                col_x = Inches(0.8) + (c_i * (col_w + col_gap))
                card_bg = slide.shapes.add_shape(1, col_x, col_y, col_w, col_h)
                card_bg.fill.solid()
                card_bg.fill.fore_color.rgb = C_WHITE
                card_bg.line.color.rgb = C_CARD_BORDER

                tb_c = slide.shapes.add_textbox(col_x + Inches(0.2), col_y + Inches(0.2), col_w - Inches(0.4), col_h - Inches(0.4))
                tf_c = tb_c.text_frame
                tf_c.word_wrap = True

                p_t = tf_c.paragraphs[0]
                p_t.text = c["title"]
                p_t.font.bold = True
                p_t.font.size = Pt(13)
                p_t.font.color.rgb = C_RED if c_i == 0 else (RGBColor(0, 120, 212) if c_i == 1 else RGBColor(16, 185, 129))

                p_d = tf_c.add_paragraph()
                p_d.text = c["detail"]
                p_d.font.size = Pt(11)
                p_d.font.color.rgb = C_TEXT_DARK
                p_d.space_before = Pt(8)

        # Speaker Notes (Bilingual TH / EN)
        notes_slide = slide.notes_slide
        tf_n = notes_slide.notes_text_frame
        tf_n.text = f"--- [SLIDE {s['num']}: THAI SCRIPT (~45s)] ---\n{s['script_th']}\n\n--- [SLIDE {s['num']}: ENGLISH SCRIPT (~45s)] ---\n{s['script_en']}"

    output_pptx = "FTH_D365_Copilot_AI_Executive_Presentation.pptx"
    prs.save(output_pptx)
    print(f"Successfully generated {output_pptx} with {len(slides_data)} slides.")

if __name__ == "__main__":
    create_deck()
