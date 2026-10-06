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
---

- **Desk (staff UI):** the stock Frappe Desk UI. Build forms from DocType JSON and extend them with form scripts, `frappe.ui.Dialog`, and the HTML templates in `healthcare/public/js/*.html` (e.g. `observation.html`, `healthcare_orders.html`). Don't add custom CSS frameworks to Desk.
- **Patient Portal:** **frappe-ui** components plus **Tailwind CSS 3** with the `frappe-ui/tailwind` preset as the token source. The only theme extension is legacy color aliases (lightBlue→sky, warmGray→stone, trueGray→neutral, coolGray→gray, blueGray→slate). Use **feather-icons** for icons. Styles start from `patient_portal/src/index.css`.
- Reuse the existing portal components (`Calendar.vue`, `DepartmentSelector.vue`, `PractitionerSelector.vue`, `Payment.vue`) before writing new ones.
