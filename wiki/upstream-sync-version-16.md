# Upstream sync ledger — earthians/marley `version-16` → `biograph-fh`

Goal: bring `biograph-fh` to parity with [earthians/marley `version-16`](https://github.com/earthians/marley/tree/version-16)
without losing biograph behaviour.

## Method

- Upstream remote: `git remote add upstream https://github.com/earthians/marley.git && git fetch upstream version-16`
- Merge-base: `df9bf5b9` (16.0.2).
- Commit list (303 commits, pinned to the pre-sync fork tip `01baf235` so the numbering stays stable
  across batches — commits resolved as already-present never get a `-x` trailer, so a list computed
  from a later `HEAD` would still contain them):
  `git rev-list --reverse --no-merges --cherry-pick --right-only 01baf235...upstream/version-16`
- Every pick uses `git cherry-pick -x`, so a picked commit's message names its upstream sha.
- Conflict policy: fork intent wins. Keep all biograph-fh behaviour and add upstream's fix on top.
  Doctype JSON: 3-way union of `fields` / `field_order`. A property that upstream changed is
  applied only if the fork left it unchanged. `patches.txt`: union. `.releaserc`: keep the fork's version.

Outcomes:

- **picked-clean**: applied without conflict.
- **picked-with-conflict-resolution**: applied, with conflicts resolved under the policy above.
- **already-present**: the fork already had the change. The pick was empty, or empty once fork code was kept, so nothing was committed.
- **skipped**: not applied. The notes give the reason. Usually the reason is that the pick would remove fork behaviour. B2 #86 is the one exception: it was skipped only because the push credential cannot write workflow files. The notes give the command to apply it by hand.

## Baseline: healthcare test failures on untouched `biograph-fh`

- **CI:** there is no baseline. `gh run list -R fossibleworks/biograph --branch biograph-fh --workflow ci.yml`
  returns nothing, and `gh api repos/fossibleworks/biograph/actions/runs` reports `total_count: 0`.
  The fork has never run `ci.yml`, so there is no CI history to compare against.
- **Local bench:** none is available in the sync environment, so the server test suite could not run locally.
- **Consequence:** the first CI run on the goal PR becomes the baseline. Compare any failure there
  against the commit that introduced it, using this ledger.
- **Lint baseline** (ruff 0.15.18, the version pre-commit pins), on the files this batch touches, before → after:
  - `clinical_procedure.py`: 1 → 1
  - `patient_appointment.py`: 196 → 196
  - `test_clinical_procedure.py`: 0 → 0
  - `healthcare/__init__.py`: 0 → 0

  So batch B1 adds no new ruff findings. All of these paths are in `.pre-commit-config.yaml`'s
  `exclude` list, so pre-commit skips them and ruff was run on them directly.

## Batch B1 — commits 1–25 (`0329e618` .. `b1c908b0`, through 16.0.7)

| # | upstream sha | subject | outcome | notes |
|---|---|---|---|---|
| 1 | 0329e618 | chore: add version-16 branch to semantic release config | already-present | `.releaserc` already lists `version-16`; the fork's file is unchanged. |
| 2 | e851a623 | fix: use of uninitalized variable in case of practitioner availability | picked-with-conflict-resolution | The fork's `get_availability_data` has no Practitioner Availability slot path: it uses schedules only and throws "does not have a Healthcare Practitioner Schedule". That fork behaviour is kept. Only upstream's `slot_details = []` initialisation is added. Practitioner Availability is not reintroduced into slot lookup. |
| 3 | 6d75a3a6 | fix: add type hints to get_availability_data arguments in Patient Appointment | already-present | The fork already has the same signature and docstring. Upstream's `from typing import Optional` is unused (it would be ruff F401), so it was not added. |
| 4 | ee074460 | fix: correct allow_overlap value fetched from service unit | already-present | Not applicable: the fork removed `get_availability_slots` / `build_availability_data`, which is where this field name was fixed. No other fork code reads `allow_appointments` as the overlap flag. |
| 5 | 1d6d67a0 | chore: bump version to 16.0.3 | picked-clean | |
| 6 | 98b1ef15 | fix: typo | picked-with-conflict-resolution | Variable rename only (`therapy_session` → `has_procedure`). The fork's `docstatus != 2` duplicate guard is kept. |
| 7 | 1773b1ba | fix: record start time of procedure | already-present | Fork commit 2e9eef8d already synced this in its later form (`actual_start_datetime`). |
| 8 | 6285fdfd | fix(refactor): method name etc. | already-present | Already in 2e9eef8d (`has_required_qty`, consolidated `db_set`). The fork deliberately calls `get_item_details(args)` with a dict and validates `self.price_list`, and both are kept. |
| 9 | a160abf4 | fix: add duration to template, end datetime to clinical procedure | picked-with-conflict-resolution | JSON 3-way union. **This fixes a real fork gap:** fork code (`set_planned_endtime`) already read `Clinical Procedure Template.default_duration`, but that field was missing from the fork's JSON, and it is now added. It also adds `search_index` on `patient` / `procedure_template`. The intermediate `end_datetime` field is removed again by #10. |
| 10 | 814a219a | fix: add planned and actual start/end times | picked-with-conflict-resolution | Python: the fork already has the later, complete form (`set_planned_start_date_and_time`, `actual_end_datetime`, price list), so the fork's code is kept. JSON: `end_datetime` removed, because upstream renamed it and the fork never had it. All fork fields are kept. |
| 11 | ec3ed108 | fix(test): add test for clinical procedure start / end datetime fields | picked-clean | Adds `test_start_and_end_time`. It relies on `default_duration` from #9. |
| 12 | 17718312 | fix: add typing hint for whitelisted method | already-present | Empty pick. |
| 13 | b76243b1 | fix: apply guard on clinical procedure start date as well rename function | already-present | The fork already has `set_planned_start_date_and_time` with the `start_date` guard. |
| 14 | 858c63c6 | fix: raise if selling price list or currency is missing for consumable item correct appointment date / time field names | already-present | The fork already has the later form: a mandatory `self.price_list` guard and the `appointment_date` / `appointment_time` fields. |
| 15 | 45efec63 | fix: consolidate two db writes to one | already-present | Empty pick. |
| 16 | 2a9b3215 | fix: add price list to clinical procedure for consumables set defaults for warehouse and pricelist | picked-with-conflict-resolution | Kept: the fork's service-request flow (`update_service_request_status` in `after_insert`, direct status set on cancel/complete) and its dict-based `get_item_details` call. Taken: upstream's `existing_procedure` rename. The auto-merged JS appended a second `let set_defaults`, which would be a SyntaxError, so the JS was reverted to the fork's version, which already has `set_defaults`. |
| 17 | 72c61a4a | chore: bump version to 16.0.4 | picked-clean | |
| 18 | 395436a6 | fix: link existing item via link field | already-present | Already in fork commit c4be9e5e (the `item` Link field and the `item:` handler in medication.js). Only the `modified` timestamp differed, so no commit was made. |
| 19 | bd13058a | fix: set sections collapsible false | already-present | The fork's `item_details` / `combinations_section` are already non-collapsible. Only `modified` differed. |
| 20 | f1500dae | fix: remove unused code | **skipped** | Upstream deletes `get_procedure_from_encounter`, `get_prescribed_procedure` and `show_procedure_templates` from patient_appointment.js. In the fork these are **used**: `patient_appointment.json` still has the `get_procedure_from_encounter` button. Applying this would remove a working fork feature. |
| 21 | 37ee8f54 | chore: bump version to 16.0.5 | picked-clean | |
| 22 | 2cfa2ba3 | fix: get prescribed procedures dialog | already-present | The fork already has the `show_orders` service-request dialog, plus insurance policy/payor propagation, which is kept. The auto-merge would have defined `get_service_request_list_html` twice (a SyntaxError), so the pick was dropped. |
| 23 | 3cae8136 | chore: bump version to 16.0.6 | picked-clean | |
| 24 | b7e395a2 | fix: workspace name correction | already-present | The fork's workspace title is already "Healthcare". |
| 25 | b1c908b0 | chore: bump version to 16.0.7 | picked-clean | `healthcare/__init__.py` is now `16.0.7`. |

B1 totals:

- picked-clean: 6
- picked-with-conflict-resolution: 5
- already-present: 13
- skipped: 1

## Batch B2 — commits 26–98 (`2d79ea82` .. `aeca803f`, through 16.0.8)

Upstream's test-suite refactor: `HealthcareTestSuite` (on top of `ERPNextTestSuite`), deterministic
masters via `BootStrapTestData` / `make_*` in `healthcare/tests/utils.py`, removal of
`IntegrationTestCase` / `EXTRA_TEST_RECORD_DEPENDENCIES`, and `before_tests` disabled. Upstream also switches CI
to `run-parallel-tests --lightmode` (#86); that one-line workflow change is skipped for now (credential), see below.

Additional rules for this batch:

- **`healthcare/tests/utils.py`.** The fork's 816-line file (from 5c82db85, insurance parity) is
  byte-identical to upstream's *final* `version-16` file. It is a superset of every intermediate state
  in this range, and only adds the `_Test HSU - OT` unit and the non-billable occupancy type.
  On every conflict the fork's file was kept. Both upstream's helpers and the fork's additions survive,
  because they are the same file.
- **Insurance tests** (`test_insurance_claim`, `test_insurance_payor`, `test_insurance_payor_contract`,
  `test_item_insurance_eligibility`, `test_patient_insurance_coverage`, `test_patient_insurance_policy`)
  are also byte-identical to upstream's final version, so the fork's copy was kept the same way.
- **Test files the fork inherited from its version-15 lineage** (`test_observation`, `test_nursing_task`)
  differed from upstream only by older code or formatting, so upstream's version was taken.
- **Test files that encode fork behaviour** keep the fork's test set and helper signatures, and take
  upstream's bootstrapped masters. In `test_patient_appointment`, the fork validates unavailability
  through its own `validate_practitioner_unavailability`, so upstream's Practitioner Availability
  scope tests are not added. Its `create_appointment` keeps `procedure_template`. In
  `test_service_request`, there are no therapy tests and `create_encounter` takes no `appointment_type`.

| # | upstream sha | subject | outcome | notes |
|---|---|---|---|---|
| 26 | 2d79ea82 | refactor(tests): introduce HealthcareTestSuite deterministic test data via BootStrapTestData WIP | already-present | Only touches `healthcare/tests/utils.py`. The fork already has upstream's final version of it (from 5c82db85), so the pick was empty. |
| 27 | bf456e49 | fix: test records missing company | picked-clean |  |
| 28 | 386c3846 | fix: set enounter.company in therapy plan | picked-with-conflict-resolution | Fork's Therapy Plan has no source_doc/order_group fields, so only doc.company was added. |
| 29 | e4cd005a | refactor(tests): deteministic medical department mster | picked-with-conflict-resolution | Insurance tests: the fork already has upstream's final version, so the fork's files are kept. test_patient_appointment: upstream's bootstrapped `_Test Medical Department` and the dt/dn child-row fix are taken (the fork's Appointment Type Service Item uses dt/dn). The unused `create_medical_department` helper is dropped. The fork's test set is kept, so upstream's department-cancel test is not re-added. |
| 30 | 0383afd3 | fix: corrected field label | picked-with-conflict-resolution | The label change is applied because the fork had left the label unchanged. The fork's `in_list_view` is kept. |
| 31 | 55e667c6 | refactor: mthods to make patient, paractioner, clinical procedure template etc. | already-present | Only touches `healthcare/tests/utils.py`. The fork already has upstream's final version of that file (from 5c82db85), so the pick was empty. |
| 32 | deee50aa | refactor: helpers to make master records | already-present | Only touches `healthcare/tests/utils.py`. The fork already has upstream's final version of that file (from 5c82db85), so the pick was empty. |
| 33 | a940862d | fix: failing test company not found | picked-clean |  |
| 34 | 61e39b4d | refactor: use master records created | picked-with-conflict-resolution | The redundant service-unit delete is removed, as upstream does. The `Practitioner Availability` wipe is not added because the fork's appointment tests do not use availability records. |
| 35 | 3b8555f4 | fix(tests): missing company link | already-present | utils.py: the fork already has the company link. test_service_request: the fork has no `make_therapy_session` (its Service Request suite does not cover therapy sessions), so the pick was empty. |
| 36 | ae17939d | refactor: remove IntegrationTestCase dependencies | picked-clean |  |
| 37 | 8c01f13f | refactor: helpers to lab test sample and lab test template | already-present | Only touches `healthcare/tests/utils.py`. The fork already has upstream's final version of that file (from 5c82db85), so the pick was empty. |
| 38 | 1ae8ca80 | refactor: test name updated | picked-with-conflict-resolution | The test is renamed. The fork's base class is kept here and migrated in #40. |
| 39 | 0ed3bb4a | fix: practitioner name temp fix | already-present | Only touches `healthcare/tests/utils.py`. The fork already has upstream's final version of that file (from 5c82db85), so the pick was empty. |
| 40 | 79fd9f9a | refactor(tests): HealthcareTestSuite instead of IntegrationTestCase | picked-with-conflict-resolution | Fork tests are migrated to `HealthcareTestSuite`, not dropped: test_medication, test_nursing_task, test_observation, test_observation_template, test_patient_appointment and test_service_request moved from FrappeTestCase / unittest.TestCase to `HealthcareTestSuite`. Fork imports are kept. Upstream-only imports are not added (`make_clinical_procedure`, therapy-plan helpers, `nowtime`, `nowdate`), because the fork's test bodies don't use them. The insurance tests already use the suite. |
| 41 | 6d778355 | fix(tests): nursing task tests | already-present | This intermediate step is superseded. The fork's test_nursing_task setUp already loads the checklist via `frappe.get_test_records`, so the fork's version was kept and the pick was empty. It converges on the bootstrapped masters in a later commit. |
| 42 | 1a82a577 | fix(tests): add more masters to make_master_data | already-present | Only touches `healthcare/tests/utils.py`. The fork already has upstream's final version of that file (from 5c82db85), so the pick was empty. |
| 43 | 29c07779 | refactor: remove commmented code, rename args | picked-clean |  |
| 44 | 3614e10e | fix: missing company in observation creation | picked-clean |  |
| 45 | d99b0e59 | fix(tests): stop removing master data  after tests are run | picked-clean |  |
| 46 | a8fb83df | chore: add a few more masters to make masters | already-present | Only touches `healthcare/tests/utils.py`. The fork already has upstream's final version of that file (from 5c82db85), so the pick was empty. |
| 47 | 739cf8bb | fix(tests): report diagnoses trends | picked-clean |  |
| 48 | 6ae35ee5 | fix(tests): refactor reuse master test reqored created | picked-with-conflict-resolution | The fork's `get_test_records` setUp is replaced by upstream's bootstrapped Nursing Checklist Template, patient and practitioner. That setUp was older upstream code from the version-15 merge, not fork behaviour. The fork's helper names are kept. |
| 49 | 1e7cdfde | fix(tests): tests for patient appointment | picked-clean |  |
| 50 | b6b06f9a | fix(tests): therapy plan | picked-clean |  |
| 51 | b79f1aa2 | fix(tests): clinical procedure | picked-with-conflict-resolution | Conflicts only in `healthcare/tests/utils.py`. The fork already has upstream's final version, so the fork's copy was kept. The other files applied cleanly. |
| 52 | a20a10f4 | fix(tests): lab tests | picked-clean |  |
| 53 | 6eb96e61 | fix(tests): fee validity | picked-clean |  |
| 54 | de6d0845 | chore: remove refs to EXTRA_TEST_RECORD_DEPENDENCIES | picked-clean |  |
| 55 | 823d672f | chore: cleanup practitioner | picked-clean |  |
| 56 | 55d64aa2 | fix(tests): service unit type | picked-clean |  |
| 57 | 83ffb3b9 | fix(test): create master for ip occupancy as well | already-present | Only touches `healthcare/tests/utils.py`. The fork already has upstream's final version of that file (from 5c82db85), so the pick was empty. |
| 58 | d8a8d075 | fix(tests): failing tests for inpatient record | picked-clean |  |
| 59 | 02c5344e | fix: remove call to create_healthcare_docs | picked-clean |  |
| 60 | 218246e7 | fix(tests): tests for observation | picked-with-conflict-resolution | The fork's test_observation was the upstream merge-base file with formatting changes only, so upstream's rewritten version is taken. utils.py: the fork already has it. |
| 61 | 4495d4e4 | fix(tests): ipmo report add patient and medicaton to bootstrapped masters | picked-with-conflict-resolution | Conflicts only in `healthcare/tests/utils.py`. The fork already has upstream's final version, so the fork's copy was kept. The other files applied cleanly. |
| 62 | a10f1d9b | fix(tests): ip medication order and entry | picked-clean |  |
| 63 | e8927632 | fix(test): inpatient record, sesrvice unit | picked-with-conflict-resolution | Conflicts only in `healthcare/tests/utils.py`. The fork already has upstream's final version, so the fork's copy was kept. The other files applied cleanly. |
| 64 | d9e036cc | fix(tests): service request | picked-with-conflict-resolution | Upstream's switch to bootstrapped masters is taken. Kept from the fork: the `create_encounter` signature with no `appointment_type` parameter, and no therapy-plan or Therapy Type usage (the fork's Service Request suite does not cover therapies). |
| 65 | 1e9d1c29 | fix(tests): medication | picked-with-conflict-resolution | Conflicts only in `healthcare/tests/utils.py`. The fork already has upstream's final version, so the fork's copy was kept. The other files applied cleanly. |
| 66 | 5b74c672 | chore: remove unused imports cleanup | picked-with-conflict-resolution | The `create_therapy_plan` import is not added because the fork's Service Request suite has no therapy test. |
| 67 | 2c039371 | fix(tests): practitioner | picked-with-conflict-resolution | Conflicts only in `healthcare/tests/utils.py`. The fork already has upstream's final version, so the fork's copy was kept. The other files applied cleanly. |
| 68 | 081fce7f | fix(tests): typo | picked-clean |  |
| 69 | 9231efe4 | fix(tests): patient history | picked-with-conflict-resolution | Conflicts only in `healthcare/tests/utils.py`. The fork already has upstream's final version, so the fork's copy was kept. The other files applied cleanly. |
| 70 | 4d3a8b09 | fix(tests): patient appointment | picked-with-conflict-resolution | Upstream's bootstrapped `self.patient` / `self.practitioner` are taken in the conflicting hunks. Those hunks differed only in formatting. |
| 71 | 7afa847c | fix(tests): make patient appointment test deterministic | picked-with-conflict-resolution | Taken from upstream: the bootstrapped patient, practitioner, service-unit type and appointment type. Kept from the fork: its test set and the name `test_teleconsultation` (upstream's `test_tele_consultation` is one of the merge-base tests the fork removed, so it is not re-added under that name), so upstream's Practitioner Availability scope tests, `test_appointment_against_an_order` and the department-cancel test are not re-added. The fork validates unavailability through its own `validate_practitioner_unavailability` and has no slot path for Practitioner Availability. Also kept: the fork's `create_appointment` signature, which has a fixed 15-minute duration and no `duration` argument. utils.py: the fork already has it. |
| 72 | 3cb414df | fix(tests): service unit type name | picked-clean |  |
| 73 | a65819c7 | fix(tests): inpatient record | picked-clean |  |
| 74 | 6a10266e | fix(tests): lab test | picked-clean |  |
| 75 | a5ad6b6f | fix(tests): patient medical record | picked-clean |  |
| 76 | ab00fbbb | fix(tests): medication request | picked-clean |  |
| 77 | 7fb7e287 | fix(tests): service request | picked-with-conflict-resolution | The `lab_test_template` rename and the bootstrapped Lab Test Template are taken. The fork's `create_encounter` call (no therapy_type) is kept. |
| 78 | c35ef8f4 | fix(tests): treatment councelling | picked-with-conflict-resolution | Conflicts only in `healthcare/tests/utils.py`. The fork already has upstream's final version, so the fork's copy was kept. The other files applied cleanly. |
| 79 | 84924854 | fix(tests): lab test, observation | picked-clean |  |
| 80 | 4d952981 | fix(tests): patient patient appointment patient encounter patient history settings practitioner availability | picked-with-conflict-resolution | The unused `create_service_unit_type` helper is dropped, and nothing imports it. The department-cancel test is not re-added, which keeps the fork's test set. |
| 81 | 0d9883de | fix(tests): insurance related doctype tests | already-present | Only touches `test_insurance_claim.py`, `test_patient_insurance_coverage.py`. The fork already has upstream's final version of those files (from 5c82db85), so the pick was empty. |
| 82 | 4f8cfadd | refactor: tests - remove unused functions, imports etc. | picked-with-conflict-resolution | Helpers that no test imports any more are removed, as upstream does: `create_healthcare_docs`, `create_healthcare_service_items`, `create_appointment_type`, `create_user`. `create_clinical_procedure_template` is kept because the fork's `create_appointment` still uses it to set `procedure_template` (the fork's Patient Appointment field). The fork's `create_appointment` body is kept. utils.py: the pick auto-merged a second, `customer_group`-less copy of `_Test Patient 2` / `_Test Patient 3` into `make_patients`; that duplicate was removed in a B2 rework commit so `healthcare/tests/utils.py` is byte-identical to upstream `version-16` again. |
| 83 | fbad72bc | fix: linter report | picked-clean |  |
| 84 | 6cfd9724 | fix: remove unnecessary customer group insert | **skipped** | Upstream deletes `create_customer_groups` from `healthcare/setup.py`, but patch `v16_0/setup_service_request_and_insurance.py` (in both the fork and upstream) imports it. Removing it would make `bench migrate` fail with an ImportError on any site that has not run that patch yet. The fork also relies on the Insurance Payor customer group being created at install. |
| 85 | 20b1a29a | fix: remove company creation in before tests | picked-clean |  |
| 86 | 4d89574c | fix: update ci comfig to run tests in lightmode | skipped | Not a fork-intent decision; skipped only because of the push credential. Only touches `.github/workflows/ci.yml`. The engine's push token has no `workflow` scope, and GitHub rejected the push with "refusing to allow an OAuth App to create or update workflow `.github/workflows/ci.yml` without `workflow` scope". The pick is left out of this batch. Someone with workflow permission needs to apply it by hand: `git cherry-pick -x 4d89574c`, which adds `--lightmode` to the Run Tests step. |
| 87 | ad9ef730 | fix: set customer group for test recrds explicitely | already-present | Only touches `healthcare/tests/utils.py`. The fork already has upstream's final version of that file (from 5c82db85), so the pick was empty. |
| 88 | ff168bf0 | fix: add type hints | picked-clean |  |
| 89 | a3701b4b | fix: explicitly set customer group for test records | picked-clean |  |
| 90 | 3085a187 | fix(tests): add missing super().setUp() call | picked-clean |  |
| 91 | 608a5761 | fix(tests): typo | picked-with-conflict-resolution | Upstream's line is taken. The conflict was only the fork's `str(id)` versus upstream's `{id!s}` formatting. |
| 92 | d925ddaa | fix(tests): use pluck within get_list | picked-clean |  |
| 93 | 1ef5f4ff | fix(tests): make patient initialisatioon determisistic | picked-clean |  |
| 94 | ffec0575 | fix(test): tharapy_type insted of therapy_type.name | picked-clean |  |
| 95 | c7ff5c58 | fix(tests): linter issues | picked-clean |  |
| 96 | 666a965e | fix: diagnostic report status for imaging observations | picked-clean |  |
| 97 | 92de3f0b | fix: only nongroup items are allowed in upstream Customer | picked-with-conflict-resolution | The conflict was only the `modified` timestamp. `link_filters` and the non-group customer-group default applied. |
| 98 | aeca803f | chore: bump version to 16.0.8 | picked-clean |  |

