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
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
---

- **Desk UI** uses the stock Frappe/ERPNext desk components: form scripts, `frm.add_custom_button`, `frm.page.set_indicator`, dialogs, `frappe.show_alert`. There is no custom component library. Shared desk helpers and templates live in `healthcare/public/js` (`healthcare_note.html`, `observation_widget.js`, etc.).
- **Patient Portal** uses **frappe-ui** as its component library (`ErrorMessage`, `toast`, buttons, dialogs) and Lucide/feather icons. Tailwind's design tokens come from the **`frappe-ui/tailwind` preset**. Use semantic classes such as `text-ink-gray-8`. `tailwind.config.js` only adds legacy colour aliases (lightBlue, warmGray, …).
- Use frappe-ui components and preset tokens. Avoid custom CSS or raw hex colours.
