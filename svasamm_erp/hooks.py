# # app_name = "svasamm_erp"
# # app_title = "SvasammERP"
# # app_publisher = "Svasamm Research"
# # app_description = "Open-source ERP for managing accounting, sales, inventory, and projects."
# # app_email = "mithune0000@outlook.com"
# # app_license = "mit"

# # # Apps
# # # ------------------

# # # required_apps = []

# # # Each item in the list will be shown as an app in the apps page
# # # add_to_apps_screen = [
# # # 	{
# # # 		"name": "svasamm_erp",
# # # 		"logo": "/assets/svasamm_erp/logo.png",
# # # 		"title": "SvasammERP",
# # # 		"route": "/svasamm_erp",
# # # 		"has_permission": "svasamm_erp.api.permission.has_app_permission"
# # # 	}
# # # ]

# # # Includes in <head>
# # # ------------------

# # # include js, css files in header of desk.html
# # # app_include_css = "/assets/svasamm_erp/css/svasamm_erp.css"
# # # app_include_js = "/assets/svasamm_erp/js/svasamm_erp.js"

# # # include js, css files in header of web template
# # # web_include_css = "/assets/svasamm_erp/css/svasamm_erp.css"
# # # web_include_js = "/assets/svasamm_erp/js/svasamm_erp.js"

# # # include custom scss in every website theme (without file extension ".scss")
# # # website_theme_scss = "svasamm_erp/public/scss/website"

# # # include js, css files in header of web form
# # # webform_include_js = {"doctype": "public/js/doctype.js"}
# # # webform_include_css = {"doctype": "public/css/doctype.css"}

# # # include js in page
# # # page_js = {"page" : "public/js/file.js"}

# # # include js in doctype views
# # # doctype_js = {"doctype" : "public/js/doctype.js"}
# # # doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# # # doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# # # doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# # # Svg Icons
# # # ------------------
# # # include app icons in desk
# # # app_include_icons = "svasamm_erp/public/icons.svg"

# # # Home Pages
# # # ----------

# # # application home page (will override Website Settings)
# # # home_page = "login"

# # # website user home page (by Role)
# # # role_home_page = {
# # # 	"Role": "home_page"
# # # }

# # # Generators
# # # ----------

# # # automatically create page for each record of this doctype
# # # website_generators = ["Web Page"]

# # # automatically load and sync documents of this doctype from downstream apps
# # # importable_doctypes = [doctype_1]

# # # Jinja
# # # ----------

# # # add methods and filters to jinja environment
# # # jinja = {
# # # 	"methods": "svasamm_erp.utils.jinja_methods",
# # # 	"filters": "svasamm_erp.utils.jinja_filters"
# # # }

# # # Installation
# # # ------------

# # # before_install = "svasamm_erp.install.before_install"
# # # after_install = "svasamm_erp.install.after_install"

# # # Uninstallation
# # # ------------

# # # before_uninstall = "svasamm_erp.uninstall.before_uninstall"
# # # after_uninstall = "svasamm_erp.uninstall.after_uninstall"

# # # Integration Setup
# # # ------------------
# # # To set up dependencies/integrations with other apps
# # # Name of the app being installed is passed as an argument

# # # before_app_install = "svasamm_erp.utils.before_app_install"
# # # after_app_install = "svasamm_erp.utils.after_app_install"

# # # Integration Cleanup
# # # -------------------
# # # To clean up dependencies/integrations with other apps
# # # Name of the app being uninstalled is passed as an argument

# # # before_app_uninstall = "svasamm_erp.utils.before_app_uninstall"
# # # after_app_uninstall = "svasamm_erp.utils.after_app_uninstall"

# # # Desk Notifications
# # # ------------------
# # # See frappe.core.notifications.get_notification_config

# # # notification_config = "svasamm_erp.notifications.get_notification_config"

# # # Permissions
# # # -----------
# # # Permissions evaluated in scripted ways

# # # permission_query_conditions = {
# # # 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# # # }
# # #
# # # has_permission = {
# # # 	"Event": "frappe.desk.doctype.event.event.has_permission",
# # # }

# # # Document Events
# # # ---------------
# # # Hook on document methods and events

# # # doc_events = {
# # # 	"*": {
# # # 		"on_update": "method",
# # # 		"on_cancel": "method",
# # # 		"on_trash": "method"
# # # 	}
# # # }

# # # Scheduled Tasks
# # # ---------------

# # # scheduler_events = {
# # # 	"all": [
# # # 		"svasamm_erp.tasks.all"
# # # 	],
# # # 	"daily": [
# # # 		"svasamm_erp.tasks.daily"
# # # 	],
# # # 	"hourly": [
# # # 		"svasamm_erp.tasks.hourly"
# # # 	],
# # # 	"weekly": [
# # # 		"svasamm_erp.tasks.weekly"
# # # 	],
# # # 	"monthly": [
# # # 		"svasamm_erp.tasks.monthly"
# # # 	],
# # # }

# # # Testing
# # # -------

# # # before_tests = "svasamm_erp.install.before_tests"

# # # Overriding Methods
# # # ------------------------------
# # #
# # # override_whitelisted_methods = {
# # # 	"frappe.desk.doctype.event.event.get_events": "svasamm_erp.event.get_events"
# # # }
# # #
# # # each overriding function accepts a `data` argument;
# # # generated from the base implementation of the doctype dashboard,
# # # along with any modifications made in other Frappe apps
# # # override_doctype_dashboards = {
# # # 	"Task": "svasamm_erp.task.get_dashboard_data"
# # # }

# # # exempt linked doctypes from being automatically cancelled
# # #
# # # auto_cancel_exempted_doctypes = ["Auto Repeat"]

# # # Ignore links to specified DocTypes when deleting documents
# # # -----------------------------------------------------------

# # # ignore_links_on_delete = ["Communication", "ToDo"]

# # # Request Events
# # # ----------------
# # # before_request = ["svasamm_erp.utils.before_request"]
# # # after_request = ["svasamm_erp.utils.after_request"]

# # # Job Events
# # # ----------
# # # before_job = ["svasamm_erp.utils.before_job"]
# # # after_job = ["svasamm_erp.utils.after_job"]

# # # User Data Protection
# # # --------------------

