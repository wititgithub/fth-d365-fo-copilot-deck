# D365 + Copilot — executive research brief

Research cut-off: **21 October 2026, Asia/Bangkok**. Prepared for discussion by Fujitsu Thailand's Dynamics 365 practice. This is a proposal, not a customer case study or an official Microsoft/Fujitsu product commitment.

## ข้อสรุปสำหรับผู้ตรวจ / Reviewer conclusion

เลือกสี่พื้นที่ที่มีหลักฐานว่าผู้ใช้พบภาระตรวจสอบจริง: AP invoice exceptions, inventory-cost investigation, warehouse short-pick investigation และ production-cost interpretation. **ไม่มีหลักฐานเพียงพอที่จะอ้างว่าเป็นสี่ pain ที่ใหญ่ที่สุดในตลาด หรือว่า D365 standard ปัจจุบันทำไม่ได้ทั้งหมด** โพสต์ Community บางรายการเป็นเรื่อง configuration ที่แก้ได้ด้วย standard จึงต้องใช้เป็นตัวอย่างภาระสืบสวน ไม่ใช่ข้ออ้างว่าระบบขาดฟีเจอร์

The proposed investment is a **specific, evaluated company workflow**, not generic chat, OCR, matching, forecasting, stock reallocation or a new costing engine. Generic ERP access, citations, actions and attachments are already part of Microsoft's agentic ERP foundation. A custom extension is justified only if a benchmark demonstrates an unresolved company-specific gap.

ข้อกำหนด “ยังไม่มีใน standard” จึงเป็น **gate ก่อนเริ่มสร้าง pilot** ไม่ใช่ข้อเท็จจริงที่ยืนยันแล้วจากการไม่พบเอกสาร. ยังไม่ได้เข้าถึง customer tenant, version, enabled features, licences, SOPs หรือข้อมูลจริง. Presentation ใช้คำว่า proposed workflow และอธิบายข้อจำกัดนี้ในบทพูดหน้า 2 และ 8.

## 1. Standard / preview / announced capabilities

| Capability | Evidence at review date | Decision implication |
|---|---|---|
| Invoice two/three-way matching, tolerances, charges | Documented standard functionality | Reuse matching and validation; do not rebuild |
| Vendor invoice automation | Documented processes include receipt matching, posting simulation and workflow | Generic invoice automation is not the proposed gap |
| Account Reconciliation Agent | Setup page labels production-ready preview; Finance 10.0.46+ and additional package/feature prerequisites | Exclude generic subledger-to-GL reconciliation from the new-build pitch |
| Procurement supplier communications | Setup page labels production-ready preview; SCM 10.0.44+ plus prerequisites | Exclude email follow-up/PO-update automation as a new idea |
| Procurement impact analysis | Microsoft announcement on 23 September 2026 calls it public preview | Do not pitch downstream PO impact as wholly absent |
| ERP MCP / ERP plugin for Copilot Cowork | September announcement describes both as generally available | A chat front end or cross-record access alone is insufficient differentiation |
| Finance Agent and AP enhancements | September announcement includes available and forthcoming investments | Recheck the specific task and tenant; avoid claiming universal availability |
| Warehouse workload insights / demand-plan analysis | Listed in Copilot capability catalogue | Exclude generic workload summaries and demand-plan chat |

Microsoft now uses the **AI at Work roadmap**; archived release-wave plans are historical references. The roadmap was opened, but retrieved text did not expose every dynamic listing. Searches without matches do **not** prove an item is absent. GA in a product announcement also does not prove every target tenant is configured, licensed or regionally enabled.

## 2. Evidence by module

### A. Finance / Accounts Payable — recommended first pilot

- Reported friction: discrepancy approval did not remove a receipt-quantity posting block. The thread has suggested answers, not a universal product diagnosis.
- Standard baseline: invoice matching, tolerance controls, receipt matching, automation history and workflow already exist.
- Proposed delta: an AP evidence pack tied to a company's approved SOP, authorized invoice attachments, linked transactions and named handoff rules. It should explain unresolved checks and identify the appropriate owner.
- Feasibility: suitable for a read-only pilot **if** approved data entities/tools expose the needed facts and the SOP is maintained. Missing attachment access may require a scoped API or document integration.
- Human boundary: do not invent receipt evidence, bypass matching, approve discrepancies or post invoices.
- Measure: median and p90 time to a correct handoff; expert-verified evidence and owner accuracy; AI plus review cost per accepted case.
- Stop/new-build exclusion: standard configuration or existing Copilot produces the same acceptable evidence pack; insufficient remaining case volume; inaccessible source evidence.

