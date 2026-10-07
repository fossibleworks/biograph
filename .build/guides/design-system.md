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
  - patient_portal/src/PatientPortal.vue
  - patient_portal/src/components/BookAppointmentModel.vue
---

- **Desk (staff) UI:** use Frappe's standard form and list framework. Doctype layouts are defined in each doctype's `.json`. Custom UI goes in form scripts and shared widgets in `healthcare/public/js` (for example `observation_widget.js`, `healthcare_orders.html`, `healthcare_note.html`), built with `frappe.ui.Dialog`, form fields and Frappe styles. Do not add a separate CSS framework to Desk.
- **Patient Portal:** use the **frappe-ui** component library (`Button`, `Dialog`, `Tabs`, `createResource`, `variant="solid|subtle"`, `size="md"`). Tokens come from the **frappe-ui Tailwind preset** (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`), extended only with legacy Tailwind colour aliases (lightBlue, warmGray, and so on). Icons are Lucide (`lucideIcons: true` in the Vite plugin) plus feather-icons. Style with Tailwind utility classes in templates. Global CSS is limited to `src/index.css`.
- Portal components live in `patient_portal/src/components/*.vue` and are named in PascalCase, often with a `...Model.vue` suffix for dialogs (for example `BookAppointmentModel.vue`).