# # # user_data_fields = [
# # # 	{
# # # 		"doctype": "{doctype_1}",
# # # 		"filter_by": "{filter_by}",
# # # 		"redact_fields": ["{field_1}", "{field_2}"],
# # # 		"partial": 1,
# # # 	},
# # # 	{
# # # 		"doctype": "{doctype_2}",
# # # 		"filter_by": "{filter_by}",
# # # 		"partial": 1,
# # # 	},
# # # 	{
# # # 		"doctype": "{doctype_3}",
# # # 		"strict": False,
# # # 	},
# # # 	{
# # # 		"doctype": "{doctype_4}"
# # # 	}
# # # ]

# # # Authentication and authorization
# # # --------------------------------

# # # auth_hooks = [
# # # 	"svasamm_erp.auth.validate"
# # # ]

# # # Automatically update python controller files with type annotations for this app.
# # # export_python_type_annotations = True

# # # default_log_clearing_doctypes = {
# # # 	"Logging DocType Name": 30  # days to retain logs
# # # }



# app_name = "svasamm_erp"
# app_title = "SvasammERP"
# app_publisher = "Svasamm Research"
# app_description = """ERP made simple for Svasamm"""
# app_icon = "fa fa-th"
# app_color = "#e74c3c"
# app_email = "mithune0000@outlook.com"
# app_license = "MIT"
# source_link = "https://github.com/svasamm/svasamm-erp"
# app_logo_url = "/assets/svasamm_erp/images/svasamm-logo.svg"
# app_home = "/app/home"

# add_to_apps_screen = [
# 	{
# 		"name": app_name,
# 		"logo": "/assets/svasamm_erp/images/svasamm-logo.svg",
# 		"title": app_title,
# 		"route": app_home,
# 		"has_permission": "svasamm_erp.check_app_permission",
# 	}
# ]

# develop_version = "1.0.0-develop"

# app_include_js = "svasamm_erp.bundle.js"
# app_include_css = "svasamm_erp.bundle.css"
# web_include_css = "svasamm_erp-web.bundle.css"
# email_css = "email_svasamm_erp.bundle.css"

# doctype_js = {
# 	"Address": "public/js/address.js",
# 	"Communication": "public/js/communication.js",
# 	"Event": "public/js/event.js",
# 	"Newsletter": "public/js/newsletter.js",
# 	"Contact": "public/js/contact.js",
# 	"Lead": "public/js/lead.js",
# 	"Opportunity": "public/js/opportunity.js",
# 	"Customer": "public/js/customer.js",
# 	"Item": "public/js/item.js",
# 	"Purchase Order": "public/js/purchase_order.js",
# 	"Sales Order": "public/js/sales_order.js",
# }

# override_whitelisted_methods = {"frappe.www.contact.send_message": "svasamm_erp.templates.utils.send_message"}

# welcome_email = "svasamm_erp.setup.utils.welcome_email"

# after_install = "svasamm_erp.setup.install.after_install"

# boot_session = "svasamm_erp.startup.boot.boot_session"
# notification_config = "svasamm_erp.startup.notifications.get_notification_config"

# treeviews = [
# 	"Account",
# 	"Cost Center",
# 	"Warehouse",
# 	"Item Group",
# 	"Customer Group",
# 	"Supplier Group",
# 	"Sales Person",
# 	"Territory",
# 	"Department",
# ]

# demo_master_doctypes = [
# 	"item_group",
# 	"item",
# 	"customer_group",
# 	"supplier_group",
# 	"customer",
# 	"supplier",
# ]
# demo_transaction_doctypes = [
# 	"purchase_order",
# 	"sales_order",
# ]

# jinja = {
# 	"methods": [
# 		"svasamm_erp.stock.serial_batch_bundle.get_serial_or_batch_nos",
# 		"svasamm_erp.utils.get_currency_symbol",
# 		"svasamm_erp.accounts.utils.get_account_balance",
# 	],
# 	"filters": [
# 		"svasamm_erp.utils.currency",
# 		"svasamm_erp.utils.format_number"
# 	]
# }

# # website
# calendars = ["Task", "Work Order", "Sales Order", "Holiday List", "ToDo"]

# website_generators = ["BOM", "Sales Partner"]

# website_context = {
# 	"favicon": "/assets/svasamm_erp/images/svasamm-favicon.svg",
# 	"splash_image": "/assets/svasamm_erp/images/svasamm-logo.svg",
# }

# website_route_rules = [
# 	{"from_route": "/orders", "to_route": "Sales Order"},
# 	{
# 		"from_route": "/orders/<path:name>",
# 		"to_route": "order",
# 		"defaults": {"doctype": "Sales Order", "parents": [{"label": "Orders", "route": "orders"}]},
# 	},
# 	{"from_route": "/invoices", "to_route": "Sales Invoice"},
# 	{
# 		"from_route": "/invoices/<path:name>",
# 		"to_route": "order",
# 		"defaults": {
# 			"doctype": "Sales Invoice",
# 			"parents": [{"label": "Invoices", "route": "invoices"}],
# 		},
# 	},
# 	{"from_route": "/purchase-orders", "to_route": "Purchase Order"},
# 	{
# 		"from_route": "/purchase-orders/<path:name>",
# 		"to_route": "order",
# 		"defaults": {
# 			"doctype": "Purchase Order",
# 			"parents": [{"label": "Purchase Order", "route": "purchase-orders"}],
# 		},
# 	},
# 	{"from_route": "/quotations", "to_route": "Quotation"},
# 	{
# 		"from_route": "/quotations/<path:name>",
# 		"to_route": "order",
# 		"defaults": {
# 			"doctype": "Quotation",
# 			"parents": [{"label": "Quotations", "route": "quotations"}],
# 		},
# 	},
# ]

# standard_portal_menu_items = [
# 	{"title": "Projects", "route": "/project", "reference_doctype": "Project", "role": "Customer"},
# 	{
# 		"title": "Purchase Orders",
# 		"route": "/purchase-orders",
# 		"reference_doctype": "Purchase Order",
# 		"role": "Supplier",
# 	},
# 	{
# 		"title": "Quotations",
# 		"route": "/quotations",
# 		"reference_doctype": "Quotation",
# 		"role": "Customer",
# 	},
# 	{
# 		"title": "Orders",
# 		"route": "/orders",
# 		"reference_doctype": "Sales Order",
# 		"role": "Customer",
# 	},
# 	{
# 		"title": "Invoices",
# 		"route": "/invoices",
# 		"reference_doctype": "Sales Invoice",
# 		"role": "Customer",
# 	},
# 	{"title": "Addresses", "route": "/addresses", "reference_doctype": "Address"},
# ]

