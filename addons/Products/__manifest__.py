{
    # Tên module
    'name': 'Products Management',
    'version': '1.0',

    # Loại module
    'category': 'Products Management',

    'sequence': 5,

    'summary': 'Module products',
    'description': '',

    'depends': ["website","product"],

    'installable': True,
    'auto_install': False,
    'application': True,

    'data': [
        'views/custom/products.xml',
    ],
    'assets': {
        'web.assets_frontend':[
            'Products/static/src/css/custom_product.css',
        ],
        'point_of_sale._assets_pos': [
            'Products/static/src/**/*'
        ],

    },
    'license': 'LGPL-3',
}
