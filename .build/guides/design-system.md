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
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/public/js/mark_unavailable.js
  - healthcare/public/images/biograph-app-icon.svg
---

# Design system

- **Desk UI:** use the standard Frappe Desk components: DocType forms, `frappe.ui.Dialog` with field definitions, list and tree views, workspaces, number cards, and dashboard charts. Do not add a custom CSS framework. Build UI from DocType JSON and Frappe dialogs.
- **Patient portal:** use the **frappe-ui** component library and its **Tailwind preset** (`presets: [frappeUIPreset]`). Tokens come from frappe-ui, using classes such as `text-ink-gray-8`. Tailwind 3.4 is extended only with legacy colour aliases (lightBlue, warmGray, etc.).
- Icons: feather-icons and Lucide (frappe-ui `lucideIcons: true`).
- App icons and images live in `healthcare/public/images` (`biograph-app-icon.svg`, `healthcare.svg`).
