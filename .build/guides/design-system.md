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
  - patient_portal/src/components/BookAppointmentModel.vue
  - patient_portal/vite.config.js
  - healthcare/public/js/observation.html
---

The project has two UI surfaces and no custom token source of its own.

1. **Frappe Desk.** Forms, lists, dialogs and reports use Frappe's built-in UI: `frappe.ui.form`, `frappe.ui.Dialog`, `frappe.msgprint`, `frappe.show_alert`, and standard field types defined in DocType JSON. Small HTML templates live in `healthcare/public/js/*.html` (`observation.html`, `healthcare_orders.html`, `healthcare_note.html`) and are rendered in form scripts. Use Desk's standard components. Do not add custom CSS frameworks here.
2. **Patient Portal.** This uses **frappe-ui** as the component library. `Button`, `Dialog`, `Badge`, `FeatherIcon`, `Tooltip` and `Card` are registered globally in `patient_portal.js`. **Tailwind CSS** uses `frappeUIPreset` as its token source, extended only with legacy color aliases (`lightBlue`→sky, `warmGray`→stone, `coolGray`→gray, `blueGray`→slate, `trueGray`→neutral). Icons are feather or lucide, through the frappe-ui vite plugin. Components live in `patient_portal/src/components/*.vue` in PascalCase (`BookAppointmentModel.vue`, `PractitionerSelector.vue`, `Calendar.vue`).

Reuse frappe-ui components and Tailwind preset classes. Do not introduce raw hex colors or a second component library.
