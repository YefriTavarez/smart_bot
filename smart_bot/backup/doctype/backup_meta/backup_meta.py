# -*- coding: utf-8 -*-
# Copyright (c) 2015, Yefri Tavarez and contributors
# For license information, please see license.txt
from __future__ import unicode_literals

from frappe.model.document import Document
from datetime import datetime
import frappe
from threading import Thread

DUMP_DATABASE = "mysqldump --user={0} --password={1} {2} > {3}.sql"
GIT_ADD = "git add {}.sql"
GIT_COMMIT = "git commit -m \"Timestamp: {}\""
GIT_PUSH = "git push upstream master"
REMOTE_ADD = "git remote add upstream {}"
REMOTE_DEL = "git remote remove upstream"
BACKUP_PATH = "./{0}/private/backups/{0}bk"

class BackupMeta(Document):
	def do_push(self):
		self.runc("Push")

	def do_commit(self):
		self.runc("Commit")

	def do_track(self):
		self.runc("Add")

	def do_backup(self):
		self.runc("Backup")

	def sync(self):
		for action in ["Backup", "Add", "Commit", "Push"]:
			self.runc(action)
		
	def start_syncing(self):
		self.stop = 0
		frappe.msgprint("Sync service has been started!")
		self.save()

	def stop_syncing(self):
		self.stop = 1
		frappe.msgprint("Sync service has been stopped!")
		self.save()

	def change_directory(self, path):
		from smart_bot.boot import change_directory
		self.previous_path = change_directory(path)

	def add_remote(self):
		from smart_bot.api import validate_URL
		validate_URL(self.github_url)
		self.runc("Add Remote")

	def runc(self, action):
		from smart_bot.boot import execute, clean_dot
		site = clean_dot(self.site) # to remove the ./
		timestamp = str(datetime.now())

		self.change_directory(BACKUP_PATH.format(site)) # to move to the backup folder

		if(action == "Add"):
			gadd = GIT_ADD.format(self.hostname if self.hostname else site)
			execute(gadd)
		elif(action == "Commit"):
			gcommit = GIT_COMMIT.format(timestamp)
			execute(gcommit)
		elif(action == "Push"):
			execute(GIT_PUSH)
		elif(action == "Backup"):
			password = self.get_password()
			filename = self.hostname if self.hostname else site
			dump_site = DUMP_DATABASE.format(self.root_user, password, self.database, filename)
			execute(dump_site)
		elif(action == "Add Remote"):
			git_remote = REMOTE_ADD.format(self.github_url)

			if execute(git_remote): # if the remote exists
				execute(REMOTE_DEL) # remove it
				execute(git_remote) # then re-add it
		else:
			frappe.throw("Unknown action for method -> git")

		self.change_directory(self.previous_path) # to go back to the original folder