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
---

- **Desk UI:** use the standard Frappe/ERPNext desk with DocType forms, list and tree views, workspaces, number cards and dashboard charts. Style comes from Frappe. Custom HTML snippets live in `public/js/*.html` and doctype `.html` templates.
- **Patient portal:** **frappe-ui** is the component library (`Card`, `ErrorMessage`, `getCachedListResource`/`getCachedResource`, …) and **Tailwind CSS** is configured with the `frappe-ui/tailwind` preset.
  - The design tokens come from that preset, extended in `patient_portal/tailwind.config.js` with legacy colour aliases: lightBlue, warmGray, trueGray, coolGray, blueGray.
  - Icons: feather-icons and Lucide (the frappe-ui vite plugin with `lucideIcons: true`).
- Do not add another CSS framework or component library to the portal.
