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
  - patient_portal/package.json
---

The app has two UI surfaces, each with its own source of components and tokens:

1. **Frappe Desk (most of the UI):** DocType forms, lists, reports, workspaces, dashboards and print formats are rendered by Frappe. Build UI with Frappe primitives: DocType JSON fields and layout, `frappe.ui.form.on` scripts, `frappe.ui.Dialog`, `frappe.msgprint` and `frappe.show_alert`. Write no custom CSS framework. The few custom HTML snippets (`healthcare/public/js/*.html`, e.g. `observation.html`, `healthcare_orders.html`) use desk classes and are loaded through `healthcare.bundle.js`.
2. **Patient Portal (Vue SPA):** the component library is **frappe-ui** (`Button`, `Dialog`, `Badge`, `FeatherIcon`, `Tooltip`, `Card`, registered globally in `patient_portal.js`). Icons come from **feather-icons**. Styling uses **Tailwind CSS 3.4** with `frappe-ui/tailwind` as the **design-token preset**. `tailwind.config.js` only extends the palette with legacy aliases (`lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`). Global styles are in `patient_portal/src/index.css`.

Use frappe-ui components and Tailwind utility classes from the preset. Don't introduce another component library or raw hex colours.