# # Define period closing doctypes for your modules
# period_closing_doctypes = [
# 	"Sales Invoice",
# 	"Purchase Invoice",
# 	"Journal Entry",
# 	"Payment Entry",
# 	"Stock Entry",
# 	"Delivery Note",
# 	"Purchase Receipt",
# 	"Stock Reconciliation",
# ]

# doc_events = {
# 	"*": {
# 		"validate": [
# 			"svasamm_erp.setup.doctype.transaction_deletion_record.transaction_deletion_record.check_for_running_deletion_job",
# 		],
# 	},
# 	tuple(period_closing_doctypes): {
# 		"validate": "svasamm_erp.accounts.doctype.accounting_period.accounting_period.validate_accounting_period_on_doc_save",
# 	},
# 	"Stock Entry": {
# 		"on_submit": "svasamm_erp.stock.doctype.material_request.material_request.update_completed_and_requested_qty",
# 		"on_cancel": "svasamm_erp.stock.doctype.material_request.material_request.update_completed_and_requested_qty",
# 	},
# 	"User": {
# 		"after_insert": "frappe.contacts.doctype.contact.contact.update_contact",
# 		"validate": "svasamm_erp.setup.doctype.employee.employee.validate_employee_role",
# 		"on_update": "svasamm_erp.portal.utils.set_default_role",
# 	},
# 	"Communication": {
# 		"after_insert": [
# 			"svasamm_erp.crm.utils.link_communications_with_prospect",
# 			"svasamm_erp.crm.utils.update_modified_timestamp",
# 		],
# 	},
# 	"Event": {
# 		"after_insert": "svasamm_erp.crm.utils.link_events_with_prospect",
# 	},
# 	"Sales Invoice": {
# 		"on_submit": [
# 			"svasamm_erp.regional.create_transaction_log",
# 		],
# 		"on_trash": "svasamm_erp.regional.check_deletion_permission",
# 	},
# 	"Purchase Invoice": {
# 		"validate": [
# 			"svasamm_erp.regional.united_arab_emirates.utils.update_grand_total_for_rcm",
# 		]
# 	},
# 	"Payment Entry": {
# 		"on_submit": [
# 			"svasamm_erp.regional.create_transaction_log",
# 		],
# 		"on_trash": "svasamm_erp.regional.check_deletion_permission",
# 	},
# 	"Contact": {
# 		"validate": ["svasamm_erp.crm.utils.update_lead_phone_numbers"],
# 	},
# 	"Lead": {
# 		"validate": "svasamm_erp.crm.doctype.lead.lead.validate_lead"
# 	},
# 	"Opportunity": {
# 		"validate": "svasamm_erp.crm.doctype.opportunity.opportunity.validate_opportunity"
# 	},
# }

# # function should expect the variable and doc as arguments
# naming_series_variables = {
# 	"FY": "svasamm_erp.accounts.utils.parse_naming_series_variable",
# 	"ABBR": "svasamm_erp.accounts.utils.parse_naming_series_variable",
# }

# auto_cancel_exempted_doctypes = [
# 	"Payment Entry",
# ]

# scheduler_events = {
# 	"cron": {
# 		"0/15 * * * *": [],
# 		"0/30 * * * *": [],
# 		"30 * * * *": [],
# 		"45 0 * * *": [],
# 	},
# 	"hourly": [],
# 	"hourly_long": [],
# 	"hourly_maintenance": [],
# 	"daily": [
# 		"svasamm_erp.crm.doctype.lead.lead.daily_lead_cleanup",
# 	],
# 	"daily_long": [],
# 	"daily_maintenance": [
# 		"svasamm_erp.crm.doctype.opportunity.opportunity.auto_close_opportunity",
# 		"svasamm_erp.controllers.accounts_controller.update_invoice_status",
# 		"svasamm_erp.accounts.doctype.fiscal_year.fiscal_year.auto_create_fiscal_year",
# 		"svasamm_erp.stock.doctype.serial_no.serial_no.update_maintenance_status",
# 		"svasamm_erp.buying.doctype.supplier_scorecard.supplier_scorecard.refresh_scorecards",
# 		"svasamm_erp.setup.doctype.company.company.cache_companies_monthly_sales_history",
# 		"svasamm_erp.assets.doctype.asset.asset.update_maintenance_status",
# 		"svasamm_erp.crm.doctype.contract.contract.update_status_for_contracts",
# 		"svasamm_erp.selling.doctype.quotation.quotation.set_expired_status",
# 		"svasamm_erp.buying.doctype.supplier_quotation.supplier_quotation.set_expired_status",
# 		"svasamm_erp.stock.reorder_item.reorder_item",
# 		"svasamm_erp.setup.doctype.email_digest.email_digest.send",
# 	],
# 	"weekly": [],
# 	"monthly_long": [
# 		"svasamm_erp.accounts.deferred_revenue.process_deferred_accounting",
# 	],
# }

# email_brand_image = "assets/svasamm_erp/images/svasamm-logo.jpg"

# default_mail_footer = """
# 	<span>
# 		Sent via
# 		<a class="text-muted" href="https://svasamm.com" target="_blank">
# 			SvasammERP
# 		</a>
# 	</span>
# """

# get_translated_dict = {("doctype", "Global Defaults"): "frappe.geo.country_info.get_translated_dict"}

# get_site_info = "svasamm_erp.utilities.get_site_info"

# payment_gateway_enabled = "svasamm_erp.accounts.utils.create_payment_gateway_account"

# communication_doctypes = ["Customer", "Supplier"]

# advance_payment_receivable_doctypes = ["Sales Order"]
# advance_payment_payable_doctypes = ["Purchase Order"]

# invoice_doctypes = ["Sales Invoice", "Purchase Invoice"]

# bank_reconciliation_doctypes = [
# 	"Payment Entry",
# 	"Journal Entry",
# 	"Purchase Invoice",
# 	"Sales Invoice",
# ]

