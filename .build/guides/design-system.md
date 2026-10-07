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
  - patient_portal/src/components/BookAppointmentModel.vue
  - patient_portal/vite.config.js
---

**Desk UI (staff):** use the standard Frappe desk components:
- `frappe.ui.form`, `frappe.ui.Dialog` and `frappe.msgprint`
- HTML partials in `healthcare/public/js/*.html`, such as `healthcare_note.html`, `observation.html` and `healthcare_orders.html`
- the app icon `/assets/healthcare/images/healthcare.svg`

Do not introduce a separate CSS framework into desk.

**Patient Portal (patients):**
- **Component library: `frappe-ui`**, including `Button` (`variant="solid"`), `Dialog` (`:options="{ size: '6xl' }"`), `Card`, `Badge` (`variant/theme`), `Progress` and `FeatherIcon`.
- Icons: `feather-icons`, with Lucide enabled through the frappe-ui vite plugin.
- **Design tokens:** Tailwind 3.4 with **`frappe-ui/tailwind` as the preset**. This is the token source for colours, spacing and type, for example `text-ink-gray-8` and the `bg-surface-*` semantic classes. The local `tailwind.config.js` only adds legacy colour aliases (`lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`).
- Styling uses Tailwind utility classes inline in the SFCs. Global styles are in `patient_portal/src/index.css`.
- Components are composed from feature SFCs in `src/components/`, such as `AppointmentModel.vue`, `BookAppointmentModel.vue`, `Calendar.vue`, `DepartmentSelector.vue`, `PractitionerSelector.vue` and `Payment.vue`. They use a responsive grid of `Card`s and a paginated, stepwise booking dialog with a `Progress` bar.

Prefer frappe-ui semantic tokens (`ink-*`, `surface-*`) over raw Tailwind greys in new code.
