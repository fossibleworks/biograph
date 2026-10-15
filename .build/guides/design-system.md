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
---

# Design system

- **Desk UI:** standard Frappe Desk components (form, list, calendar and report views; `frappe.ui.Dialog`; HTML templates in `healthcare/public/js/*.html`). Do not introduce a separate CSS framework into Desk.
- **Patient Portal:** **frappe-ui** is the component library (Button, Dialog, etc. via `frappe-ui`, auto-imported). It is styled with **Tailwind CSS 3.4 using the `frappe-ui/tailwind` preset** as the design-token source. `tailwind.config.js` only adds legacy color aliases (`lightBlue`, `warmGray`, …).
- Icons come from feather-icons and lucide (`lucideIcons: true` in the Vite plugin).
- Global portal styles live in `patient_portal/src/index.css`.
