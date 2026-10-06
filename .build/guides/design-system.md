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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
  - healthcare/public/js/healthcare.bundle.js
---

- **Desk UI:** use Frappe's standard form, list and calendar views. Customise through form scripts (`frm.add_custom_button(__("..."), fn, __("Group"))`, `frm.page.set_indicator(__("Not Saved"), "orange")`), Jinja HTML templates in `public/js/*.html` (observation, healthcare_note, healthcare_orders), and Frappe indicator colours. Do not add custom CSS frameworks to desk.
- **Patient portal:** the component library is **frappe-ui** (`frappe-ui/vite` plugin with lucideIcons, plus feather-icons). Design tokens come from the **`frappe-ui/tailwind` preset** in `patient_portal/tailwind.config.js`, which only extends colour aliases (lightBlue→sky, warmGray→stone, and so on). Style with Tailwind utility classes (`text-lg font-semibold text-gray-700`). Use frappe-ui components and dialogs before writing bespoke ones.
