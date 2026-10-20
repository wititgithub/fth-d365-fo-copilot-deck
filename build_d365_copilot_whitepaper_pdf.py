import asyncio
import os
import sys
from playwright.async_api import async_playwright

HTML_PATH = r"c:\FTH\FTH-D365_FO\D365_Copilot_Deep_UseCases_Whitepaper.html"
OUT_PDF_PATHS = [
    r"c:\FTH\FTH-D365_FO\D365_Copilot_Deep_UseCases_Whitepaper.pdf",
    r"c:\FTH\FTH-D365_FO\assets\D365_Copilot_Deep_UseCases_Whitepaper.pdf",
    r"C:\Users\witit\.gemini\antigravity\brain\7bc4ceac-b79a-4881-9938-a5db0d7782a2\D365_Copilot_Deep_UseCases_Whitepaper.pdf",
]

def build_html_content():
    return """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <title>D365 Copilot AI Deep Research Synthesis - Top 5 Strategic Use Cases (FTH)</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Sarabun:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
  <style>
    @page {
      size: A4 portrait;
      margin: 10mm 12mm 12mm 12mm;
    }
    *, *::before, *::after {
      box-sizing: border-box;
    }
    body {
      font-family: 'Plus Jakarta Sans', 'Sarabun', 'Leelawadee UI', Tahoma, sans-serif;
      color: #0f172a;
      background-color: #ffffff;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
      line-height: 1.42;
      margin: 0;
      padding: 0;
    }
    .page-container {
      width: 100%;
      min-height: 270mm;
      max-height: 270mm;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      page-break-after: always;
      break-after: page;
      padding: 3mm 2mm;
    }
    .page-container:last-child {
      page-break-after: auto;
      break-after: auto;
    }
    .card-champion {
      border: 1px solid #cbd5e1;
      border-radius: 12px;
      padding: 12px 16px;
      background: #ffffff;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
      margin-bottom: 12px;
    }
    .card-champion:last-child {
      margin-bottom: 0;
    }
  </style>
</head>
<body class="text-slate-900 text-xs">

  <!-- ==================== PAGE 1: COVER PAGE ==================== -->
  <div class="page-container">
    <div>
      <!-- Top Branding Bar -->
      <div class="flex items-center justify-between border-b border-slate-200 pb-3 mb-4">
        <div class="flex items-center gap-3">
          <div class="px-3 py-1 bg-red-600 text-white font-extrabold text-[11px] tracking-wider rounded uppercase">
            FUJITSU THAILAND
          </div>
          <span class="text-slate-300">|</span>
          <span class="text-[11px] font-bold text-slate-600 uppercase tracking-wide">Business Applications & AI Advisory</span>
        </div>
        <div class="flex items-center gap-2">
          <span class="text-[11px] font-semibold text-slate-500">In Partnership with</span>
          <span class="px-2.5 py-0.5 rounded bg-sky-50 text-sky-700 border border-sky-200 font-bold text-[11px]">Microsoft Dynamics 365</span>
        </div>
      </div>

      <!-- Main Title Block -->
      <div class="space-y-2 max-w-3xl mb-4">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-900 text-white text-[10px] font-bold uppercase tracking-wider">
          <span class="w-2 h-2 rounded-full bg-red-500 animate-pulse"></span>
          Deep Research Synthesis • Executive Blueprint 2026
        </div>

        <h1 class="text-3xl font-black text-slate-900 tracking-tight leading-tight">
          Beyond Standard: Unlocking D365 with Advanced Copilot AI
        </h1>
        <p class="text-base font-bold text-sky-700">
          การก้าวข้ามข้อจำกัด Dynamics 365 สู่ระบบอัจฉริยะ: สรุปผลการสังเคราะห์เชิงลึก Top 5 Strategic Use Cases
        </p>
        <p class="text-[11px] text-slate-600 leading-relaxed font-normal">
          รายงานผลการเปรียบเทียบระหว่าง <strong>Deep Research ล่าสุด</strong> และ <strong>ข้อจำกัดเชิงสถาปัตยกรรม ERP</strong> คัดกรองสิ่งที่มีใน D365 Standard ออก เพื่อคัดสรรเฉพาะ <strong>Top 5 Use Cases ที่มีความเป็นไปได้สูงสุด (Highest Feasibility) และคุ้มค่าการลงทุน (Highest ROI)</strong> สำหรับผู้บริหาร
        </p>
      </div>

      <!-- Hero Visual Box -->
      <div class="mb-4 rounded-xl overflow-hidden border border-slate-200 shadow-sm bg-slate-50">
        <img src="assets/copilot_d365_hero_fluent.jpg" alt="Copilot D365 Hero" class="w-full h-44 object-cover object-center">
      </div>

      <!-- Top 5 Champion Highlights Grid -->
      <div class="grid grid-cols-5 gap-2 mb-3">
        <div class="p-2.5 rounded-xl bg-sky-50/90 border border-sky-200 text-center">
          <div class="text-[10px] font-black text-sky-800 uppercase mb-0.5">🏆 #1 SCM</div>
          <div class="font-extrabold text-slate-900 text-[11px] mb-0.5">Vendor PO Email</div>
          <p class="text-[9px] text-slate-600">รับ-ส่งเมลคู่ค้า ปรับ PO อัตโนมัติ</p>
        </div>
        <div class="p-2.5 rounded-xl bg-purple-50/90 border border-purple-200 text-center">
          <div class="text-[10px] font-black text-purple-800 uppercase mb-0.5">🏆 #2 Production</div>
          <div class="font-extrabold text-slate-900 text-[11px] mb-0.5">MRP Black-Box</div>
          <p class="text-[9px] text-slate-600">ถอดรหัสคอขวด วางแผน OT คุ้มทุน</p>
        </div>
        <div class="p-2.5 rounded-xl bg-amber-50/90 border border-amber-200 text-center">
          <div class="text-[10px] font-black text-amber-800 uppercase mb-0.5">🏆 #3 Inventory</div>
          <div class="font-extrabold text-slate-900 text-[11px] mb-0.5">Stock Anomaly</div>
          <p class="text-[9px] text-slate-600">สืบหาสต็อกดิฟจาก Bin ใกล้เคียง</p>
        </div>
        <div class="p-2.5 rounded-xl bg-rose-50/90 border border-rose-200 text-center">
          <div class="text-[10px] font-black text-rose-800 uppercase mb-0.5">🏆 #4 Quality</div>
          <div class="font-extrabold text-slate-900 text-[11px] mb-0.5">Scrap &amp; AAR</div>
          <p class="text-[9px] text-slate-600">หาสาเหตุของเสีย บันทึกบทเรียน</p>
        </div>
        <div class="p-2.5 rounded-xl bg-emerald-50/90 border border-emerald-200 text-center">
          <div class="text-[10px] font-black text-emerald-800 uppercase mb-0.5">🏆 #5 Risk</div>
          <div class="font-extrabold text-slate-900 text-[11px] mb-0.5">Supply Sentinel</div>
          <p class="text-[9px] text-slate-600">เตือนท่าเรือดีเลย์ สลับเจ้าล่วงหน้า</p>
        </div>
      </div>
    </div>

    <!-- Metadata Footer of Cover Page -->
    <div class="border-t border-slate-200 pt-2 flex items-center justify-between text-[10px] text-slate-500">
      <div>
        <span class="font-bold text-slate-800">Fujitsu (Thailand) Co., Ltd. (FTH)</span> | Enterprise AI Solution Practice
      </div>
      <div>
        <span>Ref: <strong>FTH-D365-AI-TOP5-2026</strong></span> • <span>October 2026</span>
      </div>
    </div>
  </div>

  <!-- ==================== PAGE 2: COMPARATIVE SYNTHESIS & ARCHITECTURE ==================== -->
  <div class="page-container">
    <div>
      <!-- Section Title -->
      <div class="flex items-center justify-between border-b-2 border-slate-900 pb-1.5 mb-3">
        <div>
          <span class="text-[10px] font-black tracking-widest text-red-600 uppercase">Executive Gap Analysis</span>
          <h2 class="text-base font-black text-slate-900">1. การวิเคราะห์สังเคราะห์: Deep Research vs. D365 Standard ล่าสุด</h2>
        </div>
        <div class="text-right">
          <span class="px-2.5 py-0.5 bg-slate-100 rounded text-[10px] font-bold text-slate-600">Feasibility &amp; Value Filter</span>
        </div>
      </div>

      <p class="text-[11px] text-slate-700 leading-relaxed mb-2.5">
        จากการวิเคราะห์เชิงเปรียบเทียบระหว่างเอกสาร Deep Research และข้อเท็จจริงใน D365 เวอร์ชันล่าสุด เราได้ทำการ <strong>คัดกรองฟังก์ชันที่มีอยู่แล้วใน Standard ออก</strong> เพื่อไม่ให้เกิดการลงทุนซ้ำซ้อน และมุ่งเน้นเฉพาะจุดที่ต้องใช้ Custom Copilot Studio แก้ไข Pain Point ที่ยังไม่มีใครแก้ได้:
      </p>

      <!-- Comparison Matrix Table -->
      <div class="border border-slate-200 rounded-xl overflow-hidden mb-3 shadow-xs">
        <table class="w-full text-[10px] text-left">
          <thead class="bg-slate-900 text-white font-bold uppercase text-[9px]">
            <tr>
              <th class="p-2 w-1/4">หมวดหมู่และฟังก์ชัน</th>
              <th class="p-2 w-3/8 bg-slate-800 text-slate-300">สถานะใน D365 Standard (อัปเดตล่าสุด)</th>
              <th class="p-2 w-3/8 bg-red-950/80 text-red-200">กลยุทธ์การสังเคราะห์ของ Fujitsu (FTH Selection)</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-200">
            <tr class="bg-white">
              <td class="p-2 font-bold text-slate-900">1. การถามยอดสต็อกคงเหลือ (On-Hand Query)</td>
              <td class="p-2 text-slate-500">❌ มีแล้วใน <strong>Inventory Visibility Add-in Copilot</strong> สามารถแชตถามยอดสต็อกข้ามสาขาได้</td>
              <td class="p-2 text-slate-600 bg-slate-50"><strong>ตัดออก:</strong> ไม่ต้องสร้างซ้ำ ให้ใช้ Standard ของ Microsoft ได้เลย</td>
            </tr>
            <tr class="bg-slate-50/40">
              <td class="p-2 font-bold text-slate-900">2. การพยากรณ์ความต้องการ (Demand Forecast)</td>
              <td class="p-2 text-slate-500">❌ มีแล้วใน <strong>Demand Planning App (Preview/GA)</strong> ที่มี Copilot อธิบายเทรนด์ยอดขาย</td>
              <td class="p-2 text-slate-600 bg-slate-50"><strong>ตัดออก:</strong> แนะนำให้เชื่อมต่อกับแอปใหม่ของ Microsoft แทนการทำ Custom</td>
            </tr>
            <tr class="bg-white">
              <td class="p-2 font-bold text-slate-900">3. สรุปรายงาน Dashboard ผู้บริหาร (Reporting)</td>
              <td class="p-2 text-slate-500">❌ มีแล้วใน <strong>Microsoft Fabric / Power BI Copilot</strong> สรุป KPI กราฟิกได้ทันที</td>
              <td class="p-2 text-slate-600 bg-slate-50"><strong>ตัดออก:</strong> ให้ใช้ Standard Power BI Copilot สำหรับการอ่านสรุปภาพรวม</td>
            </tr>
            <tr class="bg-emerald-50/40">
              <td class="p-2 font-bold text-emerald-950">4. การจัดการอีเมลและเอกสารซัพพลายเออร์</td>
              <td class="p-2 text-emerald-800">⚠️ Standard ทำได้แค่สรุป PO ในระบบ แต่ <strong>อ่านอีเมล/PDF ภายนอกเพื่อแก้ PO ไม่ได้</strong></td>
              <td class="p-2 text-emerald-950 font-bold bg-emerald-100/50"><strong>✅ คัดเลือกเป็น #1:</strong> เป็น Pain Point ใหญ่สุดของจัดซื้อ คุ้มค่าและทำได้จริง 100%</td>
            </tr>
            <tr class="bg-purple-50/40">
              <td class="p-2 font-bold text-purple-950">5. การถอดรหัสกล่องดำ MRP &amp; คอขวด</td>
              <td class="p-2 text-purple-800">⚠️ Planning Optimization คำนวณเร็วแต่เป็นกล่องดำ <strong>ไม่อธิบายเหตุผลหรือทางเลือก OT</strong></td>
              <td class="p-2 text-purple-950 font-bold bg-purple-100/50"><strong>✅ คัดเลือกเป็น #2:</strong> เป็นจุดติดขัดอันดับ 1 ของโรงงาน สร้างความต่างให้ FTH สูงสุด</td>
            </tr>
            <tr class="bg-amber-50/40">
              <td class="p-2 font-bold text-amber-950">6. การสืบหาสาเหตุสต็อกดิฟเชิงลึก</td>
              <td class="p-2 text-amber-800">⚠️ Counting Journal บอกได้แค่ยอดดิฟ แต่ <strong>ไม่สืบหาความผิดปกติของ Bin หรือประวัติสแกน</strong></td>
              <td class="p-2 text-amber-950 font-bold bg-amber-100/50"><strong>✅ คัดเลือกเป็น #3:</strong> ลดเวลาตรวจสอบสต็อกของคลังสินค้าจากวันเหลือนาที</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Architecture Framework Blueprint -->
      <div class="p-3 rounded-xl bg-slate-900 text-white border border-slate-800 shadow-sm">
        <div class="flex items-center justify-between mb-2 border-b border-slate-800 pb-1">
          <span class="text-[10px] font-black tracking-wider text-sky-400 uppercase">Fujitsu 3-Layer Copilot Implementation Architecture</span>
          <span class="text-[9px] text-slate-400">Enterprise Security Boundary • Human-in-the-Loop Sign-off</span>
        </div>
        <div class="grid grid-cols-3 gap-2 text-center text-[9px]">
          <div class="p-2 rounded-lg bg-slate-800 border border-slate-700">
            <div class="font-bold text-emerald-400 uppercase mb-0.5">1. Enterprise Data Layer</div>
            <div class="font-extrabold text-white text-[11px] mb-0.5">Dataverse &amp; External Feeds</div>
            <p class="text-slate-300">D365 SCM Entities • Vendor Emails &amp; PDFs • IoT Shop Floor Data • News &amp; Weather Feeds</p>
          </div>
          <div class="p-2 rounded-lg bg-slate-800 border border-sky-500/50">
            <div class="font-bold text-sky-400 uppercase mb-0.5">2. Cognitive Agent Layer</div>
            <div class="font-extrabold text-white text-[11px] mb-0.5">Copilot Studio + Azure OpenAI</div>
            <p class="text-slate-300">GPT-4o Reasoning • Semantic Kernel • Domain Knowledge RAG • Multi-Step Orchestration</p>
          </div>
          <div class="p-2 rounded-lg bg-slate-800 border border-red-500/50">
            <div class="font-bold text-red-400 uppercase mb-0.5">3. Business Action Loop</div>
            <div class="font-extrabold text-white text-[11px] mb-0.5">D365 Business Events</div>
            <p class="text-slate-300">Draft PO Line Adjustments • Auto Inventory Counting Journals • Resequencing Triggers</p>
          </div>
        </div>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-1 text-[10px] text-slate-400 text-right">
      Section 1: Comparative Gap Analysis &amp; Architecture
    </div>
  </div>

  <!-- ==================== PAGE 3: CHAMPION USE CASES #1 & #2 ==================== -->
  <div class="page-container">
    <div>
      <!-- Section Header -->
      <div class="flex items-center justify-between border-b-2 border-slate-900 pb-1.5 mb-3">
        <div>
          <span class="text-[10px] font-black tracking-widest text-sky-700 uppercase">Strategic Champion Deep Dives</span>
          <h2 class="text-base font-black text-slate-900">2. เจาะลึก Champion Use Cases: อันดับ 1 และ อันดับ 2</h2>
        </div>
        <span class="px-2.5 py-0.5 bg-sky-50 text-sky-800 border border-sky-200 rounded-full text-[10px] font-bold">Priority Execution Phase</span>
      </div>

      <!-- CHAMPION #1 -->
      <div class="card-champion border-l-4 border-l-sky-500">
        <div class="flex items-center justify-between mb-1.5">
          <div class="flex items-center gap-2">
            <span class="px-2 py-0.5 rounded bg-sky-600 text-white font-black text-[10px]">CHAMPION #1</span>
            <h3 class="text-xs font-black text-slate-900">Unstructured Vendor Negotiation &amp; PO Schedule Reconciliation Copilot</h3>
          </div>
          <span class="text-[9px] font-bold text-sky-700 bg-sky-50 px-2 py-0.5 rounded border border-sky-200">SCM &amp; Procurement</span>
        </div>

        <div class="space-y-1.5 text-[11px] text-slate-700">
          <p>
            <strong class="text-slate-900">⚠️ ปัญหาคอขวดที่แท้จริง:</strong> ซัพพลายเออร์ส่วนใหญ่ไม่ยอมเข้าระบบ Vendor Portal ของ D365 แต่มักส่งอีเมลตอบกลับพร้อมไฟล์แนบ (PDF/Excel) หรือแชต แจ้งขอส่งของแยกงวด (Split-shipment), ขอเลื่อนวันส่ง, หรือขอปรับราคาวัตถุดิบบางรายการ ทำให้จัดซื้อต้องเปิดอ่านทีละฉบับแล้วมาคีย์แก้มือใน D365 PO วันละหลายสิบใบ เสี่ยงต่อข้อผิดพลาดและความล่าช้า
          </p>
          <p>
            <strong class="text-slate-900">❌ ข้อจำกัดของ Standard D365:</strong> Copilot ใน Standard ทำได้แค่สรุปข้อความใน PO ที่ถูกแก้แล้วในระบบ แต่ <em>ไม่สามารถเชื่อมต่อกล่องข้อความอีเมลภายนอกเพื่อสกัดข้อมูลและอัปเดตตาราง PO ใน D365 ได้เอง</em>
          </p>
          <div class="p-2 bg-sky-50/80 rounded-lg border border-sky-200">
            <strong class="text-sky-900 block mb-0.5">💡 สถาปัตยกรรม Copilot AI ที่พัฒนาขึ้น:</strong>
            <ol class="list-decimal list-inside space-y-0.5 text-slate-700 text-[10px]">
              <li><strong>Email &amp; PDF Ingestion:</strong> Power Automate ดักจับอีเมลและอินวอยซ์แนบจากคู่ค้า ส่งให้ Azure OpenAI แยกแยะวันส่งมอบและงวดที่ขอแบ่งส่ง</li>
              <li><strong>Production Impact Check:</strong> Copilot เชื่อมโยงกับตารางผลิตใน D365 เพื่อตรวจสอบว่าการส่งของช้ากระทบต่อใบสั่งผลิต (WO) ใดบ้าง</li>
              <li><strong>Autonomous Action &amp; Sign-off:</strong> Copilot ร่างแก้ไข Purchase Order Lines ใน D365 ทันที พร้อมร่างอีเมลตอบกลับยืนยันหรือขอต่อรองราคา ให้จัดซื้อกดยืนยันใน 1 คลิก</li>
            </ol>
          </div>
          <div class="flex items-center justify-between text-[10px] text-slate-600 pt-1">
            <span><strong>ผลลัพธ์ทางธุรกิจ (ROI):</strong> ลดเวลางานเอกสารจัดซื้อลง <strong>80%</strong>, ป้องกันไลน์ผลิตหยุดชะงักจากการรับของผิดงวด</span>
            <span class="font-bold text-sky-700 bg-white px-2 py-0.5 rounded border border-sky-200">สร้างเสร็จใน 6 สัปดาห์</span>
          </div>
        </div>
      </div>

      <!-- CHAMPION #2 -->
      <div class="card-champion border-l-4 border-l-purple-500">
        <div class="flex items-center justify-between mb-1.5">
          <div class="flex items-center gap-2">
            <span class="px-2 py-0.5 rounded bg-purple-600 text-white font-black text-[10px]">CHAMPION #2</span>
            <h3 class="text-xs font-black text-slate-900">MRP Planning Optimization "Black-Box" &amp; Bottleneck Resolution Explainer</h3>
          </div>
          <span class="text-[9px] font-bold text-purple-700 bg-purple-50 px-2 py-0.5 rounded border border-purple-200">Production &amp; MRP</span>
        </div>

        <div class="space-y-1.5 text-[11px] text-slate-700">
          <p>
            <strong class="text-slate-900">⚠️ ปัญหาคอขวดที่แท้จริง:</strong> ปัญหาอันดับ 1 ของ Community ผู้ใช้ D365 ทั่วโลกคือระบบ Master Planning (Planning Optimization) ทำงานแบบ <strong>"กล่องดำ (Black Box)"</strong> คำนวณแผนจัดซื้อ/ผลิตได้เร็ว แต่แพลนเนอร์ไม่เข้าใจเหตุผลว่า <em>ทำไมระบบถึงเลื่อนวันผลิตออเดอร์สำคัญออกไป 2 สัปดาห์? ติดคอขวดที่เครื่องจักรใด หรือติด Pegging ชิ้นส่วนตัวไหน?</em>
          </p>
          <p>
            <strong class="text-slate-900">❌ ข้อจำกัดของ Standard D365:</strong> Planning Optimization แสดงแค่รายการ Planned Orders ที่คำนวณเสร็จแล้ว แต่ไม่มีฟังก์ชันอธิบายเหตุผลเป็นภาษาคน และไม่มีการจำลอง Trade-off ทางเลือกในการแก้คอขวด
          </p>
          <div class="p-2 bg-purple-50/80 rounded-lg border border-purple-200">
            <strong class="text-purple-900 block mb-0.5">💡 สถาปัตยกรรม Copilot AI ที่พัฒนาขึ้น:</strong>
            <ol class="list-decimal list-inside space-y-0.5 text-slate-700 text-[10px]">
              <li><strong>Natural Language Query:</strong> แพลนเนอร์พิมพ์ถาม Copilot เป็นภาษาไทย: <em>"ทำไมออเดอร์ WO-9921 ถึงถูกเลื่อนวันเสร็จ?"</em></li>
              <li><strong>Pegging &amp; Capacity Reasoning:</strong> Copilot สแกน Multi-level BOM Pegging และภาระเครื่องจักร แล้วสรุป: <em>"ติดคอขวดที่เครื่องฉีดพลาสติก MC-02 และรอเรซินจาก PO-108"</em></li>
              <li><strong>Prescriptive What-If Simulator:</strong> เสนอทางเลือกเชิงรุก: <em>"หากอนุมัติ OT เครื่องจักร MC-02 จำนวน 4 ชม. ในวันเสาร์นี้ จะเลื่อนวันผลิตเสร็จเร็วขึ้นได้ 6 วัน โดยมีต้นทุน OT เพิ่มขึ้นประมาณ 8,500 บาท"</em></li>
            </ol>
          </div>
          <div class="flex items-center justify-between text-[10px] text-slate-600 pt-1">
            <span><strong>ผลลัพธ์ทางธุรกิจ (ROI):</strong> ลดชั่วโมงประชุม S&amp;OP และแพลนเนอร์ลง <strong>40%</strong>, เพิ่มอัตราการส่งมอบตรงเวลา (OTIF) สูงกว่า 95%</span>
            <span class="font-bold text-purple-700 bg-white px-2 py-0.5 rounded border border-purple-200">สร้างเสร็จใน 7 สัปดาห์</span>
          </div>
        </div>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-1 text-[10px] text-slate-400 text-right">
      Section 2: Strategic Champion Deep Dives (Part 1/2)
    </div>
  </div>

  <!-- ==================== PAGE 4: CHAMPION USE CASES #3 & #4 ==================== -->
  <div class="page-container">
    <div>
      <!-- Section Header -->
      <div class="flex items-center justify-between border-b-2 border-slate-900 pb-1.5 mb-3">
        <div>
          <span class="text-[10px] font-black tracking-widest text-amber-700 uppercase">Strategic Champion Deep Dives</span>
          <h2 class="text-base font-black text-slate-900">2. เจาะลึก Champion Use Cases: อันดับ 3 และ อันดับ 4</h2>
        </div>
        <span class="px-2.5 py-0.5 bg-amber-50 text-amber-800 border border-amber-200 rounded-full text-[10px] font-bold">Execution &amp; Operations</span>
      </div>

      <!-- CHAMPION #3 -->
      <div class="card-champion border-l-4 border-l-amber-500">
        <div class="flex items-center justify-between mb-1.5">
          <div class="flex items-center gap-2">
            <span class="px-2 py-0.5 rounded bg-amber-600 text-white font-black text-[10px]">CHAMPION #3</span>
            <h3 class="text-xs font-black text-slate-900">Intelligent Inventory Anomaly Detection &amp; Forensic Reconciliation Investigator</h3>
          </div>
          <span class="text-[9px] font-bold text-amber-800 bg-amber-50 px-2 py-0.5 rounded border border-amber-200">Inventory &amp; WMS</span>
        </div>

        <div class="space-y-1.5 text-[11px] text-slate-700">
          <p>
            <strong class="text-slate-900">⚠️ ปัญหาคอขวดที่แท้จริง:</strong> ในการนับสต็อก (Cycle Count) เมื่อเจอยอดต่าง (Variance) พนักงานคลังต้องเปิด Transaction History ไล่ดูประวัติรับ-จ่ายเป็นร้อยรายการเพื่อหาสาเหตุ ซึ่งใช้เวลาเป็นวันๆ และมักหาต้นตอไม่เจอ จนต้องปรับยอดตัดสต็อกทิ้ง (Write-off) ทำให้เกิดปัญหาสต็อกลม (Phantom Inventory)
          </p>
          <p>
            <strong class="text-slate-900">❌ ข้อจำกัดของ Standard D365:</strong> Counting Journal บันทึกได้แค่ผลต่างตัวเลข แต่ไม่สามารถวิเคราะห์พฤติกรรมการสแกน, ความผิดปกติของตำแหน่ง Bin, หรือประวัติบาร์โค้ดที่หน้าตาคล้ายกันได้
          </p>
          <div class="p-2 bg-amber-50/80 rounded-lg border border-amber-200">
            <strong class="text-amber-900 block mb-0.5">💡 สถาปัตยกรรม Copilot AI ที่พัฒนาขึ้น:</strong>
            <ol class="list-decimal list-inside space-y-0.5 text-slate-700 text-[10px]">
              <li><strong>Pattern &amp; Scan Forensics:</strong> Copilot สแกน Transaction logs, รหัสพนักงานผู้สแกน, ลำดับการเดินหยิบ และประวัติ License Plate (LP)</li>
              <li><strong>Spatial Bin Correlation:</strong> ตรวจสอบตำแหน่งทางกายภาพของ Bin ที่ติดกัน และความคล้ายกันของแพ็กเกจสินค้า</li>
              <li><strong>Root-Cause Summary:</strong> แจ้งผู้จัดการคลังทันที: <em>"พบสินค้าดิฟ -15 ชิ้น มีโอกาส 92% เกิดจากพนักงานสแกนสลับกับ SKU-402 ที่อยู่ Bin ติดกันเมื่อกะดึกวันที่ 18"</em> พร้อมร่างใบลดหนี้/ปรับยอดสต็อกให้อัตโนมัติ</li>
            </ol>
          </div>
          <div class="flex items-center justify-between text-[10px] text-slate-600 pt-1">
            <span><strong>ผลลัพธ์ทางธุรกิจ (ROI):</strong> ลดเวลาในการสืบหาสต็อกดิฟลง <strong>75%</strong> (จากหลักวันเหลือ 15 นาที), ป้องกันสต็อกลมและการตัดขาดทุนเกินจริง</span>
            <span class="font-bold text-amber-700 bg-white px-2 py-0.5 rounded border border-amber-200">สร้างเสร็จใน 5 สัปดาห์ (Quick-Win)</span>
          </div>
        </div>
      </div>

      <!-- CHAMPION #4 -->
      <div class="card-champion border-l-4 border-l-rose-500">
        <div class="flex items-center justify-between mb-1.5">
          <div class="flex items-center gap-2">
            <span class="px-2 py-0.5 rounded bg-rose-600 text-white font-black text-[10px]">CHAMPION #4</span>
            <h3 class="text-xs font-black text-slate-900">Scrap &amp; Yield Variance Root-Cause Mining with Living Knowledge Base (AAR)</h3>
          </div>
          <span class="text-[9px] font-bold text-rose-700 bg-rose-50 px-2 py-0.5 rounded border border-rose-200">Production &amp; Quality</span>
        </div>

        <div class="space-y-1.5 text-[11px] text-slate-700">
          <p>
            <strong class="text-slate-900">⚠️ ปัญหาคอขวดที่แท้จริง:</strong> โรงงานมีของเสีย (Scrap) ในกระบวนการผลิตเกินเกณฑ์มาตรฐาน D365 บันทึกได้แค่ Standard vs. Actual Costing แต่ทีมวิศวกรไม่สามารถระบุได้ว่าทำไมถึงเสีย เพราะปัจจัยหน้างานกระจัดกระจาย (ล็อตวัตถุดิบ, อุณหภูมิ/ความชื้น, หรือวิธีตั้งค่าเครื่องของช่างแต่ละกะ)
          </p>
          <p>
            <strong class="text-slate-900">❌ ข้อจำกัดของ Standard D365:</strong> ระบบบันทึกแค่ยอดต้นทุนของเสีย แต่ไม่มี Machine Learning ทำ Correlation และไม่มีระบบบันทึกองค์ความรู้แบบ Living Knowledge Base
          </p>
          <div class="p-2 bg-rose-50/80 rounded-lg border border-rose-200">
            <strong class="text-rose-900 block mb-0.5">💡 สถาปัตยกรรม Copilot AI ที่พัฒนาขึ้น:</strong>
            <ol class="list-decimal list-inside space-y-0.5 text-slate-700 text-[10px]">
              <li><strong>Deep Attribute Correlation:</strong> เชื่อมโยงข้อมูล Lot Attributes วัตถุดิบ กับเซนเซอร์สิ่งแวดล้อม และประวัติการรันเครื่องจักร</li>
              <li><strong>Root-Cause Discovery:</strong> ค้นพบสาเหตุลึก: <em>"ของเสียที่พุ่งสูงในสัปดาห์นี้สัมพันธ์กับเรซินล็อต L-409 ของคู่ค้า A ที่ถูกรันในช่วงบ่ายที่ความชื้นโรงงานเกิน 75%"</em></li>
              <li><strong>Living Knowledge Base (AAR):</strong> ฝังในแท็บเล็ตหน้างาน ช่างสามารถพิมพ์หรือพูดบอกอาการขัดข้อง Copilot จะดึงแนวทางแก้ไขที่เคยสำเร็จในอดีตขึ้นมาแนะนำทันที</li>
            </ol>
          </div>
          <div class="flex items-center justify-between text-[10px] text-slate-600 pt-1">
            <span><strong>ผลลัพธ์ทางธุรกิจ (ROI):</strong> ลดอัตราของเสียลง <strong>15–25%</strong>, รักษาองค์ความรู้ของหัวหน้าช่างไม่ให้สูญหายเมื่อลาออก</span>
            <span class="font-bold text-rose-700 bg-white px-2 py-0.5 rounded border border-rose-200">สร้างเสร็จใน 6 สัปดาห์</span>
          </div>
        </div>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-1 text-[10px] text-slate-400 text-right">
      Section 2: Strategic Champion Deep Dives (Part 2/2)
    </div>
  </div>

  <!-- ==================== PAGE 5: CHAMPION #5 & EXTENDED MATRIX ==================== -->
  <div class="page-container">
    <div>
      <!-- Section Header -->
      <div class="flex items-center justify-between border-b-2 border-slate-900 pb-1.5 mb-3">
        <div>
          <span class="text-[10px] font-black tracking-widest text-emerald-700 uppercase">Strategic Champion Deep Dives</span>
          <h2 class="text-base font-black text-slate-900">2. เจาะลึก Champion Use Case อันดับ 5 &amp; แผนผังภาพรวมทั้ง 15 ข้อ</h2>
        </div>
        <span class="px-2.5 py-0.5 bg-emerald-50 text-emerald-800 border border-emerald-200 rounded-full text-[10px] font-bold">Supply Chain Resilience</span>
      </div>

      <!-- CHAMPION #5 -->
      <div class="card-champion border-l-4 border-l-emerald-500 mb-3">
        <div class="flex items-center justify-between mb-1.5">
          <div class="flex items-center gap-2">
            <span class="px-2 py-0.5 rounded bg-emerald-600 text-white font-black text-[10px]">CHAMPION #5</span>
            <h3 class="text-xs font-black text-slate-900">Predictive Multi-Tier Supply Disruption &amp; Dynamic Allocation Sentinel</h3>
          </div>
          <span class="text-[9px] font-bold text-emerald-800 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">SCM &amp; Logistics</span>
        </div>

        <div class="space-y-1.5 text-[11px] text-slate-700">
          <p>
            <strong class="text-slate-900">⚠️ ปัญหาคอขวดที่แท้จริง:</strong> การประเมินคู่ค้าใน D365 เป็นแบบย้อนหลัง (ดูประวัติการส่งมอบในอดีต) กว่าจะรู้ว่าคู่ค้าส่งของไม่ทัน ไลน์ผลิตก็หยุดไปแล้ว และไม่สามารถตรวจจับเหตุการณ์ภายนอก (น้ำท่วม, ม็อบท่าเรือ, หรือการหยุดงานประท้วงของบริษัทเดินเรือ)
          </p>
          <div class="p-2 bg-emerald-50/80 rounded-lg border border-emerald-200">
            <strong class="text-emerald-900 block mb-0.5">💡 สถาปัตยกรรม Copilot AI ที่พัฒนาขึ้น:</strong>
            <p class="text-[10px] text-slate-700">
              Copilot ใช้ Azure OpenAI ดึงสัญญาณข่าวสารภายนอก (External Market &amp; Disruption Signals) จับคู่กับ PO และสัญญาใน D365 แบบ Real-time แจ้งเตือนผู้บริหาร: <em>"ซัพพลายเออร์ X มีความเสี่ยงส่งของช้า 85% เนื่องจากท่าเรือแหลมฉบังแออัด แนะนำให้สลับยอด 35% ไปยังซัพพลายเออร์สำรองตามสัญญา B ทันที"</em>
            </p>
          </div>
          <div class="flex items-center justify-between text-[10px] text-slate-600 pt-0.5">
            <span><strong>ผลลัพธ์ทางธุรกิจ (ROI):</strong> ป้องกันสายการผลิตหยุดชะงัก (Zero Unplanned Stoppage), ลดค่าขนส่งด่วนพิเศษ (Expedited Freight)</span>
            <span class="font-bold text-emerald-700 bg-white px-2 py-0.5 rounded border border-emerald-200">สร้างเสร็จใน 6 สัปดาห์</span>
          </div>
        </div>
      </div>

      <!-- EXTENDED 15 USE CASES MATRIX -->
      <div class="border border-slate-200 rounded-xl p-2.5 bg-slate-50/70">
        <h4 class="text-[11px] font-black text-slate-900 mb-1.5 flex items-center justify-between">
          <span>📋 ตารางสรุปสถานะการจัดลำดับความสำคัญของทั้ง 15 Use Cases (Roadmap Alignment)</span>
          <span class="text-[9px] font-normal text-slate-500">อิงตามผลสังเคราะห์ร่วมกัน</span>
        </h4>
        <div class="grid grid-cols-3 gap-2 text-[10px]">
          <!-- Inventory Col -->
          <div class="p-2 bg-white rounded-lg border border-slate-200 space-y-1">
            <div class="font-bold text-amber-800 border-b border-amber-100 pb-0.5">📦 Inventory Module</div>
            <div class="text-slate-800 font-semibold">1. Cycle Count Forensics <span class="text-emerald-600 font-bold">[Top 3]</span></div>
            <div class="text-slate-600">2. Dead Stock Liquidation Plan [Phase 2]</div>
            <div class="text-slate-600">3. Dynamic Micro-Slotting [Phase 2]</div>
            <div class="text-slate-600">4. FEFO Shelf-life Arbitrage [Phase 3]</div>
            <div class="text-slate-400">5. On-Hand Visibility Query [ใช้ Standard]</div>
          </div>
          <!-- SCM Col -->
          <div class="p-2 bg-white rounded-lg border border-slate-200 space-y-1">
            <div class="font-bold text-sky-800 border-b border-sky-100 pb-0.5">🚚 SCM &amp; Procurement</div>
            <div class="text-slate-800 font-semibold">1. Unstructured Vendor PO <span class="text-emerald-600 font-bold">[Top 1]</span></div>
            <div class="text-slate-800 font-semibold">2. Multi-tier Risk Sentinel <span class="text-emerald-600 font-bold">[Top 5]</span></div>
            <div class="text-slate-600">3. Index Formula Price Audit [Phase 2]</div>
            <div class="text-slate-600">4. Maverick Spend Optimizer [Phase 2]</div>
            <div class="text-slate-400">5. PO Changes Summarization [ใช้ Standard]</div>
          </div>
          <!-- Production Col -->
          <div class="p-2 bg-white rounded-lg border border-slate-200 space-y-1">
            <div class="font-bold text-purple-800 border-b border-purple-100 pb-0.5">🏭 Production &amp; Quality</div>
            <div class="text-slate-800 font-semibold">1. MRP Planning Explainer <span class="text-emerald-600 font-bold">[Top 2]</span></div>
            <div class="text-slate-800 font-semibold">2. Scrap Mining &amp; AAR <span class="text-emerald-600 font-bold">[Top 4]</span></div>
            <div class="text-slate-600">3. Dynamic Resequencing [Phase 2]</div>
            <div class="text-slate-600">4. ECO BOM Cutover [Phase 2]</div>
            <div class="text-slate-400">5. Maintenance Work Order [ใช้ Standard]</div>
          </div>
        </div>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-1 text-[10px] text-slate-400 text-right">
      Section 2: Strategic Champion Deep Dives &amp; Full Alignment Matrix
    </div>
  </div>

  <!-- ==================== PAGE 6: BUSINESS IMPACT & POC ROADMAP ==================== -->
  <div class="page-container">
    <div>
      <!-- Section Header -->
      <div class="flex items-center justify-between border-b-2 border-red-600 pb-1.5 mb-3">
        <div>
          <span class="text-[10px] font-black tracking-widest text-red-600 uppercase">Delivery &amp; Commercialization</span>
          <h2 class="text-base font-black text-slate-900">3. มูลค่าทางธุรกิจและแผนงานพัฒนา 8-Week Fast-Track POC</h2>
        </div>
        <span class="px-2.5 py-0.5 bg-red-50 text-red-700 border border-red-200 rounded-full text-[10px] font-bold">Executive Decision Framework</span>
      </div>

      <!-- 4 Executive Impact Cards -->
      <div class="grid grid-cols-4 gap-2 mb-3">
        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-center">
          <div class="text-xl font-black text-emerald-600 mb-0.5">-80%</div>
          <div class="text-[10px] font-bold text-slate-800">PO Transcription Time</div>
          <div class="text-[9px] text-slate-500">ลดเวลางานจัดซื้อจากอีเมลคู่ค้า</div>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-center">
          <div class="text-xl font-black text-sky-600 mb-0.5">-40%</div>
          <div class="text-[10px] font-bold text-slate-800">S&amp;OP Meeting Hours</div>
          <div class="text-[9px] text-slate-500">ถอดรหัสคอขวด MRP เข้าใจทันที</div>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-center">
          <div class="text-xl font-black text-purple-600 mb-0.5">-75%</div>
          <div class="text-[10px] font-bold text-slate-800">Variance Investigation</div>
          <div class="text-[9px] text-slate-500">สืบหาสต็อกดิฟจากวันเหลือนาที</div>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-center">
          <div class="text-xl font-black text-red-600 mb-0.5">-20%</div>
          <div class="text-[10px] font-bold text-slate-800">Production Scrap Rate</div>
          <div class="text-[9px] text-slate-500">ลดของเสียด้วย Living Knowledge</div>
        </div>
      </div>

      <!-- 8-Week POC Delivery Roadmap -->
      <div class="border border-slate-200 rounded-xl p-3 bg-white shadow-xs mb-3">
        <h3 class="text-xs font-black text-slate-900 mb-2 flex items-center gap-1.5">
          <span>🚀</span>
          <span>Fujitsu 8-Week Fast-Track POC to Production Framework</span>
        </h3>
        <div class="grid grid-cols-4 gap-2 text-[10px]">
          <div class="p-2 rounded-lg bg-slate-50 border-l-4 border-l-slate-400 border border-slate-200">
            <div class="font-bold text-slate-900 text-[10px] mb-0.5">Week 1–2: Discovery</div>
            <p class="text-[9px] text-slate-600 leading-snug">สำรวจ Dataverse Entity, ตัวอย่างอีเมลคู่ค้า และเลือก 1st Champion Use Case สำหรับการนำร่อง</p>
          </div>
          <div class="p-2 rounded-lg bg-slate-50 border-l-4 border-l-sky-500 border border-slate-200">
            <div class="font-bold text-sky-900 text-[10px] mb-0.5">Week 3–4: AI Copilot Build</div>
            <p class="text-[9px] text-slate-600 leading-snug">คอนฟิก Copilot Studio, Azure OpenAI Prompt และ RAG บนประวัติการผลิตและสัญญา</p>
          </div>
          <div class="p-2 rounded-lg bg-slate-50 border-l-4 border-l-purple-500 border border-slate-200">
            <div class="font-bold text-purple-900 text-[10px] mb-0.5">Week 5–6: Integration &amp; UAT</div>
            <p class="text-[9px] text-slate-600 leading-snug">เชื่อมต่อ D365 Business Events, ทดสอบระบบ Human-in-the-Loop และทดสอบความแม่นยำ</p>
          </div>
          <div class="p-2 rounded-lg bg-slate-50 border-l-4 border-l-emerald-500 border border-slate-200">
            <div class="font-bold text-emerald-900 text-[10px] mb-0.5">Week 7–8: Go-Live &amp; Scale</div>
            <p class="text-[9px] text-slate-600 leading-snug">เปิดใช้งานจริงบน Production Tenant, วัดผลประหยัดเวลา และวางแผนขยายผลสู่โมดูลถัดไป</p>
          </div>
        </div>
      </div>

      <!-- Fujitsu IP Proposition -->
      <div class="p-3 rounded-xl bg-gradient-to-r from-red-50 to-orange-50 border border-red-200 mb-2">
        <div class="text-[10px] font-black text-red-700 uppercase tracking-wider mb-1">🏆 Fujitsu Thailand Strategic IP Advantage</div>
        <p class="text-[11px] text-slate-800 leading-relaxed">
          การมุ่งเน้นพัฒนาโซลูชัน <strong>Top 5 Champion Use Cases</strong> ที่ผ่านการสังเคราะห์นี้ จะสร้างความได้เปรียบเชิงการแข่งขันสูงสุดให้แก่ <strong>Fujitsu Thailand (FTH)</strong> ในฐานะผู้นำด้าน Enterprise AI ที่ก้าวล้ำกว่าการทำเพียง Chatbot ทั่วไป สู่การเป็น <strong>Autonomous System of Intelligence</strong> ที่ตอบโจทย์ภาคการผลิตและธุรกิจจัดจำหน่ายในประเทศไทยได้อย่างแท้จริง
        </p>
      </div>
    </div>

    <!-- Sign-off Block -->
    <div class="border-t border-slate-200 pt-2 flex items-center justify-between text-[10px] text-slate-500">
      <div>
        <span class="font-bold text-slate-800">Fujitsu (Thailand) Co., Ltd.</span> | 22nd Floor, Column Tower, Sukhumvit Road, Bangkok, Thailand<br>
        Web: <a href="https://wititgithub.github.io/fth-d365-fo-copilot-deck/" class="text-sky-600 underline">https://wititgithub.github.io/fth-d365-fo-copilot-deck/</a>
      </div>
      <div class="text-right font-medium">
        Contact: Enterprise AI Consulting Practice<br>
        Email: consulting@th.fujitsu.com
      </div>
    </div>
  </div>

</body>
</html>
"""

