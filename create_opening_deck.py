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

    # Pristine Executive White Corporate Theme
    BG_COLOR = RGBColor(248, 250, 252)       # Slate 50
    CARD_BG = RGBColor(255, 255, 255)        # Pure White
    CARD_BORDER = RGBColor(226, 232, 240)    # Slate 200
    ACCENT_RED = RGBColor(220, 38, 38)       # Fujitsu Red (Crimson)
    ACCENT_SKY = RGBColor(2, 132, 199)       # Sky 600 / Azure
    ACCENT_PURPLE = RGBColor(124, 58, 237)   # Indigo / Purple 600
    ACCENT_EMERALD = RGBColor(5, 150, 105)   # Emerald 600
    TEXT_TITLE = RGBColor(15, 23, 42)        # Slate 900 (High contrast)
    TEXT_BODY = RGBColor(51, 65, 85)         # Slate 700
    TEXT_MUTED = RGBColor(100, 116, 139)     # Slate 500

    LOGO_PATH = r"c:\FTH\FTH-D365_FO\fujitsu_wordmark_clean.png"
    blank_layout = prs.slide_layouts[6]

    def add_slide_base(badge_text, title_text, subtitle_text, slide_num):
        slide = prs.slides.add_slide(blank_layout)

        # 1. Background fill (Slate 50)
        bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg_shape.fill.solid()
        bg_shape.fill.fore_color.rgb = BG_COLOR
        bg_shape.line.fill.background()

        # Top accent line (Fujitsu Red)
        top_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.08))
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
        p_badge.font.color.rgb = ACCENT_RED
        p_badge.space_after = Pt(3)

        # Title
        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.name = "Segoe UI"
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_TITLE
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
        p_ftr.text = f"FUJITSU THAILAND (FTH) • DYNAMICS 365 & COPILOT AI EXECUTIVE KEYNOTE • SLIDE {slide_num} OF 4"
        p_ftr.font.name = "Segoe UI"
        p_ftr.font.size = Pt(9)
        p_ftr.font.bold = True
        p_ftr.font.color.rgb = TEXT_MUTED

        return slide

    # =========================================================================
    # SLIDE 1: Title & Executive Welcome (English White Theme)
    # =========================================================================
    s1 = add_slide_base(
        "Fujitsu Thailand (FTH) • Strategic Keynote",
        "Empowering Enterprise ERP with Microsoft Copilot AI",
        "Advancing Dynamics 365 Finance & Operations into Autonomous AI & Unlocking Strategic Value for Fujitsu Thailand",
        1
    )

    card_width_3 = Inches(3.64)
    card_height = Inches(4.85)
    top_pos = Inches(1.85)
    gap = Inches(0.4)

    # 3 Strategic Pillars Cards
    pillars = [
        ("⚡ 1. Autonomous ERP", ACCENT_SKY, [
            ("Speed & Precision", "Transforming manual accounting workflows into an intelligent system that reads, verifies, and pre-drafts invoices."),
            ("Seamless Dynamics 365", "Direct native fusion between Copilot Studio, Azure AI, and D365 F&O via Dataverse."),
            ("Labor Savings", "Slashes repetitive Accounts Payable cycle time by over 70%, freeing teams for strategic finance.")
        ]),
        ("🏛️ 2. Thai Tax Compliance", ACCENT_PURPLE, [
            ("100% Tax Alignment", "Built for Revenue Department standards: PP.30 VAT 7%, PND 3/53, and 50 Tawi certificates."),
            ("e-Tax Pre-Validation", "Automatic gate checking 13-digit Tax IDs and 5-digit branch codes before XML generation."),
            ("Continuous Subledger Audit", "Monitors GL against AP/AR/Tax continuously, preventing month-end tax filing panic.")
        ]),
        ("🏆 3. Value for Fujitsu (FTH)", ACCENT_RED, [
            ("Proprietary IP Leadership", "FTH owns a distinctive, repeatable AI-infused Thai Localization package in Thailand."),
            ("High-Margin Reusability", "Packaged solution scales across Japanese MNCs and major Thai corporate clients."),
            ("Trusted Global Partner", "Combines Fujitsu’s Japanese quality and governance with Microsoft’s premier enterprise AI.")
        ])
    ]

    for i, (p_title, border_color, p_items) in enumerate(pillars):
        left_pos = Inches(0.8) + i * (card_width_3 + gap)
        c = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos, top_pos, card_width_3, card_height)
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = border_color
        c.line.width = Pt(1.5)
        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = p_title
        p.font.name = "Segoe UI"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = border_color
        p.space_after = Pt(12)

        for heading, body in p_items:
            pb = tf.add_paragraph()
            pb.text = f"• {heading}: "
            pb.font.name = "Segoe UI"
            pb.font.size = Pt(10.5)
            pb.font.bold = True
            pb.font.color.rgb = TEXT_TITLE

            run = pb.add_run()
            run.text = body
            run.font.name = "Segoe UI"
            run.font.size = Pt(10)
            run.font.bold = False
            run.font.color.rgb = TEXT_BODY
            pb.space_after = Pt(8)

    s1.notes_slide.notes_text_frame.text = (
        "【English Executive Host Script - Slide 1: Welcome & Visionary Opening】\n\n"
        "\"Good morning and welcome, esteemed executives, colleagues, and distinguished guests. Welcome to this strategic executive briefing "
        "from Fujitsu Thailand (FTH) on 'Empowering Enterprise ERP with Microsoft Copilot AI'.\n\n"
        "Today, we are thrilled to present our vision for advancing Microsoft Dynamics 365 Finance & Operations by natively infusing "
        "Microsoft Copilot Studio and Azure AI into everyday financial and Thai tax compliance workflows.\n\n"
        "Our purpose today is not merely introducing new AI features, but creating high-value Strategic Intellectual Property (IP) for FTH—strengthening "
        "our market position as Thailand's most trusted partner in enterprise digital transformation.\"\n\n"
        "----------------------------------------------------------------------\n"
        "【บทพูดภาษาไทยสำหรับพิธีกร - สไลด์ที่ 1: ต้อนรับผู้บริหารและเกริ่นนำวิสัยทัศน์】\n\n"
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
        "Navigating Thai financial and tax complexities, and unlocking Fujitsu’s breakthrough opportunity.",
        2
    )

    s2_cards = [
        ("⚠️ Traditional ERP Limits", ACCENT_RED, [
            ("Manual Overload", "AP teams spend >70% of time verifying PDF invoices, receipts, and line items manually."),
            ("Human Error Risks", "Typos in 13-digit Tax IDs or 5-digit branch codes trigger tax discrepancies."),
            ("Closing Delays", "Month-end crunch delays PP.30 submissions and obscures real-time cash visibility.")
        ]),
        ("🏛️ Strict Thai Mandates", ACCENT_PURPLE, [
            ("e-Tax Enforcement", "Revenue Dept requires strict XML schemas and 100% pre-validation before submission."),
            ("Complex WHT Rules", "Variable 1%, 2%, 3%, 5% rates require exact categorization based on service nature."),
            ("Penalty Exposure", "Late or erroneous filings result in unnecessary surcharges and audit friction.")
        ]),
        ("🚀 Fujitsu's Opportunity", ACCENT_SKY, [
            ("System of Intelligence", "Elevating D365 to analyze, pre-validate, and predict issues before transactions post."),
            ("Human-in-the-Loop", "AI prepares validated drafts; accountants retain full approval authority."),
            ("Market Leadership", "FTH delivers modern AI innovation that traditional competitors in Thailand cannot match.")
        ])
    ]

    for i, (title, color, items) in enumerate(s2_cards):
        left_pos = Inches(0.8) + i * (card_width_3 + gap)
        c = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos, top_pos, card_width_3, card_height)
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = color
        c.line.width = Pt(1.5)
        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Segoe UI"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = color
        p.space_after = Pt(12)

        for heading, body in items:
            pb = tf.add_paragraph()
            pb.text = f"• {heading}: "
            pb.font.name = "Segoe UI"
            pb.font.size = Pt(10.5)
            pb.font.bold = True
            pb.font.color.rgb = TEXT_TITLE

            run = pb.add_run()
            run.text = body
            run.font.name = "Segoe UI"
            run.font.size = Pt(10)
            run.font.bold = False
            run.font.color.rgb = TEXT_BODY
            pb.space_after = Pt(8)

    s2.notes_slide.notes_text_frame.text = (
        "【English Executive Host Script - Slide 2: Industry Shift & Local Challenges】\n\n"
        "\"Distinguished guests, looking at day-to-day operations across Thailand, traditional ERP systems have served effectively "
        "as Systems of Record. However, the true operational bottleneck lies within Accounts Payable—where finance teams spend over 70% "
        "of their time manually reviewing hundreds of PDF tax invoices.\n\n"
        "From verifying 13-digit Tax IDs and 5-digit branch codes to 3-way matching and withholding tax calculations, manual workloads "
        "create severe month-end crunches. Coupled with the Revenue Department's aggressive push toward e-Tax Invoice and e-Receipt mandates, "
        "a single clerical oversight risks delayed filings and compliance penalties.\n\n"
        "This is precisely why Fujitsu sees an unprecedented opportunity to elevate D365 into a 'System of Intelligence'—automating "
        "repetitive burdens and equipping our finance professionals with predictive, pre-validated intelligence.\"\n\n"
        "----------------------------------------------------------------------\n"
        "【บทพูดภาษาไทยสำหรับพิธีกร - สไลด์ที่ 2: ชี้ให้เห็นความท้าทายและโอกาส】\n\n"
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
        "Strengthening Dynamics 365 & Maximizing Fujitsu (FTH) Value",
        "A strategic technology fusion that drives mutual ROI for our clients and Fujitsu Thailand.",
        3
    )

    col_width = Inches(5.66)
    col_gap = Inches(0.4)

    # Left Column: D365 Product Enhancement
    p_card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top_pos, col_width, card_height)
    p_card.fill.solid()
    p_card.fill.fore_color.rgb = CARD_BG
    p_card.line.color.rgb = ACCENT_SKY
    p_card.line.width = Pt(1.5)
    ptf = p_card.text_frame
    ptf.word_wrap = True
    ptf.margin_left = ptf.margin_right = ptf.margin_top = Inches(0.35)

    p = ptf.paragraphs[0]
    p.text = "💎 1. D365 Product Enhancement"
    p.font.name = "Segoe UI"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_SKY
    p.space_after = Pt(10)

    p_items = [
        ("Native Copilot Fusion", "Direct integration with Copilot Studio and Azure AI via Dataverse and standard APIs—zero external data leakage."),
        ("Autonomous Draft Preparation", "AI reads documents, validates 3-way matching rules, and creates draft vendor invoices—slashing AP review time by >70%."),
        ("Strict Human-in-the-Loop", "AI prepares validated drafts; accountants retain exclusive approval authority before any journal posting."),
        ("Total Thai Tax Compliance", "Full support for PP.30, PND 3/53, 50 Tawi certificates, and Revenue Dept e-Tax XML formats.")
    ]
    for title, desc in p_items:
        pt = ptf.add_paragraph()
        pt.text = f"• {title}: "
        pt.font.name = "Segoe UI"
        pt.font.size = Pt(11)
        pt.font.bold = True
        pt.font.color.rgb = TEXT_TITLE

        run = pt.add_run()
        run.text = desc
        run.font.name = "Segoe UI"
        run.font.size = Pt(10)
        run.font.bold = False
        run.font.color.rgb = TEXT_BODY
        pt.space_after = Pt(7)

    # Right Column: Fujitsu (FTH) Strategic Value
    f_card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8) + col_width + col_gap, top_pos, col_width, card_height)
    f_card.fill.solid()
    f_card.fill.fore_color.rgb = CARD_BG
    f_card.line.color.rgb = ACCENT_RED
    f_card.line.width = Pt(1.5)
    ftf = f_card.text_frame
    ftf.word_wrap = True
    ftf.margin_left = ftf.margin_right = ftf.margin_top = Inches(0.35)

    p = ftf.paragraphs[0]
    p.text = "🏆 2. Fujitsu (FTH) Strategic Value"
    p.font.name = "Segoe UI"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_RED
    p.space_after = Pt(10)

    f_items = [
        ("First-Mover Advantage in Thailand", "FTH becomes the first partner offering a pre-packaged, AI-infused Thai Localization solution, creating a strong moat."),
        ("High-Margin Reusable IP Asset", "Packaged as commercial IP, enabling rapid deployment across enterprise clients with lower implementation costs."),
        ("Expands Japanese MNC & Enterprise Footprint", "Tailored to Japanese MNCs and major Thai conglomerates seeking modern, compliant ERP modernization."),
        ("Reinforces Global Trusted Partner Brand", "Combines Fujitsu’s renowned Japanese quality and governance standards with Microsoft’s premier AI technology.")
    ]
    for title, desc in f_items:
        ft = ftf.add_paragraph()
        ft.text = f"• {title}: "
        ft.font.name = "Segoe UI"
        ft.font.size = Pt(11)
        ft.font.bold = True
        ft.font.color.rgb = TEXT_TITLE

        run = ft.add_run()
        run.text = desc
        run.font.name = "Segoe UI"
        run.font.size = Pt(10)
        run.font.bold = False
        run.font.color.rgb = TEXT_BODY
        ft.space_after = Pt(7)

    s3.notes_slide.notes_text_frame.text = (
        "【English Executive Host Script - Slide 3: Product Excellence & Fujitsu Value】\n\n"
        "\"From a strategic value and ROI perspective, this initiative drives dual impact:\n\n"
        "First, Product Excellence for Dynamics 365: By natively embedding Copilot Studio and Azure AI via Dataverse, enterprise data "
        "remains 100% secure within company boundaries. AI extracts, cross-checks against Thai tax laws, and prepares draft vendor invoices—reducing "
        "cycle time by over 70%, while strictly maintaining Human-in-the-Loop governance so that finance professionals retain full approval "
        "authority before any journal posting.\n\n"
        "Second, Unmatched Business Value for Fujitsu Thailand: FTH establishes a distinctive first-mover advantage by offering a pre-packaged, "
        "AI-infused Thai Localization solution. This high-margin, reusable IP enables our sales and consulting teams to scale rapidly across "
        "Japanese multinationals (MNCs) and top-tier Thai conglomerates—reinforcing Fujitsu’s global reputation for quality, governance, and trust.\"\n\n"
        "----------------------------------------------------------------------\n"
        "【บทพูดภาษาไทยสำหรับพิธีกร - สไลด์ที่ 3: เสริมแกร่งผลิตภัณฑ์และคุณค่าของ FTH】\n\n"
        "\"ในแง่ของความคุ้มค่าและผลประโยชน์เชิงกลยุทธ์ โครงการนี้ได้สร้างคุณค่าสองด้านพร้อมกันครับ\n\n"
        "ด้านแรก คือความแข็งแกร่งของผลิตภัณฑ์ Dynamics 365 ที่ได้รับการอัปเกรดให้มี AI ทำงานอยู่เบื้องหลังอย่างแท้จริง "
        "ช่วยเตรียมเอกสารร่าง ตรวจสอบกฎหมายภาษีไทย และคงมาตรฐานความปลอดภัยระดับสูงสุด โดยไม่ปล่อยให้ AI โพสต์ข้อมูลโดยพลการ\n\n"
        "และด้านที่สอง ซึ่งสำคัญยิ่งต่อ ฟูจิตสึ ประเทศไทย คือการสร้าง 'ความแตกต่างที่เหนือกว่า' ในตลาด ERP "
        "เราจะไม่ได้เป็นเพียงผู้ Implement ระบบตามคู่มือทั่วไป แต่เราจะเป็นเจ้าของ Intellectual Property หรือทรัพย์สินทางปัญญา "
        "ที่ตอบโจทย์ภาษีไทยด้วย AI ซึ่งสร้าง Margin ที่สูงขึ้น เปิดประตูสู่กลุ่มลูกค้าบริษัทข้ามชาติทั้งญี่ปุ่นและไทย "
        "และตอกย้ำภาพลักษณ์ของ Fujitsu ในฐานะผู้นำด้านนวัตกรรมองค์กรครับ\""
    )

    # =========================================================================
    # SLIDE 4: Executive Agenda & Transition to Live Solution Pitch
    # =========================================================================
    s4 = add_slide_base(
        "Solution Roadmap & Live Demonstration",
        "Executive Agenda & Transition to Live Solution Pitch",
        "Today’s 12-slide walkthrough and formal handover into the live interactive demonstration platform.",
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
    p.text = "📑 Key Milestones in Live Interactive Pitch (12 Slides)"
    p.font.name = "Segoe UI"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_SKY
    p.space_after = Pt(10)

    agenda_items = [
        ("1. Official Architecture", "Multi-Agent Framework and 100% secure enterprise integration with D365 via Dataverse."),
        ("2. Top 5 Thai Use Cases", "Live walkthrough: AP Invoice Intelligence, Thai Tax Copilot, e-Tax Gateway, and Continuous Reconciliation."),
        ("3. 8-Week POC Delivery Plan", "Pragmatic, low-risk deployment roadmap delivering fast measurable value and fast payback."),
        ("4. Dual-Host AI Narration", "Production neural studio voice in English & Thai with automated auto-tour mode.")
    ]
    for num, txt in agenda_items:
        ap = atf.add_paragraph()
        ap.text = f"• {num}: "
        ap.font.name = "Segoe UI"
        ap.font.size = Pt(11)
        ap.font.bold = True
        ap.font.color.rgb = TEXT_TITLE

        run = ap.add_run()
        run.text = txt
        run.font.name = "Segoe UI"
        run.font.size = Pt(10)
        run.font.bold = False
        run.font.color.rgb = TEXT_BODY
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
    p.text = "🚀 Ready for Live Demonstration"
    p.font.name = "Segoe UI"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_EMERALD
    p.space_after = Pt(10)

    p_hand = ctf.add_paragraph()
    p_hand.text = "\"Without further ado, let us now transition directly into the live interactive platform to experience the future of D365 and Copilot AI firsthand...\""
    p_hand.font.name = "Segoe UI"
    p_hand.font.size = Pt(11)
    p_hand.font.italic = True
    p_hand.font.color.rgb = TEXT_BODY
    p_hand.space_after = Pt(16)

    # Link button box
    p_btn = ctf.add_paragraph()
    p_btn.text = "🌐 Direct Platform Link (GitHub Pages):"
    p_btn.font.name = "Segoe UI"
    p_btn.font.size = Pt(10.5)
    p_btn.font.bold = True
    p_btn.font.color.rgb = TEXT_TITLE
    p_btn.space_after = Pt(4)

    p_url = ctf.add_paragraph()
    p_url.text = "https://wititgithub.github.io/fth-d365-fo-copilot-deck/"
    p_url.font.name = "Segoe UI"
    p_url.font.size = Pt(10)
    p_url.font.bold = True
    p_url.font.color.rgb = ACCENT_SKY
    p_url.space_after = Pt(14)

    p_sub_cue = ctf.add_paragraph()
    p_sub_cue.text = "💡 Host Guidance:\nClick the live link or switch to the browser window to start the 12-slide interactive tour."
    p_sub_cue.font.name = "Segoe UI"
    p_sub_cue.font.size = Pt(9.5)
    p_sub_cue.font.color.rgb = TEXT_MUTED

    s4.notes_slide.notes_text_frame.text = (
        "【English Executive Host Script - Slide 4: Agenda & Live Demonstration Handover】\n\n"
        "\"Looking ahead to today’s session, we have prepared a comprehensive 12-slide Live Interactive Solution Pitch "
        "that demonstrates the actual production-ready capabilities:\n\n"
        "We will walk through the official Microsoft Copilot Studio multi-agent architecture, explore our top five Thai localization "
        "use cases—from AP Invoice Intelligence to Continuous Reconciliation—and outline our practical 8-week POC delivery roadmap.\n\n"
        "Without further ado, I would now like to invite our executive team to transition directly into the live interactive platform "
        "to experience the future of Dynamics 365 and Copilot AI firsthand. Let us begin.\"\n\n"
        "----------------------------------------------------------------------\n"
        "【บทพูดภาษาไทยสำหรับพิธีกร - สไลด์ที่ 4: สรุปหัวข้อและส่งต่อเข้าสู่ Live Interactive Deck】\n\n"
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
        print(f"Generated PowerPoint Deck (White Theme) -> {p} ({os.path.getsize(p)//1024} KB)")

if __name__ == "__main__":
    build_presentation()
