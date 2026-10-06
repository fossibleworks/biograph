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
  - patient_portal/vite.config.js
  - patient_portal/package.json
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
---

- **Patient Portal:** the component library is **frappe-ui**, and its Tailwind preset is the source of design tokens (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`). The only theme extensions are colour aliases (lightBlue, warmGray, trueGray, coolGray, blueGray). Icons come from Lucide (`lucideIcons: true` in the Vite plugin) and feather-icons. Build new UI from frappe-ui components and Tailwind utility classes, and do not add custom CSS tokens. Components live in `patient_portal/src/components/`.
- **Desk UI:** uses the standard Frappe desk widgets: form custom buttons (`frm.add_custom_button`), indicators (`frm.page.set_indicator`), `frappe.ui.Dialog`, and list and calendar views. HTML templates (`healthcare_note.html`, `observation.html`) are in `healthcare/public/js`. Indicator colours follow Frappe names (`orange`, `green`, `red`).
