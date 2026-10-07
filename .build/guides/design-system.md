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
  - patient_portal/src/PatientPortal.vue
  - patient_portal/vite.config.js
  - patient_portal/package.json
---

- **Desk UI** uses the stock Frappe Desk components: form scripts, `frappe.ui.Dialog`, `frappe.show_alert` and indicators. There are no custom tokens. Templates such as `observation.html` and `healthcare_orders.html` live in `healthcare/public/js`.
- **Patient Portal** uses **frappe-ui** as its component library (`Tabs`, `Dialog`, `Card`, `ErrorMessage`, resources). Styling is **Tailwind CSS 3.4** with the `frappe-ui/tailwind` preset as the token source. It adds only legacy colour aliases (`lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`). Icons come from feather-icons and lucide (enabled in the frappe-ui vite plugin).
- Use frappe-ui components and preset utility classes rather than custom CSS. `patient_portal/src/index.css` is the only stylesheet.
- The brand icon assets are `healthcare/public/images/healthcare.svg` and `biograph-app-icon.svg`.
