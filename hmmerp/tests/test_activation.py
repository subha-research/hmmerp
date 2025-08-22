from frappe.tests import IntegrationTestCase

from hmmerp.utilities.activation import get_level


class TestActivation(IntegrationTestCase):
	def test_activation(self):
		levels = get_level()
		self.assertTrue(levels)
