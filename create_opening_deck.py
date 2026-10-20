import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Color Palette matching the interactive pitch deck
    BG_COLOR = RGBColor(11, 17, 32)         # Deep Slate 950 / Navy
    CARD_BG = RGBColor(20, 29, 47)          # Slate 900
    CARD_BORDER = RGBColor(38, 52, 85)      # Slate 700 / Border
    ACCENT_RED = RGBColor(230, 0, 18)       # Fujitsu Red
    ACCENT_SKY = RGBColor(56, 189, 248)     # Sky 400
    ACCENT_PURPLE = RGBColor(168, 85, 247)  # Purple 400
    ACCENT_EMERALD = RGBColor(16, 185, 129) # Emerald 400
    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_MUTED = RGBColor(148, 163, 184)    # Slate 400
    TEXT_LIGHT = RGBColor(226, 232, 240)    # Slate 200

    LOGO_PATH = r"c:\FTH\FTH-D365_FO\fujitsu_wordmark_clean.png"
    blank_layout = prs.slide_layouts[6]

    def add_slide_base(badge_text, title_text, subtitle_text, slide_num):
        slide = prs.slides.add_slide(blank_layout)

        # 1. Background fill
        bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg_shape.fill.solid()
        bg_shape.fill.fore_color.rgb = BG_COLOR
        bg_shape.line.fill.background()

        # Top subtle accent line (Fujitsu red gradient tone)
        top_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.06))
        top_line.fill.solid()
        top_line.fill.fore_color.rgb = ACCENT_RED
        top_line.line.fill.background()

        # 2. Fujitsu Logo in Top Right
        if os.path.exists(LOGO_PATH):
            slide.shapes.add_picture(LOGO_PATH, Inches(11.4), Inches(0.4), width=Inches(1.4))

        # 3. Header Text Box
        hdr_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(10.2), Inches(1.3))
        tf = hdr_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        # Badge
        p_badge = tf.paragraphs[0]
        p_badge.text = badge_text.upper()
        p_badge.font.name = "Segoe UI"
        p_badge.font.size = Pt(10)
        p_badge.font.bold = True
        p_badge.font.color.rgb = ACCENT_SKY
        p_badge.space_after = Pt(3)

        # Title
        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.name = "Segoe UI"
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE
        p_title.space_after = Pt(3)

        # Subtitle
        p_sub = tf.add_paragraph()
        p_sub.text = subtitle_text
        p_sub.font.name = "Segoe UI"
        p_sub.font.size = Pt(12)
        p_sub.font.color.rgb = TEXT_MUTED

        # Footer Slide indicator
        ftr_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.7), Inches(0.35))
        ftf = ftr_box.text_frame
        ftf.word_wrap = True
        ftf.margin_left = ftf.margin_top = ftf.margin_right = ftf.margin_bottom = 0
        p_ftr = ftf.paragraphs[0]
        p_ftr.text = f"FUJITSU THAILAND (FTH) • DYNAMICS 365 & COPILOT AI EXECUTIVE BRIEFING • SLIDE {slide_num} OF 4"
        p_ftr.font.name = "Segoe UI"
        p_ftr.font.size = Pt(9)
        p_ftr.font.color.rgb = RGBColor(100, 116, 139)

        return slide

    # =========================================================================
    # SLIDE 1: Title & Executive Welcome
    # =========================================================================
    s1 = add_slide_base(
        "Fujitsu Thailand (FTH) • Executive Opening Keynote",
        "Empowering Enterprise ERP with Microsoft Copilot AI",
        "ยกระดับศักยภาพ Dynamics 365 Finance & Operations สู่ยุค Autonomous AI & ขับเคลื่อนคุณค่าเชิงกลยุทธ์ให้ ฟูจิตสึ ประเทศไทย",
        1
    )

    # Main Center Hero Banner Card
    hero = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.85), Inches(11.733), Inches(4.85))
    hero.fill.solid()
    hero.fill.fore_color.rgb = CARD_BG
    hero.line.color.rgb = CARD_BORDER
    hero.line.width = Pt(1.5)

    # Content inside Slide 1 Hero Card
    htf = hero.text_frame
    htf.word_wrap = True
    htf.margin_left = Inches(0.6)
    htf.margin_right = Inches(0.6)
    htf.margin_top = Inches(0.4)

    p0 = htf.paragraphs[0]
    p0.text = "🎯 จุดมุ่งหมายเชิงกลยุทธ์ของการบรรยายในวันนี้ (Executive Purpose)"
    p0.font.name = "Segoe UI"
    p0.font.size = Pt(16)
    p0.font.bold = True
    p0.font.color.rgb = ACCENT_SKY
    p0.space_after = Pt(12)

    p1 = htf.add_paragraph()
    p1.text = "1. การปฏิวัติระบบ ERP สู่ Autonomous AI: นำเสนอแนวทางการผสาน Dynamics 365 F&O เข้ากับ Microsoft Copilot Studio เพื่อเปลี่ยนจากการทำงานแบบ Manual ซ้ำซ้อน สู่การประมวลผลอัจฉริยะแบบอัตโนมัติ"
    p1.font.name = "Segoe UI"
    p1.font.size = Pt(13)
    p1.font.color.rgb = TEXT_LIGHT
    p1.space_after = Pt(10)

    p2 = htf.add_paragraph()
    p2.text = "2. เจาะลึก Thai Localization & Tax Compliance: แก้โจทย์ความซับซ้อนของภาษีไทย ทั้ง VAT 7%, ภาษีหัก ณ ที่จ่าย ภ.พ.30, ภ.ง.ด.3/53, และ e-Tax Invoice ให้ถูกต้อง แม่นยำ รวดเร็ว และตรวจสอบย้อนกลับได้ 100%"
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(13)
    p2.font.color.rgb = TEXT_LIGHT
    p2.space_after = Pt(10)

    p3 = htf.add_paragraph()
    p3.text = "3. เสริมความแข็งแกร่งของผลิตภัณฑ์ & มูลค่าของ FTH: ตอกย้ำความเป็นผู้นำของ ฟูจิตสึ ประเทศไทย ในฐานะ Trusted Partner ที่ครอบครอง High-Value Intellectual Property (IP) ด้าน AI ERP ในระดับภูมิภาค"
    p3.font.name = "Segoe UI"
    p3.font.size = Pt(13)
    p3.font.color.rgb = TEXT_LIGHT
    p3.space_after = Pt(16)

    # Speaker info badge
    p4 = htf.add_paragraph()
    p4.text = "🎤 ผู้นำเสนอ: Solution Principal & Executive Host, Fujitsu Thailand (FTH) | ⏱️ ระยะเวลาเกริ่นนำ: ~2 นาที"
    p4.font.name = "Segoe UI"
    p4.font.size = Pt(11)
    p4.font.bold = True
    p4.font.color.rgb = ACCENT_PURPLE

    # Slide 1 Notes (Presenter Script)
    s1.notes_slide.notes_text_frame.text = (
        "【บทพูดพิธีกร - สไลด์ที่ 1: ต้อนรับผู้บริหารและเกริ่นนำวิสัยทัศน์】\n\n"
        "\"กราบเรียนท่านผู้บริหาร คณะทำงาน และแขกผู้มีเกียรติทุกท่านครับ ผมขอต้อนรับทุกท่านเข้าสู่การนำเสนอเชิงกลยุทธ์ "
        "ของ ฟูจิตสึ ประเทศไทย (FTH) ในหัวข้อ 'Empowering Enterprise ERP with Microsoft Copilot AI' ครับ\n\n"
        "ในวันนี้ เรามีความยินดีเป็นอย่างยิ่งที่จะแบ่งปันวิสัยทัศน์ในการยกระดับระบบ Dynamics 365 Finance & Operations "
        "โดยการนำเทคโนโลยีปัญญาประดิษฐ์ระดับองค์กรอย่าง Microsoft Copilot Studio และ Azure AI เข้ามาเสริมความแข็งแกร่ง "
        "ให้กับกระบวนการบัญชีและการเงินของไทย\n\n"
        "เป้าหมายสำคัญของเราในวันนี้ ไม่ใช่เพียงการแนะนำเทคโนโลยีใหม่ แต่เป็นการสร้าง New Strategic Asset และเพิ่มมูลค่าการแข่งขัน "
        "ให้กับ FTH ในฐานะผู้นำโซลูชันด้านดิจิทัลทรานส์ฟอร์เมชันที่ได้รับความไว้วางใจสูงสุดในประเทศไทยครับ\""
    )

    # =========================================================================
    # SLIDE 2: Industry Shift - System of Record to System of Intelligence
    # =========================================================================
    s2 = add_slide_base(
        "Market Drivers & Business Challenges",
        "The Paradigm Shift: From System of Record to System of Intelligence",
        "ทำไมระบบ ERP ในปัจจุบันจึงต้องก้าวข้ามขีดจำกัดเดิม สู่การเป็นระบบอัจฉริยะที่ช่วยวิเคราะห์และตัดสินใจ",
        2
    )

    # 3 Cards Layout
    card_width = Inches(3.64)
    card_height = Inches(4.85)
    top_pos = Inches(1.85)
    gap = Inches(0.4)

    # Card 1: Traditional Bottlenecks
    c1 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top_pos, card_width, card_height)
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = RGBColor(239, 68, 68) # Red alert border
    c1.line.width = Pt(1.5)
    t1 = c1.text_frame
    t1.word_wrap = True
    t1.margin_left = t1.margin_right = t1.margin_top = Inches(0.3)
    p = t1.paragraphs[0]
    p.text = "⚠️ ความท้าทายของ ERP ดั้งเดิม"
    p.font.name = "Segoe UI"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = RGBColor(248, 113, 113)
    p.space_after = Pt(8)

    bullets1 = [
        "งาน Manual สูง: พนักงานต้องใช้เวลากว่า 70% ตรวจสอบเอกสารใบแจ้งหนี้ PDF และใบเสร็จรับเงินด้วยตาเปล่า",
        "ความเสี่ยงเรื่อง Human Error: การคีย์เลขประจำตัวผู้เสียภาษี 13 หลัก หรือรหัสสาขา 5 หลัก ผิดพลาด นำไปสู่ปัญหาภาษี",
        "ปิดงวดบัญชีล่าช้า: คอขวดในช่วงสิ้นเดือน ส่งผลกระทบต่อการยื่นแบบ ภ.พ.30 และการบริหารสภาพคล่องขององค์กร"
    ]
    for b in bullets1:
        pb = t1.add_paragraph()
        pb.text = "• " + b
        pb.font.name = "Segoe UI"
        pb.font.size = Pt(11)
        pb.font.color.rgb = TEXT_LIGHT
        pb.space_after = Pt(8)

    # Card 2: Regulatory Pressures
    c2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8) + card_width + gap, top_pos, card_width, card_height)
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = ACCENT_PURPLE
    c2.line.width = Pt(1.5)
    t2 = c2.text_frame
    t2.word_wrap = True
    t2.margin_left = t2.margin_right = t2.margin_top = Inches(0.3)
    p = t2.paragraphs[0]
    p.text = "🏛️ กฎระเบียบภาษีไทยที่เข้มงวด"
    p.font.name = "Segoe UI"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE
    p.space_after = Pt(8)

    bullets2 = [
        "นโยบาย e-Tax Mandate: กรมสรรพากรผลักดันระบบ e-Tax Invoice & e-Receipt จำเป็นต้องมีระบบตรวจสอบความสมบูรณ์ก่อนส่ง",
        "ภาษีหัก ณ ที่จ่าย (WHT): มีอัตราภาษีหลากหลายและเงื่อนไขซับซ้อนตามประเภทบริการ",
        "โทษปรับและภาระดอกเบี้ย: ความผิดพลาดเพียงจุดเดียวส่งผลกระทบต่อการยื่นภาษีและสร้างภาระค่าใช้จ่ายที่ไม่จำเป็นแก่ธุรกิจ"
    ]
    for b in bullets2:
        pb = t2.add_paragraph()
        pb.text = "• " + b
        pb.font.name = "Segoe UI"
        pb.font.size = Pt(11)
        pb.font.color.rgb = TEXT_LIGHT
        pb.space_after = Pt(8)

    # Card 3: AI-First Opportunity
    c3 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8) + (card_width + gap)*2, top_pos, card_width, card_height)
    c3.fill.solid()
    c3.fill.fore_color.rgb = CARD_BG
    c3.line.color.rgb = ACCENT_SKY
    c3.line.width = Pt(1.5)
    t3 = c3.text_frame
    t3.word_wrap = True
    t3.margin_left = t3.margin_right = t3.margin_top = Inches(0.3)
    p = t3.paragraphs[0]
    p.text = "🚀 โอกาสของ Fujitsu (FTH)"
    p.font.name = "Segoe UI"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_SKY
    p.space_after = Pt(8)

    bullets3 = [
        "System of Intelligence: เปลี่ยน D365 F&O ให้กลายเป็นศูนย์บัญชาการการเงินที่คิด วิเคราะห์ และตรวจทานข้อมูลล่วงหน้า",
        "Human-in-the-Loop: AI ช่วยอ่านและร่างเอกสาร แต่ให้อำนาจการตัดสินใจและอนุมัติขั้นสุดท้ายแก่บุคลากรผู้เชี่ยวชาญ",
        "สร้างแต้มต่อทางธุรกิจ: FTH สามารถส่งมอบโซลูชันที่เหนือกว่าคู่แข่งรายอื่นในตลาด และตอบโจทย์องค์กรยุคใหม่อย่างแท้จริง"
    ]
    for b in bullets3:
        pb = t3.add_paragraph()
        pb.text = "• " + b
        pb.font.name = "Segoe UI"
        pb.font.size = Pt(11)
        pb.font.color.rgb = TEXT_LIGHT
        pb.space_after = Pt(8)

    s2.notes_slide.notes_text_frame.text = (
        "【บทพูดพิธีกร - สไลด์ที่ 2: ชี้ให้เห็นความท้าทายและโอกาส】\n\n"
        "\"ทุกท่านครับ เมื่อมองย้อนกลับมาที่การดำเนินงานจริงในปัจจุบัน ระบบ ERP แบบดั้งเดิมทำหน้าที่บันทึกประวัติ หรือ System of Record "
        "ได้ดี แต่ปัญหาคอขวดที่แท้จริงขององค์กรธุรกิจในประเทศไทย คือภาระงานของทีมบัญชี (AP) ที่ต้องตรวจสอบเอกสารใบกำกับภาษี PDF "
        "จำนวนหลายร้อยหลายพันใบในแต่ละเดือน\n\n"
        "ทั้งการตรวจสอบเลขประจำตัวผู้เสียภาษี 13 หลัก, สาขา 5 หลัก, การจับคู่ 3-Way Matching, และการคำนวณภาษีหัก ณ ที่จ่าย "
        "ประกอบกับนโยบายของกรมสรรพากรที่กำลังขับเคลื่อนสู่ e-Tax Invoice อย่างเต็มรูปแบบ ความผิดพลาดแม้เพียงเล็กน้อย "
        "ย่อมหมายถึงความล่าช้าและผลกระทบทางภาษี\n\n"
        "นี่คือสาเหตุที่ ฟูจิตสึ เล็งเห็นโอกาสครั้งสำคัญ ในการเปลี่ยนผ่าน D365 ให้กลายเป็น 'System of Intelligence' "
        "เพื่อช่วยแบ่งเบาภาระงานซ้ำซ้อน และเพิ่มความแม่นยำให้กับการเงินขององค์กรครับ\""
    )

    # =========================================================================
    # SLIDE 3: Strengthening D365 & Maximizing FTH Value
    # =========================================================================
    s3 = add_slide_base(
        "Product Excellence & Strategic Value",
        "Strengthening Dynamics 365 & Maximizing Fujitsu (FTH) Enterprise Value",
        "เสริมความแข็งแกร่งของโซลูชัน และสร้างมูลค่าเพิ่มมหาศาลให้กับ ฟูจิตสึ ประเทศไทย",
        3
    )

    col_width = Inches(5.66)
    col_gap = Inches(0.4)

    # Left Column: Product Strength
    p_card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top_pos, col_width, card_height)
    p_card.fill.solid()
    p_card.fill.fore_color.rgb = CARD_BG
    p_card.line.color.rgb = ACCENT_SKY
    p_card.line.width = Pt(1.5)
    ptf = p_card.text_frame
    ptf.word_wrap = True
    ptf.margin_left = ptf.margin_right = ptf.margin_top = Inches(0.35)

    p = ptf.paragraphs[0]
    p.text = "💎 1. เสริมความแข็งแกร่งของผลิตภัณฑ์ (D365 F&O)"
    p.font.name = "Segoe UI"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_SKY
    p.space_after = Pt(10)

    p_items = [
        ("Native Copilot Fusion", "ผสาน Microsoft Copilot Studio และ Azure AI เข้ากับ D365 ผ่าน Dataverse และ standard API โดยตรง ไม่มีการส่งข้อมูลออกนอกระบบ"),
        ("Autonomous Draft Workflow", "AI ช่วยอ่านเอกสาร ตรวจสอบกฎระเบียบ และสร้าง Draft Vendor Invoice ล่วงหน้า ลดเวลางานลงกว่า 70%"),
        ("Strict Human-in-the-Loop", "รักษาความปลอดภัยสูงสุด AI ทำหน้าที่เป็นผู้ช่วยจัดเตรียม แต่พนักงานต้องกด Confirm และ Approve เสมอก่อนโพสต์ลงสมุดบัญชี"),
        ("Comprehensive Thai Localization", "ครอบคลุมรายงานภาษีไทยครบวงจร: ภ.พ.30, ภ.ง.ด.3, ภ.ง.ด.53, หนังสือรับรองการหักภาษี 50 ทวิ และ e-Tax XML")
    ]
    for title, desc in p_items:
        pt = ptf.add_paragraph()
        pt.text = f"• {title}: "
        pt.font.name = "Segoe UI"
        pt.font.size = Pt(11)
        pt.font.bold = True
        pt.font.color.rgb = TEXT_WHITE

        # Add description
        run = pt.add_run()
        run.text = desc
        run.font.name = "Segoe UI"
        run.font.size = Pt(10.5)
        run.font.bold = False
        run.font.color.rgb = TEXT_LIGHT
        pt.space_after = Pt(6)

    # Right Column: FTH Business Value
    f_card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8) + col_width + col_gap, top_pos, col_width, card_height)
    f_card.fill.solid()
    f_card.fill.fore_color.rgb = CARD_BG
    f_card.line.color.rgb = ACCENT_RED
    f_card.line.width = Pt(1.5)
    ftf = f_card.text_frame
    ftf.word_wrap = True
    ftf.margin_left = ftf.margin_right = ftf.margin_top = Inches(0.35)

    p = ftf.paragraphs[0]
    p.text = "🏆 2. เพิ่มมูลค่าและแต้มต่อทางธุรกิจให้ Fujitsu (FTH)"
    p.font.name = "Segoe UI"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = RGBColor(248, 113, 113)
    p.space_after = Pt(10)

    f_items = [
        ("First-Mover Advantage ในไทย", "FTH เป็นผู้นำรายแรกที่นำเสนอ Thai Localization Package ที่มี AI ฝังตัว ช่วยสร้างแต้มต่อที่ยากแก่การลอกเลียนแบบ"),
        ("High-Margin Reusable IP", "สามารถแพ็กเกจเป็น Commercial IP Asset นำไปติดตั้งและต่อยอดให้กับลูกค้าองค์กรได้อย่างรวดเร็ว ลดเวลา Implement"),
        ("ขยายฐานลูกค้าญี่ปุ่นและองค์กรชั้นนำ", "ตอบโจทย์ Japanese MNCs และกลุ่มธุรกิจขนาดใหญ่ในไทยที่ต้องการยกระดับ ERP ให้ทันสมัยและสอดรับกฎหมายไทย"),
        ("Fujitsu Trusted Brand Heritage", "ผสานจุดแข็งด้าน Service Quality และมาตรฐานความปลอดภัยขั้นสูงของ Fujitsu เข้ากับนวัตกรรม AI ระดับโลกของ Microsoft")
    ]
    for title, desc in f_items:
        ft = ftf.add_paragraph()
        ft.text = f"• {title}: "
        ft.font.name = "Segoe UI"
        ft.font.size = Pt(11)
        ft.font.bold = True
        ft.font.color.rgb = TEXT_WHITE

        run = ft.add_run()
        run.text = desc
        run.font.name = "Segoe UI"
        run.font.size = Pt(10.5)
        run.font.bold = False
        run.font.color.rgb = TEXT_LIGHT
        ft.space_after = Pt(6)

    s3.notes_slide.notes_text_frame.text = (
        "【บทพูดพิธีกร - สไลด์ที่ 3: เสริมแกร่งผลิตภัณฑ์และคุณค่าของ FTH】\n\n"
        "\"ในแง่ของความคุ้มค่าและผลประโยชน์เชิงกลยุทธ์ โครงการนี้ได้สร้างคุณค่าสองด้านพร้อมกันครับ\n\n"
        "ด้านแรก คือความแข็งแกร่งของผลิตภัณฑ์ Dynamics 365 ที่ได้รับการอัปเกรดให้มี AI ทำงานอยู่เบื้องหลังอย่างแท้จริง "
        "ช่วยเตรียมเอกสารร่าง ตรวจสอบกฎหมายภาษีไทย และคงมาตรฐานความปลอดภัยระดับสูงสุด โดยไม่ปล่อยให้ AI โพสต์ข้อมูลโดยพลการ\n\n"
        "และด้านที่สอง ซึ่งสำคัญยิ่งต่อ ฟูจิตสึ ประเทศไทย คือการสร้าง 'ความแตกต่างที่เหนือกว่า' ในตลาด ERP "
        "เราจะไม่ได้เป็นเพียงผู้ Implement ระบบตามคู่มือทั่วไป แต่เราจะเป็นเจ้าของ Intellectual Property หรือทรัพย์สินทางปัญญา "
        "ที่ตอบโจทย์ภาษีไทยด้วย AI ซึ่งสร้าง Margin ที่สูงขึ้น เปิดประตูสู่กลุ่มลูกค้าบริษัทข้ามชาติทั้งญี่ปุ่นและไทย "
        "และตอกย้ำภาพลักษณ์ของ Fujitsu ในฐานะผู้นำด้านนวัตกรรมองค์กรครับ\""
    )

    # =========================================================================
    # SLIDE 4: Executive Agenda & Transition to Interactive Pitch Deck
    # =========================================================================
    s4 = add_slide_base(
        "Solution Roadmap & Live Demonstration",
        "Executive Agenda & Transition to Live Interactive Solution Pitch",
        "โครงสร้างเนื้อหาที่จะได้รับชมในวันนี้ และการส่งมอบเข้าสู่แพลตฟอร์มจำลองระบบจริง (Interactive Deck)",
        4
    )

    # Left Section: 4 Key Agenda Blocks
    agenda_w = Inches(6.8)
    agenda_h = Inches(4.85)
    ag_card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top_pos, agenda_w, agenda_h)
    ag_card.fill.solid()
    ag_card.fill.fore_color.rgb = CARD_BG
    ag_card.line.color.rgb = CARD_BORDER
    ag_card.line.width = Pt(1.5)
    atf = ag_card.text_frame
    atf.word_wrap = True
    atf.margin_left = atf.margin_right = atf.margin_top = Inches(0.35)

    p = atf.paragraphs[0]
    p.text = "📑 4 ประเด็นสำคัญใน Live Interactive Solution Pitch (12 สไลด์)"
    p.font.name = "Segoe UI"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_SKY
    p.space_after = Pt(10)

    agenda_items = [
        ("1. Official Architecture", "สถาปัตยกรรมอ้างอิง Microsoft Copilot Studio & Multi-Agent Framework ที่ทำงานร่วมกับ D365 อย่างปลอดภัย"),
        ("2. Top 5 Thai Use Cases", "สาธิต 5 รูปแบบการใช้งานจริง: AP Invoice, Tax Compliance, e-Tax Gateway, Continuous Reconciliation และ Knowledge Q&A"),
        ("3. 8-Week POC Roadmap", "แผนการดำเนินงานโครงการนำร่อง 8 สัปดาห์ เพื่อประเมินผลความคุ้มค่า (ROI) และความพร้อมในการใช้งานจริง"),
        ("4. Dual-Host AI Narration", "ระบบเสียงบรรยายจำลองแบบ Dual-Host รองรับทั้งภาษาอังกฤษและภาษาไทย พร้อมระบบเลื่อนสไลด์อัตโนมัติ")
    ]
    for num, txt in agenda_items:
        ap = atf.add_paragraph()
        ap.text = f"• {num}: "
        ap.font.name = "Segoe UI"
        ap.font.size = Pt(11)
        ap.font.bold = True
        ap.font.color.rgb = TEXT_WHITE

        run = ap.add_run()
        run.text = txt
        run.font.name = "Segoe UI"
        run.font.size = Pt(10.5)
        run.font.bold = False
        run.font.color.rgb = TEXT_LIGHT
        ap.space_after = Pt(8)

    # Right Section: Handover Card & Direct URL
    call_w = Inches(4.533)
    call_card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8) + agenda_w + Inches(0.4), top_pos, call_w, agenda_h)
    call_card.fill.solid()
    call_card.fill.fore_color.rgb = CARD_BG
    call_card.line.color.rgb = ACCENT_EMERALD
    call_card.line.width = Pt(1.5)
    ctf = call_card.text_frame
    ctf.word_wrap = True
    ctf.margin_left = ctf.margin_right = ctf.margin_top = Inches(0.35)

    p = ctf.paragraphs[0]
    p.text = "🚀 คำกล่าวส่งต่อและเปิดตัวระบบจำลอง (Live Handover)"
    p.font.name = "Segoe UI"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_EMERALD
    p.space_after = Pt(10)

    p_hand = ctf.add_paragraph()
    p_hand.text = "\"บัดนี้ ผมขอเรียนเชิญคณะผู้บริหารทุกท่าน ร่วมสัมผัสและทดสอบระบบจำลองจริงผ่าน Interactive Pitch Deck ได้ ณ บัดนี้ครับ...\""
    p_hand.font.name = "Segoe UI"
    p_hand.font.size = Pt(11.5)
    p_hand.font.italic = True
    p_hand.font.color.rgb = RGBColor(167, 243, 208)
    p_hand.space_after = Pt(16)

    # Link button box
    p_btn = ctf.add_paragraph()
    p_btn.text = "🌐 Direct Solution Link:"
    p_btn.font.name = "Segoe UI"
    p_btn.font.size = Pt(11)
    p_btn.font.bold = True
    p_btn.font.color.rgb = TEXT_WHITE
    p_btn.space_after = Pt(4)

    p_url = ctf.add_paragraph()
    p_url.text = "https://wititgithub.github.io/fth-d365-fo-copilot-deck/"
    p_url.font.name = "Segoe UI"
    p_url.font.size = Pt(10)
    p_url.font.bold = True
    p_url.font.color.rgb = ACCENT_SKY
    p_url.space_after = Pt(14)

    p_sub_cue = ctf.add_paragraph()
    p_sub_cue.text = "💡 คำแนะนำสำหรับพิธีกร:\nเมื่อกล่าวประโยคส่งมอบจบ สามารถคลิกเปิดลิงก์ด้านบน หรือสลับหน้าต่างไปยังเบราว์เซอร์เพื่อเริ่มระบบสไลด์จำลองได้ทันที"
    p_sub_cue.font.name = "Segoe UI"
    p_sub_cue.font.size = Pt(9.5)
    p_sub_cue.font.color.rgb = TEXT_MUTED

    s4.notes_slide.notes_text_frame.text = (
        "【บทพูดพิธีกร - สไลด์ที่ 4: สรุปหัวข้อและส่งต่อเข้าสู่ Live Interactive Deck】\n\n"
        "\"และในลำดับถัดไป เพื่อให้ทุกท่านได้เห็นภาพการทำงานจริงอย่างเป็นรูปธรรม ทางทีมงานได้จัดเตรียม "
        "แพลตฟอร์มการนำเสนอแบบ Interactive Pitch Deck จำนวน 12 สไลด์ ที่จำลองการทำงานจริงอย่างละเอียด\n\n"
        "โดยประกอบด้วยสถาปัตยกรรมทางเทคนิค, 5 Use Cases หลักที่ออกแบบมาเพื่อภาษีไทยโดยเฉพาะ, "
        "และแผนการดำเนินงาน POC 8 สัปดาห์ พร้อมเสียงบรรยายจำลองแบบ Dual-Host ที่ปรับแต่งมาอย่างเป็นทางการ\n\n"
        "บัดนี้ ผมขออนุญาตนำพาทุกท่านเข้าสู่ระบบจำลองผ่านลิงก์โครงการ เพื่อร่วมทดสอบและสัมผัสประสบการณ์แห่งอนาคต "
        "ของ Dynamics 365 และ Copilot AI ไปพร้อมกันได้ ณ บัดนี้ครับ ขอเรียนเชิญทุกท่านครับ\""
    )

    out_pptx_paths = [
        r"c:\FTH\FTH-D365_FO\FTH_D365_Executive_Opening_Deck.pptx",
        r"c:\FTH\FTH-D365_FO\assets\FTH_D365_Executive_Opening_Deck.pptx",
        r"C:\Users\witit\.gemini\antigravity\brain\7bc4ceac-b79a-4881-9938-a5db0d7782a2\FTH_D365_Executive_Opening_Deck.pptx"
    ]

    for p in out_pptx_paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        prs.save(p)
        print(f"Generated PowerPoint Deck -> {p} ({os.path.getsize(p)//1024} KB)")

if __name__ == "__main__":
    build_presentation()
