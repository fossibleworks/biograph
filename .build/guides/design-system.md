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
  - patient_portal/package.json
  - healthcare/public/js/healthcare.bundle.js
---

# Design system

The two UIs follow different conventions.

## Desk UI (staff)
- Standard **Frappe Desk** components, generated from DocType JSON: forms, list, calendar and tree views, workspaces, number cards and dashboard charts.
- Custom widgets in `healthcare/public/js` (observation widget, healthcare notes, orders) use Frappe's `frappe.ui` APIs and Jinja/HTML micro-templates (`*.html` imported in `healthcare.bundle.js`).
- Do not bring in other CSS frameworks.

## Patient portal
- **frappe-ui** is the component library (`Card`, `ErrorMessage`, `createResource`, `getCachedResource`, etc.).
- **Tailwind CSS** uses the `frappe-ui/tailwind` preset as the design-token source.
- `tailwind.config.js` only adds legacy colour aliases: `lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`.
- Icons: lucide (through the frappe-ui vite plugin) and feather-icons.
- Build new portal UI from frappe-ui components and preset tokens, not hard-coded colours.
