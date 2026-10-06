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
  - patient_portal/src/components/AppointmentModel.vue
  - patient_portal/vite.config.js
  - healthcare/public/js/observation.html
---

- **Desk UI** (the clinician and admin screens) uses Frappe Desk's own form, list and workspace components. Customise it with DocType JSON, form scripts (`frappe.ui.form.on`), HTML templates in `healthcare/public/js/*.html` (for example `healthcare_note.html`, `observation.html`) and Jinja print formats. Do not introduce another component library there.
- **Patient portal** uses **frappe-ui** as its component library: `Button` (`variant="subtle"`, `theme="gray"`, `size="sm"/"md"`), `toast`, and Lucide/feather icons.
- **Design tokens** come from the **frappe-ui Tailwind preset** (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`). The config only adds legacy colour aliases (lightBlue=sky, warmGray=stone, and so on).
- Style with Tailwind utility classes in the Vue SFCs. Global styles live in `patient_portal/src/index.css`.