# accounting_dimension_doctypes = [
# 	"GL Entry",
# 	"Payment Ledger Entry",
# 	"Sales Invoice",
# 	"Purchase Invoice",
# 	"Payment Entry",
# 	"Asset",
# 	"Stock Entry",
# 	"Budget",
# 	"Delivery Note",
# 	"Sales Invoice Item",
# 	"Purchase Invoice Item",
# 	"Purchase Order Item",
# 	"Sales Order Item",
# 	"Journal Entry Account",
# 	"Material Request Item",
# 	"Delivery Note Item",
# 	"Purchase Receipt Item",
# 	"Stock Entry Detail",
# 	"Payment Entry Deduction",
# 	"Sales Taxes and Charges",
# 	"Purchase Taxes and Charges",
# 	"Shipping Rule",
# 	"Landed Cost Item",
# 	"Asset Value Adjustment",
# 	"Asset Repair",
# 	"Asset Capitalization",
# 	"Stock Reconciliation",
# 	"POS Profile",
# 	"Opening Invoice Creation Tool",
# 	"Opening Invoice Creation Tool Item",
# 	"POS Invoice",
# 	"POS Invoice Item",
# 	"Purchase Order",
# 	"Purchase Receipt",
# 	"Sales Order",
# 	"Supplier Quotation",
# 	"Supplier Quotation Item",
# 	"Payment Reconciliation",
# 	"Payment Reconciliation Allocation",
# 	"Payment Request",
# ]

# regional_overrides = {
# 	"India": {
# 		"svasamm_erp.controllers.taxes_and_totals.update_itemised_tax_data": "svasamm_erp.regional.india.utils.update_itemised_tax_data"
# 	},
# 	"United Arab Emirates": {
# 		"svasamm_erp.controllers.taxes_and_totals.update_itemised_tax_data": "svasamm_erp.regional.united_arab_emirates.utils.update_itemised_tax_data",
# 		"svasamm_erp.accounts.doctype.purchase_invoice.purchase_invoice.make_regional_gl_entries": "svasamm_erp.regional.united_arab_emirates.utils.make_regional_gl_entries",
# 	},
# }

# user_privacy_documents = [
# 	{
# 		"doctype": "Lead",
# 		"match_field": "email_id",
# 		"personal_fields": ["phone", "mobile_no", "fax", "website", "lead_name"],
# 	},
# 	{
# 		"doctype": "Opportunity",
# 		"match_field": "contact_email",
# 		"personal_fields": ["contact_mobile", "contact_display", "customer_name"],
# 	},
# ]

# # SvasammERP doctypes for Global Search
# global_search_doctypes = {
# 	"Default": [
# 		{"doctype": "Customer", "index": 0},
# 		{"doctype": "Supplier", "index": 1},
# 		{"doctype": "Item", "index": 2},
# 		{"doctype": "Warehouse", "index": 3},
# 		{"doctype": "Account", "index": 4},
# 		{"doctype": "BOM", "index": 6},
# 		{"doctype": "Sales Invoice", "index": 7},
# 		{"doctype": "Sales Order", "index": 8},
# 		{"doctype": "Quotation", "index": 9},
# 		{"doctype": "Work Order", "index": 10},
# 		{"doctype": "Purchase Order", "index": 11},
# 		{"doctype": "Purchase Receipt", "index": 12},
# 		{"doctype": "Purchase Invoice", "index": 13},
# 		{"doctype": "Delivery Note", "index": 14},
# 		{"doctype": "Stock Entry", "index": 15},
# 		{"doctype": "Material Request", "index": 16},
# 		{"doctype": "Payment Entry", "index": 22},
# 		{"doctype": "Lead", "index": 23},
# 		{"doctype": "Opportunity", "index": 24},
# 		{"doctype": "Item Price", "index": 25},
# 		{"doctype": "Purchase Taxes and Charges Template", "index": 26},
# 		{"doctype": "Sales Taxes and Charges", "index": 27},
# 		{"doctype": "Asset", "index": 28},
# 		{"doctype": "Project", "index": 29},
# 		{"doctype": "Task", "index": 30},
# 		{"doctype": "Serial No", "index": 33},
# 		{"doctype": "Batch", "index": 34},
# 		{"doctype": "Department", "index": 36},
# 	],
# }

# default_log_clearing_doctypes = {
# 	"Repost Item Valuation": 60,
# }

# export_python_type_annotations = True

# fields_for_group_similar_items = ["qty", "amount"]


app_name = "svasamm_erp"
app_title = "svasamm_erp"
app_publisher = "Frappe Technologies Pvt. Ltd."
app_description = """ERP made simple"""
app_icon = "fa fa-th"
app_color = "#e74c3c"
app_email = "hello@frappe.io"
app_license = "GNU General Public License (v3)"
source_link = "https://github.com/frappe/svasamm_erp"
app_logo_url = "/assets/svasamm_erp/images/svasamm_erp-logo.svg"
app_home = "/app/home"

add_to_apps_screen = [
	{
		"name": app_name,
		"logo": "/assets/svasamm_erp/images/svasamm_erp-logo.svg",
		"title": app_title,
		"route": app_home,
		"has_permission": "svasamm_erp.check_app_permission",
	}
]

develop_version = "15.x.x-develop"

app_include_js = "svasamm_erp.bundle.js"
app_include_css = "svasamm_erp.bundle.css"
web_include_css = "svasamm_erp-web.bundle.css"
email_css = "svasamm_erp_email.bundle.css"

app_include_icons = [
	"/assets/svasamm_erp/icons/pos-icons.svg",
]

web_include_icons = [
	"/assets/svasamm_erp/icons/pos-icons.svg",
]

doctype_js = {
	"Address": "public/js/address.js",
	"Communication": "public/js/communication.js",
	"Event": "public/js/event.js",
	"Newsletter": "public/js/newsletter.js",
	"Contact": "public/js/contact.js",
}
doctype_list_js = {
	"Code List": [
		"edi/doctype/code_list/code_list_import.js",
	],
	"Common Code": [
		"edi/doctype/code_list/code_list_import.js",
	],
}

override_doctype_class = {"Address": "svasamm_erp.accounts.custom.address.ERPNextAddress"}

override_whitelisted_methods = {"frappe.www.contact.send_message": "svasamm_erp.templates.utils.send_message"}

welcome_email = "svasamm_erp.setup.utils.welcome_email"

