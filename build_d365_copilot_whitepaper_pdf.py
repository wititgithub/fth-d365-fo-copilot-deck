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
  <title>D365 Copilot AI Deep Use Cases Whitepaper - Fujitsu Thailand (FTH)</title>
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
      line-height: 1.4;
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
      padding: 4mm 2mm;
    }
    .page-container:last-child {
      page-break-after: auto;
      break-after: auto;
    }
    .card-usecase {
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 10px 14px;
      background: #ffffff;
      box-shadow: 0 1px 2px rgba(0,0,0,0.03);
      margin-bottom: 9px;
    }
    .card-usecase:last-child {
      margin-bottom: 0;
    }
  </style>
</head>
<body class="text-slate-900 text-xs">

  <!-- ==================== PAGE 1: COVER PAGE ==================== -->
  <div class="page-container">
    <div>
      <!-- Top Branding Bar -->
      <div class="flex items-center justify-between border-b border-slate-200 pb-3 mb-5">
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
      <div class="space-y-2.5 max-w-3xl mb-4">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-900 text-white text-[10px] font-bold uppercase tracking-wider">
          <span class="w-2 h-2 rounded-full bg-red-500 animate-pulse"></span>
          Enterprise Strategic Whitepaper • Solution Blueprint
        </div>

        <h1 class="text-3xl font-black text-slate-900 tracking-tight leading-tight">
          Beyond Standard: Unlocking D365 with Advanced Copilot AI
        </h1>
        <p class="text-lg font-bold text-sky-700">
          การก้าวข้ามข้อจำกัด Dynamics 365 สู่ระบบอัจฉริยะด้วย Copilot AI
        </p>
        <p class="text-xs text-slate-600 leading-relaxed font-normal">
          เจาะลึก <strong>Top 15 Strategic Use Cases</strong> แก้ไขข้อจำกัดทางสถาปัตยกรรมและ Pain Points เรื้อรังของ D365 ในโมดูล 
          <strong>Inventory, SCM & Procurement, และ Production</strong> ด้วย Autonomous Copilot Agents ที่ก้าวหน้ากว่าฟังก์ชันมาตรฐาน
        </p>
      </div>

      <!-- Hero Visual Box -->
      <div class="mb-4 rounded-xl overflow-hidden border border-slate-200 shadow-sm bg-slate-50">
        <img src="assets/copilot_d365_hero_fluent.jpg" alt="Copilot D365 Hero" class="w-full h-44 object-cover object-center">
      </div>

      <!-- Executive Overview Grid -->
      <div class="grid grid-cols-3 gap-3 mb-3">
        <div class="p-3 rounded-xl bg-amber-50/80 border border-amber-200">
          <div class="flex items-center gap-1.5 text-amber-800 font-bold text-[11px] uppercase mb-1">
            <span>📦</span>
            <span>Inventory Management</span>
          </div>
          <div class="text-base font-black text-slate-900 mb-0.5">5 Deep Solutions</div>
          <p class="text-[11px] text-slate-600 leading-snug">Cycle count forensics, dead stock liquidation, dynamic slotting, and shelf-life arbitrage.</p>
        </div>

        <div class="p-3 rounded-xl bg-sky-50/80 border border-sky-200">
          <div class="flex items-center gap-1.5 text-sky-800 font-bold text-[11px] uppercase mb-1">
            <span>🚚</span>
            <span>SCM & Procurement</span>
          </div>
          <div class="text-base font-black text-slate-900 mb-0.5">5 Deep Solutions</div>
          <p class="text-[11px] text-slate-600 leading-snug">Unstructured vendor emails, index price audits, multi-tier risk sentinel, and maverick spend.</p>
        </div>

        <div class="p-3 rounded-xl bg-purple-50/80 border border-purple-200">
          <div class="flex items-center gap-1.5 text-purple-800 font-bold text-[11px] uppercase mb-1">
            <span>🏭</span>
            <span>Production & MRP</span>
          </div>
          <div class="text-base font-black text-slate-900 mb-0.5">5 Deep Solutions</div>
          <p class="text-[11px] text-slate-600 leading-snug">MRP black-box explainer, shop floor resequencing, yield pattern mining, and ECO cutover.</p>
        </div>
      </div>
    </div>

    <!-- Metadata Footer of Cover Page -->
    <div class="border-t border-slate-200 pt-2 flex items-center justify-between text-[11px] text-slate-500">
      <div>
        <span class="font-bold text-slate-800">Fujitsu (Thailand) Co., Ltd. (FTH)</span> | Enterprise Application Practice
      </div>
      <div>
        <span>Document Ref: <strong>FTH-WP-D365-AI-2026</strong></span> • <span>October 2026</span>
      </div>
    </div>
  </div>

  <!-- ==================== PAGE 2: CONTEXT & ARCHITECTURE ==================== -->
  <div class="page-container">
    <div>
      <!-- Section Title -->
      <div class="flex items-center justify-between border-b-2 border-slate-900 pb-2 mb-3">
        <div>
          <span class="text-[10px] font-black tracking-widest text-red-600 uppercase">Strategic Context</span>
          <h2 class="text-lg font-black text-slate-900">1. นิยามความแตกต่าง: Standard Copilot vs. Fujitsu Advanced AI</h2>
        </div>
        <div class="text-right">
          <span class="px-2.5 py-0.5 bg-slate-100 rounded text-[10px] font-bold text-slate-600">Architectural Gap Analysis</span>
        </div>
      </div>

      <p class="text-[11px] text-slate-700 leading-relaxed mb-3">
        Microsoft Dynamics 365 ได้เปิดตัวความสามารถด้าน Copilot ในเวอร์ชันล่าสุด ซึ่งมุ่งเน้นความสามารถแบบ <strong>Conversational &amp; Informational (ถามข้อมูลทั่วไปและสรุปเอกสาร)</strong> เช่น การถามยอดสต็อกคงเหลือ หรือสรุปข้อความใน PO รายใบ อย่างไรก็ตาม ปัญหาคอขวดที่แท้จริงของการดำเนินธุรกิจโรงงานและการจัดซื้อในประเทศไทย เกิดจาก <strong>ความซับซ้อนเชิงเงื่อนไขและข้อมูลที่อยู่นอกระบบ (Unstructured &amp; Multi-Variable Decisions)</strong> ซึ่งระบบมาตรฐานยังไม่สามารถก้าวข้ามได้
      </p>

      <!-- Matrix Table -->
      <div class="border border-slate-200 rounded-xl overflow-hidden mb-4 shadow-xs">
        <table class="w-full text-[11px] text-left">
          <thead class="bg-slate-900 text-white font-bold uppercase text-[10px]">
            <tr>
              <th class="p-2.5 w-1/4">มิติการทำงาน (Dimension)</th>
              <th class="p-2.5 w-3/8 bg-slate-800 text-slate-300">Standard D365 Copilot (ล่าสุด)</th>
              <th class="p-2.5 w-3/8 bg-red-950/80 text-red-200">Fujitsu Advanced Copilot AI (FTH Blueprint)</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-200">
            <tr class="bg-white">
              <td class="p-2.5 font-bold text-slate-900">ระดับการตัดสินใจ (Decision Level)</td>
              <td class="p-2.5 text-slate-600"><strong>Informational / Passive:</strong> ตอบคำถามสต็อกคงเหลือตามคิวรี หรือสรุปข้อความบรรทัดต่อบรรทัด</td>
              <td class="p-2.5 text-red-900 font-semibold bg-red-50/40"><strong>Prescriptive &amp; Autonomous:</strong> เสนอทางเลือกเชิงกลยุทธ์ จำลองผลกระทบต้นทุน (Trade-off) และร่าง Action ให้ทันที</td>
            </tr>
            <tr class="bg-slate-50/60">
              <td class="p-2.5 font-bold text-slate-900">การจัดการข้อมูลภายนอก (External Data)</td>
              <td class="p-2.5 text-slate-600">จำกัดเฉพาะข้อมูลที่มีอยู่แล้วในตาราง Dataverse หรือ ERP Database ภายในระบบ</td>
              <td class="p-2.5 text-red-900 font-semibold bg-red-50/40">เชื่อมต่ออีเมลคู่ค้า, ตลาดซื้อขายโภคภัณฑ์ (Commodity Indices), ข่าวสารท่าเรือ และข้อมูล IoT สภาพแวดล้อม</td>
            </tr>
            <tr class="bg-white">
              <td class="p-2.5 font-bold text-slate-900">การสืบหาต้นตอ (Root-Cause Forensics)</td>
              <td class="p-2.5 text-slate-600">แสดงผลเฉพาะความต่าง (Variance) เช่น ยอดขาด-เกิน, ของเสีย แต่ไม่สามารถอธิบาย "ทำไม"</td>
              <td class="p-2.5 text-red-900 font-semibold bg-red-50/40">สืบค้นความสัมพันธ์แบบ Multi-dimensional ข้ามตารางเพื่อชี้ชัดสาเหตุที่แท้จริง (Root-Cause Pattern)</td>
            </tr>
            <tr class="bg-slate-50/60">
              <td class="p-2.5 font-bold text-slate-900">การเชื่อมต่อเพื่อสั่งการ (Action Loop)</td>
              <td class="p-2.5 text-slate-600">ผู้ใช้ต้องสลับหน้าจอไปคีย์ข้อมูลหรือออกเอกสารด้วยตนเอง</td>
              <td class="p-2.5 text-red-900 font-semibold bg-red-50/40">ทำงานร่วมกับ D365 Business Events &amp; Power Automate ปรับปรุงข้อมูลหรือออกเอกสารหลังมนุษย์อนุมัติ (Human-in-the-Loop)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Solution Architecture Framework Diagram (Stylized) -->
      <div class="p-3.5 rounded-xl bg-slate-900 text-white border border-slate-800 shadow-sm mb-3">
        <div class="flex items-center justify-between mb-2.5 border-b border-slate-800 pb-1.5">
          <span class="text-[11px] font-black tracking-wider text-sky-400 uppercase">Fujitsu Enterprise AI Architecture Blueprint</span>
          <span class="text-[9px] text-slate-400">Secure Enterprise Boundary • Zero Data Leakage • 100% PDPA Compliant</span>
        </div>

        <div class="grid grid-cols-3 gap-2.5 text-center text-[10px]">
          <!-- Layer 1 -->
          <div class="p-2.5 rounded-lg bg-slate-800/90 border border-slate-700">
            <div class="text-[9px] font-bold text-emerald-400 uppercase tracking-wider mb-0.5">Layer 1: Enterprise Data</div>
            <div class="font-extrabold text-white text-xs mb-0.5">D365 &amp; External Signals</div>
            <p class="text-[10px] text-slate-300">Dataverse • Azure Synapse Link • Microsoft Fabric • IoT Sensors • Vendor Emails &amp; PDFs</p>
          </div>

          <!-- Layer 2 -->
          <div class="p-2.5 rounded-lg bg-slate-800/90 border border-sky-500/50 shadow-inner">
            <div class="text-[9px] font-bold text-sky-400 uppercase tracking-wider mb-0.5">Layer 2: AI Cognitive Engine</div>
            <div class="font-extrabold text-white text-xs mb-0.5">Copilot Studio + Azure OpenAI</div>
            <p class="text-[10px] text-slate-300">Semantic Kernel • Custom Domain AI Agents • RAG บนคู่มือและสัญญา • Prompt Engineering</p>
          </div>

          <!-- Layer 3 -->
          <div class="p-2.5 rounded-lg bg-slate-800/90 border border-red-500/50">
            <div class="text-[9px] font-bold text-red-400 uppercase tracking-wider mb-0.5">Layer 3: Autonomous Actions</div>
            <div class="font-extrabold text-white text-xs mb-0.5">D365 Business Events</div>
            <p class="text-[10px] text-slate-300">Auto Draft POs • Reslotting Work • Rescheduling Triggers • Human-in-the-Loop Sign-off</p>
          </div>
        </div>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-1 text-[10px] text-slate-400 text-right">
      Section 1: Executive Architectural Analysis
    </div>
  </div>

  <!-- ==================== PAGE 3: INVENTORY PART 1 (USE CASES 1, 2, 3) ==================== -->
  <div class="page-container">
    <div>
      <!-- Section Header -->
      <div class="flex items-center justify-between border-b-2 border-amber-600 pb-1.5 mb-3">
        <div class="flex items-center gap-2">
          <span class="text-xl">📦</span>
          <div>
            <span class="text-[10px] font-black tracking-widest text-amber-700 uppercase">Module Deep Dive 01</span>
            <h2 class="text-base font-black text-slate-900">Inventory &amp; Warehouse: Top 5 Deep Use Cases (Part 1/2)</h2>
          </div>
        </div>
        <span class="px-2.5 py-0.5 bg-amber-50 text-amber-800 border border-amber-200 rounded-full text-[10px] font-bold">WMS &amp; Stock Optimization</span>
      </div>

      <!-- Use Case 1.1 -->
      <div class="card-usecase">
        <div class="flex items-center justify-between mb-1">
          <h3 class="text-xs font-extrabold text-slate-900 flex items-center gap-1.5">
            <span class="w-5 h-5 rounded-full bg-amber-600 text-white flex items-center justify-center text-[10px] font-bold">1</span>
            Forensic Cycle Count &amp; Discrepancy Investigator (นักสืบหาสาเหตุสต็อกดิฟ)
          </h3>
          <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">Counting Journal &amp; WMS</span>
        </div>
        <div class="space-y-1 text-[11px] text-slate-600">
          <p><strong class="text-slate-800">⚠️ ข้อจำกัดใน D365 &amp; Pain Point:</strong> D365 บันทึกยอดนับสต็อกต่างได้ แต่บอกได้แค่ว่ายอดขาดหรือเกินกี่ชิ้น ผู้จัดการคลังต้องเปิด Transaction History ไล่ดูประวัติรับ-จ่ายเป็นร้อยบรรทัดเพื่อหาสาเหตุ ซึ่งใช้เวลาเป็นวันและมักหาต้นตอไม่เจอ</p>
          <p><strong class="text-slate-800">❌ สิ่งที่ Standard ทำไม่ได้:</strong> ไม่สามารถวิเคราะห์พฤติกรรมการสแกน, ความใกล้เคียงของตำแหน่ง Bin, หรือประวัติบาร์โค้ดที่หน้าตาคล้ายกันได้</p>
          <p class="p-1.5 bg-amber-50 border-l-4 border-amber-500 text-amber-950 rounded-r">
            <strong>💡 โซลูชัน Copilot AI:</strong> เป็น Forensic Agent วิเคราะห์ Transaction logs, ลำดับการสแกนของพนักงาน, ตำแหน่ง Bin ติดกัน, และ License Plate history แล้วสรุปสาเหตุทันที เช่น: <em>"พบสินค้าดิฟ -20 ชิ้น มีความเป็นไปได้ 94% เกิดจากพนักงานสแกนสลับกับ SKU-B ที่อยู่ Bin ติดกันเมื่อกะดึกวันที่ 14"</em> พร้อมร่างใบลดหนี้/ปรับปรุงสต็อกให้อัตโนมัติ
          </p>
        </div>
      </div>

      <!-- Use Case 1.2 -->
      <div class="card-usecase">
        <div class="flex items-center justify-between mb-1">
          <h3 class="text-xs font-extrabold text-slate-900 flex items-center gap-1.5">
            <span class="w-5 h-5 rounded-full bg-amber-600 text-white flex items-center justify-center text-[10px] font-bold">2</span>
            Dead Stock &amp; Slow-Moving Diagnostic with Auto-Liquidation Strategy
          </h3>
          <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">Inventory Aging &amp; Sales</span>
        </div>
        <div class="space-y-1 text-[11px] text-slate-600">
          <p><strong class="text-slate-800">⚠️ ข้อจำกัดใน D365 &amp; Pain Point:</strong> รายงาน Inventory Aging ของ D365 เป็นตารางตัวเลขแบบคงที่ ไม่สามารถวิเคราะห์ได้ว่าทำไมของถึงค้างสต็อก (เช่น มีการเปลี่ยนแบบวิศวกรรม ECN, สินค้าใหม่กินตลาดกันเอง, หรือซัพพลายเออร์บังคับซื้อ MOQ เกินจำเป็น)</p>
          <p><strong class="text-slate-800">❌ สิ่งที่ Standard ทำไม่ได้:</strong> ไม่มีกลไกแนะนำ Action ในการระบายสต็อกแบบข้ามมิติ</p>
          <p class="p-1.5 bg-amber-50 border-l-4 border-amber-500 text-amber-950 rounded-r">
            <strong>💡 โซลูชัน Copilot AI:</strong> Copilot วิเคราะห์ประวัติการสั่งซื้อ, Seasonal Drop, และรอบอายุผลิตภัณฑ์ พร้อมสร้าง <em>"แผนระบายสต็อกเชิงรุก (Actionable Liquidation Plan)"</em> เช่น แนะนำให้จัด Bundle กับสินค้าขายดีตัวไหน, เจรจาคืนซัพพลายเออร์เจ้าใด หรือคำนวณภาษีหากต้องทำลาย (Scrap Write-off)
          </p>
        </div>
      </div>

      <!-- Use Case 1.3 -->
      <div class="card-usecase">
        <div class="flex items-center justify-between mb-1">
          <h3 class="text-xs font-extrabold text-slate-900 flex items-center gap-1.5">
            <span class="w-5 h-5 rounded-full bg-amber-600 text-white flex items-center justify-center text-[10px] font-bold">3</span>
            Dynamic Micro-Slotting &amp; Real-Time Reslotting Advisor
          </h3>
          <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">Advanced WMS &amp; Picking</span>
        </div>
        <div class="space-y-1 text-[11px] text-slate-600">
          <p><strong class="text-slate-800">⚠️ ข้อจำกัดใน D365 &amp; Pain Point:</strong> โมดูล Advanced WMS Slotting ของ D365 เป็นแบบ Rule-based ตายตัว (แบ่งกลุ่ม A/B/C) หากพฤติกรรมการหยิบเปลี่ยนตามโปรโมชั่น พนักงานต้องเดินอ้อมคลังไกลมาก ทำให้รอบการหยิบช้าลง</p>
          <p><strong class="text-slate-800">❌ สิ่งที่ Standard ทำไม่ได้:</strong> ไม่สามารถปรับเปลี่ยนผังตำแหน่งจัดเก็บสินค้า (Reslotting) ให้สอดคล้องกับ Picking Waves และขนาดมิติเชิงปริมาตรแบบ Real-time</p>
          <p class="p-1.5 bg-amber-50 border-l-4 border-amber-500 text-amber-950 rounded-r">
            <strong>💡 โซลูชัน Copilot AI:</strong> คำนวณระยะทางและเส้นทางการเดินของ Forklift วิเคราะห์ออเดอร์ล่วงหน้าในอีก 48 ชั่วโมง แล้วสั่งสร้างใบงาน <em>"Proactive Reslotting Work"</em> ย้ายสินค้าขายดีมาไว้ที่ Front-row ในช่วงกะว่าง ลดเวลาเดินหยิบของลงได้ 30–40%
          </p>
        </div>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-1 text-[10px] text-slate-400 text-right">
      Section 2: Inventory Management (Part 1/2)
    </div>
  </div>

  <!-- ==================== PAGE 4: INVENTORY PART 2 (USE CASES 4, 5 + SUMMARY) ==================== -->
  <div class="page-container">
    <div>
      <!-- Section Header -->
      <div class="flex items-center justify-between border-b-2 border-amber-600 pb-1.5 mb-3">
        <div class="flex items-center gap-2">
          <span class="text-xl">📦</span>
          <div>
            <span class="text-[10px] font-black tracking-widest text-amber-700 uppercase">Module Deep Dive 01</span>
            <h2 class="text-base font-black text-slate-900">Inventory &amp; Warehouse: Top 5 Deep Use Cases (Part 2/2)</h2>
          </div>
        </div>
        <span class="px-2.5 py-0.5 bg-amber-50 text-amber-800 border border-amber-200 rounded-full text-[10px] font-bold">WMS &amp; Stock Optimization</span>
      </div>

      <!-- Use Case 1.4 -->
      <div class="card-usecase">
        <div class="flex items-center justify-between mb-1">
          <h3 class="text-xs font-extrabold text-slate-900 flex items-center gap-1.5">
            <span class="w-5 h-5 rounded-full bg-amber-600 text-white flex items-center justify-center text-[10px] font-bold">4</span>
            Dynamic FEFO &amp; Shelf-Life Arbitrage for Regulated Goods (สินค้าควบคุม/อาหาร/ยา)
          </h3>
          <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">Batch Management &amp; Expiry</span>
        </div>
        <div class="space-y-1 text-[11px] text-slate-600">
          <p><strong class="text-slate-800">⚠️ ข้อจำกัดใน D365 &amp; Pain Point:</strong> D365 รองรับ FEFO แบบตรงไปตรงมา แต่ในชีวิตจริง ลูกค้าแต่ละรายมีเงื่อนไขอายุสินค้าต่างกัน (เช่น Modern Trade เจ้า A ขอ Shelf-life &ge; 75%, แต่ลูกค้า B ยอมรับที่ 50% แลกกับส่วนลด) D365 มักติด Hard Error จองของไม่ได้ หรือปล่อยให้สต็อกหมดอายุค้าง</p>
          <p><strong class="text-slate-800">❌ สิ่งที่ Standard ทำไม่ได้:</strong> ขาดการจัดสรรล็อต (Batch Allocation) แบบ Arbitrage ที่จับคู่เงื่อนไขสัญญาลูกค้าหลายรายพร้อมกัน</p>
          <p class="p-1.5 bg-amber-50 border-l-4 border-amber-500 text-amber-950 rounded-r">
            <strong>💡 โซลูชัน Copilot AI:</strong> วิเคราะห์สัญญา Master SLA ของลูกค้าแต่ละเจ้า, วันหมดอายุของทุกล็อต และระยะเวลาขนส่ง แล้วจัดสรรล็อตอย่างชาญฉลาด เพื่อไม่ให้มีของหมดอายุค้างในคลังแม้แต่ชิ้นเดียว
          </p>
        </div>
      </div>

      <!-- Use Case 1.5 -->
      <div class="card-usecase">
        <div class="flex items-center justify-between mb-1">
          <h3 class="text-xs font-extrabold text-slate-900 flex items-center gap-1.5">
            <span class="w-5 h-5 rounded-full bg-amber-600 text-white flex items-center justify-center text-[10px] font-bold">5</span>
            Multi-Echelon Stockout Early-Warning &amp; Lead-Time Drift Explainer
          </h3>
          <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">Safety Stock &amp; Lead Time</span>
        </div>
        <div class="space-y-1 text-[11px] text-slate-600">
          <p><strong class="text-slate-800">⚠️ ข้อจำกัดใน D365 &amp; Pain Point:</strong> เมื่อ Master Planning แจ้งเตือน Safety Stock พลานเนอร์มักไม่เข้าใจว่าสต็อกจะขาดเพราะอะไร และมักสั่งของช้าไปเพราะ Lead Time ของซัพพลายเออร์ในระบบถูกตั้งไว้แบบคงที่ ซึ่งไม่ตรงกับความเป็นจริง</p>
          <p><strong class="text-slate-800">❌ สิ่งที่ Standard ทำไม่ได้:</strong> ไม่มีระบบเรียนรู้ว่า Lead Time จริงในอดีตกำลังยืดออก (Drift) แบบค่อยเป็นค่อยไป</p>
          <p class="p-1.5 bg-amber-50 border-l-4 border-amber-500 text-amber-950 rounded-r">
            <strong>💡 โซลูชัน Copilot AI:</strong> ตรวจจับแนวโน้มความล่าช้าสะสมของซัพพลายเออร์ และคำนวณความเสี่ยงสต็อกขาดล่วงหน้า พร้อมสรุป: <em>"วัตถุดิบ X เสี่ยงขาดสต็อก 88% ในอีก 18 วัน แม้ Master Planning จะยังไม่เตือน เพราะช่วง 3 เดือนที่ผ่านมา ท่าเรือต้นทางดีเลย์เพิ่มขึ้น 6 วัน แนะนำให้ออก PR วันนี้"</em>
          </p>
        </div>
      </div>

      <!-- Strategic Value Box for Inventory -->
      <div class="p-3 bg-gradient-to-r from-amber-50 to-orange-50 border border-amber-200 rounded-xl mt-3">
        <div class="text-[11px] font-black text-amber-900 uppercase tracking-wide mb-1.5">
          🎯 Inventory Transformation Business Impact
        </div>
        <div class="grid grid-cols-3 gap-2 text-center text-[10px]">
          <div class="p-2 bg-white rounded-lg border border-amber-200/80 shadow-xs">
            <div class="text-sm font-black text-amber-700">-70%</div>
            <div class="font-bold text-slate-800">Count Investigation Time</div>
            <div class="text-slate-500">ลดเวลาสืบหาสต็อกดิฟจากวันเหลือนาที</div>
          </div>
          <div class="p-2 bg-white rounded-lg border border-amber-200/80 shadow-xs">
            <div class="text-sm font-black text-amber-700">-25%</div>
            <div class="font-bold text-slate-800">Dead Stock Write-offs</div>
            <div class="text-slate-500">ระบายสต็อกค้างก่อนเสื่อมมูลค่า</div>
          </div>
          <div class="p-2 bg-white rounded-lg border border-amber-200/80 shadow-xs">
            <div class="text-sm font-black text-amber-700">+35%</div>
            <div class="font-bold text-slate-800">Picking Path Velocity</div>
            <div class="text-slate-500">จัดวางสินค้าใกล้จุดหยิบตามฤดูกาล</div>
          </div>
        </div>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-1 text-[10px] text-slate-400 text-right">
      Section 2: Inventory Management (Part 2/2)
    </div>
  </div>

  <!-- ==================== PAGE 5: SCM PART 1 (USE CASES 1, 2, 3) ==================== -->
  <div class="page-container">
    <div>
      <!-- Section Header -->
      <div class="flex items-center justify-between border-b-2 border-sky-600 pb-1.5 mb-3">
        <div class="flex items-center gap-2">
          <span class="text-xl">🚚</span>
          <div>
            <span class="text-[10px] font-black tracking-widest text-sky-700 uppercase">Module Deep Dive 02</span>
            <h2 class="text-base font-black text-slate-900">SCM &amp; Procurement: Top 5 Deep Use Cases (Part 1/2)</h2>
          </div>
        </div>
        <span class="px-2.5 py-0.5 bg-sky-50 text-sky-800 border border-sky-200 rounded-full text-[10px] font-bold">Sourcing &amp; Supplier Governance</span>
      </div>

      <!-- Use Case 2.1 -->
      <div class="card-usecase">
        <div class="flex items-center justify-between mb-1">
          <h3 class="text-xs font-extrabold text-slate-900 flex items-center gap-1.5">
            <span class="w-5 h-5 rounded-full bg-sky-600 text-white flex items-center justify-center text-[10px] font-bold">1</span>
            Unstructured Vendor Negotiation &amp; Split-Delivery Auto-Reconciliation
          </h3>
          <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">Purchase Order &amp; Email EDI</span>
        </div>
        <div class="space-y-1 text-[11px] text-slate-600">
          <p><strong class="text-slate-800">⚠️ ข้อจำกัดใน D365 &amp; Pain Point:</strong> ซัพพลายเออร์ส่วนใหญ่ไม่ยอมเข้าระบบ Vendor Portal ของ D365 แต่มักส่งอีเมลตอบกลับเป็นไฟล์ PDF, ตาราง Excel หรือแชต แจ้งขอส่งของแยกงวด (Split shipment), ขอเลื่อนวัน, หรือขอขึ้นราคาบางรายการ ทำให้จัดซื้อต้องคีย์แก้มือทีละบรรทัด</p>
          <p><strong class="text-slate-800">❌ สิ่งที่ Standard ทำไม่ได้:</strong> Standard Copilot ทำได้แค่ "สรุปข้อความในระบบ" แต่ไม่สามารถอ่านอีเมลภายนอกแล้วนำมาอัปเดต Line PO ใน D365 เองได้</p>
          <p class="p-1.5 bg-sky-50 border-l-4 border-sky-500 text-sky-950 rounded-r">
            <strong>💡 โซลูชัน Copilot AI:</strong> ตรวจจับอีเมลและเอกสารแนบจากซัพพลายเออร์ สกัดข้อมูลวันส่งของที่ขอแบ่งงวด เทียบกับผลกระทบในตารางผลิต และร่างการแก้ไข PO พร้อมส่งเมลตอบกลับซัพพลายเออร์ให้จัดซื้อกดยืนยันในคลิกเดียว
          </p>
        </div>
      </div>

      <!-- Use Case 2.2 -->
      <div class="card-usecase">
        <div class="flex items-center justify-between mb-1">
          <h3 class="text-xs font-extrabold text-slate-900 flex items-center gap-1.5">
            <span class="w-5 h-5 rounded-full bg-sky-600 text-white flex items-center justify-center text-[10px] font-bold">2</span>
            Contract Price Index-Formula Auditing (ตรวจสอบสูตรราคาผันผวนตามดัชนีสินค้าโภคภัณฑ์)
          </h3>
          <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">Trade Agreement &amp; Pricing</span>
        </div>
        <div class="space-y-1 text-[11px] text-slate-600">
          <p><strong class="text-slate-800">⚠️ ข้อจำกัดใน D365 &amp; Pain Point:</strong> D365 Trade Agreement รองรับราคาตายตัวหรือส่วนลดตามจำนวน แต่สัญญาจัดซื้ออุตสาหกรรมมักผูกกับดัชนีราคาตลาดโลก (เช่น ราคาเม็ดพลาสติก ICIS, น้ำมัน, ดัชนี LME ทองแดง) จัดซื้อต้องมานั่งคำนวณตรวจสอบอินวอยซ์ เสี่ยงต่อเงินรั่วไหล</p>
          <p><strong class="text-slate-800">❌ สิ่งที่ Standard ทำไม่ได้:</strong> ไม่มีกลไกเชื่อมต่อดัชนีสินค้าโภคภัณฑ์ภายนอกเพื่อตรวจสอบความถูกต้องของสูตรราคาในสัญญา</p>
          <p class="p-1.5 bg-sky-50 border-l-4 border-sky-500 text-sky-950 rounded-r">
            <strong>💡 โซลูชัน Copilot AI:</strong> เชื่อมต่อ Live Market Feeds และดึงสูตรราคาจากเอกสารสัญญา PDF มาคำนวณเทียบกับ Invoice ที่ซัพพลายเออร์เรียกเก็บ ตรวจจับทันทีหากมีการคิดส่วนต่างเกินจริงก่อนทำ 3-Way Matching
          </p>
        </div>
      </div>

      <!-- Use Case 2.3 -->
      <div class="card-usecase">
        <div class="flex items-center justify-between mb-1">
          <h3 class="text-xs font-extrabold text-slate-900 flex items-center gap-1.5">
            <span class="w-5 h-5 rounded-full bg-sky-600 text-white flex items-center justify-center text-[10px] font-bold">3</span>
            Predictive Multi-Tier Vendor Risk Sentinel (ตรวจจับความเสี่ยงคู่ค้าล่วงหน้าจากข้อมูลภายนอก)
          </h3>
          <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">Vendor Rating &amp; SCM Risk</span>
        </div>
        <div class="space-y-1 text-[11px] text-slate-600">
          <p><strong class="text-slate-800">⚠️ ข้อจำกัดใน D365 &amp; Pain Point:</strong> การประเมินคะแนนซัพพลายเออร์ใน D365 เป็นแบบย้อนหลัง (ดูประวัติส่งตรงเวลา OTIF ในอดีต) ไม่สามารถเตือนล่วงหน้าได้ว่าโรงงานคู่ค้ากำลังจะหยุดงานประท้วง, มีปัญหาทางการเงิน หรือโดนผลกระทบจากภัยธรรมชาติ</p>
          <p><strong class="text-slate-800">❌ สิ่งที่ Standard ทำไม่ได้:</strong> ไม่มีการดึง External News &amp; Geopolitical Risk เข้ามาวิเคราะห์ร่วมกับ Open Purchase Orders</p>
          <p class="p-1.5 bg-sky-50 border-l-4 border-sky-500 text-sky-950 rounded-r">
            <strong>💡 โซลูชัน Copilot AI:</strong> สแกนข่าวสาร กฎหมาย ศุลกากร และแนวโน้มสภาพอากาศ แล้วจับคู่กับรายการ PO ที่เปิดค้างอยู่ แจ้งเตือนจัดซื้อ: <em>"ซัพพลายเออร์ A กำลังประสบปัญหาน้ำท่วม มีความเสี่ยงกระทบออเดอร์ผลิตสัปดาห์หน้า แนะนำให้สลับยอด 30% ไปยังซัพพลายเออร์สำรองตามสัญญา B ทันที"</em>
          </p>
        </div>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-1 text-[10px] text-slate-400 text-right">
      Section 3: SCM &amp; Procurement (Part 1/2)
    </div>
  </div>

  <!-- ==================== PAGE 6: SCM PART 2 (USE CASES 4, 5 + SUMMARY) ==================== -->
  <div class="page-container">
    <div>
      <!-- Section Header -->
      <div class="flex items-center justify-between border-b-2 border-sky-600 pb-1.5 mb-3">
        <div class="flex items-center gap-2">
          <span class="text-xl">🚚</span>
          <div>
            <span class="text-[10px] font-black tracking-widest text-sky-700 uppercase">Module Deep Dive 02</span>
            <h2 class="text-base font-black text-slate-900">SCM &amp; Procurement: Top 5 Deep Use Cases (Part 2/2)</h2>
          </div>
        </div>
        <span class="px-2.5 py-0.5 bg-sky-50 text-sky-800 border border-sky-200 rounded-full text-[10px] font-bold">Sourcing &amp; Supplier Governance</span>
      </div>

      <!-- Use Case 2.4 -->
      <div class="card-usecase">
        <div class="flex items-center justify-between mb-1">
          <h3 class="text-xs font-extrabold text-slate-900 flex items-center gap-1.5">
            <span class="w-5 h-5 rounded-full bg-sky-600 text-white flex items-center justify-center text-[10px] font-bold">4</span>
            Intelligent Maverick Spend &amp; Long-Tail Procurement Optimizer
          </h3>
          <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">Purchase Requisition (PR)</span>
        </div>
        <div class="space-y-1 text-[11px] text-slate-600">
          <p><strong class="text-slate-800">⚠️ ข้อจำกัดใน D365 &amp; Pain Point:</strong> พนักงานเปิดใบขอซื้อ (PR) ด้วยการพิมพ์ Free Text หรือเลือกหมวดหมู่กว้างๆ ทำให้ฝ่ายจัดซื้อไม่สามารถคุมการซื้อนอกสัญญา (Maverick Spend) ได้ เกิดการสั่งซื้อซ้ำซ้อนหรือซื้อของแพง</p>
          <p><strong class="text-slate-800">❌ สิ่งที่ Standard ทำไม่ได้:</strong> ระบบไม่สามารถเข้าใจความหมายเชิงบริบท (Semantic Understanding) ของคำขอซื้อที่เขียนต่างกัน</p>
          <p class="p-1.5 bg-sky-50 border-l-4 border-sky-500 text-sky-950 rounded-r">
            <strong>💡 โซลูชัน Copilot AI:</strong> สแกนข้อความคำขอซื้อของพนักงาน แล้วตรวจจับว่าสินค้านี้มีอยู่ในคลังสาขาอื่นที่กำลังค้างอยู่หรือไม่ หรือจับคู่กับ Vendor Catalog ที่มีสัญญาพิเศษอยู่แล้ว เพื่อรวมคำสั่งซื้อ (Consolidate PO) ประหยัดต้นทุน 10–15%
          </p>
        </div>
      </div>

      <!-- Use Case 2.5 -->
      <div class="card-usecase">
        <div class="flex items-center justify-between mb-1">
          <h3 class="text-xs font-extrabold text-slate-900 flex items-center gap-1.5">
            <span class="w-5 h-5 rounded-full bg-sky-600 text-white flex items-center justify-center text-[10px] font-bold">5</span>
            Landed Cost &amp; Customs Tariff Classification Dispute Copilot
          </h3>
          <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">Landed Cost &amp; Customs HS Code</span>
        </div>
        <div class="space-y-1 text-[11px] text-slate-600">
          <p><strong class="text-slate-800">⚠️ ข้อจำกัดใน D365 &amp; Pain Point:</strong> โมดูล Landed Cost ใน D365 ซับซ้อนมาก การแบ่งเฉลี่ยค่าขนส่งเรือ, ภาษีนำเข้าตามพิกัดศุลกากร (HS Code), และค่า Demurrage ต้องใช้ผู้เชี่ยวชาญ หากศุลกากรปรับแก้พิกัดภาษี การแก้ไขจะติดขัดเป็นสัปดาห์</p>
          <p><strong class="text-slate-800">❌ สิ่งที่ Standard ทำไม่ได้:</strong> ขาดระบบช่วยตรวจสอบและร่างหนังสือโต้แย้งพิกัดภาษีนำเข้า</p>
          <p class="p-1.5 bg-sky-50 border-l-4 border-sky-500 text-sky-950 rounded-r">
            <strong>💡 โซลูชัน Copilot AI:</strong> ตรวจสอบเอกสาร Bill of Lading เทียบกับ D365 Landed Cost Voyage หากตรวจพบว่าพิกัดภาษีของศุลกากรคลาดเคลื่อน Copilot จะค้นหากฎหมายศุลกากรและร่างหนังสืออุทธรณ์พร้อมเอกสารอ้างอิงให้ฝ่ายชิปปิ้งทันที
          </p>
        </div>
      </div>

      <!-- Strategic Value Box for Procurement -->
      <div class="p-3 bg-gradient-to-r from-sky-50 to-indigo-50 border border-sky-200 rounded-xl mt-3">
        <div class="text-[11px] font-black text-sky-900 uppercase tracking-wide mb-1.5">
          🎯 SCM &amp; Procurement Transformation Business Impact
        </div>
        <div class="grid grid-cols-3 gap-2 text-center text-[10px]">
          <div class="p-2 bg-white rounded-lg border border-sky-200/80 shadow-xs">
            <div class="text-sm font-black text-sky-700">10-15%</div>
            <div class="font-bold text-slate-800">Maverick Spend Recovery</div>
            <div class="text-slate-500">รวมศูนย์การซื้อผ่านสัญญาหลัก</div>
          </div>
          <div class="p-2 bg-white rounded-lg border border-sky-200/80 shadow-xs">
            <div class="text-sm font-black text-sky-700">100%</div>
            <div class="font-bold text-slate-800">Price Index Compliance</div>
            <div class="text-slate-500">ตรวจสอบสูตรราคาดัชนีโภคภัณฑ์แม่นยำ</div>
          </div>
          <div class="p-2 bg-white rounded-lg border border-sky-200/80 shadow-xs">
            <div class="text-sm font-black text-sky-700">-80%</div>
            <div class="font-bold text-slate-800">PO Manual Amendment</div>
            <div class="text-slate-500">อัปเดตวันส่งของจากอีเมลอัตโนมัติ</div>
          </div>
        </div>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-1 text-[10px] text-slate-400 text-right">
      Section 3: SCM &amp; Procurement (Part 2/2)
    </div>
  </div>

  <!-- ==================== PAGE 7: PRODUCTION PART 1 (USE CASES 1, 2, 3) ==================== -->
  <div class="page-container">
    <div>
      <!-- Section Header -->
      <div class="flex items-center justify-between border-b-2 border-purple-600 pb-1.5 mb-3">
        <div class="flex items-center gap-2">
          <span class="text-xl">🏭</span>
          <div>
            <span class="text-[10px] font-black tracking-widest text-purple-700 uppercase">Module Deep Dive 03</span>
            <h2 class="text-base font-black text-slate-900">Production &amp; MRP: Top 5 Deep Use Cases (Part 1/2)</h2>
          </div>
        </div>
        <span class="px-2.5 py-0.5 bg-purple-50 text-purple-800 border border-purple-200 rounded-full text-[10px] font-bold">Shop Floor &amp; Planning</span>
      </div>

      <!-- Use Case 3.1 -->
      <div class="card-usecase">
        <div class="flex items-center justify-between mb-1">
          <h3 class="text-xs font-extrabold text-slate-900 flex items-center gap-1.5">
            <span class="w-5 h-5 rounded-full bg-purple-600 text-white flex items-center justify-center text-[10px] font-bold">1</span>
            MRP Planning Optimization "Black-Box" Explainer &amp; Trade-Off Simulator
          </h3>
          <span class="text-[10px] font-bold text-red-600 bg-red-50 border border-red-200 px-1.5 py-0.5 rounded font-black">⭐ #1 Community Pain</span>
        </div>
        <div class="space-y-1 text-[11px] text-slate-600">
          <p><strong class="text-slate-800">⚠️ ข้อจำกัดใน D365 &amp; Pain Point:</strong> นี่คือ Pain Point อันดับ 1 ของ Community D365! ปัจจุบันระบบ Planning Optimization คำนวณแผนจัดซื้อ/ผลิตได้เร็วมาก แต่ผลลัพธ์เป็น "กล่องดำ (Black Box)" แพลนเนอร์ไม่รู้เลยว่าทำไมระบบถึงเลื่อนวันผลิตออเดอร์นี้ออกไป 2 สัปดาห์? ติด Capacity ตรงไหน หรือติด Pegging ตัวไหน?</p>
          <p><strong class="text-slate-800">❌ สิ่งที่ Standard ทำไม่ได้:</strong> ไม่มีคำอธิบายแบบ Human-readable สำหรับการตัดสินใจของ Master Planning</p>
          <p class="p-1.5 bg-purple-50 border-l-4 border-purple-500 text-purple-950 rounded-r">
            <strong>💡 โซลูชัน Copilot AI:</strong> เป็น "Planning Explainer" ให้แพลนเนอร์พิมพ์ถามเป็นภาษาธรรมชาติ: <em>"ทำไมใบสั่งผลิต WO-9921 ถึงถูกเลื่อนไปเดือนหน้า?"</em> Copilot จะไล่ Pegging Tree แล้วตอบว่า: <em>"ติดคอขวดที่เครื่องจักร MC-04 และรอเม็ดพลาสติกจาก PO-102 หากอนุมัติ OT ให้เครื่องจักร MC-04 จำนวน 4 ชม. จะเลื่อนวันเสร็จเร็วขึ้นได้ 5 วัน"</em>
          </p>
        </div>
      </div>

      <!-- Use Case 3.2 -->
      <div class="card-usecase">
        <div class="flex items-center justify-between mb-1">
          <h3 class="text-xs font-extrabold text-slate-900 flex items-center gap-1.5">
            <span class="w-5 h-5 rounded-full bg-purple-600 text-white flex items-center justify-center text-[10px] font-bold">2</span>
            Autonomous Dynamic Shop Floor Resequencing (จัดคิวผลิตใหม่ทันทีเมื่อเครื่องจักรพัง)
          </h3>
          <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">Finite Capacity &amp; Dispatching</span>
        </div>
        <div class="space-y-1 text-[11px] text-slate-600">
          <p><strong class="text-slate-800">⚠️ ข้อจำกัดใน D365 &amp; Pain Point:</strong> เมื่อเครื่องจักรเสียกลางคันหรือมี Rush Order แทรกเข้ามา Finite Scheduling ของ D365 ทำงานแข็งทื่อ หากสั่งรัน Schedule ใหม่ แผนทั้งหมดจะสะเทือน (Schedule Nervousness) และมักละเลยข้อจำกัดหน้างานจริง เช่น ทักษะช่าง, เวลาล้างโมลด์/ล้างถัง (Changeover matrix)</p>
          <p><strong class="text-slate-800">❌ สิ่งที่ Standard ทำไม่ได้:</strong> ไม่สามารถทำ Micro-resequencing ที่กระทบต่อออเดอร์อื่นน้อยที่สุดแบบเรียลไทม์</p>
          <p class="p-1.5 bg-purple-50 border-l-4 border-purple-500 text-purple-950 rounded-r">
            <strong>💡 โซลูชัน Copilot AI:</strong> รับสัญญาณแจ้งเตือนจาก IoT เซนเซอร์หรือ Job Card Device คำนวณเมทริกซ์เวลาล้างเครื่องและทักษะพนักงาน แล้วสร้างลำดับคิวการผลิตใหม่ (Micro-Resequence) ที่ลดเวลา Downtime และยังส่งงานให้ลูกค้ารายใหญ่ได้ตรงเวลา
          </p>
        </div>
      </div>

      <!-- Use Case 3.3 -->
      <div class="card-usecase">
        <div class="flex items-center justify-between mb-1">
          <h3 class="text-xs font-extrabold text-slate-900 flex items-center gap-1.5">
            <span class="w-5 h-5 rounded-full bg-purple-600 text-white flex items-center justify-center text-[10px] font-bold">3</span>
            Deep Scrap &amp; Yield Variance Root-Cause Pattern Mining (หาสาเหตุของเสียสะสม)
          </h3>
          <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">Standard vs. Actual Costing</span>
        </div>
        <div class="space-y-1 text-[11px] text-slate-600">
          <p><strong class="text-slate-800">⚠️ ข้อจำกัดใน D365 &amp; Pain Point:</strong> D365 บันทึก Scrap และ Yield Variance ได้ แต่บอกได้แค่ตัวเลขว่า "รอบนี้มีของเสีย 12% ซึ่งเกินมาตรฐาน 5%" แต่ไม่สามารถระบุได้ว่าทำไมถึงเสีย</p>
          <p><strong class="text-slate-800">❌ สิ่งที่ Standard ทำไม่ได้:</strong> ไม่สามารถเชื่อมโยงมิติแวดล้อม (อุณหภูมิ, ความชื้นหน้างาน, กะการทำงาน) เข้ากับ Lot Attributes ของวัตถุดิบได้</p>
          <p class="p-1.5 bg-purple-50 border-l-4 border-purple-500 text-purple-950 rounded-r">
            <strong>💡 โซลูชัน Copilot AI:</strong> วิเคราะห์ความสัมพันธ์ระหว่างของเสีย กับ Lot วัตถุดิบ, เซนเซอร์สภาพแวดล้อม และประวัติช่างผู้คุมเครื่อง เช่น: <em>"ของเสียที่พุ่งสูงในสัปดาห์นี้สัมพันธ์กับเรซินล็อต L-908 ของซัพพลายเออร์ X ที่ถูกรันในช่วงบ่ายที่ความชื้นในโรงงานสูงเกิน 75%"</em> ช่วยให้โรงงานแก้ปัญหาได้ตรงจุด
          </p>
        </div>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-1 text-[10px] text-slate-400 text-right">
      Section 4: Production &amp; MRP (Part 1/2)
    </div>
  </div>

  <!-- ==================== PAGE 8: PRODUCTION PART 2 (USE CASES 4, 5 + SUMMARY) ==================== -->
  <div class="page-container">
    <div>
      <!-- Section Header -->
      <div class="flex items-center justify-between border-b-2 border-purple-600 pb-1.5 mb-3">
        <div class="flex items-center gap-2">
          <span class="text-xl">🏭</span>
          <div>
            <span class="text-[10px] font-black tracking-widest text-purple-700 uppercase">Module Deep Dive 03</span>
            <h2 class="text-base font-black text-slate-900">Production &amp; MRP: Top 5 Deep Use Cases (Part 2/2)</h2>
          </div>
        </div>
        <span class="px-2.5 py-0.5 bg-purple-50 text-purple-800 border border-purple-200 rounded-full text-[10px] font-bold">Shop Floor &amp; Planning</span>
      </div>

      <!-- Use Case 3.4 -->
      <div class="card-usecase">
        <div class="flex items-center justify-between mb-1">
          <h3 class="text-xs font-extrabold text-slate-900 flex items-center gap-1.5">
            <span class="w-5 h-5 rounded-full bg-purple-600 text-white flex items-center justify-center text-[10px] font-bold">4</span>
            Engineering Change Order (ECO) &amp; BOM Revision Cutover Orchestrator
          </h3>
          <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">Product Lifecycle &amp; BOM Version</span>
        </div>
        <div class="space-y-1 text-[11px] text-slate-600">
          <p><strong class="text-slate-800">⚠️ ข้อจำกัดใน D365 &amp; Pain Point:</strong> เมื่อฝ่ายวิศวกรรมปล่อย BOM/Route Version ใหม่ออกมา การกำหนดวันตัดเปลี่ยน (Cutover Date) ใน D365 มักเกิดปัญหา สต็อกอะไหล่รุ่นเก่ายังเหลือบานเบอะจนต้องตัดเป็น Scrap ขาดทุนย่อยยับ หรือตัดเปลี่ยนช้าเกินไปจนละเมิดมาตรฐานความปลอดภัย</p>
          <p><strong class="text-slate-800">❌ สิ่งที่ Standard ทำไม่ได้:</strong> ขาดการคำนวณจุดตัดเปลี่ยนทางคณิตศาสตร์แบบสมดุลต้นทุน (Cost-Optimal Cutover Point)</p>
          <p class="p-1.5 bg-purple-50 border-l-4 border-purple-500 text-purple-950 rounded-r">
            <strong>💡 โซลูชัน Copilot AI:</strong> จำลองอัตราการใช้ชิ้นส่วนเก่าที่เหลืออยู่ในคลัง เทียบกับออเดอร์ในอนาคตและต้นทุน Scrap แล้วเสนอวัน Effective Date ของ BOM ใหม่ที่ทำให้ใช้อะไหล่เก่าหมดพอดีเป็นศูนย์ (Zero-waste phase-out)
          </p>
        </div>
      </div>

      <!-- Use Case 3.5 -->
      <div class="card-usecase">
        <div class="flex items-center justify-between mb-1">
          <h3 class="text-xs font-extrabold text-slate-900 flex items-center gap-1.5">
            <span class="w-5 h-5 rounded-full bg-purple-600 text-white flex items-center justify-center text-[10px] font-bold">5</span>
            Multimodal Shop Floor Maintenance &amp; SOP Troubleshooting Copilot
          </h3>
          <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">Job Card Device &amp; Asset Management</span>
        </div>
        <div class="space-y-1 text-[11px] text-slate-600">
          <p><strong class="text-slate-800">⚠️ ข้อจำกัดใน D365 &amp; Pain Point:</strong> หน้าจอ Job Card Device มีคู่มือ SOP ให้ดูเป็นไฟล์ PDF ธรรมดา แต่เวลาช่างหน้างานเจอปัญหาเครื่องจักรสะบัด อุณหภูมิขึ้น หรือมีเสียงผิดปกติ ต้องหยุดไลน์แล้วตามหัวหน้าช่างมาดู ทำให้สูญเสีย OEE อย่างมาก</p>
          <p><strong class="text-slate-800">❌ สิ่งที่ Standard ทำไม่ได้:</strong> ไม่รองรับการรับภาพถ่าย/เสียง หรือการโต้ตอบถาม-ตอบปัญหากับคู่มือเครื่องจักรแบบสองทาง</p>
          <p class="p-1.5 bg-purple-50 border-l-4 border-purple-500 text-purple-950 rounded-r">
            <strong>💡 โซลูชัน Copilot AI:</strong> ฝังอยู่ในแท็บเล็ตหน้างาน ช่างสามารถถ่ายรูปชิ้นงานที่แตกหัก หรือพิมพ์บอกอาการเสียง Copilot จะค้นประวัติการซ่อมใน Asset Management และคู่มือ OEM ส่งคลิปวิธีตั้งค่าและจุดที่ต้องไขน็อตแก้ไขให้ช่างทำตามได้ทันทีใน 2 นาที
          </p>
        </div>
      </div>

      <!-- Strategic Value Box for Production -->
      <div class="p-3 bg-gradient-to-r from-purple-50 to-pink-50 border border-purple-200 rounded-xl mt-3">
        <div class="text-[11px] font-black text-purple-900 uppercase tracking-wide mb-1.5">
          🎯 Production &amp; MRP Transformation Business Impact
        </div>
        <div class="grid grid-cols-3 gap-2 text-center text-[10px]">
          <div class="p-2 bg-white rounded-lg border border-purple-200/80 shadow-xs">
            <div class="text-sm font-black text-purple-700">+18%</div>
            <div class="font-bold text-slate-800">Shop Floor OEE</div>
            <div class="text-slate-500">ลดเวลา Downtime จากการแก้ไขทันใจ</div>
          </div>
          <div class="p-2 bg-white rounded-lg border border-purple-200/80 shadow-xs">
            <div class="text-sm font-black text-purple-700">0% Scrap</div>
            <div class="font-bold text-slate-800">ECO BOM Cutover</div>
            <div class="text-slate-500">เคลียร์สต็อกอะไหล่เก่าหมดพอดี</div>
          </div>
          <div class="p-2 bg-white rounded-lg border border-purple-200/80 shadow-xs">
            <div class="text-sm font-black text-purple-700">-40%</div>
            <div class="font-bold text-slate-800">Planning Meeting Hours</div>
            <div class="text-slate-500">เข้าใจเหตุผลของ MRP ทันทีโดยไม่ต้องประชุม</div>
          </div>
        </div>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-1 text-[10px] text-slate-400 text-right">
      Section 4: Production &amp; MRP (Part 2/2)
    </div>
  </div>

  <!-- ==================== PAGE 9: BUSINESS IMPACT & FTH IP ROADMAP ==================== -->
  <div class="page-container">
    <div>
      <!-- Section Header -->
      <div class="flex items-center justify-between border-b-2 border-red-600 pb-1.5 mb-3">
        <div>
          <span class="text-[10px] font-black tracking-widest text-red-600 uppercase">Strategic Value &amp; Commercialization</span>
          <h2 class="text-base font-black text-slate-900">5. มูลค่าทางธุรกิจและแนวทางการพัฒนาเป็น Fujitsu IP Asset</h2>
        </div>
        <span class="px-2.5 py-0.5 bg-red-50 text-red-700 border border-red-200 rounded-full text-[10px] font-bold">Executive Summary &amp; ROI</span>
      </div>

      <!-- ROI Impact Summary Cards -->
      <div class="grid grid-cols-4 gap-2 mb-3">
        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-center">
          <div class="text-xl font-black text-emerald-600 mb-0.5">-75%</div>
          <div class="text-[10px] font-bold text-slate-800">Variance Investigation</div>
          <div class="text-[9px] text-slate-500">ลดเวลาสืบหาของหายเหลือ 15 นาที</div>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-center">
          <div class="text-xl font-black text-sky-600 mb-0.5">10-15%</div>
          <div class="text-[10px] font-bold text-slate-800">Maverick Spend Cut</div>
          <div class="text-[9px] text-slate-500">ประหยัดงบจัดซื้อผ่าน Contract Catalog</div>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-center">
          <div class="text-xl font-black text-purple-600 mb-0.5">+18%</div>
          <div class="text-[10px] font-bold text-slate-800">Shop Floor OEE</div>
          <div class="text-[9px] text-slate-500">ลด Downtime จากการแก้เครื่องจักรทันใจ</div>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-center">
          <div class="text-xl font-black text-red-600 mb-0.5">0% Scrap</div>
          <div class="text-[10px] font-bold text-slate-800">ECO BOM Cutover</div>
          <div class="text-[9px] text-slate-500">กำจัดอะไหล่รุ่นเก่าค้างสต็อกสมบูรณ์</div>
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
            <p class="text-[9px] text-slate-600 leading-snug">สำรวจ Dataverse Entity, วิเคราะห์ประวัติ Cycle Count &amp; Scrap variance, กำหนดขอบเขต 2 Use Cases แรก</p>
          </div>
          <div class="p-2 rounded-lg bg-slate-50 border-l-4 border-l-sky-500 border border-slate-200">
            <div class="font-bold text-sky-900 text-[10px] mb-0.5">Week 3–4: AI Copilot Build</div>
            <p class="text-[9px] text-slate-600 leading-snug">ตั้งค่า Azure OpenAI, RAG บนสัญญาคู่ค้า/คู่มือ SOP และพัฒนา Copilot Studio custom plugins</p>
          </div>
          <div class="p-2 rounded-lg bg-slate-50 border-l-4 border-l-purple-500 border border-slate-200">
            <div class="font-bold text-purple-900 text-[10px] mb-0.5">Week 5–6: D365 Integration</div>
            <p class="text-[9px] text-slate-600 leading-snug">เชื่อมต่อ D365 Business Events, ทดสอบ Human-in-the-Loop approval และทดสอบ User Acceptance (UAT)</p>
          </div>
          <div class="p-2 rounded-lg bg-slate-50 border-l-4 border-l-emerald-500 border border-slate-200">
            <div class="font-bold text-emerald-900 text-[10px] mb-0.5">Week 7–8: Go-Live &amp; Scale</div>
            <p class="text-[9px] text-slate-600 leading-snug">Deploy บน Production Tenant, ประเมินผลลัพธ์ ROI จริง และจัดทำแผนขยายผลสู่โมดูลอื่นๆ</p>
          </div>
        </div>
      </div>

      <!-- Fujitsu IP Proposition -->
      <div class="p-3 rounded-xl bg-gradient-to-r from-red-50 to-orange-50 border border-red-200 mb-2">
        <div class="text-[10px] font-black text-red-700 uppercase tracking-wider mb-1">🏆 Fujitsu Thailand Competitive Edge</div>
        <p class="text-[11px] text-slate-800 leading-relaxed">
          การนำเสนอโซลูชัน AI เชิงลึกเหล่านี้ ไม่เพียงแต่แก้ปัญหาจริงให้ลูกค้าองค์กร แต่ยังยกระดับให้ <strong>Fujitsu Thailand (FTH)</strong> กลายเป็นผู้ให้บริการรายแรกในเอเชียตะวันออกเฉียงใต้ที่มี <strong>"Proprietary AI Accelerators for D365 SCM"</strong> เป็นทรัพย์สินทางปัญญา (IP Asset) ของตนเอง ซึ่งยากที่คู่แข่งจะลอกเลียนแบบได้ และสร้างความเชื่อมั่นสูงสุดแก่กลุ่มทุนญี่ปุ่นและบรรษัทข้ามชาติชั้นนำ
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
    print("Writing refined HTML whitepaper...")
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
                header_template='<div style="font-size: 8px; color: #94a3b8; width: 100%; display: flex; justify-content: space-between; padding: 0 10mm; font-family: sans-serif; font-weight: 600;"><span>FUJITSU THAILAND (FTH) • D365 ADVANCED COPILOT AI WHITEPAPER</span><span>CONFIDENTIAL</span></div>',
                footer_template='<div style="font-size: 8px; color: #94a3b8; width: 100%; display: flex; justify-content: space-between; padding: 0 10mm; font-family: sans-serif;"><span>© 2026 Fujitsu Thailand Co., Ltd. All rights reserved.</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>'
            )
            print(f"Successfully generated PDF -> {out_pdf} ({os.path.getsize(out_pdf)//1024} KB)")

        await browser.close()
    print("PDF generation complete!")

if __name__ == "__main__":
    asyncio.run(main())
