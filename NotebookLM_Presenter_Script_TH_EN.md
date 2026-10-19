# 🎙️ FTH x D365 F&O x Copilot Studio: Executive Pitch Script & NotebookLM Pack (EN / TH)

เอกสารนี้ประกอบด้วย:
1. **Prompt คำสั่งสำหรับ Google NotebookLM** (เพื่อสร้างรายการ Podcast พิธีกรคู่แบบตื่นเต้น มีไฟ ทั้งภาษาอังกฤษและภาษาไทย)
2. **บทพูดพิธีกรรายสไลด์ (Slide-by-Slide Presenter Script)** ทั้งภาษาอังกฤษ (Simple, Energetic English) และภาษาไทย (ตื่นเต้น เป็นกันเอง กระชับ หน้าละไม่เกิน 1 นาที)

---

## 🎧 ส่วนที่ 1: คำสั่ง Custom Prompt สำหรับใส่ใน NotebookLM (Audio Overview)

> [!TIP]
> **วิธีใช้งานใน Google NotebookLM:**
> 1. อัปโหลดไฟล์นี้ (และรูปภาพทั้ง 2 ภาพของคุณ) เข้าไปในสมุดบันทึก (Notebook) บนเว็บ [notebooklm.google.com](https://notebooklm.google.com)
> 2. ในกรอบ **Audio Overview (Deep Dive Conversation)** กดปุ่ม **Customize**
> 3. ก๊อปปี้ Prompt ด้านล่างนี้ใส่ลงไป (เลือกภาษาอังกฤษ หรือ ภาษาไทย ตามต้องการ) แล้วกด **Generate**

### 🇬🇧 NotebookLM Prompt (English Version)
```text
Act as two super-energetic, friendly, and inspiring innovation hosts presenting an executive pitch to Fujitsu Thailand (FTH) leadership. 
Keep the English very simple, clear, punchy, and exciting! Avoid overly dense jargon.
Walk through our 12-slide pitch for "D365 Finance & Operations Thailand Localization powered by Microsoft Copilot AI":
1. Hook the audience: Thailand finance is transforming with AI while keeping people 100% in control.
2. Highlight the month-end pain: Manual PDF typing, 13-digit Tax ID checks, 5-digit branch codes, 7% VAT, and WHT errors discovered too late.
3. Explain the Microsoft AI Powerhouse: Copilot Studio + Azure AI + D365 F&O working together securely.
4. Briefly overview the Top 5 AI Use Cases for Thailand, and zoom into our #1 Quick Win POC: AP Invoice Intelligence.
5. Emphasize why Azure AI Document Intelligence v4.0 + Custom Model (trained on just 5-10 samples) solves the Thai language & THB challenge effortlessly.
6. Reassure leadership on safety: Deterministic rules check the math (Modulo 11 Tax ID, 7% VAT), and there is ZERO auto-posting—a human accountant always approves Drafts.
7. Share the exciting numbers: Target >=80% accuracy, >=70% faster processing, $0 software cost for the 4-week POC (using Azure Free Tier), and only ~0.35 THB per page in production!
End with a high-energy call to action uniting FTH, D365 F&O, and Microsoft Copilot Studio!
```

### 🇹🇭 NotebookLM Prompt (เวอร์ชันภาษาไทย)
```text
ช่วยดำเนินรายการด้วยน้ำเสียงที่ตื่นเต้น มีไฟ ดูทันสมัย แต่เป็นกันเองและเข้าใจง่าย เพื่อนำเสนอโครงการขออนุมัติจากผู้บริหารของ Fujitsu Thailand (FTH)
เล่าเรื่องตามโครงสร้างสไลด์ 12 หน้าของโครงการ "D365 Finance & Operations Thailand Localization ด้วย Microsoft Copilot AI":
1. เปิดตัวให้น่าตื่นเต้นว่าเรากำลังยกระดับงานบัญชีและการเงินของไทยด้วย AI โดยที่คนยังเป็นผู้ควบคุม 100% (People in Control)
2. ชี้ให้เห็นปัญหาคลาสสิกตอนปิดงบ: ต้องคีย์ใบกำกับภาษี PDF ด้วยมือ เช็คเลข 13 หลัก สาขา 5 หลัก VAT 7% และหัก ณ ที่จ่าย กว่าจะรู้ว่าผิดก็ตอนยื่น ภ.พ.30 หรือ ภ.ง.ด.3/53
3. อธิบายภาพรวม Copilot Studio + Azure AI + D365 F&O และ 5 Use Cases หลักของไทย
4. เจาะลึก POC แรกที่เราจะเริ่มทันที: AP Invoice Intelligence โดยใช้ความล้ำของ Azure AI Document Intelligence v4.0 และ Custom Model ที่ใช้ตัวอย่างแค่ 5-10 ใบก็จำฟอร์มใบแจ้งหนี้ไทยได้แม่นยำ
5. ย้ำความมั่นใจให้ผู้บริหาร: กฎภาษีใช้ Deterministic Rules คำนวณเป๊ะ และปลอดภัย 100% เพราะ AI สร้างแค่ Draft Pending Invoice เท่านั้น ไม่มี Auto-post เด็ดขาด
6. ปิดท้ายด้วยความคุ้มค่า: POC 4 สัปดาห์ใช้งบซอฟต์แวร์เพิ่ม 0 บาท (ใช้ Free Tier 500 หน้า/เดือน) และตอนใช้งานจริงตกหน้าละแค่ 35 สตางค์! ชวนผู้บริหารกดอนุมัติเพื่อสร้างปรากฏการณ์ร่วมกันระหว่าง FTH, D365 F&O และ Microsoft Copilot Studio!
```

---

## 🎤 ส่วนที่ 2: บทพูดพิธีกรประจำสไลด์ (12-Slide Dual-Language Script)
*(บทพูดชุดนี้ถูกฝังอยู่ใน Interactive Slide Deck พร้อมปุ่มสลับภาษา 🇹🇭/🇬🇧 และปุ่มกดฟังเสียงพากย์อัตโนมัติในตัวสไลด์แล้ว)*

### Slide 1: The Future of Finance in Thailand (0:45)
* **🇬🇧 EN:** "Hello everyone! Welcome to the future of finance at FTH! Today, we are going to show you how combining D365 Finance & Operations with Microsoft Copilot AI will transform Thai accounting forever. We’re talking about working faster, staying 100% tax-compliant, and keeping our people firmly in control. Let’s dive in!"
* **🇹🇭 TH:** "สวัสดีครับทุกท่าน! ยินดีต้อนรับสู่อนาคตของงานการเงินยุคใหม่ของ FTH ครับ! วันนี้เราจะพาทุกท่านมาดูว่า เมื่อเรานำ D365 Finance & Operations มาผสานพลังกับ Microsoft Copilot AI มันจะพลิกโฉมงานบัญชีและภาษีไทยไปตลอดกาลได้อย่างไร งานจะเร็วขึ้น ถูกต้องตามกฎสรรพากร 100% และที่สำคัญ คนของเรายังเป็นผู้ควบคุมทุกขั้นตอน ไปชมกันเลยครับ!"

### Slide 2: The Month-End Pain Point (0:50)
* **🇬🇧 EN:** "Let’s be honest—month-end closing in Thailand is tough! Every day, our AP team reads hundreds of PDF invoices by hand. They manually check 13-digit Tax IDs, 5-digit branch codes, PO numbers, 7% VAT, and withholding tax. One tiny typo means big headaches during tax filing. It’s time to take this robotic work off our team’s shoulders!"
* **🇹🇭 TH:** "ต้องยอมรับความจริงกันก่อนครับว่า ช่วงปิดงบสิ้นเดือนของไทยเรานั้นหนักหน่วงมาก! ทุกวันทีมบัญชีต้องเปิดอ่านไฟล์ PDF ใบกำกับภาษีนับร้อยใบด้วยตาเปล่า ต้องคอยเช็คเลขผู้เสียภาษี 13 หลัก รหัสสาขา 5 หลัก เลข PO ยอด VAT 7% และภาษีหัก ณ ที่จ่าย พลาดแค่ตัวเดียวก็ปวดหัวยาวตอนยื่นแบบ ถึงเวลาแล้วครับที่เราจะปลดล็อกงานซ้ำๆ เหล่านี้ออกจากบ่าของทีมงานเรา!"

### Slide 3: Meet Our Microsoft AI Powerhouse (0:55)
* **🇬🇧 EN:** "And here is the game-changer! Look at Microsoft’s official Copilot Studio blueprint. On the left, we feed it our Thai tax manuals and connect directly to D365 F&O via Dataverse and APIs. In the center, smart AI agents orchestrate the workflow. And on the right, our team interacts right inside Microsoft Teams and D365—all protected by enterprise-grade Microsoft security!"
* **🇹🇭 TH:** "และนี่คือพระเอกของเราครับ! ดูจากพิมพ์เขียวทางการของ Microsoft Copilot Studio ได้เลย ด้านซ้ายเราป้อนความรู้คู่มือภาษีไทยและเชื่อมตรงเข้ากับข้อมูล D365 F&O ผ่าน Dataverse และ API ตรงกลางคือกองทัพ AI Agent ที่ช่วยกันคิดและจัดการงาน ส่วนด้านขวา ทีมงานสามารถสั่งงานผ่าน Teams หรือหน้าจอ D365 ได้ทันที ทั้งหมดนี้อยู่ภายใต้ระบบความปลอดภัยสูงสุดของ Microsoft ครับ!"

### Slide 4: Top 5 AI Use Cases for Thailand (1:00)
* **🇬🇧 EN:** "We’ve mapped out the Top 5 AI Use Cases specifically for Thailand Localization on D365 F&O! Number 1: AP Invoice Intelligence. Number 2: Thai Tax Compliance Copilot for VAT and WHT. Number 3: e-Tax Invoice Control. Number 4: Continuous Subledger Reconciliation. And Number 5: A 24/7 Finance & Tax Knowledge Assistant. Everything connects straight into D365 F&O and Fujitsu Thai Localization!"
* **🇹🇭 TH:** "เราวางพิมพ์เขียว 5 สุดยอด Use Cases สำหรับกฎหมายภาษีไทยบน D365 F&O ไว้ครบวงจรแล้วครับ! 1. อ่านและตรวจสอบใบแจ้งหนี้อัตโนมัติ 2. ผู้ช่วยตรวจภาษี VAT และ WHT ก่อนยื่นสรรพากร 3. ระบบคุมคุณภาพ e-Tax Invoice 4. AI กระทบยอดทางบัญชีอย่างต่อเนื่อง และ 5. ผู้ช่วยถาม-ตอบระเบียบการเงินและภาษีไทย ทุกส่วนเชื่อมต่อกับแกนกลาง D365 F&O และ Fujitsu Thai Localization อย่างสมบูรณ์แบบ!"

### Slide 5: Our First Big Win (POC): AP Invoice Intelligence (0:55)
* **🇬🇧 EN:** "Where should we start for the fastest return? Use Case #1: AP Invoice Intelligence! Watch how smooth this official flow is: A Thai or English invoice arrives. Document AI extracts the header and lines, checks the confidence score, performs a 3-way match against the PO, Goods Receipt, and VAT setup in D365, and creates a ready-to-review Draft Invoice in seconds!"
* **🇹🇭 TH:** "คำถามคือ เราจะเริ่มตรงไหนให้เห็นผลเร็วและคุ้มที่สุด? คำตอบคือข้อที่ 1 ครับ: AP Invoice Intelligence! ดู Flow การทำงานนี้สิครับ ทันทีที่ใบแจ้งหนี้ภาษาไทยหรืออังกฤษเข้ามา AI จะสกัดข้อมูลหัวเอกสารและรายการสินค้า ตรวจค่าความมั่นใจ วิ่งไปเช็ค 3-Way Match กับใบสั่งซื้อ ใบรับของ และรหัสภาษีใน D365 จากนั้นสร้างเป็น Draft Invoice รอให้คนตรวจได้ในพริบตาเดียว!"

### Slide 6: The Secret Sauce: Azure AI Document Intelligence v4.0 (0:55)
* **🇬🇧 EN:** "Now you might ask: Can AI really read complex Thai fonts and Thai Baht accurately? Standard OCR struggles, yes—but Azure AI Document Intelligence version 4.0 natively understands Thai and THB! Even better, with a Custom Model, we just label 5 to 10 sample invoices in Azure Studio, and the AI learns our exact vendor layouts with pinpoint precision. And it’s 100% Microsoft-compliant!"
* **🇹🇭 TH:** "หลายท่านอาจสงสัยว่า AI จะอ่านฟอนต์ภาษาไทยและสกุลเงินบาทได้แม่นจริงหรือ? ถ้าเป็นตัวมาตรฐานทั่วไปอาจจะยากครับ แต่ด้วย Azure AI Document Intelligence เวอร์ชัน 4.0 ตัวใหม่ล่าสุด มันรองรับภาษาไทยเต็มรูปแบบ! ยิ่งไปกว่านั้น เราสามารถสร้าง Custom Model โดยใช้ตัวอย่างใบกำกับภาษีแค่ 5-10 ใบมาตีกรอบสอน AI ให้จำฟอร์มคู่ค้าของเราได้แม่นยำสุดๆ โดยไม่ผิดข้อบังคับใดๆ ของ D365 เลยครับ!"

### Slide 7: Smart Guardrails: Deterministic Rules + Human in the Loop (0:55)
* **🇬🇧 EN:** "For finance, accuracy and control are non-negotiable. That’s why we never let AI 'guess' tax laws! We use strict Deterministic Rules: Modulo-11 math checks on 13-digit Tax IDs, exact 5-digit branch validation, and 7% VAT tolerance checks. Most importantly: ZERO auto-posting! The AI only creates a Draft. A human accountant always clicks Approve!"
* **🇹🇭 TH:** "สำหรับงานการเงิน ความถูกต้องคือสิ่งสูงสุดครับ เราจึงไม่ปล่อยให้ AI คิดกฎภาษีเองเด็ดขาด! แต่เราใช้ Deterministic Rules หรือสูตรคำนวณที่ตายตัว เช่น เช็คสูตร Modulo-11 ของเลข 13 หลัก เช็ครหัสสาขา 5 หลัก และคำนวณ VAT 7% อย่างเป๊ะๆ และกฎเหล็กของเราคือ ไม่มีการโพสต์บัญชีอัตโนมัติเด็ดขาด! AI สร้างได้แค่ Draft เท่านั้น นักบัญชีตัวจริงต้องเป็นคนกดอนุมัติเสมอครับ!"

### Slide 8: Future Roadmap: Phase 2 & Beyond (0:50)
* **🇬🇧 EN:** "Once our AP Invoice POC succeeds, look at where we go next! Phase 2 launches the Thai Tax Compliance Copilot—pre-validating ภ.พ.30 and ภ.ง.ด.3/53 with built-in Rule Versioning ready for the Revenue Department’s new 2026 formats—plus our Knowledge Q&A Agent. Phase 3 unlocks e-Tax XML error translation and continuous month-end reconciliation!"
* **🇹🇭 TH:** "และเมื่อ POC ใบแจ้งหนี้ของเราสำเร็จ ดูสเต็ปต่อไปที่เราจะขยายผลสิครับ! เฟส 2 เราจะเปิดใช้งานผู้ช่วยตรวจภาษี ภ.พ.30 และ ภ.ง.ด.3/53 ล่วงหน้า ซึ่งรองรับฟอร์มสรรพากรยุคใหม่ปี 2569 ได้ทันที พร้อมระบบแชทบอทถาม-ตอบภาษี และเฟส 3 ขยายไปสู่งานแปล Error ของ e-Tax และการกระทบยอดบัญชีอัตโนมัติครับ!"

### Slide 9: How We Measure Success (POC Scorecard) (0:50)
* **🇬🇧 EN:** "We don’t just hope for success—we measure it with clear numbers! Using 50 real test invoices across Thai, English, and mixed formats, our target is at least 80% overall extraction accuracy, 60% straight-through processing to Draft with zero manual typing, over 70% time saved per invoice, and a strict 100% record of zero unauthorized auto-posting!"
* **🇹🇭 TH:** "เราไม่ได้ทำแค่ให้ดูล้ำ แต่เราวัดผลด้วยตัวเลขที่ชัดเจนครับ! เราจะทดสอบด้วยเอกสารจริง 50 ฉบับ ทั้งไทย อังกฤษ และแบบผสม โดยมีเป้าหมายคือ ความแม่นยำรวมต้องไม่ต่ำกว่า 80%, เอกสารไหลเข้าเป็น Draft โดยไม่ต้องแก้เลยอย่างน้อย 60%, ลดเวลาทำงานต่อใบลงกว่า 70% และต้องไม่มีการหลุดโพสต์เองโดยพลการ 100% เต็มครับ!"

### Slide 10: Budget & Investment: Almost Zero for POC! (0:50)
* **🇬🇧 EN:** "Here is the best part for executives: How much extra software budget do we need for this POC? Zero dollars! Azure AI gives us 500 free pages every month, and D365 OData and Dataverse Virtual Entities are already included in our license! Even when we go live in production, Azure AI costs just 10 dollars per 1,000 pages—that’s only 35 satang per invoice!"
* **🇹🇭 TH:** "และนี่คือข่าวดีที่สุดสำหรับผู้บริหารครับ: โครงการ POC นี้ต้องของบซื้อซอฟต์แวร์เพิ่มเท่าไหร่? คำตอบคือ 0 บาทครับ! เพราะ Azure AI มีโควต้าให้อ่านฟรีเดือนละ 500 หน้า ส่วน OData และ Dataverse ก็รวมอยู่ใน License D365 เดิมของเราแล้ว! และแม้แต่ตอนขึ้นใช้งานจริง ค่าอ่านเอกสารของ Azure AI ก็ถูกมาก ตกเพียงหน้าละ 35 สตางค์เท่านั้นเองครับ!"

### Slide 11: 4-Week POC Action Plan (0:45)
* **🇬🇧 EN:** "Our execution plan is fast and focused—just 4 weeks! Week 1: Complete internal AI RMS registration and collect 50 masked sample invoices. Week 2: Configure Azure AI v4.0 and train our Thai Custom Model. Week 3: Connect the flow to our D365 Sandbox and run validation rules. Week 4: Present the Scorecard results for your Go/No-Go decision!"
* **🇹🇭 TH:** "แผนการลงมือทำของเรารวดเร็วและชัดเจนใน 4 สัปดาห์ครับ! สัปดาห์ที่ 1 ลงทะเบียน AI RMS และเตรียมเอกสารทดสอบ 50 ใบ สัปดาห์ที่ 2 ตั้งค่า Azure AI v4.0 และสอน Custom Model ภาษาไทย สัปดาห์ที่ 3 เชื่อมเข้า D365 Sandbox เพื่อทดสอบกฎการตรวจสอบ และสัปดาห์ที่ 4 สรุปผลคะแนน Scorecard เพื่อตัดสินใจไปต่อทันทีครับ!"

### Slide 12: Finale – Uniting FTH, D365 F&O & Microsoft Copilot Studio (0:55)
* **🇬🇧 EN:** "Look at this synergy in motion! Fujitsu Thailand—FTH—joining forces with Microsoft Dynamics 365 Finance & Operations and Microsoft Copilot Studio! Zero extra POC cost, 100% safe guardrails, and massive productivity gains for our people. Give us the green light for this 4-week POC, and let’s lead the future of AI-powered Finance in Thailand together! Thank you!"
* **🇹🇭 TH:** "ดูพลังของการผสานเทคโนโลยีตรงหน้านี้สิครับ! เมื่อ Fujitsu Thailand หรือ FTH ของเรา รวมพลังกับ Dynamics 365 Finance & Operations และ Microsoft Copilot Studio! งบซอฟต์แวร์เริ่มต้น 0 บาท ปลอดภัยตามหลักธรรมาภิบาล 100% และช่วยยกระดับการทำงานของทีมเราได้อย่างก้าวกระโดด ขอไฟเขียวอนุมัติ POC 4 สัปดาห์นี้ แล้วมาสร้างปรากฏการณ์ AI แห่งอนาคตไปด้วยกันนะครับ ขอบคุณครับ!"