# setup wizard
setup_wizard_requires = "assets/svasamm_erp/js/setup_wizard.js"
setup_wizard_stages = "svasamm_erp.setup.setup_wizard.setup_wizard.get_setup_stages"
setup_wizard_complete = "svasamm_erp.setup.setup_wizard.setup_wizard.setup_demo"
setup_wizard_test = "svasamm_erp.setup.setup_wizard.test_setup_wizard.run_setup_wizard_test"

after_install = "svasamm_erp.setup.install.after_install"

boot_session = "svasamm_erp.startup.boot.boot_session"
notification_config = "svasamm_erp.startup.notifications.get_notification_config"
get_help_messages = "svasamm_erp.utilities.activation.get_help_messages"
leaderboards = "svasamm_erp.startup.leaderboard.get_leaderboards"
filters_config = "svasamm_erp.startup.filters.get_filters_config"
additional_print_settings = "svasamm_erp.controllers.print_settings.get_print_settings"

on_session_creation = "svasamm_erp.portal.utils.create_customer_or_supplier"

treeviews = [
	"Account",
	"Cost Center",
	"Warehouse",
	"Item Group",
	"Customer Group",
	"Supplier Group",
	"Sales Person",
	"Territory",
	"Department",
]

demo_master_doctypes = [
	"item_group",
	"item",
	"customer_group",
	"supplier_group",
	"customer",
	"supplier",
]
demo_transaction_doctypes = [
	"purchase_order",
	"sales_order",
]

jinja = {
	"methods": [
		"svasamm_erp.stock.serial_batch_bundle.get_serial_or_batch_nos",
	],
}

# website
webform_list_context = "svasamm_erp.controllers.website_list_for_contact.get_webform_list_context"

calendars = ["Task", "Work Order", "Sales Order", "Holiday List", "ToDo"]

website_generators = ["BOM", "Sales Partner"]

website_context = {
	"favicon": "/assets/svasamm_erp/images/svasamm_erp-favicon.svg",
	"splash_image": "/assets/svasamm_erp/images/svasamm_erp-logo.svg",
}

# nosemgrep
website_route_rules = [
	{"from_route": "/orders", "to_route": "Sales Order"},
	{
		"from_route": "/orders/<path:name>",
		"to_route": "order",
		"defaults": {"doctype": "Sales Order", "parents": [{"label": "Orders", "route": "orders"}]},
	},
	{"from_route": "/invoices", "to_route": "Sales Invoice"},
	{
		"from_route": "/invoices/<path:name>",
		"to_route": "order",
		"defaults": {
			"doctype": "Sales Invoice",
			"parents": [{"label": "Invoices", "route": "invoices"}],
		},
	},
	{"from_route": "/supplier-quotations", "to_route": "Supplier Quotation"},
	{
		"from_route": "/supplier-quotations/<path:name>",
		"to_route": "order",
		"defaults": {
			"doctype": "Supplier Quotation",
			"parents": [{"label": "Supplier Quotation", "route": "supplier-quotations"}],
		},
	},
	{"from_route": "/purchase-orders", "to_route": "Purchase Order"},
	{
		"from_route": "/purchase-orders/<path:name>",
		"to_route": "order",
		"defaults": {
			"doctype": "Purchase Order",
			"parents": [{"label": "Purchase Order", "route": "purchase-orders"}],
		},
	},
	{"from_route": "/purchase-invoices", "to_route": "Purchase Invoice"},
	{
		"from_route": "/purchase-invoices/<path:name>",
		"to_route": "order",
		"defaults": {
			"doctype": "Purchase Invoice",
			"parents": [{"label": "Purchase Invoice", "route": "purchase-invoices"}],
		},
	},
	{"from_route": "/quotations", "to_route": "Quotation"},
	{
		"from_route": "/quotations/<path:name>",
		"to_route": "order",
		"defaults": {
			"doctype": "Quotation",
			"parents": [{"label": "Quotations", "route": "quotations"}],
		},
	},
	{"from_route": "/shipments", "to_route": "Delivery Note"},
	{
		"from_route": "/shipments/<path:name>",
		"to_route": "order",
		"defaults": {
			"doctype": "Delivery Note",
			"parents": [{"label": "Shipments", "route": "shipments"}],
		},
	},
	{"from_route": "/rfq", "to_route": "Request for Quotation"},
	{
		"from_route": "/rfq/<path:name>",
		"to_route": "rfq",
		"defaults": {
			"doctype": "Request for Quotation",
			"parents": [{"label": "Request for Quotation", "route": "rfq"}],
		},
	},
	{"from_route": "/addresses", "to_route": "Address"},
	{
		"from_route": "/addresses/<path:name>",
		"to_route": "addresses",
		"defaults": {"doctype": "Address", "parents": [{"label": "Addresses", "route": "addresses"}]},
	},
	{"from_route": "/boms", "to_route": "BOM"},
	{"from_route": "/timesheets", "to_route": "Timesheet"},
	{"from_route": "/material-requests", "to_route": "Material Request"},
	{
		"from_route": "/material-requests/<path:name>",
		"to_route": "material_request_info",
		"defaults": {
			"doctype": "Material Request",
			"parents": [{"label": "Material Request", "route": "material-requests"}],
		},
	},
	{"from_route": "/project", "to_route": "Project"},
	{"from_route": "/tasks", "to_route": "Task"},
]

standard_portal_menu_items = [
	{"title": "Projects", "route": "/project", "reference_doctype": "Project", "role": "Customer"},
	{
		"title": "Request for Quotations",
		"route": "/rfq",
		"reference_doctype": "Request for Quotation",
		"role": "Supplier",
	},
	{
		"title": "Supplier Quotation",
		"route": "/supplier-quotations",
		"reference_doctype": "Supplier Quotation",
		"role": "Supplier",
	},
	{
		"title": "Purchase Orders",
		"route": "/purchase-orders",
		"reference_doctype": "Purchase Order",
		"role": "Supplier",
	},
	{
		"title": "Purchase Invoices",
		"route": "/purchase-invoices",
		"reference_doctype": "Purchase Invoice",
		"role": "Supplier",
	},
	{
		"title": "Quotations",
		"route": "/quotations",
		"reference_doctype": "Quotation",
		"role": "Customer",
	},
	{
		"title": "Orders",
		"route": "/orders",
		"reference_doctype": "Sales Order",
		"role": "Customer",
	},
	{
		"title": "Invoices",
		"route": "/invoices",
		"reference_doctype": "Sales Invoice",
		"role": "Customer",
	},
	{
		"title": "Shipments",
		"route": "/shipments",
		"reference_doctype": "Delivery Note",
		"role": "Customer",
	},
	{"title": "Issues", "route": "/issues", "reference_doctype": "Issue", "role": "Customer"},
	{"title": "Addresses", "route": "/addresses", "reference_doctype": "Address"},
	{
		"title": "Timesheets",
		"route": "/timesheets",
		"reference_doctype": "Timesheet",
		"role": "Customer",
	},
	{"title": "Newsletter", "route": "/newsletters", "reference_doctype": "Newsletter"},
	{
		"title": "Material Request",
		"route": "/material-requests",
		"reference_doctype": "Material Request",
		"role": "Customer",
	},
	{"title": "Appointment Booking", "route": "/book_appointment"},
]

