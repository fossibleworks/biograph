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
  - healthcare/public/js/healthcare_orders.html
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
---

- **Desk UI** (most screens) uses the stock Frappe desk: DocType forms, list and calendar views, `frm.add_custom_button` grouped under labels like `__("Status")`, `frm.page.set_indicator`, and Frappe dialogs. Custom HTML fragments live as Jinja micro-templates (`healthcare/public/js/*.html`, e.g. `observation.html`, `healthcare_orders.html`). Use Frappe's indicator colours (`orange`, `green`, `red`) rather than custom CSS.
- **Patient portal** uses **frappe-ui** as its component library (`Card`, `ErrorMessage`, resources) and **Tailwind CSS 3** with the `frappe-ui/tailwind` preset as its token source. `tailwind.config.js` only adds colour aliases (lightBlue→sky, warmGray→stone, etc.). Icons come from feather-icons and lucide (through the frappe-ui vite plugin).
- New portal UI should compose frappe-ui components and Tailwind utilities, not new CSS files. There is a single `src/index.css`.
