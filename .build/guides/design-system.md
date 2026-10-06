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
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/public/js/healthcare.bundle.js
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.js
---

There are two UI surfaces, each with its own system.

**1. Frappe Desk (staff UI).** Use Frappe's built-in form, list, tree and calendar views and widgets: `frm.add_custom_button(__("..."), fn, __("Group"))`, `frm.page.set_indicator`, `frappe.ui.Dialog`, `frappe.show_alert({message, indicator})`, indicator colours (orange, green, red) and Jinja `.html` templates for widgets (`observation.html`, `healthcare_orders.html`, `healthcare_note.html`). Don't introduce a separate CSS framework into Desk.

**2. Patient Portal (`patient_portal/`).** Built on **frappe-ui** components (`Dialog`, `Button` with `variant="solid"`/`"subtle"` and `size="md"`, `Progress`, ...) and **Tailwind**. The design tokens come from the **frappe-ui Tailwind preset** (`presets: [frappeUIPreset]` in `tailwind.config.js`), using semantic classes such as `text-ink-gray-8`, plus a few legacy colour aliases (lightBlue, warmGray, ...). Icons come from feather and lucide through the frappe-ui Vite plugin (`lucideIcons: true`). Feature components live in `patient_portal/src/components/*.vue` in PascalCase (`BookAppointmentModel.vue`, `DepartmentSelector.vue`).

Reuse frappe-ui components and preset tokens before adding custom CSS or new colours.