sounds = [
	{"name": "incoming-call", "src": "/assets/svasamm_erp/sounds/incoming-call.mp3", "volume": 0.2},
	{"name": "call-disconnect", "src": "/assets/svasamm_erp/sounds/call-disconnect.mp3", "volume": 0.2},
	{"name": "numpad-touch", "src": "/assets/svasamm_erp/sounds/numpad-touch.mp3", "volume": 0.8},
]

has_upload_permission = {"Employee": "svasamm_erp.setup.doctype.employee.employee.has_upload_permission"}

has_website_permission = {
	"Sales Order": "svasamm_erp.controllers.website_list_for_contact.has_website_permission",
	"Quotation": "svasamm_erp.controllers.website_list_for_contact.has_website_permission",
	"Sales Invoice": "svasamm_erp.controllers.website_list_for_contact.has_website_permission",
	"Supplier Quotation": "svasamm_erp.controllers.website_list_for_contact.has_website_permission",
	"Purchase Order": "svasamm_erp.controllers.website_list_for_contact.has_website_permission",
	"Purchase Invoice": "svasamm_erp.controllers.website_list_for_contact.has_website_permission",
	"Material Request": "svasamm_erp.controllers.website_list_for_contact.has_website_permission",
	"Delivery Note": "svasamm_erp.controllers.website_list_for_contact.has_website_permission",
	"Issue": "svasamm_erp.support.doctype.issue.issue.has_website_permission",
	"Timesheet": "svasamm_erp.controllers.website_list_for_contact.has_website_permission",
	"Project": "svasamm_erp.controllers.website_list_for_contact.has_website_permission",
}

before_tests = "svasamm_erp.setup.utils.before_tests"


period_closing_doctypes = [
	"Sales Invoice",
	"Purchase Invoice",
	"Journal Entry",
	"Bank Clearance",
	"Stock Entry",
	"Dunning",
	"Invoice Discounting",
	"Payment Entry",
	"Period Closing Voucher",
	"Process Deferred Accounting",
	"Asset",
	"Asset Capitalization",
	"Asset Repair",
	"Delivery Note",
	"Landed Cost Voucher",
	"Purchase Receipt",
	"Stock Reconciliation",
	"Subcontracting Receipt",
]

doc_events = {
	"*": {
		"validate": [
			"svasamm_erp.support.doctype.service_level_agreement.service_level_agreement.apply",
			"svasamm_erp.setup.doctype.transaction_deletion_record.transaction_deletion_record.check_for_running_deletion_job",
		],
	},
	tuple(period_closing_doctypes): {
		"validate": "svasamm_erp.accounts.doctype.accounting_period.accounting_period.validate_accounting_period_on_doc_save",
	},
	"Stock Entry": {
		"on_submit": "svasamm_erp.stock.doctype.material_request.material_request.update_completed_and_requested_qty",
		"on_cancel": "svasamm_erp.stock.doctype.material_request.material_request.update_completed_and_requested_qty",
	},
	"User": {
		"after_insert": "frappe.contacts.doctype.contact.contact.update_contact",
		"validate": "svasamm_erp.setup.doctype.employee.employee.validate_employee_role",
		"on_update": "svasamm_erp.portal.utils.set_default_role",
	},
	"Communication": {
		"on_update": [
			"svasamm_erp.support.doctype.service_level_agreement.service_level_agreement.on_communication_update",
			"svasamm_erp.support.doctype.issue.issue.set_first_response_time",
		],
		"after_insert": [
			"svasamm_erp.crm.utils.link_communications_with_prospect",
			"svasamm_erp.crm.utils.update_modified_timestamp",
		],
	},
	"Event": {
		"after_insert": "svasamm_erp.crm.utils.link_events_with_prospect",
	},
	"Sales Invoice": {
		"on_submit": [
			"svasamm_erp.regional.create_transaction_log",
			"svasamm_erp.regional.italy.utils.sales_invoice_on_submit",
		],
		"on_cancel": ["svasamm_erp.regional.italy.utils.sales_invoice_on_cancel"],
		"on_trash": "svasamm_erp.regional.check_deletion_permission",
	},
	"Purchase Invoice": {
		"validate": [
			"svasamm_erp.regional.united_arab_emirates.utils.update_grand_total_for_rcm",
			"svasamm_erp.regional.united_arab_emirates.utils.validate_returns",
		]
	},
	"Payment Entry": {
		"on_submit": [
			"svasamm_erp.regional.create_transaction_log",
			"svasamm_erp.accounts.doctype.dunning.dunning.resolve_dunning",
		],
		"on_cancel": ["svasamm_erp.accounts.doctype.dunning.dunning.resolve_dunning"],
		"on_trash": "svasamm_erp.regional.check_deletion_permission",
	},
	"Address": {
		"validate": [
			"svasamm_erp.regional.italy.utils.set_state_code",
		],
	},
	"Contact": {
		"on_trash": "svasamm_erp.support.doctype.issue.issue.update_issue",
		"after_insert": "svasamm_erp.telephony.doctype.call_log.call_log.link_existing_conversations",
		"validate": ["svasamm_erp.crm.utils.update_lead_phone_numbers"],
	},
	"Email Unsubscribe": {
		"after_insert": "svasamm_erp.crm.doctype.email_campaign.email_campaign.unsubscribe_recipient"
	},
	"Integration Request": {
		"validate": "svasamm_erp.accounts.doctype.payment_request.payment_request.validate_payment"
	},
}

