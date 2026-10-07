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
  - patient_portal/package.json
  - patient_portal/vite.config.js
  - patient_portal/components.d.ts
  - healthcare/public/js/healthcare_note.js
  - healthcare/hooks.py
---

- **Desk UI** (most screens) uses Frappe's standard form, list, calendar and dialog widgets. Build UI from `frappe.ui.Dialog`, `frappe.ui.form.on`, field definitions in DocType JSON, HTML templates in `healthcare/public/js/*.html` (`healthcare_note.html`, `observation.html`, `healthcare_orders.html`), and Frappe indicators (`indicator: "warning"` / green / red). Do not add a separate CSS framework to Desk.
- **Patient Portal** uses **frappe-ui** as its component library and **TailwindCSS** through the `frappe-ui/tailwind` preset. Design tokens come from that preset.
  - `tailwind.config.js` adds only legacy colour aliases (`lightBlue` → sky, `warmGray` → stone, `trueGray` → neutral, `coolGray` → gray, `blueGray` → slate).
  - Icons are feather-icons, plus lucide through the frappe-ui Vite plugin.
  - Prefer frappe-ui components (`Button`, `Dialog`, `FormControl`, …), which are auto-imported per `components.d.ts`, over hand-rolled ones.
- **Brand assets:** `healthcare/public/images/healthcare.svg`, `biograph-app-icon.svg` and `healthcare.png`.
