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
---

- **Desk (staff) UI:** use the standard Frappe/ERPNext desk components. DocType JSON drives forms, list views, and calendar views, and custom HTML templates (e.g. `observation.html`, `healthcare_orders.html`) are rendered inside forms. Shared desk JS lives in `healthcare/public/js` and is bundled by `healthcare.bundle.js`. Reuse existing widgets (observation widget, patient quick entry) rather than building new UI frameworks.
- **Patient Portal:** use **frappe-ui** as the component library (Button, Dialog, etc.) with the **`frappe-ui/tailwind` preset** as the design-token source. `tailwind.config.js` extends colors only with legacy aliases (lightBlue→sky, warmGray→stone, …). Icons are feather-icons and lucide (via the frappe-ui Vite plugin).
- Do not introduce other CSS frameworks or component libraries.
