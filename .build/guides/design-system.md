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
  - patient_portal/components.d.ts
---

- **Desk UI** (most screens): standard Frappe Desk forms, lists, trees, dashboards, workspaces and print formats. Styling comes from Frappe, so customise through doctype JSON (fields, sections, depends_on), form scripts and Jinja HTML snippets (`healthcare/public/js/*.html`, `observation.html`) rather than custom CSS.
- **Patient Portal:** **frappe-ui** is the component library and token source (`frappe-ui/tailwind` preset). Use frappe-ui components (Button, Dialog, etc., auto-imported via `components.d.ts`) and Tailwind utility classes. The Tailwind config only adds legacy colour aliases (`lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`). Icons come from feather-icons and lucide (enabled in the frappe-ui Vite plugin). Global styles are in `patient_portal/src/index.css`.
- Brand assets: `healthcare/public/images/biograph-app-icon.svg`, `healthcare.svg`.
