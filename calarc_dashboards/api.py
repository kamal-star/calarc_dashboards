import frappe


def has_app_permission():
	"""Show the Dashboards tile to desk (System) users only."""
	user = frappe.session.user
	if user == "Guest":
		return False
	if user == "Administrator":
		return True
	return frappe.get_cached_value("User", user, "user_type") == "System User"
