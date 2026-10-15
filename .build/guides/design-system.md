---
title: Design System
category: design-system
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - patient_portal/tailwind.config.js
  - patient_portal/src/patient_portal.js
  - patient_portal/src/index.css
  - patient_portal/vite.config.js
  - healthcare/public/js/healthcare_note.html
---

# Design system

- **Desk UI** uses Frappe's standard form, list, dialog and calendar components through DocType JSON and form scripts. Custom widgets use `frappe.ui.Dialog`/form fields and small HTML templates in `healthcare/public/js/*.html` (`healthcare_note.html`, `observation.html`, `healthcare_orders.html`). Do not introduce custom CSS frameworks in desk.
- **Patient Portal** uses **frappe-ui** as its component library: `Button`, `Dialog`, `Badge`, `FeatherIcon`, `Tooltip`, `Card`, `ErrorMessage` and `toast`. These are registered globally in `patient_portal.js`.
- **Tokens** come from the `frappe-ui/tailwind` preset in `tailwind.config.js`. The only extensions are legacy color aliases (lightBlue, warmGray, trueGray, coolGray, blueGray). `index.css` sets `--font-sans` to an Inter/system stack.
- **Icons**: feather-icons and lucide (frappe-ui Vite plugin `lucideIcons: true`).
- **App branding**: `healthcare/public/images/biograph-app-icon.svg`, `healthcare.svg`/`.png`, plus desk icons in `healthcare/desktop_icon/*.json`.
