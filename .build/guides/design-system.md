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
  - patient_portal/src/PatientPortal.vue
  - healthcare/public/js/healthcare_orders.html
---

- **Desk UI** (most screens) is rendered by Frappe from DocType JSON. Customise it with Frappe form APIs and small HTML templates in `healthcare/public/js/*.html`, not custom CSS frameworks.
- **Patient portal** uses **frappe-ui** as its component library and token source:
  - `tailwind.config.js` uses `presets: [frappeUIPreset]` from `frappe-ui/tailwind` and adds only legacy colour aliases (lightBlue→sky, warmGray→stone, …).
  - Import components (`Button`, `Dialog`, …) and `createResource` from `frappe-ui`.
  - Icons come from feather-icons and lucide (enabled through `frappeui({ lucideIcons: true })`).
  - Global styles live in `patient_portal/src/index.css`.
- Use Tailwind utility classes. Do not add a second component library or hard-code colour values.
