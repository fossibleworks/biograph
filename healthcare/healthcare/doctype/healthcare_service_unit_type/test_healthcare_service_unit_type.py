# Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt


import frappe
from frappe.tests import IntegrationTestCase


class TestHealthcareServiceUnitType(IntegrationTestCase):
	def test_item_creation(self):
		unit_type = get_unit_type()
		self.assertTrue(frappe.db.exists("Item", unit_type.item))

		# check item disabled
		unit_type.disabled = 1
		unit_type.save()
		self.assertEqual(frappe.db.get_value("Item", unit_type.item, "disabled"), 1)

	def test_both_flags_allowed(self):
		frappe.delete_doc_if_exists("Healthcare Service Unit Type", "_Test Dual Use Unit Type")
		unit_type = frappe.get_doc(
			{
				"doctype": "Healthcare Service Unit Type",
				"service_unit_type": "_Test Dual Use Unit Type",
				"allow_appointments": 1,
				"inpatient_occupancy": 1,
			}
		).insert()
		unit_type.reload()
		self.assertEqual(unit_type.allow_appointments, 1)
		self.assertEqual(unit_type.inpatient_occupancy, 1)

	def test_no_flags_allowed(self):
		frappe.delete_doc_if_exists("Healthcare Service Unit Type", "_Test No Flag Unit Type")
		unit_type = frappe.get_doc(
			{
				"doctype": "Healthcare Service Unit Type",
				"service_unit_type": "_Test No Flag Unit Type",
				"allow_appointments": 0,
				"inpatient_occupancy": 0,
			}
		).insert()
		self.assertTrue(frappe.db.exists("Healthcare Service Unit Type", unit_type.name))


def get_unit_type():
	if frappe.db.exists("Healthcare Service Unit Type", "Inpatient Rooms"):
		return frappe.get_doc("Healthcare Service Unit Type", "Inpatient Rooms")

	unit_type = frappe.new_doc("Healthcare Service Unit Type")
	unit_type.service_unit_type = "Inpatient Rooms"
	unit_type.inpatient_occupancy = 1
	unit_type.is_billable = 1
	unit_type.item_code = "Inpatient Rooms"
	unit_type.item_group = "Services"
	unit_type.uom = "Hour"
	unit_type.no_of_hours = 1
	unit_type.rate = 4000
	unit_type.save()
	return unit_type
