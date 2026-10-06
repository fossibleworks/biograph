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
  - patient_portal/src/components/PractitionerSelector.vue
  - patient_portal/vite.config.js
  - healthcare/public/js/healthcare_orders.html
  - healthcare/public/js/mark_unavailable.js
---

There are two UI surfaces, each with its own system:

1. **Frappe Desk** (most of the app): use Frappe's built-in form, list, tree, dialog and widget primitives. Examples: `frappe.ui.form.on`, `new frappe.ui.Dialog({ title: __(...), fields: [...], primary_action_label: __('Add') })`, and Jinja `.html` microtemplates in `healthcare/public/js/*.html` (healthcare_orders, healthcare_note, observation). Do not add custom CSS frameworks here.
2. **Patient Portal** (`patient_portal/`):
   - Components come from **frappe-ui** (`Button`, `Card`, `Dialog`, `createResource`, `createDocumentResource`…). Icons are lucide (through the frappe-ui vite plugin) and feather-icons.
   - Design tokens come from the **frappe-ui Tailwind preset** (`presets: [frappeUIPreset]` in `tailwind.config.js`). It only adds legacy colour aliases (lightBlue→sky, warmGray→stone, trueGray→neutral, coolGray→gray, blueGray→slate).
   - Style with Tailwind utility classes. Reuse the existing components in `patient_portal/src/components/` (DepartmentSelector, PractitionerSelector, Calendar, BookAppointmentModel, Payment…).
