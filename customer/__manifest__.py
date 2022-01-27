{
    'name': "Customer Care",
    'summary': """Manage customer care information""",
    'description': "",
    'author': "",
    'website': "https://odoo.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/customer.xml',
        'report/report.xml',
        'report/template_report_customer.xml'
        ],
    'demo': [],
    'installable': True,
    'application': True,
}
