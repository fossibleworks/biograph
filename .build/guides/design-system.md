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
  - patient_portal/src/utils/formatters.js
---

- **Desk UI** (most of the product) uses Frappe's standard form, list, tree and dialog widgets and indicators (`indicator: "warning"|"error"`), plus Jinja print formats. There are no custom design tokens. Use `frappe.ui.Dialog`, form `add_custom_button(__("Create"), ...)` groups and existing HTML templates in `healthcare/public/js/*.html`, e.g. `healthcare_orders.html` and `observation.html`.
- **Patient Portal** uses **frappe-ui** as its component library: buttons, dialogs, `createResource` and `createDocumentResource`, and `ErrorMessage`. Styling is **Tailwind CSS 3** with `frappe-ui/tailwind` as the preset, which is the design-token source. The local theme only adds legacy colour aliases (`lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`). Icons are feather-icons and lucide (`lucideIcons: true`).
- Portal components are PascalCase SFCs in `patient_portal/src/components`, such as `BookAppointmentModel.vue`, `PractitionerSelector.vue` and `Payment.vue`. Formatting helpers live in `src/utils/formatters.js`, e.g. `formatCurrency`, which uses `Intl` with an en-IN locale for India.