# function should expect the variable and doc as arguments
naming_series_variables = {
	"FY": "svasamm_erp.accounts.utils.parse_naming_series_variable",
	"ABBR": "svasamm_erp.accounts.utils.parse_naming_series_variable",
}

# On cancel event Payment Entry will be exempted and all linked submittable doctype will get cancelled.
# to maintain data integrity we exempted payment entry. it will un-link when sales invoice get cancelled.
# if payment entry not in auto cancel exempted doctypes it will cancel payment entry.
auto_cancel_exempted_doctypes = [
	"Payment Entry",
]

scheduler_events = {
	"cron": {
		"0/15 * * * *": [
			"svasamm_erp.manufacturing.doctype.bom_update_log.bom_update_log.resume_bom_cost_update_jobs",
		],
		"0/30 * * * *": [],
		# Hourly but offset by 30 minutes
		"30 * * * *": [
			"svasamm_erp.accounts.doctype.gl_entry.gl_entry.rename_gle_sle_docs",
		],
		# Daily but offset by 45 minutes
		"45 0 * * *": [],
	},
	"hourly": [
		"svasamm_erp.projects.doctype.project.project.hourly_reminder",
	],
	"hourly_long": [],
	"hourly_maintenance": [
		"svasamm_erp.stock.doctype.repost_item_valuation.repost_item_valuation.repost_entries",
		"svasamm_erp.utilities.bulk_transaction.retry",
		"svasamm_erp.projects.doctype.project.project.collect_project_status",
		"svasamm_erp.projects.doctype.project.project.project_status_update_reminder",
		"svasamm_erp.svasamm_erp_integrations.doctype.plaid_settings.plaid_settings.automatic_synchronization",
		"svasamm_erp.utilities.doctype.video.video.update_youtube_data",
	],
	"daily": [],
	"daily_long": [],
	"daily_maintenance": [
		"svasamm_erp.support.doctype.issue.issue.auto_close_tickets",
		"svasamm_erp.crm.doctype.opportunity.opportunity.auto_close_opportunity",
		"svasamm_erp.controllers.accounts_controller.update_invoice_status",
		"svasamm_erp.accounts.doctype.fiscal_year.fiscal_year.auto_create_fiscal_year",
		"svasamm_erp.projects.doctype.task.task.set_tasks_as_overdue",
		"svasamm_erp.stock.doctype.serial_no.serial_no.update_maintenance_status",
		"svasamm_erp.buying.doctype.supplier_scorecard.supplier_scorecard.refresh_scorecards",
		"svasamm_erp.setup.doctype.company.company.cache_companies_monthly_sales_history",
		"svasamm_erp.assets.doctype.asset.asset.update_maintenance_status",
		"svasamm_erp.assets.doctype.asset.asset.make_post_gl_entry",
		"svasamm_erp.crm.doctype.contract.contract.update_status_for_contracts",
		"svasamm_erp.projects.doctype.project.project.update_project_sales_billing",
		"svasamm_erp.projects.doctype.project.project.send_project_status_email_to_users",
		"svasamm_erp.quality_management.doctype.quality_review.quality_review.review",
		"svasamm_erp.support.doctype.service_level_agreement.service_level_agreement.check_agreement_status",
		"svasamm_erp.crm.doctype.email_campaign.email_campaign.send_email_to_leads_or_contacts",
		"svasamm_erp.crm.doctype.email_campaign.email_campaign.set_email_campaign_status",
		"svasamm_erp.selling.doctype.quotation.quotation.set_expired_status",
		"svasamm_erp.buying.doctype.supplier_quotation.supplier_quotation.set_expired_status",
		"svasamm_erp.accounts.doctype.process_statement_of_accounts.process_statement_of_accounts.send_auto_email",
		"svasamm_erp.accounts.utils.auto_create_exchange_rate_revaluation_daily",
		"svasamm_erp.accounts.utils.run_ledger_health_checks",
		"svasamm_erp.assets.doctype.asset_maintenance_log.asset_maintenance_log.update_asset_maintenance_log_status",
		"svasamm_erp.stock.reorder_item.reorder_item",
		"svasamm_erp.accounts.doctype.process_subscription.process_subscription.create_subscription_process",
		"svasamm_erp.setup.doctype.email_digest.email_digest.send",
		"svasamm_erp.manufacturing.doctype.bom_update_tool.bom_update_tool.auto_update_latest_price_in_all_boms",
		"svasamm_erp.crm.utils.open_leads_opportunities_based_on_todays_event",
		"svasamm_erp.assets.doctype.asset.depreciation.post_depreciation_entries",
	],
	"weekly": [
		"svasamm_erp.accounts.utils.auto_create_exchange_rate_revaluation_weekly",
	],
	"monthly_long": [
		"svasamm_erp.accounts.deferred_revenue.process_deferred_accounting",
		"svasamm_erp.accounts.utils.auto_create_exchange_rate_revaluation_monthly",
	],
}

email_brand_image = "assets/svasamm_erp/images/svasamm_erp-logo.jpg"

default_mail_footer = """
	<span>
		Sent via
		<a class="text-muted" href="https://frappe.io/svasamm_erp?source=via_email_footer" target="_blank">
			ERPNext
		</a>
	</span>
"""

get_translated_dict = {("doctype", "Global Defaults"): "frappe.geo.country_info.get_translated_dict"}

bot_parsers = [
	"svasamm_erp.utilities.bot.FindItemBot",
]

get_site_info = "svasamm_erp.utilities.get_site_info"

payment_gateway_enabled = "svasamm_erp.accounts.utils.create_payment_gateway_account"

communication_doctypes = ["Customer", "Supplier"]

advance_payment_receivable_doctypes = ["Sales Order"]
advance_payment_payable_doctypes = ["Purchase Order"]

invoice_doctypes = ["Sales Invoice", "Purchase Invoice"]

bank_reconciliation_doctypes = [
	"Payment Entry",
	"Journal Entry",
	"Purchase Invoice",
	"Sales Invoice",
]

