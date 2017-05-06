import frappe

def do_task():

	print "==========================================================="
	print " *** Running sync for Backup Meta"
	print "==========================================================="

	doc = frappe.get_single("Backup Meta")

	print " *** if not doc.stop: {}".format(doc.stop)

	if not int(doc.stop):
		doc.sync()
		print " *** doc.sync()"
	else:
		print " *** sync is off"


	print "==========================================================="

