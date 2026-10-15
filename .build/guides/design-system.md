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
  - patient_portal/src/components/DepartmentSelector.vue
  - healthcare/public/js/healthcare.bundle.js
  - healthcare/healthcare/page/patient_history/patient_history.css
  - healthcare/public/images/healthcare.svg
---

Biograph has two UI surfaces, and each uses its host framework's design system. The repo has no custom token file.

**1. Frappe Desk** (most screens: doctype forms, lists, calendars, reports, workspaces, dashboards, number cards)
- Use Frappe's standard form and list UI. Lay it out declaratively in DocType JSON (sections, columns, tabs, field types) rather than with custom HTML.
- Dialogs use `frappe.ui.Dialog` with `fields: [...]`. Custom widgets use small Jinja-like `.html` templates bundled through `healthcare.bundle.js`, e.g. `observation.html`, `healthcare_note.html`, `healthcare_orders.html`.
- The only custom CSS is scoped to `page/patient_history/patient_history.css` and `page/patient_progress/patient_progress.css`. Use Frappe's CSS variables and classes; do not add new global styles.
- Navigation comes from `workspace/`, `workspace_sidebar/*.json` and `desktop_icon/`. The app icon is `healthcare/public/images/healthcare.svg` / `biograph-app-icon.svg`.

**2. Patient Portal (Vue)**
- The component library is **frappe-ui**: `Button`, `Dialog`, `Badge`, `Card`, `Tooltip` and `FeatherIcon`, registered globally in `patient_portal.js`. The Vite plugin also enables Lucide icons.
- Tokens come from the **frappe-ui Tailwind preset** (`presets: [frappeUIPreset]` in `tailwind.config.js`). The only extensions are legacy colour aliases (lightBlue→sky, warmGray→stone, and so on).
- Style with Tailwind utility classes in templates. `src/index.css` holds only the Tailwind layers.

Prefer existing frappe-ui components and preset tokens over raw hex colours or new CSS files.
