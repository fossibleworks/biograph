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
  - patient_portal/src/index.css
---

- **Desk UI** (practitioner and admin screens) uses the standard **Frappe desk** components: forms, list views, `frappe.ui.Dialog`, and HTML templates in `healthcare/public/js/*.html` (healthcare_note, observation, healthcare_orders). Do not invent new widget styling. Extend the existing JS controllers such as `observation_widget.js` and `healthcare_note.js`.
- **Patient Portal** uses **frappe-ui** (^0.1.176) as its component library and design-token source. Tailwind is configured with `presets: [frappeUIPreset]` (from `frappe-ui/tailwind`) and only adds legacy color aliases (lightBlue→sky, warmGray→stone, trueGray→neutral, coolGray→gray, blueGray→slate). Icons come from feather-icons/lucide (the `lucideIcons: true` plugin option).
- Styles go in Tailwind utility classes inside SFCs. Global CSS is limited to `patient_portal/src/index.css`.
- Shared formatting helpers live in `patient_portal/src/utils/formatters.js`.