async def main():
    print("Writing synthesized Top 5 HTML whitepaper...")
    html_content = build_html_content()
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Saved HTML -> {HTML_PATH}")

    print("Launching Playwright to generate high-resolution vector PDF...")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        file_url = "file:///" + HTML_PATH.replace("\\", "/")
        await page.goto(file_url, wait_until="networkidle")
        await page.evaluate("document.fonts.ready")
        await page.wait_for_timeout(1000)

        for out_pdf in OUT_PDF_PATHS:
            os.makedirs(os.path.dirname(out_pdf), exist_ok=True)
            await page.pdf(
                path=out_pdf,
                format="A4",
                print_background=True,
                margin={"top": "8mm", "bottom": "10mm", "left": "10mm", "right": "10mm"},
                display_header_footer=True,
                header_template='<div style="font-size: 8px; color: #94a3b8; width: 100%; display: flex; justify-content: space-between; padding: 0 10mm; font-family: sans-serif; font-weight: 600;"><span>FUJITSU THAILAND (FTH) • D365 ADVANCED COPILOT AI (TOP 5 SYNTHESIS)</span><span>CONFIDENTIAL</span></div>',
                footer_template='<div style="font-size: 8px; color: #94a3b8; width: 100%; display: flex; justify-content: space-between; padding: 0 10mm; font-family: sans-serif;"><span>© 2026 Fujitsu Thailand Co., Ltd. All rights reserved.</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>'
            )
            print(f"Successfully generated PDF -> {out_pdf} ({os.path.getsize(out_pdf)//1024} KB)")

        await browser.close()
    print("PDF generation complete!")

if __name__ == "__main__":
    asyncio.run(main())
