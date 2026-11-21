# Lab 13 Solo Completion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete the reproducible code and truthful, rubric-aligned lab reports for a solo learner, without fabricating independent or peer evidence.

**Architecture:** Implement calculations in the existing `src/lab13.py` and use that executable as the source of computed outputs. Populate the existing report templates from the lab guide and verified outputs, preserving required paths and distinguishing trace measurements from `_simulated` estimates.

**Tech Stack:** Python 3, pandas, numpy, scipy, statsmodels, PyYAML; Markdown and YAML.

**Spec:** `docs/superpowers/specs/2026-11-21-lab13-single-member-completion-design.md`

## Global Constraints

- Do not modify `src/logix_runs.csv` or `src/logix_requests.csv`.
- Read requests with `keep_default_na=False`.
- Cost numerator includes all agent attempts; success denominator includes only `ket_qua == 'thanh_cong'`.
- Label every result that uses `*_simulated` inputs as `simulated`.
- Do not fabricate names, student IDs, two independent labelers, independent agreement, or cross-team review.
- Do not use the forbidden term specified in `RULES.md` in submission reports.
- Preserve required report filenames.

## Review Focus

- Empty/zero success counts could make cost-per-success invalid; guard or report explicitly, and test with an empty successful subset.
- Retry caps must omit later trace costs and transfer over-cap requests to staff consistently; test caps of one and two against known totals.
- Blank review decisions must remain blank rather than NaN; verify `keep_default_na=False` and measured metrics.
- All report figures derived from simulated minute columns must be labeled; audit report text for those labels.
- YAML values that are numeric counts or absent cluster fields must parse with intended types; validate with `yaml.safe_load` and inspect required keys.

---

### Task 1: Implement and verify the cost model

**Files:**
- Modify: `src/lab13.py`
- Test: executable assertions in `src/lab13.py` and focused Python checks run from `src/`

**Interfaces:**
- Consumes: CSV schemas described in `docs/du_lieu_va_cong_thuc.md`.
- Produces: `so_lan_chay_ky_vong(p, k=None)`, `ti_le_thanh_cong(p, k=None)`, `he_so_chi_phi_moi_viec_thanh_cong(p, k=None)`, and `mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000, he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None)`.

- [ ] **Step 1: Confirm the existing A1 assertions fail before implementation.** Run `python3 lab13.py` from `src/`; expected: `NotImplementedError` at the first missing helper.
- [ ] **Step 2: Implement the three A1 formula helpers minimally.** Preserve exact expected results 1.20, 1.25, and 1.25 for p=0.8 and documented caps.
- [ ] **Step 3: Run A1 assertions.** Run `python3 lab13.py` from `src/`; expected: all three known-answer assertions pass before the next missing implementation.
- [ ] **Step 4: Implement `mo_hinh` with all attempt costs, simulated review/rework minutes, success-only denominator, and optional retry cap behavior as defined by the detailed guide.** Return token, tool, retry cost, review, rework, total, success count, cost per success, and token/tool invoice per request.
- [ ] **Step 5: Verify against provided A2 values and edge cases.** Run from `src/`; assert token 245585, tool 84000, retry cost 93804, review 1780000, rework 2264000, total 4373585, successes 978, and CPS approximately 4472. Check 1- and 2-attempt caps against guide totals; check an all-failed miniature input is handled explicitly.

### Task 2: Complete checkpoint analyses A3, A4, B1–B4, and D1

**Files:**
- Modify: `src/lab13.py`

**Interfaces:**
- Consumes: Task 1 `mo_hinh` and loaded `runs`, `reqs`.
- Produces: reproducible printed result sections for per-type costs, fixed-cost scope, sensitivity, system cost under retry caps, full-review scenario, and sample-size/design calculations.

- [ ] **Step 1: Add output for A3 by request type and retry success rates.** Print request count, success rate, attempts/request, CPS, baseline ratio, and per-attempt success rates.
- [ ] **Step 2: Add A4 scope calculations for `noi_dia` + `hang_nang`.** Print full-volume and half-volume fixed cost per success, showing scope volume assumptions.
- [ ] **Step 3: Add B1/B2 sensitivity scenarios and ranking.** Include all nine required cases and token-double plus review-double combined case.
- [ ] **Step 4: Add B3 total-system cost and B4 full-review scenarios.** Include staff fallback at 12,000 đ per unsuccessful request and both 9-minute and observed simulated rework-time sensitivity for B4.
- [ ] **Step 5: Add D1 sample size and cluster calculations.** Show five results: 5-point individual randomization sample, m=75 design effect/sample, 20 staff/arm effective maximum, 6 depots/arm effective maximum, and 6-point MDE with m per staff.
- [ ] **Step 6: Run script and compare all outputs with the detailed guide.** Accept expected rounding differences only within 2%; confirm all required rows and calculations are printed.

