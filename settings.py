# -*- coding: utf-8 -*-

INSTALLED_ADDONS = [
    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    'aldryn-sso',
    # </INSTALLED_ADDONS>
]

import aldryn_addons.settings  # noqa
aldryn_addons.settings.load(locals())


# all django settings can be altered here

INSTALLED_APPS.extend([  # noqa
    # add your project specific apps here
])
