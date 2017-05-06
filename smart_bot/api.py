import frappe

ZIP_FILE = "gzip {0}.sql"

def zip_file(filename):
	zip_backup = ZIP_FILE.format(filename)
	execute(zip_backup)

def execute(cmd):
	return smart_bot.boot.execute(cmd)

def change_directory(path):
	return smart_bot.boot.change_directory(path)

def validate_URL(string):
	if not isinstance(string, unicode):
		frappe.throw("Method was expecting a String!")

	regex = get_regex()

	if not regex.match(string):
		frappe.throw("Invalid URL")

	return True

def get_regex():
	import re # regular expresion library

	regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
	return regex




