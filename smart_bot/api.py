import frappe

from time import sleep

ZIP_FILE = "gzip {0}.sql"

def zip_file(filename):
	zip_backup = ZIP_FILE.format(filename)
	execute(zip_backup)


def execute(cmd):
	return smart_bot.boot.execute(cmd)

def change_directory(path):
	return smart_bot.boot.change_directory(path)

