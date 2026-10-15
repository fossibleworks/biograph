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
  - healthcare/public/js/healthcare.bundle.js
---

The app has two UI surfaces, each with its own system:

1. **Frappe Desk** (most of the app): standard Frappe form, list and tree views driven by DocType JSON, plus form scripts in `healthcare/public/js` and per-doctype `.js`. Custom widgets use Frappe UI primitives (`frappe.ui.Dialog`, form layouts) and small HTML templates (`healthcare_note.html`, `observation.html`, `healthcare_orders.html`). There are no separate design tokens; styling follows the Desk theme.
2. **Patient portal (Vue):** the **frappe-ui** component library (`Card`, `Button`, `ErrorMessage`, `toast`, `getCachedResource`/`getCachedListResource`) on **TailwindCSS** with the `frappe-ui/tailwind` preset as the token source. `tailwind.config.js` adds only legacy color aliases (lightBlue to sky, warmGray to stone, and so on). Icons come from feather-icons and lucide (through the frappe-ui vite plugin). Global CSS is in `patient_portal/src/index.css`.

Reuse frappe-ui components and Tailwind preset classes rather than adding custom CSS or new UI libraries.
