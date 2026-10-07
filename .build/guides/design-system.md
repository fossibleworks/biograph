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
  - patient_portal/src/components/BookAppointmentModel.vue
  - patient_portal/src/utils/formatters.js
  - healthcare/public/js/observation_widget.js
  - healthcare/hooks.py
---

There are two UI surfaces, and each has its own system.

**1. Desk (Frappe UI framework)**
- Most UI is generated from DocType JSON metadata: forms, lists, tree views (Healthcare Service Unit, Medication), calendars (Patient Appointment) and workspaces in `healthcare/healthcare/workspace`.
- Customise through form scripts using Frappe primitives: `frm.add_custom_button(__("..."))`, `frm.page.set_indicator(__("Not Saved"), "orange")`, `frappe.ui.Dialog`, `frappe.msgprint`. Use Frappe's indicator colour names (`orange`, `green`, `red`, `blue`, `gray`) rather than custom CSS.
- Shared desk widgets live in `healthcare/public/js` (`observation_widget.js`, `healthcare_note.js`, `diagnostic_report_controller.js`, plus `.html` templates).
- App icon: `/assets/healthcare/images/healthcare.svg`.

**2. Patient Portal (Vue)**
- The component library is **frappe-ui**: `Button`, `Dialog`, `Progress`, `createResource`, and others. The design tokens come from the **frappe-ui Tailwind preset** (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`). Its only extension is aliasing legacy Tailwind colour names (`lightBlue`→sky, `warmGray`→stone, `coolGray`→gray, and so on).
- Icons are feather-icons and lucide (`lucideIcons: true` in the Vite plugin).
- App-level components live in `patient_portal/src/components/`, named PascalCase with a `*Model.vue` suffix for dialogs (`BookAppointmentModel.vue`, `AppointmentModel.vue`, `DiagnosticModel.vue`) and `*Selector.vue` for pickers. Formatting helpers live in `src/utils/formatters.js` (`formatCurrency`).
- Use frappe-ui components and Tailwind utility classes. Do not introduce another component library or hard-code colours outside the preset.
