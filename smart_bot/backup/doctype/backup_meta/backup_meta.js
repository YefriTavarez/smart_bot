// Copyright (c) 2016, Yefri Tavarez and contributors
// For license information, please see license.txt

frappe.ui.form.on('Backup Meta', {
	refresh: function(frm) {

	},
	github_url: function(frm) {
		$c('runserverobj', { "method": "add_remote", "docs": frm.doc }, function(respose){
			frm.save()
		})
	},
	password: function(frm){
		frm.save()
	},
	sync_period: function(frm){
		frm.save()
	},
	start_sync: function(frm) {
		$c('runserverobj', {"method": "start_syncing", "docs": frm.doc}, function(respose){
			frm.reload_doc()

			setTimeout(function() {
				frappe.hide_msgprint()
			}, 1500)
		})
	},
	stop_sync: function(frm) {
		$c('runserverobj', {"method": "stop_syncing", "docs": frm.doc}, function(respose){
			frm.reload_doc()

			setTimeout(function() {
				frappe.hide_msgprint()
			}, 1500)
		})
	}
});
