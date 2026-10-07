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
  - patient_portal/src/components/PractitionerSelector.vue
---

**Desk UI:** use standard Frappe Desk components:
- Form scripts and `frappe.ui.Dialog`
- `frappe.show_alert` and `frappe.msgprint`
- Jinja/HTML templates in `healthcare/public/js/*.html` (`healthcare_orders.html`, `observation.html`)

Don't introduce a separate CSS framework into Desk.

**Patient Portal:**
- Component library: **frappe-ui**. Commonly used pieces are `Card`, `Button`, `ErrorMessage`, `createResource`, `createDocumentResource`, and `getCachedResource`.
- Design tokens come from the **frappe-ui Tailwind preset** (`presets: [frappeUIPreset]`). The local theme only adds legacy color aliases (lightBlue→sky, warmGray→stone, etc.).
- Style with Tailwind utility classes. Reuse frappe-ui components before writing custom ones.
- Icons: `feather-icons`.
- Branding assets live in `healthcare/public/images` (`healthcare.svg` app logo).
