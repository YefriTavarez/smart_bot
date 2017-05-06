import frappe, os

def after_install():
	doc = set_database_name()
	create_bk_folder(doc)
	initialize_repo(doc)

def set_database_name():
	doc = frappe.new_doc("Backup Meta")
	doc.root_user = "root"
	doc.stop = 1
	doc.database = frappe.conf.db_name
	doc.site = frappe.utils.get_site_path()

	get_public_key(doc)

	return doc.insert() # to save the changes to the DB

def create_bk_folder(doc):
	from os import mkdir

	backup_path = "{0}/private/backups/{0}bk".format(doc.site)
	mkdir(backup_path)

def initialize_repo(doc):
	site = clean_dot(doc.site)
	backup_path = "./{0}/private/backups/{0}bk".format(site)
	
	doc.previous_path = change_directory(backup_path) # to move to the backup folder
	
	execute(">{}.sql".format(site)) # to create an empty file
	execute("git init") # to initialize the git repository

	change_directory(doc.previous_path)

def get_public_key(doc):
	import getpass
   	username = getpass.getuser()
	path2id_rsa = "/home/{}/.ssh/id_rsa.pub".format(username)

	pk_file = open(path2id_rsa)
	public_key = pk_file.readline()

	doc.id_rsa_public = public_key
	#doc.db_update()


def execute(cmd):
	return os.system(cmd)

def clean_dot(s):
	return s.replace("./", "")

def change_directory(path):
	old_path = os.getcwd()
	os.chdir(path)

	return old_path



