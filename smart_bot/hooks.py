# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "smart_bot"
app_title = "Smart Bot"
app_publisher = "Yefri Tavarez"
app_description = "An application for helping the the user to do more with less in the Frappe framework"
app_icon = "octicon octicon-hubot"
app_color = "#194085"
app_email = "yefritavarez@hotmail.com"
app_license = "General Public License v3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/smart_bot/css/smart_bot.css"
# app_include_js = "/assets/smart_bot/js/smart_bot.js"

# include js, css files in header of web template
# web_include_css = "/assets/smart_bot/css/smart_bot.css"
# web_include_js = "/assets/smart_bot/js/smart_bot.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "smart_bot.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "smart_bot.install.before_install"
after_install = "smart_bot.boot.after_install"
before_uninstall = "smart_bot.boot.before_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "smart_bot.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
	"all": [
		"smart_bot.bot.do_task"
	]
}

# scheduler_events = {
# 	"all": [
# 		"smart_bot.tasks.all"
# 	],
# 	"daily": [
# 		"smart_bot.tasks.daily"
# 	],
# 	"hourly": [
# 		"smart_bot.tasks.hourly"
# 	],
# 	"weekly": [
# 		"smart_bot.tasks.weekly"
# 	]
# 	"monthly": [
# 		"smart_bot.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "smart_bot.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "smart_bot.event.get_events"
# }

