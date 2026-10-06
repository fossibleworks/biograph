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
  - patient_portal/vite.config.js
  - patient_portal/src/components/PractitionerSelector.vue
---

- **Desk UI** (most of the product) uses standard Frappe Desk forms, list, calendar and report views, configured through DocType JSON and form scripts. Do not build custom CSS frameworks for it.
- **Patient portal** uses **frappe-ui** as its component library: `Button`, `Dialog`, `Badge`, `FeatherIcon`, `Tooltip` and `Card` are registered globally in `patient_portal.js`.
- **Design tokens** come from the `frappe-ui/tailwind` preset in `patient_portal/tailwind.config.js`, which adds only legacy colour aliases (lightBlue→sky, warmGray→stone, …). Use frappe-ui semantic classes (for example `text-ink-*`, `shadow-xs`) and Tailwind utilities, and keep layouts responsive (`grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4`).
- **Icons:** feather-icons through `<FeatherIcon name="…">`. Lucide icons are enabled in the Vite plugin.
