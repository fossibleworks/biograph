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
  - patient_portal/package.json
---

- **Desk UI** (most screens) uses Frappe's standard form, list, calendar and report UI, defined through DocType JSON and form scripts. There are no custom CSS tokens. Desk templates such as `healthcare/public/js/*.html` (observation, healthcare_orders, healthcare_note) follow Frappe desk markup.
- **Patient Portal** uses **frappe-ui** as its component library. `Button`, `Dialog`, `Badge`, `FeatherIcon`, `Tooltip` and `Card` are registered globally in `patient_portal.js`.
- **Design tokens:** Tailwind 3 with the **`frappe-ui/tailwind` preset**, which is the token source for colours, spacing and typography. `tailwind.config.js` only adds legacy colour aliases (`lightBlue`, `warmGray`, `trueGray`, `coolGray`, `blueGray`).
- Icons: feather-icons, with Lucide icons enabled through the frappe-ui Vite plugin.
- Use frappe-ui components and Tailwind utility classes instead of new CSS. Global styles are in `patient_portal/src/index.css`.