B2 totals (73 commits):

- picked-clean: 35
- picked-with-conflict-resolution: 24
- already-present: 12
- skipped: 2 (one for fork intent; #86 only because the CI workflow file cannot be pushed)

### B2 follow-up commit: migrate the remaining fork tests

`test: migrate remaining fork tests to HealthcareTestSuite (upstream sync B2)`. This commit has no upstream sha.

- `test_package_subscription`, `test_healthcare_package` and `test_doctor_advice_template` are fork-only
  tests that no upstream commit touches. They move from `FrappeTestCase` to `HealthcareTestSuite`,
  so they run on the suite's bootstrapped `_Test Company` and masters.
  The helpers they use are unchanged: `create_observation_template`, `create_therapy_type`, `create_patient`.
  The bootstrapped "Basic Rehab" (rate 5000) matches what `create_therapy_type` creates, so the expected
  package total of 5200 still holds.
- `test_nursing_task` now uses upstream's file. The remaining fork delta was a v15 leftover: the
  `start_nusing_tasks` typo, and a Vital Signs *Document* assigned to `task_document_name` instead of its name.
- `test_patient_appointment`:
  - `create_appointment(..., duration=15)` takes a duration whose default is unchanged.
    Before this, the eight `duration=` calls in `test_practitioner_availability` raised `TypeError`,
    and that was already true on `b229aad8`.
  - The check-in test passes `appointment_type.name` instead of the Document, as upstream does.
- Recurring and block booking (`recuring_appointment_handler.py`) have **no tests in the fork**, so
  there was nothing to migrate. Writing new ones is out of scope for a sync batch.

### B2 verification

There is still no local bench, so the server suite cannot run here. The first CI run on the goal PR
remains the baseline. What was checked statically on the final tree:

- All 73 commits are accounted for: 59 `-x` commits match the picked rows exactly, and the rest are
  12 already-present and 2 skipped (one of them #86, the workflow file). Each commit's message names its upstream sha.
- **Import resolution:** an AST check finds that every `from healthcare… import name` in the app
  resolves to a top-level definition. 0 problems.
- **Call signatures:** an AST check finds that every call to a helper imported from a `test_*` or
  `healthcare.tests` module matches the helper's parameters. 0 problems.
- **No test class remains on the old bases:** `FrappeTestCase`, `unittest.TestCase` and
  `IntegrationTestCase` are gone. The only `load_test_records` user is upstream's own `custom_doctype/test_sales_invoice.py`.
- **Fork tests still exist:**
  - `test_package_subscription`, `test_healthcare_package` and `test_doctor_advice_template`
  - `test_patient_appointment`: all 19 tests the fork had on `b229aad8`, including check-in and service-unit capacity
  - `test_service_request`
  - the six insurance tests
  - `test_nursing_task`, `test_observation`, `test_observation_template`, `test_medication` and `test_clinical_procedure`
- **ruff 0.15.18 (`--select F`)** on every `.py` file B2 changed:
  - Before: 3 findings, all already in the fork: `patient_encounter.py` F811 ×2 and `test_service_request.py` F401.
  - After: 3 findings, the same three. Upstream `aeca803f` left two new F401s, and the fork drops both
    imports (see "B2 rework, round 2" below):
    - `healthcare/healthcare/utils.py` `setup_healthcare`, unused because upstream comments out `before_tests`.
    - `test_medication_request.py` `create_item`.
  - Non-test files only: 2 → 2.
- **ruff 0.15.18, full repo config** (same basis as the B1 baseline), on every non-test `.py` file B2
  changed, `b229aad8` → HEAD:
  - `healthcare/__init__.py`: 0 → 0
  - `observation.py`: 5 → 5
  - `patient.py`: 3 → 3
  - `patient_encounter.py`: 47 → 47
  - `healthcare/healthcare/utils.py`: 0 → 0
  - `healthcare/hooks.py`: 0 → 0

  So batch B2 adds no new ruff findings under the full config either.

Effect of deferring #86: until `--lightmode` lands in `ci.yml`, CI runs the suite in normal mode.
`before_tests` is commented out, and `HealthcareTestSuite` sets up its own masters through `ERPNextTestSuite`,
so the tests should not depend on the flag. Normal mode still builds each doctype's legacy test records,
which makes runs slower. If CI shows failures that only happen in normal mode, apply #86 first, before
treating them as regressions.

### B2 rework (review round)

`fix: restore fork test name, dedupe utils.py, let CI install on fork branches (upstream sync B2)`. No upstream sha.

- `test_patient_appointment`: `test_tele_consultation` is renamed back to the fork's `test_teleconsultation`.
  Upstream already used `test_tele_consultation` at the merge-base `df9bf5b9`, so this was never an
  upstream rename inside B2. A sweep of every `def test_*` / `class Test*` in `healthcare/**/test_*.py`
  at `b229aad8` against the final tree finds only the seven allowed upstream renames missing (including #38's `test_creation_on_encounter_submission` → `test_service_request_creation_on_encounter_submission`), each with its
  successor present. None of the 13 merge-base `test_patient_appointment` tests the fork removed is back.
- `healthcare/tests/utils.py`: the duplicate `_Test Patient 2` / `_Test Patient 3` records from #82 are
  dropped. `git diff upstream/version-16 -- healthcare/tests/utils.py` is empty.
- `.github/helper/install.sh` (not a workflow file, so it is pushable): a base ref that is not `develop` or
  `version-*` (for example `biograph-fh`, or a `goal/*` push) maps to `version-16` before it clones frappe
  and fetches erpnext and payments. Before this, CI ran `git clone frappe --branch biograph-fh` and could not
  install. `payments` now also gets `--branch`, as upstream's `install.sh` does.
- Still pending, needs a person with the `workflow` scope: #86 (`git cherry-pick -x 4d89574c`) on top of
  the fork's `BIOGRAPH_BRANCH` rename in `ci.yml`.

Known gaps carried forward (not introduced by B2):

- `test_patient_medical_record` reads `appointment.template_dn`, but the fork's Patient Appointment
  uses `procedure_template`.
- `test_practitioner_availability` exercises upstream's Practitioner Availability slot semantics.
  The fork deliberately removed those from slot lookup (see B1 #2).

Both are upstream tests written against upstream behaviour. If CI flags them, decide per test
whether it is fork behaviour or a gap, rather than changing app code inside a sync batch.

### B2 rework, round 2 (review round)

`fix: drop unused imports left by upstream aeca803f (upstream sync B2)`. No upstream sha.

- `healthcare/healthcare/utils.py`: removed `from healthcare.setup import setup_healthcare`. Its only user is
  the `before_tests` body that upstream commented out. Nothing imports `setup_healthcare` from this module.
- `test_medication_request.py`: removed the unused `create_item` import.
- ruff 0.15.18 `--select F --isolated` over the 84 `.py` files changed since `b5f55a02` (16.0.7):
  3 findings before, 3 after. These are the fork's existing `patient_encounter.py` F811 ×2 and
  `test_service_request.py` F401.
- Upstream #86 (`4d89574c`, `--lightmode` in `.github/workflows/ci.yml`) is still deferred. This run's GitHub
  token has no `workflow` scope, and GitHub rejects any push that changes a workflow file. Someone with that
  scope needs to run `git cherry-pick -x 4d89574c` on this goal branch.

### B2 rework, round 3

- Retried #86 in this run with `git cherry-pick -x 4d89574c`. The pick applies cleanly on top of the
  `BIOGRAPH_BRANCH` rename and changes one line in `ci.yml`. The push was rejected again: "refusing to
  allow an OAuth App to create or update workflow `.github/workflows/ci.yml` without `workflow` scope".
  The local pick was dropped so the branch can still be pushed.
- The ledger now records #86 as `skipped`, not `deferred`, so it uses only the AC-4 outcome words. The
  reason is still in the row's notes. Once someone applies the pick by hand, the row becomes picked-clean.

### B2 rework, round 4

- Ledger: added full-repo-config ruff counts for B2's non-test files, matching how B1 records its baseline.
- #86 is unchanged: still `skipped`, for the same `workflow`-scope push rejection as rounds 2 and 3. It needs a
  person with that scope to run `git cherry-pick -x 4d89574c` on this goal branch and push.
