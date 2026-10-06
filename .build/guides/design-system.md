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
  - patient_portal/src/components/Payment.vue
  - patient_portal/vite.config.js
---

- **Desk UI** uses the standard Frappe Desk components: forms, list, tree and calendar views, dialogs, `frappe.ui.*`. Doctype-specific UI goes in `<doctype>.js`, `_list.js`, `_tree.js` and `_calendar.js`. Shared widgets live in `healthcare/public/js` (`observation_widget.js`, `healthcare_orders.html`, `healthcare_note.js`). Don't introduce a separate CSS framework into the desk.
- **Patient portal** uses **frappe-ui** as its component library. `Button`, `Dialog`, `Badge`, `FeatherIcon`, `Tooltip` and `Card` are registered globally in `patient_portal.js`. Styling uses **Tailwind** with the `frappe-ui/tailwind` preset as the token source. `tailwind.config.js` only adds colour aliases (lightBlue, warmGray, …). Icons come from feather and lucide through the frappe-ui Vite plugin.
- Existing portal styling: cards are `rounded-xl shadow-sm p-5`, text uses the gray scale (`text-gray-900/800/500`), and amounts are shown in `font-bold` with green or blue accents. Format currency with `formatCurrency` from `src/utils/formatters.js`.
