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
  - patient_portal/vite.config.js
  - healthcare/public/js/mark_unavailable.js
---

- **Desk (staff) UI** uses Frappe Desk's native components: doctype forms, `frappe.ui.Dialog` with `fields` definitions and `primary_action_label`, list and calendar views, workspaces, number cards and dashboard charts. Shared widgets live in `healthcare/public/js/` (e.g. `observation_widget.js`, `healthcare_orders.html`, `mark_unavailable.js`). Do not invent custom CSS frameworks for desk.
- **Patient Portal** uses **frappe-ui** as its component library (`createResource`, plus frappe-ui's own components) and **Tailwind CSS**. The design tokens come from `frappe-ui/tailwind` (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`). The only local extension is aliases for legacy Tailwind color names (lightBlue, warmGray, …). Icons are feather and lucide (`lucideIcons: true`). Global styles live in `patient_portal/src/index.css`.
- Build new portal UI from frappe-ui components and Tailwind utility classes from the preset, not hard-coded colors.
