---
title: Design system
category: design-system
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - patient_portal/tailwind.config.js
  - patient_portal/src/patient_portal.js
  - patient_portal/vite.config.js
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
  - healthcare/public/js/observation.html
---

There are two UI surfaces, and each follows its host framework's design system. There is no custom token file.

**Desk (staff UI)**
- Standard Frappe Desk widgets: forms built from DocType JSON, `frappe.ui.Dialog`, `frm.add_custom_button`, indicators such as `frm.page.set_indicator(__("Not Saved"), "orange")`, and list and tree views.
- Templated HTML snippets live in `healthcare/public/js/*.html` (healthcare_note, observation, healthcare_orders).
- Use Frappe's colour names for indicators (orange, green, red, blue).
- Workspaces, number cards and dashboard charts are defined as JSON under `healthcare/healthcare/`.

**Patient Portal**
- Components: **frappe-ui**. Registered globally are `Button`, `Dialog`, `Badge`, `FeatherIcon`, `Tooltip` and `Card`; lucide icons are enabled through the Vite plugin.
- Tokens: the `frappe-ui/tailwind` preset in `patient_portal/tailwind.config.js`, plus legacy colour aliases (lightBlue → sky, warmGray → stone, etc.). Global CSS is in `patient_portal/src/index.css`.
- Build new portal UI from frappe-ui components and Tailwind utilities. Do not add a second component library or hard-code hex colours.
- Data fetching uses frappe-ui resources (`setConfig('resourceFetcher', frappeRequest)`).
