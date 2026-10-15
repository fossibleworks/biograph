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
  - patient_portal/src/patient_portal.js
  - patient_portal/src/PatientPortal.vue
  - patient_portal/vite.config.js
  - healthcare/public/js/mark_unavailable.js
---

## Desk UI (the main staff UI)

- Use Frappe's standard Desk components: DocType forms and lists, `frappe.ui.Dialog` with `fields`, `primary_action_label`, and `frappe.show_alert` / `frappe.msgprint` / `frappe.confirm`.
- Custom HTML snippets are Jinja/microtemplates in `healthcare/public/js/*.html`, e.g. `healthcare_note.html`, `observation.html`, `healthcare_orders.html`.
- Navigation is defined as JSON in `workspace_sidebar/*.json`, `desktop_icon/*.json` and `healthcare/workspace`.
- Icons and branding live in `healthcare/public/images` (`biograph-app-icon.svg`, `healthcare.svg`).
- Don't introduce a separate CSS framework into the desk.

## Patient Portal

- The component library is **frappe-ui**. It provides `Dialog`, `Button`, `createResource` and related components, registered in `patient_portal/src/patient_portal.js`.
- Design tokens come from the **frappe-ui Tailwind preset** (`presets: [frappeUIPreset]` in `tailwind.config.js`). Only legacy Tailwind color aliases are added (lightBlue, warmGray, trueGray, coolGray, blueGray).
- Icons are feather-icons and lucide (enabled via the `lucideIcons` option of the frappe-ui Vite plugin).
- Styles are Tailwind utility classes in SFCs. Global CSS is in `src/index.css`.