accounting_dimension_doctypes = [
	"GL Entry",
	"Payment Ledger Entry",
	"Sales Invoice",
	"Purchase Invoice",
	"Payment Entry",
	"Asset",
	"Stock Entry",
	"Budget",
	"Delivery Note",
	"Sales Invoice Item",
	"Purchase Invoice Item",
	"Purchase Order Item",
	"Sales Order Item",
	"Journal Entry Account",
	"Material Request Item",
	"Delivery Note Item",
	"Purchase Receipt Item",
	"Stock Entry Detail",
	"Payment Entry Deduction",
	"Sales Taxes and Charges",
	"Purchase Taxes and Charges",
	"Shipping Rule",
	"Landed Cost Item",
	"Asset Value Adjustment",
	"Asset Repair",
	"Asset Capitalization",
	"Loyalty Program",
	"Stock Reconciliation",
	"POS Profile",
	"Opening Invoice Creation Tool",
	"Opening Invoice Creation Tool Item",
	"Subscription",
	"Subscription Plan",
	"POS Invoice",
	"POS Invoice Item",
	"Purchase Order",
	"Purchase Receipt",
	"Sales Order",
	"Subcontracting Order",
	"Subcontracting Order Item",
	"Subcontracting Receipt",
	"Subcontracting Receipt Item",
	"Account Closing Balance",
	"Supplier Quotation",
	"Supplier Quotation Item",
	"Payment Reconciliation",
	"Payment Reconciliation Allocation",
	"Payment Request",
	"Asset Movement Item",
	"Asset Depreciation Schedule",
]

get_matching_queries = (
	"svasamm_erp.accounts.doctype.bank_reconciliation_tool.bank_reconciliation_tool.get_matching_queries"
)

get_amounts_not_reflected_in_system_for_bank_reconciliation_statement = "svasamm_erp.accounts.report.bank_reconciliation_statement.bank_reconciliation_statement.get_amounts_not_reflected_in_system_for_bank_reconciliation_statement"

get_payment_entries_for_bank_clearance = (
	"svasamm_erp.accounts.doctype.bank_clearance.bank_clearance.get_payment_entries_for_bank_clearance"
)

get_entries_for_bank_clearance_summary = "svasamm_erp.accounts.report.bank_clearance_summary.bank_clearance_summary.get_entries_for_bank_clearance_summary"

get_entries_for_bank_reconciliation_statement = "svasamm_erp.accounts.report.bank_reconciliation_statement.bank_reconciliation_statement.get_entries_for_bank_reconciliation_statement"

regional_overrides = {
	"France": {"svasamm_erp.tests.test_regional.test_method": "svasamm_erp.regional.france.utils.test_method"},
	"United Arab Emirates": {
		"svasamm_erp.controllers.taxes_and_totals.update_itemised_tax_data": "svasamm_erp.regional.united_arab_emirates.utils.update_itemised_tax_data",
		"svasamm_erp.accounts.doctype.purchase_invoice.purchase_invoice.make_regional_gl_entries": "svasamm_erp.regional.united_arab_emirates.utils.make_regional_gl_entries",
	},
	"Saudi Arabia": {
		"svasamm_erp.controllers.taxes_and_totals.update_itemised_tax_data": "svasamm_erp.regional.united_arab_emirates.utils.update_itemised_tax_data"
	},
	"Italy": {
		"svasamm_erp.controllers.taxes_and_totals.update_itemised_tax_data": "svasamm_erp.regional.italy.utils.update_itemised_tax_data",
		"svasamm_erp.controllers.accounts_controller.validate_regional": "svasamm_erp.regional.italy.utils.sales_invoice_validate",
	},
}
user_privacy_documents = [
	{
		"doctype": "Lead",
		"match_field": "email_id",
		"personal_fields": ["phone", "mobile_no", "fax", "website", "lead_name"],
	},
	{
		"doctype": "Opportunity",
		"match_field": "contact_email",
		"personal_fields": ["contact_mobile", "contact_display", "customer_name"],
	},
]

# ERPNext doctypes for Global Search
global_search_doctypes = {
	"Default": [
		{"doctype": "Customer", "index": 0},
		{"doctype": "Supplier", "index": 1},
		{"doctype": "Item", "index": 2},
		{"doctype": "Warehouse", "index": 3},
		{"doctype": "Account", "index": 4},
		{"doctype": "Employee", "index": 5},
		{"doctype": "BOM", "index": 6},
		{"doctype": "Sales Invoice", "index": 7},
		{"doctype": "Sales Order", "index": 8},
		{"doctype": "Quotation", "index": 9},
		{"doctype": "Work Order", "index": 10},
		{"doctype": "Purchase Order", "index": 11},
		{"doctype": "Purchase Receipt", "index": 12},
		{"doctype": "Purchase Invoice", "index": 13},
		{"doctype": "Delivery Note", "index": 14},
		{"doctype": "Stock Entry", "index": 15},
		{"doctype": "Material Request", "index": 16},
		{"doctype": "Delivery Trip", "index": 17},
		{"doctype": "Pick List", "index": 18},
		{"doctype": "Payment Entry", "index": 22},
		{"doctype": "Lead", "index": 23},
		{"doctype": "Opportunity", "index": 24},
		{"doctype": "Item Price", "index": 25},
		{"doctype": "Purchase Taxes and Charges Template", "index": 26},
		{"doctype": "Sales Taxes and Charges", "index": 27},
		{"doctype": "Asset", "index": 28},
		{"doctype": "Project", "index": 29},
		{"doctype": "Task", "index": 30},
		{"doctype": "Timesheet", "index": 31},
		{"doctype": "Issue", "index": 32},
		{"doctype": "Serial No", "index": 33},
		{"doctype": "Batch", "index": 34},
		{"doctype": "Branch", "index": 35},
		{"doctype": "Department", "index": 36},
		{"doctype": "Designation", "index": 38},
		{"doctype": "Maintenance Schedule", "index": 45},
		{"doctype": "Maintenance Visit", "index": 46},
		{"doctype": "Warranty Claim", "index": 47},
	],
}

additional_timeline_content = {"*": ["svasamm_erp.telephony.doctype.call_log.call_log.get_linked_call_logs"]}


extend_bootinfo = [
	# "svasamm_erp.support.doctype.service_level_agreement.service_level_agreement.add_sla_doctypes",
	"svasamm_erp.startup.boot.bootinfo",
]


default_log_clearing_doctypes = {
	"Repost Item Valuation": 60,
}

export_python_type_annotations = True

fields_for_group_similar_items = ["qty", "amount"]
