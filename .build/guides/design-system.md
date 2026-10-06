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

- **Desk UI:** use Frappe desk's native components (`frappe.ui.Dialog`, form fields, `frappe.ui.form.on`), and define fields in doctype JSON. Do not add custom CSS frameworks to desk. HTML snippets for widgets live in `healthcare/public/js/*.html`, for example `healthcare_note.html`, `observation.html` and `healthcare_orders.html`.
- **Patient Portal:** use the **frappe-ui** component library with its **Tailwind preset** (`frappeUIPreset`). That preset is the source of design tokens. `tailwind.config.js` only adds legacy colour aliases (lightBlue→sky, warmGray→stone, and so on).
  - Icons: feather-icons and lucide (frappe-ui Vite plugin `lucideIcons: true`).
  - Styling: Tailwind utility classes in Vue SFCs, plus `src/index.css`.
- **Static assets:** under `healthcare/public/images` (app logo `healthcare.svg`).
