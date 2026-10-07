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
---

- **Desk UI:** use Frappe desk's native form, list and tree views and controls. Use `frappe.ui.Dialog`, `frappe.show_alert` and `frappe.msgprint`. There are small shared HTML templates in `healthcare/public/js` (`healthcare_note.html`, `observation.html`, `healthcare_orders.html`). Don't introduce a separate component library for desk screens.
- **Patient Portal:** **frappe-ui** is the component library. `Button`, `Dialog`, `Badge`, `FeatherIcon`, `Tooltip` and `Card` are registered globally in `patient_portal.js`, and `frappeRequest` is the resource fetcher.
  - Styling is **Tailwind CSS** with `frappe-ui/tailwind` as the preset, which is the design-token source. It is extended only with legacy color aliases (lightBlue→sky, warmGray→stone, trueGray→neutral, coolGray→gray, blueGray→slate).
  - Icons: feather-icons, and lucide via the frappe-ui Vite plugin.
  - Global CSS is in `patient_portal/src/index.css`.
  - Reuse frappe-ui components and Tailwind utilities rather than custom CSS.
