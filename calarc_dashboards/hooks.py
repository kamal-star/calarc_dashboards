app_name = "calarc_dashboards"
app_title = "Calarc Dashboards"
app_publisher = "Kamal"
app_description = "Adds a Dashboards tile to the Frappe desk apps screen"
app_email = "92625927+kamal-star@users.noreply.github.com"
app_license = "mit"

# The tile on /desk (Desktop Settings > Desktop Page = Apps).
# It opens the "Dashboards" workspace, which lists the dashboards as cards.
# sequence_id 1.5 places it right after ERPNext (1) and before Frappe HR (2).
add_to_apps_screen = [
	{
		"name": "calarc_dashboards",
		"logo": "/assets/calarc_dashboards/images/dashboards-logo.svg",
		"title": "Dashboards",
		"route": "/desk/dashboards",
		"sequence_id": 1.5,
		"has_permission": "calarc_dashboards.api.has_app_permission",
	}
]
