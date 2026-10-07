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
  - patient_portal/src/components/Payment.vue
  - healthcare/public/js/observation_widget.js
---

The UI has two surfaces, and each uses its host framework's design system.

**Desk (staff UI)**
- Use the standard Frappe Desk components: `frappe.ui.form`, `frappe.ui.Dialog`, list, tree and calendar views, workspaces, number cards and dashboard charts.
- Add custom widgets in `healthcare/public/js` (`observation_widget.js`, `healthcare_note.js`) with small HTML templates (`*.html`).
- Do not introduce a separate CSS framework in Desk.
- The app icon and branding live in `healthcare/public/images/` (`biograph-app-icon.svg`, `healthcare.svg`).

**Patient Portal**
- Components come from **frappe-ui** (`Card`, `Button`, `Dialog`, and so on). Icons are lucide/feather, enabled through the frappe-ui Vite plugin.
- **Tailwind CSS 3** with `frappe-ui/tailwind` as the preset is the design-token source. `tailwind.config.js` only adds legacy colour aliases (`lightBlue`→sky, `warmGray`→stone, and so on).
- Existing screens use a consistent utility vocabulary:
  - text: `text-gray-900` / `text-gray-500` / `text-gray-800`
  - cards: `rounded-xl shadow-sm p-5`
  - accents: `text-green-600` / `text-blue-600`
  - layout: `flex`, `space-y-*`, `max-w-md`
