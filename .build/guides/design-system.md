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
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/public/js/observation.html
---

- **Patient Portal:** the component library is **frappe-ui**, which provides `Button` (with `variant="solid"|"subtle"`, `size="md"` and `:loading`), `Dialog`, form controls and resources. Styling is **Tailwind CSS 3.4** using the **`frappe-ui/tailwind` preset**, which is the design-token source for colours, spacing and typography. `patient_portal/tailwind.config.js` only adds legacy colour aliases (`lightBlue`, `warmGray`, `coolGray`, ...). Icons come from feather-icons and lucide (enabled in the frappe-ui Vite plugin). Global CSS is in `patient_portal/src/index.css`.
- Build new portal UI from frappe-ui components and Tailwind utilities. Don't add custom CSS frameworks or hard-coded hex colours.
- **Desk UI:** use standard Frappe Desk form, list and dialog widgets (`frappe.ui.Dialog`, form `add_custom_button`, field groups) and Frappe's CSS. Custom HTML snippets (`healthcare_note.html`, `observation.html`, `healthcare_orders.html`) are Jinja/Frappe templates in `healthcare/public/js/`.
