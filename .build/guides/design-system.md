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
  - patient_portal/package.json
  - patient_portal/vite.config.js
  - patient_portal/src/components/Payment.vue
  - patient_portal/src/utils/formatters.js
  - healthcare/healthcare/page/patient_history/patient_history.css
---

## Desk (staff UI)

Use Frappe Desk's built-in UI: form layouts defined in DocType JSON, `frappe.ui.Dialog`, `frappe.msgprint` indicators (`orange`, `green`, `red`), workspaces, number cards, and dashboard charts. Custom HTML fragments use Frappe micro-templates (`healthcare/public/js/*.html`, `page/*/*.html`). Their small CSS files are scoped per page (`patient_history.css`). There is no separate token system. Use Frappe's CSS variables and Bootstrap classes, which Desk already ships.

## Patient Portal

- The component library is **frappe-ui** (`Card`, `ErrorMessage`, `Button`, `Dialog`, and others). Import from `'frappe-ui'` before writing new primitives.
- **Design tokens** come from the **frappe-ui Tailwind preset** (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`). The only local extension aliases legacy Tailwind color names (`lightBlue` → sky, `warmGray` → stone, `trueGray` → neutral, `coolGray` → gray, `blueGray` → slate).
- Icons are **lucide** (enabled through the frappe-ui Vite plugin) and **feather-icons**.
- Global styles live in `patient_portal/src/index.css`. Style components with Tailwind utility classes, not bespoke CSS.
- Shared formatting helpers live in `patient_portal/src/utils/formatters.js` (`formatCurrency`).
- Components are modal-centric: `AppointmentModel.vue`, `BookAppointmentModel.vue`, `DiagnosticModel.vue`, plus selector components and `Calendar.vue`.
