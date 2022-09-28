# -*- coding: utf-8 -*-

{
    'name': "Mis_ubicaciones",
    'summary': """
        software para registrar ubicaciones de 
        tiendas existentes.
      """,
    'author': 'Ernesto porras',
    'category': 'General',
    'depends': ['mail'],
    'data': [
        'views/mis_ubicaciones_view.xml',
        'views/menu_view.xml',
        'security/mis_ubicaciones_security.xml',
        'security/ir.model.access.csv',
    ],

}






