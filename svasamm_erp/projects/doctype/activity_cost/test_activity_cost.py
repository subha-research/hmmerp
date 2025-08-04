# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors and Contributors
# See license.txt
import unittest

import frappe
from frappe.tests import IntegrationTestCase

from svasamm_erp.projects.doctype.activity_cost.activity_cost import DuplicationError
from svasamm_erp.tests.utils import ERPNextTestSuite


class TestActivityCost(ERPNextTestSuite):
	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		# TODO: only 1 employee is required
		cls.make_employees()

	def test_duplication(self):
		frappe.db.sql("delete from `tabActivity Cost`")
		activity_cost1 = frappe.new_doc("Activity Cost")
		activity_cost1.update(
			{
				"employee": self.employees[0].name,
				"employee_name": self.employees[0].first_name,
				"activity_type": "_Test Activity Type 1",
				"billing_rate": 100,
				"costing_rate": 50,
			}
		)
		activity_cost1.insert()
		activity_cost2 = frappe.copy_doc(activity_cost1)
		self.assertRaises(DuplicationError, activity_cost2.insert)
		frappe.db.sql("delete from `tabActivity Cost`")
