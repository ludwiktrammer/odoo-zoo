# -*- coding: utf-8 -*-
{
    'name': "Zoo Animals Management",
    'summary': "Manage animals in a ZOO.",
    'author': "Ludwik Trammer",
    'website': "https://github.com/ludwiktrammer/odoo-zoo",
    'category': "Specific Industry Applications",
    'version': "1.0",
    'application': True,
    'post_load': 'print_on_load',
    'depends': [
        'base',
    ],
    'data': [
        'views/animal.xml',
        'menu.xml',
    ],
}
