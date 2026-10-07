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
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
---

# Design system

## Desk UI (staff)
- Uses the standard **Frappe Desk** look. Build forms from DocType JSON. Form scripts use the Frappe UI APIs: `frm.add_custom_button`, `frm.page.set_indicator(__("Not Saved"), "orange")`, `frappe.ui.form.on`, `frappe.ui.Dialog`, and list/calendar view JS (`*_list.js`, `*_calendar.js`).
- Custom widgets live in `healthcare/public/js/`: `observation_widget.js`, `healthcare_orders.html`, and Jinja-style `.html` templates rendered with Frappe templates. They use Frappe/Bootstrap utility classes, not a separate token system.
- Indicator colors follow Frappe names: orange, green, red, blue, gray.

## Patient Portal
- The component library is **frappe-ui**: `Card`, `Button`, `ErrorMessage`, resources such as `createDocumentResource` and `getCachedListResource`. Use lucide or feather icons.
- Design tokens come from **Tailwind CSS** with the **`frappe-ui/tailwind` preset**. `patient_portal/tailwind.config.js` extends colors only with legacy Tailwind aliases (`lightBlue`→sky, `warmGray`→stone, `coolGray`→gray, etc.). Use frappe-ui and Tailwind classes rather than custom CSS. `src/index.css` holds the Tailwind layers.
- Do not add another component library.
