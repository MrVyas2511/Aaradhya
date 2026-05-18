{
	'name':'Cheques',
	'summary': 'Track leads and close opportunities',
	'version' : '1.2',
	'depends': ['mail', 'students'],
    'data':[
		'security/ir.model.access.csv', 
		'views/student_property_view.xml',
		'views/cheque_property_view.xml',
	],
    'application' : True

}