### Task 3: Complete cost report

**Files:**
- Modify: `report/team/bang_chi_phi.md`

**Interfaces:**
- Consumes: verified output from Tasks 1–2.
- Produces: filled A1–A4 and B1–B4 tables, concise answers, and explicit simulated labels.

- [ ] **Step 1: Fill every result from the executable output.** Retain the report's required tables and filenames.
- [ ] **Step 2: Check all `_simulated`-derived amounts and ratios carry a `simulated` label.**
- [ ] **Step 3: Verify totals and short-answer requirements.** Ensure required answers contain numbers and stay within three lines each.

### Task 4: Complete failure taxonomy and mitigations without false independence claims

**Files:**
- Modify: `report/team/bang_loi.md`

**Interfaces:**
- Consumes: 20 cases and reference taxonomy in the detailed lab guide.
- Produces: transparent solo classification, reference labels clearly identified as reference (not two independent raters), and five measurable mitigations.

- [ ] **Step 1: Fill the five-category reference classification for cases 1–20, clearly label it as one learner's/reference-assisted classification, and mark independent agreement as not measured.** Do not claim 20/20 agreement.
- [ ] **Step 2: Add concise boundary rules for the documented ambiguous cases.**
- [ ] **Step 3: Fill the five mitigation rows with measurable detection, action, and one accountable role each.**
- [ ] **Step 4: Verify the report explicitly states that the independent-rater rubric criterion remains unmet in a solo submission.**

### Task 5: Complete pilot plan and quantitative/launch reports

**Files:**
- Modify: `report/team/pilot_plan.yaml`
- Modify: `report/team/chi_so.md`
- Modify: `report/team/ho_so_launch_v0.md`

**Interfaces:**
- Consumes: Tasks 1–2 outputs and guide-provided metrics/event/stop-rule examples.
- Produces: parseable, complete pilot plan; metrics/events/risk report; seven-section launch v0 with evidence-based conditional recommendation.

- [ ] **Step 1: Fill D1/D2 comments and all YAML fields using the staff-randomized 20+20 plan, 6-point MDE, and documented power trade-off.** Include scope, identifiability, three threshold/time/owner/action stop rules, rollback, decision date, and simulated inputs.
- [ ] **Step 2: Validate YAML with `python3 -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"` from `src/`.** Confirm no unresolved `?` outside comments and no missing required values.
- [ ] **Step 3: Fill three observed metric calculations and propose one additional usage and one additional safety metric.** Include at least six trace-linked events and at least two numeric economic risks.
- [ ] **Step 4: Fill all seven launch sections with primary number, status, and one accountable role.** State adverse evidence and treatment; recommendation must be Go, Go có điều kiện, or No-go.
- [ ] **Step 5: Audit consistency across cost, scope, sample size, safety baseline, and recommendation.** Keep the limitation that one-person classification and peer review cannot be claimed as completed.

### Task 6: Reflect solo status and validate submission checklist

**Files:**
- Modify: `TEAM.md`
- Modify: `report/team/group_report.md`
- Modify: `report/team/phieu_cham.md`
- Modify: `report/team/MSSV_HoTen.md` only if identity is supplied; otherwise leave template and note required personal action in group report.

**Interfaces:**
- Consumes: user's explicit statement that they are the only group member; identity data if later supplied.
- Produces: accurate single-member role/contribution declaration and honest pending peer-review evidence.

- [ ] **Step 1: Update TEAM.md to state one member covers applicable roles and note lab constraints that cannot be independently satisfied.** Do not invent identity fields.
- [ ] **Step 2: Complete group report with work performed, AI/tool disclosure, verification evidence, solo limitation, and submission actions still required.**
- [ ] **Step 3: Keep peer review unclaimed in `phieu_cham.md`; mark pending until an actual assigned team's report is provided.**
- [ ] **Step 4: Run final validation from `src/`: `python3 lab13.py`; YAML parse; grep report text for the forbidden term; grep report files for unresolved template ellipses/question placeholders; check `git diff --check`.** Report unresolved identity and cross-team submission requirements clearly.