### B. Inventory / Cost Management — investigation, not reconciliation replacement

- Reported friction: zero quantity with residual value. The cited user's final response concerns main/transit warehouse site configuration; it is not proof that every residual value is caused by uninvoiced receipts.
- Standard baseline: settlements, inventory close logs, open-quantity checks and inventory valuation already exist.
- Proposed delta: a company-specific investigation sequence that links original transactions, financial status, dates and site configuration with month-end procedures and an assigned owner.
- Feasibility: medium; historical data and settlement links may need prepared read-only APIs or reporting views. Costing models must be separated. Never use LLM arithmetic instead of the D365 costing engine.
- Human boundary: no cost adjustment, close reversal or accounting decision by the pilot agent.
- Measure: investigation time and expert-confirmed root-cause evidence, with incorrect causal claims tracked explicitly.
- Stop/new-build exclusion: logs/report configuration plus standard Copilot already satisfy the investigation need, or there is insufficient traceable transaction history.

### C. Warehouse Management — short-pick investigation

- Reported friction: investigating shortages before stock write-off; counting work not appearing as expected. The latter includes standard configuration and existing open-count checks, not a proven defect.
- Standard baseline: work exceptions, reallocation and counting processes. Workload insights are also documented; a general warehouse summary is not new.
- Proposed delta: connect exception history, authorized movement data, existing open counts and supervisor notes into a suggested investigation and accountable handoff.
- Feasibility: medium; usable event history, process discipline and supervisor validation matter more than model choice.
- Human boundary: the agent cannot prove physical stock; no autonomous write-off or relocation. Moving stock to a virtual discrepancy location is a separate inventory workflow/customization question, not something AI inherently enables.
- Measure: investigation time, age of open exceptions and evidence/handoff correctness. Avoid attributing all reduction in short picks to AI.
- Stop/new-build exclusion: standard counting/reallocation setup already resolves the actual problem; the business lacks reliable history or a defined investigation owner.

### D. Production Control / Costing — exploratory, lower priority

- Evidence strength: weaker for the exact proposed extension than AP/warehouse. The Community example is a standard-cost prerequisite issue resolved with standard functionality. It proves user confusion, not that a custom AI agent is needed.
- Standard baseline: cost comparisons, variance pages/reports and documented causes already exist. Standard-cost variances after ending an order must be distinguished from estimated-versus-realized comparisons.
- Proposed delta: join system-calculated variance components with authorized factory shift notes, version changes and a company explanation template. Present candidate causes with evidence for a controller to confirm.
- Feasibility: medium to high data dependency; structured journals and version history are necessary. Shift notes must exist and be authorized. This workflow is a hypothesis requiring customer interviews and a benchmark.
- Human boundary: no automatic BOM/route/cost updates; no claim that a correlated note proves causation.
- Measure: controller review time, accepted evidence coverage and rate of unsupported causal claims.
- Stop/new-build exclusion: standard reports, Finance Agent or standard ERP tools already produce the required explanation; missing shop-floor evidence; prerequisite problems alone explain the pain.

## 3. Architecture proposal

Copilot Studio orchestrates an approved read-only workflow. D365 ERP MCP is a candidate access route, with existing APIs or scoped custom APIs where tools/entities do not cover requirements. Approved SOPs and attachments can provide additional context, with user-aware document access and source references.

MCP uses the assigned authenticated identity and F&O authorization/business validation. It does not independently grant rights. An autonomous identity requires its own limited permissions. The complete agent client's retention, cross-system data movement, DLP and regional configuration need review; MCP alone does not settle them. Prompt injection in attachments should be treated as document content, not executable instructions. Log evidence, agent version, user review and approval outcomes. No customer data or credentials belong in this presentation repository.

## 4. Pilot and acceptance design

Illustrative **six-week** plan, not a delivery promise:

1. Weeks 1–2: one legal entity, one AP exception type and one process owner. Establish resolved case ground truth and baseline. Check enabled standard/Copilot/roadmap. Benchmark identical tasks before deciding to build.
2. Weeks 3–4: only if a gap remains, implement read-only evidence retrieval and the handoff format. Verify company scope and document permissions. Include unresolved and ambiguous cases; an appropriate abstention is a valid outcome.
3. Weeks 5–6: evaluate on held-out cases with AP and functional experts. Compare comparable case complexity; record median and p90 time, evidence accuracy, correct owner and per-case cost. Agree volume/sample size and acceptance thresholds with the owner after seeing the baseline; no fabricated targets.

