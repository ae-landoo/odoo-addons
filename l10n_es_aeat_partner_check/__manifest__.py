# Copyright 2019 Acysos S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'AEAT - Comprobación de Calidad de datos identificativos',
    'author': 'Acysos S.L.',
    'website': 'https://www.acysos.com',
    'category': 'Accounting',
    'version': '12.0.0.1.0',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'base_vat',
        'l10n_es_aeat_soap'
    ],
    'data': [
        'views/res_partner_view.xml',
        'views/res_company_view.xml',
        'views/res_config_settings_view.xml'
    ],
    'images': ['static/description/banner.jpg'],
    'installable': True,
}
