# -*- coding: utf-8 -*-

# Copyright Notice:
#
# ---------------------------------------------------
# Copyright (c) 2023 WE2 Creative Agency. All rights reserved.
#
# Author: WE2 Creative Agency
# Email: info@we2design.nl
#
# This file, including its source code and accompanying comments, is protected by copyright 
# law. Unauthorized copying, distribution, or modification of this file, in whole or in part, 
# is strictly prohibited without the express written permission of WE2 Creative Agency.
# ---------------------------------------------------
{
    'name': "Konings",
    'summary': "WE2 Theme",
    'description': "Website thema voor Konings.",
    'category': 'Theme',
    'version': '16.0.0',
    'license': 'OPL-1',
    'author': "WE2 Creative Agency",
    'website': "https://www.we2design.nl",
    'depends': ['website'],
    'assets': {
        'web.assets_frontend': [
            'we2_konings/static/src/scss/style.scss',
            'we2_konings/static/src/scss/fonts.scss'
        ],
        'web._assets_primary_variables': [
            'we2_konings/static/src/scss/primary_variables.scss'
        ],
        'web._assets_frontend_helpers': [
            ('prepend', 'we2_konings/static/src/scss/bootstrap_overridden.scss'),
        ],
    },
    # 'data': [
    #     'views/website_templates.xml'
    # ],
    'images': [
        'static/description/we2_logo.png'
    ]
}