Value model for discussion: eligible cases × measured minutes saved × agreed loaded labour rate, minus implementation, integration, AI/Copilot consumption, maintenance and review costs. Saved minutes are capacity, not automatically cash savings. No ROI percentage, licence price or adoption promise is asserted.

## 5. Source register

All links were researched on 21 October 2026. Dates of several forum posts were not exposed in the readable page; do not label those cases as newly posted or unresolved today. Forum status is not equivalent to product support verification. All descriptions are paraphrases.

<!-- GENERATED SOURCE REGISTER -->

### catalog

[Microsoft Learn — Copilot and AI capabilities](https://learn.microsoft.com/en-us/dynamics365/copilot/ai-get-started)

Type: Microsoft documentation

รายการความสามารถ Finance และ SCM รวม summaries, collections, demand planning และ warehouse workload insights; สถานะแต่ละฟีเจอร์ต้องตรวจหน้ารายละเอียด

### update

[Microsoft — Agentic ERP update · 23 Sep 2026](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/09/23/build-the-future-of-agentic-erp-with-new-microsoft-dynamics-365-capabilities/)

Type: Microsoft product announcement

ประกาศ ERP MCP และ ERP plugin for Copilot Cowork เป็น GA; ระบุ Procurement impact analysis เป็น public preview และมี AP/Finance Agent enhancements บน roadmap ไม่ควรอ้างงานเหล่านี้เป็นของใหม่ทั้งหมด

### roadmap

[Microsoft — AI at Work roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap)

Type: Live roadmap

ตรวจหน้า roadmap แล้ว แต่เนื้อหาที่ดึงอ่านไม่ได้ครอบคลุมรายการแบบ dynamic ทั้งหมด จึงไม่ใช้การค้นไม่พบเป็นหลักฐานยืนยันว่า Microsoft ไม่มีฟีเจอร์ ต้องตรวจ tenant และ roadmap รายรายการก่อนลงทุน

### recon

[Microsoft Learn — Account Reconciliation Agent setup](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/configure-acct-recon-agent)

Type: Microsoft documentation · preview

เอกสารระบุ production-ready preview และ Finance 10.0.46+; เป็นงาน subledger-to-GL จึงไม่ใช่ช่องว่างใหม่ที่ควรสร้างซ้ำ

### procurement

[Microsoft Learn — Procurement Agent supplier communications](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/procurement-agent-supplier-com-setup)

Type: Microsoft documentation · preview

เอกสารระบุ production-ready preview, SCM 10.0.44+ และการตั้งค่า mail/identity/สิทธิ์ ไม่ใช่ความสามารถที่ทุก tenant เปิดใช้แล้ว

### apCommunity

[Community — Purchase order: Invoice variation approval](https://community.dynamics.com/forums/thread/details/?threadid=3eac7e99-b991-4615-b58e-9e807150277e)

Type: Community case · suggested answer

ผู้ใช้อนุมัติ discrepancy แล้วแต่ posting ยังติด receipt quantity; แสดงความสับสนระหว่างการอนุมัติ variance กับ validation ของ receipt ไม่ได้พิสูจน์ว่า standard matching ใช้ไม่ได้ ไม่ปรากฏวันโพสต์จากหน้าที่อ่าน

### apStandard

[Microsoft Learn — Accounts payable invoice matching](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/accounts-payable-invoice-matching)

Type: Microsoft documentation

standard มี two/three-way matching, tolerance และ charges matching อยู่แล้ว; ส่วนเพิ่มที่เสนอคือ evidence pack เฉพาะ SOP/เอกสาร/owner ของลูกค้า

### apAutomation

[Microsoft Learn — Automated vendor invoicing processes](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/auto-vendr-invc-process)

Type: Microsoft documentation

มี receipt matching, workflow submission, posting simulation และ automation history; โครงการไม่ควรสร้าง invoice OCR หรือ matching engine ใหม่

### costCommunity

[Community — Inventory value with zero quantity](https://community.dynamics.com/forums/thread/details/?threadid=cde371be-8c8d-f011-b4cc-00224826fe9a)

Type: Community case · answered

พบ inventory value ค้างทั้งที่จำนวนศูนย์; ผู้ถามยืนยันเรื่องการตั้งค่า site ของ main/transit warehouse ในเคสนี้ ห้ามสรุปว่าสาเหตุทุกเคสคือใบซื้อยังไม่ invoice; วันโพสต์ไม่ปรากฏจากหน้าที่อ่าน

### costStandard

[Microsoft Learn — Inventory close](https://learn.microsoft.com/en-us/dynamics365/supply-chain/cost-management/inventory-close)

Type: Microsoft documentation

standard มี settlement, check open quantities และ close log; บาง warning เกิดจาก receipt ที่ยังไม่ financial update หรือ subproduction ยังไม่ cost calculated; ให้ engine เดิมคำนวณต้นทุน

### whCommunity

[Community — Short Pick Loop](https://community.dynamics.com/forums/thread/details/?threadid=3fe4f094-1148-ef11-a317-6045bda97426)

Type: Community case · suggested answer

ลูกค้าต้องการสืบสวนสินค้าขาดโดยไม่ให้คลัง write-off ทันที; moderator อธิบายข้อจำกัดการย้ายไป virtual location และชี้ไป open work exceptions; ไม่อ้างว่า AI สามารถย้าย stock ได้เอง

### whCase2

[Community — Short pick cycle count not created](https://community.dynamics.com/forums/thread/details/?threadid=f1654acd-61af-f011-bbd3-00224833c336)

Type: Community case · suggested answers

ผู้ใช้ถามทั้งงานนับไม่เกิดและ reservation status; คำตอบชี้ให้ตรวจ open count work และ worker settings เป็นหลักฐานของภาระตรวจหลายจุด ไม่ใช่ยืนยัน software defect; วันโพสต์ไม่ปรากฏจากหน้าที่อ่าน

### whStandard

[Microsoft Learn — Short picking item reallocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/tasks/set-up-short-picking-item-reallocation)

Type: Microsoft documentation

standard มี work exceptions, automatic/manual reallocation และ Adjust inventory; การย้าย location ใหม่หรือเก็บ stock ไว้สืบสวนต้องวิเคราะห์ workflow/extension แยก

### prodCommunity

[Community — Production Variance is disabled](https://community.dynamics.com/forums/thread/details/?threadid=b3b1d272-31c9-422f-9c6a-1dd69c0785be)

Type: Community case · answered

Variance เป็นสีเทาหลัง End; verified answer ชี้เรื่อง standard cost และผู้ถามตอบว่าใช้ได้แล้ว เป็นปัญหาการตีความ prerequisite ที่ standard แก้ได้ จึงไม่เสนอ AI เพื่อแก้ปุ่มนี้ แต่ใช้เป็นเหตุให้มี prerequisite checks ก่อนวิเคราะห์

### prodStandard

[Microsoft Learn — Production order cost analysis](https://learn.microsoft.com/en-us/dynamics365/supply-chain/cost-management/production-order-cost-analysis)

Type: Microsoft documentation

standard มีรายงาน variance แยก lot size/quantity/price/substitution สำหรับ standard cost หลัง End; ตัวเลขต้องมาจากรายงาน ไม่ให้ LLM คำนวณทดแทน

### prodCauses

[Microsoft Learn — Common sources of production variances](https://learn.microsoft.com/en-us/dynamics365/supply-chain/cost-management/common-sources-of-production-variances)

Type: Microsoft documentation

อธิบายสาเหตุเช่น material/time consumption, version และ cost category; ส่วนเพิ่มคือเชื่อมรายงานกับบันทึกกะและเหตุการณ์เฉพาะโรงงาน พร้อมหลักฐานและการยืนยันของผู้เชี่ยวชาญ

### mcp

[Microsoft Learn — Use ERP MCP for finance and operations](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp)

Type: Microsoft documentation

มีเครื่องมือเข้าถึงข้อมูลและ business actions รวม custom API ที่กำหนดสิทธิ์แล้ว; ไม่ใช่ทุก table/action จะเหมาะกับทุก use case ต้องตรวจ tools และ entity ที่เปิดจริง

### security

[Microsoft Learn — Security for Dynamics 365 ERP MCP](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/mcp/mcp-security)

Type: Microsoft documentation

คำขอใช้ identity/สิทธิ์/validation ของ F&O; ต้องพิจารณา retention และการส่งต่อข้อมูลของ agent client เองด้วย ไม่ได้แปลว่าข้อมูลไม่ออกจาก tenant ทุกกรณี

### logo

[Fujitsu — Original symbol mark asset](https://www.fmworld.net/fmv/img2019/common/symbolmark.svg)

Type: Brand asset

ไฟล์โลโก้จากโดเมน Fujitsu; ใช้สัดส่วนเดิม ภาพ infinity ปิดท้ายเป็นภาพที่ผู้ใช้ให้มา ไม่ใช่โลโก้ Fujitsu ที่ดัดแปลง
