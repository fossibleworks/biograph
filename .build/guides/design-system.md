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

- **Desk UI (staff):** Use stock Frappe Desk components. These include form scripts (`frm.add_custom_button`, `frm.page.set_indicator`), dialogs, list and calendar views, and Jinja print formats. Use Frappe indicator colours (`orange`, `green`, `red`) rather than custom CSS. Shared widgets live in `healthcare/public/js` (observation widget, healthcare notes, orders `.html` templates).
- **Patient portal:** Use the **frappe-ui** component library and its Tailwind preset (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`). The design tokens are the frappe-ui ones. The only local extension is legacy colour aliases (lightBlue, warmGray, trueGray, coolGray, blueGray). Icons come from feather-icons / lucide (`lucideIcons: true`). Global styles are in `patient_portal/src/index.css`.
- Prefer existing frappe-ui components (Button, Dialog, FormControl, etc.) and Tailwind utility classes over new bespoke CSS.
