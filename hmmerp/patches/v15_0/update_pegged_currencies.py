import frappe

from .setup.install import update_pegged_currencies


def execute():
	update_pegged_currencies()
