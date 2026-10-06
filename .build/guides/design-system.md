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
  - patient_portal/src/index.css
  - healthcare/public/js/observation_widget.js
---

- **Desk UI** (most screens) uses Frappe's built-in Desk components: form, list and tree views, dialogs, and `frappe.ui.form` controls. Custom widgets are plain JS and HTML templates in `healthcare/public/js` (`observation_widget.js`, `healthcare_orders.html`, `healthcare_note.html`). Reuse Frappe controls rather than adding new UI libraries.
- **Patient portal** uses **frappe-ui** (`^0.1.176`) as its component library, and the **frappe-ui Tailwind preset** (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`) as the design-token source. The config only adds legacy colour aliases (`lightBlue`→sky, `warmGray`→stone, and others).
- Icons: feather-icons and Lucide (frappe-ui vite plugin `lucideIcons: true`).
- Global styles are in `patient_portal/src/index.css`. Components are in `patient_portal/src/components/*.vue`, and shared formatting helpers in `src/utils/formatters.js`.
- Use Tailwind utility classes and frappe-ui components (Button, Dialog, and so on) before writing custom CSS.
