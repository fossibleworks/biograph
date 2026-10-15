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
  - patient_portal/src/PatientPortal.vue
  - patient_portal/src/components/AppointmentModel.vue
  - healthcare/public/js/healthcare.bundle.js
---

## Desk UI

Desk screens use **Frappe Desk's** standard form, list, report, workspace and dialog components. Extend them with doctype JSON (fields, sections, tabs) and form scripts (`frappe.ui.form.on`, `frappe.ui.Dialog`, `frappe.show_alert`) rather than custom HTML/CSS. Shared Desk widgets live in `healthcare/public/js` (observation widget, healthcare notes/orders HTML templates, mark-unavailable and recurring-appointment dialogs). They are loaded through `healthcare.bundle.js`. App icons are `healthcare/public/images/healthcare.svg` and `biograph-app-icon.svg`. Desktop icon groupings are in `healthcare/desktop_icon/*.json`.

## Patient portal

- The component library is **frappe-ui** (`Tabs`, `Dialog`, `Button`, and others), with icons from feather / lucide (`lucideIcons: true`).
- Design tokens come from **Tailwind CSS 3 with `frappe-ui/tailwind` preset** (`patient_portal/tailwind.config.js`). The only additions are legacy color aliases (`lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`).
- Styling is utility classes such as `text-gray-700 font-medium` and `text-sm text-gray-500`. The global stylesheet is `src/index.css`.
- Dialogs use frappe-ui's `options` API (`title`, `message`, `icon: {name, appearance}`, `actions: [{label, variant: 'solid'}]`).

Use frappe-ui components and the preset's gray scale and spacing. Do not add custom CSS or another UI kit.
