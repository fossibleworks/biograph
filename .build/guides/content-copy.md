---
title: Content & copy
category: content-copy
layer: project
applies_to: []
inclusion: always
binding: recommended
source: inferred
evidence:
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment.py
  - healthcare/healthcare/utils.py
  - healthcare/healthcare/doctype/patient_appointment/patient_appointment_list.js
  - patient_portal/src/components/BookAppointmentModel.vue
  - healthcare/locale/main.pot
---

- **Terminology:** use the DocType names as written in Title Case: Patient, Patient Appointment, Patient Encounter, Healthcare Practitioner, Healthcare Service Unit, Medical Department, Fee Validity, Sales Invoice, Insurance Payor, Service Request. Use "Practitioner", not "Doctor".
- **Tone:** short, plain and direct.
  - Errors state the problem: `"Appointment Date and Time are required."`, `"Appointment end must be after start."`, `"Registration Fee cannot be negative or zero"`, `"Configure a service Item for {0}"`.
  - Success alerts: `"Sales Invoice {0} created"`, `"Unavailability record cancelled successfully"`.
  - Degraded paths: `"SMS not sent, please check SMS Settings"`.
- **Formatting:** use `{0}` placeholders with `.format()` after `_()`. Interpolate before translating, as in `_("{0} is a holiday".format(date))`, only in legacy code; do not copy it. Dialog titles are Title Case (`"Not Available"`, `"Missing Configuration"`).
- **Desk buttons and labels:** Title Case verbs and nouns wrapped in `__()`, for example `"Repeat Appointments"` and `"Mark Unavailable"`.
- **Portal copy** is friendly and patient-facing: "Book an Appointment", "Available Slots", "Pay Your Bill", "Payment Successful". The empty state reads "Looks like you don't have any appointments yet." and there is also "No Records Found".
- Every string must be translatable. The POT file is regenerated weekly.
