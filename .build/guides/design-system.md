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
  - patient_portal/src/utils/formatters.js
---

- **Desk UI:** the standard Frappe Desk. Forms, lists, workspaces, number cards and dashboard charts are defined by DocType and workspace JSON plus form scripts (`frappe.ui.form.on`, `frappe.ui.Dialog`). Don't add custom CSS frameworks to Desk screens. The app's icon and logo are in `healthcare/public/images`.
- **Patient Portal:** uses the **frappe-ui** component library (`frappe-ui ^0.1.176`) with its Tailwind preset (`presets: [frappeUIPreset]` in `patient_portal/tailwind.config.js`). That preset is the design-token source. The config only adds legacy Tailwind color aliases (`lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`). Icons come from `feather-icons`. Global styles live in `patient_portal/src/index.css`.
- **Pattern:** build portal UI from frappe-ui components and Tailwind utility classes. Modals and selectors are self-contained SFCs in `patient_portal/src/components/` (`*Model.vue` for modal dialogs, `*Selector.vue` for pickers). Formatting helpers live in `src/utils/formatters.js`.
