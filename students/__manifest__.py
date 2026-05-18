{
	'name':'Students',
	'summary': 'Track leads and close opportunities',
	'version' : '1.2',
	'depends': ['mail'],
    'data':[
		# 'data/ir_cron.xml',
		'security/ir.model.access.csv', 
        
		'views/student_property_view.xml',
		'views/res_users_view.xml',
		# 'views/student_menus.xml'
	],
    'application' : True

}
