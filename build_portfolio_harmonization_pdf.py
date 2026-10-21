import asyncio
import os
import sys
from playwright.async_api import async_playwright

HTML_PATH = r"c:\FTH\FTH-D365_FO\FTH_D365_Localization_Portfolio_Harmonization.html"
OUT_PDF_PATHS = [
    r"c:\FTH\FTH-D365_FO\FTH_D365_Localization_Portfolio_Harmonization.pdf",
    r"c:\FTH\FTH-D365_FO\assets\FTH_D365_Localization_Portfolio_Harmonization.pdf",
    r"C:\Users\witit\.gemini\antigravity\brain\7bc4ceac-b79a-4881-9938-a5db0d7782a2\FTH_D365_Localization_Portfolio_Harmonization.pdf",
]

def build_html_content():
    return """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <title>Master Localization &amp; AI Portfolio Harmonization Report - Fujitsu Thailand (FTH)</title>
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
    .card-box {
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 10px 14px;
      background: #ffffff;
      box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }
    .badge-tag {
      font-size: 8.5px;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }
  </style>
</head>
<body class="text-slate-900 text-xs">

  <!-- ==================== PAGE 1: COVER & EXECUTIVE DASHBOARD ==================== -->
  <div class="page-container">
    <div>
      <!-- Top Branding Bar -->
      <div class="flex items-center justify-between border-b border-slate-200 pb-3 mb-4">
        <div class="flex items-center gap-3">
          <div class="px-3 py-1 bg-red-600 text-white font-extrabold text-[11px] tracking-wider rounded uppercase">
            FUJITSU THAILAND
          </div>
          <span class="text-slate-300">|</span>
          <span class="text-[11px] font-bold text-slate-600 uppercase tracking-wide">Enterprise Advisory &amp; AI Practice</span>
        </div>
        <div class="flex items-center gap-2">
          <span class="text-[11px] font-semibold text-slate-500">Initiative:</span>
          <span class="px-2.5 py-0.5 rounded bg-sky-50 text-sky-700 border border-sky-200 font-bold text-[11px]">D365FO Localization Harmonization</span>
        </div>
      </div>

      <!-- Main Title Block -->
      <div class="space-y-2 max-w-3xl mb-4">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-900 text-white text-[10px] font-bold uppercase tracking-wider">
          <span class="w-2 h-2 rounded-full bg-red-500 animate-pulse"></span>
          Executive Portfolio Harmonization &amp; Overlap Analysis
        </div>

        <h1 class="text-2xl font-black text-slate-900 tracking-tight leading-tight">
          รายงานวิเคราะห์ความซ้ำซ้อน &amp; การจัดพอร์ตโฟลิโอเชิงบูรณาการ
        </h1>
        <p class="text-sm font-bold text-sky-700">
          ผสานข้อเสนอ FTH Localization (17 ข้อ) กับ Top 5 Finance AI และ Module Top 5 (SCM / Inventory / Production)
        </p>
        <p class="text-[11px] text-slate-600 leading-relaxed font-normal">
          รายงานฉบับนี้ทำการวิเคราะห์เปรียบเทียบไขว้ 3 ทิศทางระหว่างข้อเสนอการพัฒนา Localize ทั้งหมดในโครงการ เพื่อตรวจจับ 
          <strong>จุดที่ซ้ำซ้อนกันโดยตรง, จุดที่เกื้อหนุนกัน, และจุดเฉพาะทาง</strong> เพื่อนำมาปรับระเบียบพอร์ตโฟลิโอใหม่ 
          ช่วยตัดลด Man-Days ที่ซ้ำซ้อนทิ้ง ป้องกันความขัดแย้งของระบบ และส่งมอบแพ็กเกจโซลูชันที่ทรงพลังที่สุดให้ลูกค้า
        </p>
      </div>

      <!-- Comparison Metrics Dashboard Grid -->
      <div class="grid grid-cols-4 gap-3 mb-4">
        <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 text-center">
          <div class="text-[10px] font-bold text-slate-500 uppercase mb-0.5">Total Scope Evaluated</div>
          <div class="text-xl font-black text-slate-800">37 Items</div>
          <p class="text-[9px] text-slate-500">17 FTH + 5 Finance + 15 Ops</p>
        </div>
        <div class="p-3 rounded-xl bg-rose-50 border border-rose-200 text-center">
          <div class="text-[10px] font-bold text-rose-700 uppercase mb-0.5">Direct Overlaps</div>
          <div class="text-xl font-black text-rose-600">4 Key Areas</div>
          <p class="text-[9px] text-rose-700">ซ้ำซ้อนในโจทย์และฟังก์ชัน</p>
        </div>
        <div class="p-3 rounded-xl bg-emerald-50 border border-emerald-200 text-center">
          <div class="text-[10px] font-bold text-emerald-700 uppercase mb-0.5">Effort Eliminated</div>
          <div class="text-xl font-black text-emerald-600">45-50 MD</div>
          <p class="text-[9px] text-emerald-700">ตัดงานซ้ำซ้อนทิ้งทันที</p>
        </div>
        <div class="p-3 rounded-xl bg-sky-50 border border-sky-200 text-center">
          <div class="text-[10px] font-bold text-sky-700 uppercase mb-0.5">Unified Strategy</div>
          <div class="text-xl font-black text-sky-600">1 Product Suite</div>
          <p class="text-[9px] text-sky-700">Core X++ Engine + Smart AI</p>
        </div>
      </div>

      <!-- Strategic Overview Box -->
      <div class="p-3.5 bg-gradient-to-r from-slate-900 to-slate-800 text-white rounded-xl mb-3 shadow-xs">
        <div class="flex items-center justify-between">
          <div>
            <div class="text-[10px] font-black text-amber-400 uppercase tracking-wider mb-0.5">Executive Harmonization Summary</div>
            <p class="text-[11px] text-slate-200 leading-snug">
              เมื่อนำทั้ง 3 โครงการมาทาบกัน พบว่า <strong>FTH ข้อ 3 (DMF Tax Info) ซ้ำกับ AP Invoice AI 100%</strong> และ <strong>FTH ข้อ 6 &amp; 7 (Inquiries) ซ้ำกับ Copilot Chat 100%</strong> การรวมศูนย์พอร์ตโฟลิโอใหม่จะทำให้ FTH ประหยัดงบพัฒนาไปได้กว่า 45 Man-Days โดยไม่ต้องเขียนหน้าจอแบบเดิม และสร้างแพ็กเกจ <strong>"Core Tax Compliance + Generative AI"</strong> ที่ไร้คู่แข่งในตลาด
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Metadata Footer of Cover Page -->
    <div class="border-t border-slate-200 pt-2 flex items-center justify-between text-[10px] text-slate-500">
      <div>
        <span class="font-bold text-slate-800">Fujitsu (Thailand) Co., Ltd. (FTH)</span> | Enterprise Portfolio Steering Committee
      </div>
      <div>
        <span>Document Ref: <strong>FTH-PORTFOLIO-HARMONIZATION-2026</strong></span> • <span>October 2026</span>
      </div>
    </div>
  </div>

  <!-- ==================== PAGE 2: 3-WAY MAPPING MATRIX ==================== -->
  <div class="page-container">
    <div>
      <!-- Section Title -->
      <div class="flex items-center justify-between border-b-2 border-slate-900 pb-1.5 mb-2.5">
        <div>
          <span class="text-[10px] font-black tracking-widest text-red-600 uppercase">Cross-Referencing Analysis</span>
          <h2 class="text-base font-black text-slate-900">1. ตารางเปรียบเทียบความสัมพันธ์และความซ้ำซ้อน (3-Way Mapping Matrix)</h2>
        </div>
        <div class="text-right">
          <span class="px-2 py-0.5 bg-slate-100 rounded text-[9px] font-bold text-slate-600">37 Initiatives Mapped</span>
        </div>
      </div>

      <!-- Matrix Table -->
      <div class="border border-slate-200 rounded-xl overflow-hidden mb-2 shadow-xs">
        <table class="w-full text-[9.5px] text-left">
          <thead class="bg-slate-900 text-white font-bold uppercase text-[8.5px]">
            <tr>
              <th class="p-2 w-1/5">หัวข้อทางธุรกิจ (Domain)</th>
              <th class="p-2 w-1/4 bg-slate-800 text-slate-300">FTH Localize (17 ข้อเดิม)</th>
              <th class="p-2 w-1/4 bg-sky-950 text-sky-200">Top 5 Finance (Thai Tax AI)</th>
              <th class="p-2 w-1/4 bg-purple-950 text-purple-200">Module Top 5 (Ops &amp; SCM)</th>
              <th class="p-2 w-20 text-center">สถานะความซ้ำ</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-200 text-slate-700">
            <!-- Overlap 1 -->
            <tr class="bg-rose-50/40">
              <td class="p-1.5 font-bold text-slate-900">
                1. การนำเข้าข้อมูลภาษี &amp; บิล
              </td>
              <td class="p-1.5">
                <strong>ข้อ 3:</strong> DMF Entity นำเข้า Tax ID, สาขา, วันที่ใบกำกับภาษี ผ่าน Excel (9 MD)
              </td>
              <td class="p-1.5 font-medium text-sky-950 bg-sky-50/40">
                <strong>ข้อ 1:</strong> AP Invoice AI สกัดเลข 13 หลัก, สาขา, VAT/WHT จาก PDF &amp; 3-Way Match
              </td>
              <td class="p-1.5 text-slate-400">
                -
              </td>
              <td class="p-1.5 text-center">
                <span class="badge-tag bg-rose-100 text-rose-800">ซ้ำกัน 100%</span>
              </td>
            </tr>

            <!-- Overlap 2 -->
            <tr class="bg-amber-50/30">
              <td class="p-1.5 font-bold text-slate-900">
                2. การตรวจภาษี WHT &amp; Unrealized VAT
              </td>
              <td class="p-1.5">
                <strong>ข้อ 1 &amp; 2:</strong> เพิ่มฟิลด์ Reverse Unrealized VAT และรายงาน AR WHT (18 MD)
              </td>
              <td class="p-1.5 font-medium text-sky-950 bg-sky-50/40">
                <strong>ข้อ 2:</strong> Thai Tax Compliance Copilot ตรวจเช็ค Tax ID, สาขา, WHT ก่อนปิดงวด
              </td>
              <td class="p-1.5 text-slate-400">
                -
              </td>
              <td class="p-1.5 text-center">
                <span class="badge-tag bg-amber-100 text-amber-800">เกื้อหนุนกัน</span>
              </td>
            </tr>

            <!-- Overlap 3 -->
            <tr class="bg-amber-50/30">
              <td class="p-1.5 font-bold text-slate-900">
                3. ใบกำกับภาษี &amp; ใบเสร็จรับเงิน
              </td>
              <td class="p-1.5">
                <strong>ข้อ 8:</strong> SSRS Form ใบเสร็จ/ใบกำกับภาษี Detail/Summary (23 MD)
              </td>
              <td class="p-1.5 font-medium text-sky-950 bg-sky-50/40">
                <strong>ข้อ 3:</strong> e-Tax Invoice &amp; e-Receipt Control ตรวจสอบ XML/PDF ตามเกณฑ์ สพธ.
              </td>
              <td class="p-1.5 text-slate-400">
                -
              </td>
              <td class="p-1.5 text-center">
                <span class="badge-tag bg-amber-100 text-amber-800">วิวัฒนาการ</span>
              </td>
            </tr>

            <!-- Overlap 4 -->
            <tr class="bg-rose-50/40">
              <td class="p-1.5 font-bold text-slate-900">
                4. ปัญหา Voucher ย่อยกระจัดกระจาย
              </td>
              <td class="p-1.5">
                <strong>ข้อ 4:</strong> รวม Voucher ย่อยเข้าใบหลัก (17 MD)<br>
                <strong>ข้อ 11, 14:</strong> พิมพ์ Voucher ล่วงหน้าและเป็นชุด (26 MD)
              </td>
              <td class="p-1.5 font-medium text-sky-950 bg-sky-50/40">
                <strong>ข้อ 4:</strong> Continuous Reconciliation AI ตรวจสอบกระทบยอด Sub-ledger กับ GL
              </td>
              <td class="p-1.5 text-slate-400">
                -
              </td>
              <td class="p-1.5 text-center">
                <span class="badge-tag bg-rose-100 text-rose-800">แก้จุดเดียวกัน</span>
              </td>
            </tr>

            <!-- Overlap 5 -->
            <tr class="bg-rose-50/40">
              <td class="p-1.5 font-bold text-slate-900">
                5. สอบถามยอดค้างส่ง/ค้างรับ
              </td>
              <td class="p-1.5">
                <strong>ข้อ 6 &amp; 7:</strong> พัฒนาฟอร์ม X++ Inquiry ใหม่ดูยอด SO/PO (20 MD)
              </td>
              <td class="p-1.5 text-slate-400">
                -
              </td>
              <td class="p-1.5 font-medium text-purple-950 bg-purple-50/40">
                <strong>SCM ข้อ 1:</strong> Copilot แชตถามยอดค้างส่ง และเชื่อมโยงอีเมลคู่ค้าอัตโนมัติ
              </td>
              <td class="p-1.5 text-center">
                <span class="badge-tag bg-rose-100 text-rose-800">ซ้ำซ้อนฟังก์ชัน</span>
              </td>
            </tr>

            <!-- Unique 1 -->
            <tr class="bg-white">
              <td class="p-1.5 font-bold text-slate-900">
                6. งานเฉพาะจุดการเงิน/ธนาคาร/FA
              </td>
              <td class="p-1.5">
                <strong>ข้อ 5, 9, 10, 12, 13, 15, 16, 17:</strong> Selling/Buying FX, Split FA, Bank Route (55 MD)
              </td>
              <td class="p-1.5 text-slate-400">
                -
              </td>
              <td class="p-1.5 text-slate-400">
                -
              </td>
              <td class="p-1.5 text-center">
                <span class="badge-tag bg-emerald-100 text-emerald-800">เฉพาะ FTH</span>
              </td>
            </tr>

            <!-- Unique 2 -->
            <tr class="bg-white">
              <td class="p-1.5 font-bold text-slate-900">
                7. งานโรงงาน คลัง และซัพพลายเชนลึก
              </td>
              <td class="p-1.5 text-slate-400">
                -
              </td>
              <td class="p-1.5 text-slate-400">
                -
              </td>
              <td class="p-1.5 font-medium text-purple-950 bg-purple-50/40">
                <strong>10 Use Cases:</strong> MRP Black-box, Resequencing, Scrap Mining, FEFO, Vendor Risk
              </td>
              <td class="p-1.5 text-center">
                <span class="badge-tag bg-purple-100 text-purple-800">เฉพาะ Module</span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Quick Summary of Overlap Count -->
      <div class="grid grid-cols-3 gap-2 text-[10px]">
        <div class="p-2 bg-rose-50 border border-rose-200 rounded-lg text-center">
          <div class="font-extrabold text-rose-800">🔴 จุดซ้ำซ้อนโดยตรง (3 จุดใหญ่)</div>
          <p class="text-[9px] text-slate-600">นำเข้าบิล (DMF vs AI), ฟอร์ม Inquiry, การรวม Voucher</p>
        </div>
        <div class="p-2 bg-amber-50 border border-amber-200 rounded-lg text-center">
          <div class="font-extrabold text-amber-800">🟡 จุดเกื้อหนุนกัน (2 จุดใหญ่)</div>
          <p class="text-[9px] text-slate-600">ตารางภาษี X++ ทำหน้าที่เป็นฐานข้อมูลให้ AI Pre-validation</p>
        </div>
        <div class="p-2 bg-emerald-50 border border-emerald-200 rounded-lg text-center">
          <div class="font-extrabold text-emerald-800">🟢 จุดเฉพาะทางไม่ซ้ำกัน</div>
          <p class="text-[9px] text-slate-600">งาน FX/FA ฐานราก และงานโรงงาน Manufacturing เชิงลึก</p>
        </div>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-1 text-[10px] text-slate-400 text-right">
      Section 1: 3-Way Overlap Mapping Matrix
    </div>
  </div>

  <!-- ==================== PAGE 3: DEEP DIVE ON DIRECT OVERLAPS ==================== -->
  <div class="page-container">
    <div>
      <!-- Section Title -->
      <div class="flex items-center justify-between border-b-2 border-rose-600 pb-1.5 mb-2.5">
        <div>
          <span class="text-[10px] font-black tracking-widest text-rose-600 uppercase">Conflict &amp; Redundancy Analysis</span>
          <h2 class="text-base font-black text-slate-900">2. เจาะลึกจุดซ้ำซ้อนโดยตรง &amp; การตัดสินใจเลือกแนวทาง (Trade-Offs)</h2>
        </div>
        <span class="px-2 py-0.5 bg-rose-50 text-rose-700 rounded text-[9px] font-bold">Rationalization Decision</span>
      </div>

      <!-- Deep Dive 1 -->
      <div class="card-box mb-2.5 border-l-4 border-l-rose-500">
        <div class="flex items-center justify-between mb-1">
          <h3 class="font-black text-slate-900 text-[11px] flex items-center gap-1.5">
            <span class="px-1.5 py-0.5 rounded bg-rose-600 text-white font-bold text-[9px]">จุดซ้ำที่ 1</span>
            การนำเข้าข้อมูลภาษี: FTH ข้อ 3 (DMF - 9 MD) vs. Top 5 Finance ข้อ 1 (AP Invoice AI)
          </h3>
          <span class="badge-tag bg-rose-100 text-rose-800">ซ้ำกัน 100%</span>
        </div>
        <div class="grid grid-cols-2 gap-2 text-[10px] mb-1.5">
          <div class="p-1.5 bg-slate-50 rounded border border-slate-200">
            <div class="font-bold text-slate-800 text-[9.5px]">สิ่งที่ทีมงานเสนอ (FTH ข้อ 3):</div>
            <p class="text-slate-600 text-[9px]">เขียน DMF Entity เพื่อให้คนนั่งกรอกตาราง Excel นำเข้าเลขที่บิล, วันที่, Tax Branch และ Tax ID เข้าสมุดรายวัน</p>
          </div>
          <div class="p-1.5 bg-sky-50 rounded border border-sky-200">
            <div class="font-bold text-sky-900 text-[9.5px]">สิ่งที่อยู่ใน Top 5 Finance (ข้อ 1):</div>
            <p class="text-slate-600 text-[9px]">ใช้ Azure Document Intelligence อ่านไฟล์ PDF/รูปถ่ายบิลไทย สกัดเลข 13 หลัก, สาขา, ยอด VAT แล้วสร้าง Journal ให้อัตโนมัติ</p>
          </div>
        </div>
        <p class="text-[9.5px] text-slate-800 bg-rose-50/70 p-1.5 rounded border border-rose-200 leading-snug">
          <strong>⚖️ การตัดสินใจเชิงกลยุทธ์:</strong> <strong>"ตัดข้อ 3 ของทีมงานทิ้ง"</strong> แล้วใช้ AP Invoice AI แทน เพราะหากมี AI สกัดข้อมูลจากบิลให้อัตโนมัติแล้ว จะไม่มีพนักงานคนใดต้องการนั่งพิมพ์ Excel เพื่ออัปโหลดอีกต่อไป ช่วยประหยัดเวลา Dev 9 MD ทันที
        </p>
      </div>

      <!-- Deep Dive 2 -->
      <div class="card-box mb-2.5 border-l-4 border-l-amber-500">
        <div class="flex items-center justify-between mb-1">
          <h3 class="font-black text-slate-900 text-[11px] flex items-center gap-1.5">
            <span class="px-1.5 py-0.5 rounded bg-amber-600 text-white font-bold text-[9px]">จุดซ้ำที่ 2</span>
            หน้าจอสอบถามยอดค้าง: FTH ข้อ 6 &amp; 7 (Inquiries - 20 MD) vs. Copilot SCM Assistant
          </h3>
          <span class="badge-tag bg-amber-100 text-amber-800">ซ้ำซ้อนเชิงฟังก์ชัน</span>
        </div>
        <div class="grid grid-cols-2 gap-2 text-[10px] mb-1.5">
          <div class="p-1.5 bg-slate-50 rounded border border-slate-200">
            <div class="font-bold text-slate-800 text-[9.5px]">สิ่งที่ทีมงานเสนอ (FTH ข้อ 6 &amp; 7):</div>
            <p class="text-slate-600 text-[9px]">สร้างฟอร์ม X++ ใหม่ 2 หน้าจอ เพื่อดู Order Qty, Packing Slip Qty, Invoice Qty และ Remaining Qty ของ SO/PO</p>
          </div>
          <div class="p-1.5 bg-purple-50 rounded border border-purple-200">
            <div class="font-bold text-purple-900 text-[9.5px]">สิ่งที่อยู่ใน Module Top 5 (SCM Copilot):</div>
            <p class="text-slate-600 text-[9px]">ให้ผู้ใช้พิมพ์ถามภาษาธรรมชาติผ่าน Copilot: <em>"PO ไหนยังส่งของไม่ครบ"</em> หรือใช้ Standard Open Order Workspace</p>
          </div>
        </div>
        <p class="text-[9.5px] text-slate-800 bg-amber-50/70 p-1.5 rounded border border-amber-200 leading-snug">
          <strong>⚖️ การตัดสินใจเชิงกลยุทธ์:</strong> <strong>"ไม่สร้างฟอร์มใหม่ 20 MD"</strong> เนื่องจาก D365 Standard มี Open Order Line Workspace ที่ Personalize ได้อยู่แล้ว และ Copilot AI ตอบคำถามเหล่านี้ได้ดีกว่า ประหยัด Effort ได้ถึง 20 MD
        </p>
      </div>

      <!-- Deep Dive 3 -->
      <div class="card-box border-l-4 border-l-rose-500">
        <div class="flex items-center justify-between mb-1">
          <h3 class="font-black text-slate-900 text-[11px] flex items-center gap-1.5">
            <span class="px-1.5 py-0.5 rounded bg-rose-600 text-white font-bold text-[9px]">จุดซ้ำที่ 3</span>
            ปัญหา Voucher ย่อย: FTH ข้อ 4 (17 MD) &amp; ข้อ 11, 14 (26 MD) vs. Continuous Recon AI
          </h3>
          <span class="badge-tag bg-rose-100 text-rose-800">แก้โจทย์เดียวกันคนละวิธี</span>
        </div>
        <div class="grid grid-cols-2 gap-2 text-[10px] mb-1.5">
          <div class="p-1.5 bg-slate-50 rounded border border-slate-200">
            <div class="font-bold text-slate-800 text-[9.5px]">สิ่งที่ทีมงานเสนอ (FTH ข้อ 4, 11, 14):</div>
            <p class="text-slate-600 text-[9px]">แก้ Posting Engine รวบ Voucher ภาษี/WHT เข้าใบหลัก และเขียนลูปพิมพ์ Voucher ออกมาตรวจด้วยตาเปล่า (รวม 43 MD)</p>
          </div>
          <div class="p-1.5 bg-sky-50 rounded border border-sky-200">
            <div class="font-bold text-sky-900 text-[9.5px]">สิ่งที่อยู่ใน Top 5 Finance (ข้อ 4):</div>
            <p class="text-slate-600 text-[9px]">ใช้ AI ทำ Continuous Reconciliation ตรวจกระทบยอด Sub-ledger กับ GL และอธิบาย Voucher อัตโนมัติ</p>
          </div>
        </div>
        <p class="text-[9.5px] text-slate-800 bg-rose-50/70 p-1.5 rounded border border-rose-200 leading-snug">
          <strong>⚖️ การตัดสินใจเชิงกลยุทธ์:</strong> <strong>"ปฏิเสธการแก้ Core Posting Voucher รวม"</strong> เพราะเสี่ยงทำให้ Trial Balance ไม่ดุล และผิดหลัก Audit Trail ให้ใช้ Continuous Reconciliation AI ในการสืบย้อนความสัมพันธ์ของ Voucher แทน ปลอดภัยกว่า 100%
        </p>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-1 text-[10px] text-slate-400 text-right">
      Section 2: Detailed Redundancy &amp; Trade-off Analysis
    </div>
  </div>

  <!-- ==================== PAGE 4: UNIFIED TARGET PORTFOLIO ==================== -->
  <div class="page-container">
    <div>
      <!-- Section Title -->
      <div class="flex items-center justify-between border-b-2 border-emerald-600 pb-1.5 mb-2.5">
        <div>
          <span class="text-[10px] font-black tracking-widest text-emerald-700 uppercase">Target Architecture</span>
          <h2 class="text-base font-black text-slate-900">3. สถาปัตยกรรมพอร์ตโฟลิโอใหม่ที่ควบรวมแล้ว (Unified Product Suite)</h2>
        </div>
        <span class="px-2 py-0.5 bg-emerald-50 text-emerald-800 rounded text-[9px] font-bold">Consolidated Portfolio</span>
      </div>

      <p class="text-[10px] text-slate-600 mb-2">
        จากการตัดสิ่งที่ซ้ำซ้อนออก เราสามารถจัดระเบียบพอร์ตโฟลิโอใหม่ของ <strong>Fujitsu Thailand (FTH)</strong> ออกเป็น <strong>3 เสาหลักที่ชัดเจน ไม่ทับซ้อนกัน</strong> ดังนี้:
      </p>

      <!-- 3 Pillars Grid -->
      <div class="grid grid-cols-3 gap-2.5 mb-3 text-[10px]">
        <!-- Pillar 1 -->
        <div class="p-2.5 rounded-xl bg-amber-50/70 border border-amber-200">
          <div class="flex items-center justify-between mb-1 border-b border-amber-200 pb-1">
            <span class="font-extrabold text-amber-900 text-[11px]">เสาหลักที่ 1: Core Tax X++</span>
            <span class="badge-tag bg-amber-200 text-amber-900">~50-60 MD</span>
          </div>
          <div class="text-[9px] font-bold text-slate-800 mb-1">ฐานรากภาษีสรรพากร (Thai Tax Foundation)</div>
          <p class="text-slate-600 text-[9px] mb-2">
            ทำเฉพาะข้อกำหนดที่กฎหมายภาษีไทยบังคับตายตัว เพื่อความแม่นยำทางบัญชี 100%:
          </p>
          <ul class="list-disc list-inside space-y-0.5 text-[9px] text-slate-700 font-medium">
            <li><strong>FTH ข้อ 1:</strong> Reverse Unrealized VAT ฟิลด์ &amp; รายงาน</li>
            <li><strong>FTH ข้อ 2:</strong> AR Withholding Tax Journal Report</li>
            <li><strong>FTH ข้อ 8:</strong> แบบฟอร์มใบกำกับภาษี/ใบเสร็จเต็มรูป</li>
            <li><strong>FTH ข้อ 10:</strong> แยก Buying &amp; Selling Exchange Rate</li>
            <li><strong>FTH ข้อ 12:</strong> Split Fixed Asset by Quantity</li>
          </ul>
        </div>

        <!-- Pillar 2 -->
        <div class="p-2.5 rounded-xl bg-sky-50/70 border border-sky-200">
          <div class="flex items-center justify-between mb-1 border-b border-sky-200 pb-1">
            <span class="font-extrabold text-sky-900 text-[11px]">เสาหลักที่ 2: Smart AI Localize</span>
            <span class="badge-tag bg-sky-200 text-sky-900">Core IP Package</span>
          </div>
          <div class="text-[9px] font-bold text-slate-800 mb-1">โซลูชันชูโรงขายลูกค้า (Primary Revenue Engine)</div>
          <p class="text-slate-600 text-[9px] mb-2">
            ผสาน Top 5 Finance AI เข้ามาทดแทนงานคีย์มือและงานตรวจสอบกระดาษ:
          </p>
          <ul class="list-disc list-inside space-y-0.5 text-[9px] text-slate-700 font-medium">
            <li><strong>AP Invoice AI:</strong> แทนที่ FTH ข้อ 3 (อ่านบิลอัตโนมัติ)</li>
            <li><strong>Tax Compliance Copilot:</strong> ตรวจ 13 หลัก/สาขาก่อนปิดงวด</li>
            <li><strong>e-Tax &amp; e-Receipt:</strong> ควบคุม XML &amp; Digital Signature</li>
            <li><strong>Continuous Recon Agent:</strong> ตรวจสอบ Voucher ข้ามตาราง</li>
            <li><strong>Finance &amp; Tax Assistant:</strong> แชตถามข้อกฎหมายและแนวทางลงบัญชี</li>
          </ul>
        </div>

        <!-- Pillar 3 -->
        <div class="p-2.5 rounded-xl bg-purple-50/70 border border-purple-200">
          <div class="flex items-center justify-between mb-1 border-b border-purple-200 pb-1">
            <span class="font-extrabold text-purple-900 text-[11px]">เสาหลักที่ 3: SCM &amp; Plant AI</span>
            <span class="badge-tag bg-purple-200 text-purple-900">Add-On Expansion</span>
          </div>
          <div class="text-[9px] font-bold text-slate-800 mb-1">โซลูชันเสริมสำหรับโรงงาน (Manufacturing Add-on)</div>
          <p class="text-slate-600 text-[9px] mb-2">
            แพ็กเกจขยายผลสำหรับนิคมอุตสาหกรรม (ระยอง, ชลบุรี, อยุธยา):
          </p>
          <ul class="list-disc list-inside space-y-0.5 text-[9px] text-slate-700 font-medium">
            <li><strong>MRP Black-box Explainer:</strong> ถอดรหัสคอขวดและวางแผน OT</li>
            <li><strong>Shop Floor Resequencing:</strong> สลับคิวผลิตเมื่อเครื่องจักรพัง</li>
            <li><strong>Scrap &amp; Yield Pattern Mining:</strong> วิเคราะห์หาสาเหตุของเสียสะสม</li>
            <li><strong>Living Knowledge Base (AAR):</strong> องค์ความรู้ช่างหน้างาน</li>
            <li><strong>Supply Chain Sentinel:</strong> ตรวจจับความเสี่ยงท่าเรือแออัด</li>
          </ul>
        </div>
      </div>

      <!-- Architectural Interlock Diagram (Text-based Box) -->
      <div class="p-3 bg-slate-900 text-white rounded-xl shadow-xs">
        <div class="text-[10px] font-black text-sky-400 uppercase tracking-wider mb-1">
          🔗 Architectural Interlock: การทำงานประสานกันอย่างไร้รอยต่อ
        </div>
        <p class="text-[9.5px] text-slate-300 leading-relaxed">
          <strong>Pillar 1 (Core Tax X++)</strong> ทำหน้าที่สร้างฐานข้อมูลที่ถูกต้องตามกฎหมายใน D365 &rarr; 
          <strong>Pillar 2 (Smart AI Localize)</strong> ใช้ Copilot อ่านเอกสารภายนอก ยิงเข้าสู่ Pillar 1 และตรวจความถูกต้องล่วงหน้า &rarr; 
          <strong>Pillar 3 (Operations AI)</strong> เชื่อมโยงข้อมูลคำสั่งซื้อและสต็อกไปวางแผนการผลิตระดับโรงงาน โดยไม่มีส่วนใดขัดแย้งหรือซ้ำซ้อนกัน
        </p>
      </div>
    </div>

    <div class="border-t border-slate-200 pt-1 text-[10px] text-slate-400 text-right">
      Section 3: Unified Product Suite &amp; Target Architecture
    </div>
  </div>

  <!-- ==================== PAGE 5: FINANCIAL IMPACT & ROADMAP ==================== -->
  <div class="page-container">
    <div>
      <!-- Section Title -->
      <div class="flex items-center justify-between border-b-2 border-red-600 pb-1.5 mb-2.5">
        <div>
          <span class="text-[10px] font-black tracking-widest text-red-600 uppercase">Execution &amp; Governance</span>
          <h2 class="text-base font-black text-slate-900">4. ผลกระทบทางการเงิน แผนงานส่งมอบ และการตัดสินใจ</h2>
        </div>
        <span class="px-2 py-0.5 bg-red-50 text-red-700 rounded text-[9px] font-bold">Executive Decision Framework</span>
      </div>

      <!-- Financial Comparison Cards -->
      <div class="grid grid-cols-4 gap-2 mb-3 text-[10px]">
        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-center">
          <div class="text-[9px] font-bold text-slate-500 uppercase">Effort เดิมที่เสนอ</div>
          <div class="text-lg font-black text-slate-800">168 MD</div>
          <div class="text-[8.5px] text-slate-500">23 สัปดาห์ (3 Phases)</div>
        </div>
        <div class="p-2.5 rounded-xl bg-rose-50 border border-rose-200 text-center">
          <div class="text-[9px] font-bold text-rose-700 uppercase">Effort ที่ตัดทิ้งได้</div>
          <div class="text-lg font-black text-rose-600">-45 MD</div>
          <div class="text-[8.5px] text-rose-700">ตัดงานซ้ำซ้อนและเสี่ยงสูง</div>
        </div>
        <div class="p-2.5 rounded-xl bg-emerald-50 border border-emerald-200 text-center">
          <div class="text-[9px] font-bold text-emerald-700 uppercase">Effort ควบรวมใหม่</div>
          <div class="text-lg font-black text-emerald-600">~85-95 MD</div>
          <div class="text-[8.5px] text-emerald-700">ประหยัดงบได้ถึง -43%</div>
        </div>
        <div class="p-2.5 rounded-xl bg-sky-50 border border-sky-200 text-center">
          <div class="text-[9px] font-bold text-sky-700 uppercase">เวลาส่งมอบ (Timeline)</div>
          <div class="text-lg font-black text-sky-600">10-12 Wks</div>
          <div class="text-[8.5px] text-sky-700">เร็วขึ้นกว่าเดิม 2 เท่าตัว</div>
        </div>
      </div>

      <!-- 10-Week Harmonized Roadmap -->
      <div class="border border-slate-200 rounded-xl p-2.5 bg-white shadow-xs mb-3">
        <h3 class="text-xs font-black text-slate-900 mb-2 flex items-center gap-1.5">
          <span>🚀</span>
          <span>แผนงานส่งมอบแบบบูรณาการ 10 สัปดาห์ (Harmonized Fast-Track Schedule)</span>
        </h3>
        <div class="grid grid-cols-4 gap-2 text-[9.5px]">
          <div class="p-2 rounded-lg bg-slate-50 border-l-4 border-l-slate-400 border border-slate-200">
            <div class="font-bold text-slate-900 text-[10px] mb-0.5">Sprint 1 (W1–2): Setup</div>
            <p class="text-[9px] text-slate-600 leading-snug">ขึ้นโครงสร้าง Core Tax X++ (Unrealized VAT, WHT) และตั้งค่า Azure OpenAI Studio</p>
          </div>
          <div class="p-2 rounded-lg bg-slate-50 border-l-4 border-l-sky-500 border border-slate-200">
            <div class="font-bold text-sky-900 text-[10px] mb-0.5">Sprint 2 (W3–5): Build AI</div>
            <p class="text-[9px] text-slate-600 leading-snug">เทรนโมเดล AP Invoice AI อ่านบิลไทย และสร้าง Compliance Pre-validation Rules</p>
          </div>
          <div class="p-2 rounded-lg bg-slate-50 border-l-4 border-l-purple-500 border border-slate-200">
            <div class="font-bold text-purple-900 text-[10px] mb-0.5">Sprint 3 (W6–8): Integration</div>
            <p class="text-[9px] text-slate-600 leading-snug">เชื่อมต่อ D365 Business Events, ทดสอบ 3-Way Match และรายงานใบกำกับภาษี/ใบเสร็จ</p>
          </div>
          <div class="p-2 rounded-lg bg-slate-50 border-l-4 border-l-emerald-500 border border-slate-200">
            <div class="font-bold text-emerald-900 text-[10px] mb-0.5">Sprint 4 (W9–10): UAT</div>
            <p class="text-[9px] text-slate-600 leading-snug">ทดสอบ UAT ร่วมกับผู้ใช้จริง, ปิดงานเอกสารคู่มือ และเตรียม Go-Live แพ็กเกจสมบูรณ์</p>
          </div>
        </div>
      </div>

      <!-- Actionable Endorsement Box -->
      <div class="p-3 rounded-xl bg-gradient-to-r from-red-50 to-orange-50 border border-red-200 mb-2">
        <div class="text-[10px] font-black text-red-700 uppercase tracking-wider mb-0.5">🏆 ข้อสรุปเพื่อการตัดสินใจของผู้บริหาร (Executive Decision)</div>
        <p class="text-[10px] text-slate-800 leading-relaxed">
          การอนุมัติแผนพอร์ตโฟลิโอใหม่นี้ จะช่วยให้ <strong>Fujitsu Thailand (FTH)</strong> หลีกเลี่ยงความสูญเปล่าในการพัฒนาฟังก์ชันซ้ำซ้อน (ประหยัดงบพัฒนาได้กว่า 45 Man-Days) ตัดความเสี่ยงเรื่องระบบบัญชีพัง และทำให้ FTH มีผลิตภัณฑ์ <strong>"Smart AI Thai Localization Package"</strong> ที่พร้อมทำตลาดและสร้างผลกำไรสูงสุดทันทีครับ
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
    print("Writing HTML portfolio harmonization report...")
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
                header_template='<div style="font-size: 8px; color: #94a3b8; width: 100%; display: flex; justify-content: space-between; padding: 0 10mm; font-family: sans-serif; font-weight: 600;"><span>FUJITSU THAILAND (FTH) • MASTER LOCALIZATION & AI PORTFOLIO HARMONIZATION</span><span>CONFIDENTIAL</span></div>',
                footer_template='<div style="font-size: 8px; color: #94a3b8; width: 100%; display: flex; justify-content: space-between; padding: 0 10mm; font-family: sans-serif;"><span>© 2026 Fujitsu Thailand Co., Ltd. All rights reserved.</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>'
            )
            print(f"Successfully generated PDF -> {out_pdf} ({os.path.getsize(out_pdf)//1024} KB)")

        await browser.close()
    print("PDF generation complete!")

if __name__ == "__main__":
    asyncio.run(main())
