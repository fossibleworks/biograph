---
title: Design System
category: design-system
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - patient_portal/tailwind.config.js
  - patient_portal/vite.config.js
  - patient_portal/src/components/Payment.vue
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/public/js/observation.js
  - healthcare/public/js/healthcare.bundle.js
---

- **Desk UI (staff):** use the standard Frappe Desk components. Forms are defined by DocType JSON. Dialogs use `new frappe.ui.Dialog({title: __(...), fields, primary_action_label})`. There are shared widgets in `healthcare/public/js/` (`observation_widget.js`, `healthcare_note.js`, `diagnostic_report_controller.js`) with HTML templates (`*.html`) bundled in `healthcare.bundle.js`. Desk navigation is JSON in `workspace_sidebar/` and `desktop_icon/`. Don't add custom CSS frameworks to Desk.
- **Patient Portal:**
  - Components come from **frappe-ui** (`Card`, `Button`, `ErrorMessage`, `Dialog`, etc.).
  - Design tokens come from `frappe-ui/tailwind`, used as the Tailwind preset in `patient_portal/tailwind.config.js`. That config extends colors with legacy aliases (lightBlue=sky, warmGray=stone, ...).
  - Use Tailwind utility classes. Existing code mixes the frappe-ui semantic tokens (`text-ink-gray-8`) with raw Tailwind grays (`text-gray-900`, `text-gray-500`). Prefer the frappe-ui `ink-*`/`surface-*` tokens for new code.
  - Use Lucide icons (`lucideIcons: true` in the Vite plugin) and feather-icons.
  - Common layout patterns: centered `flex flex-col`, `rounded-xl shadow-sm` cards, `text-2xl font-bold` page headings and `text-sm text-gray-500` subtitles.
