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
- **skipped**: deliberately not applied because it would remove fork behaviour. The reason is given in the notes.

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
