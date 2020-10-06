SITE_PACKAGE_PATH = "D:\\home\\site\\wwwroot\\env\\Lib\\site-packages"
CODE_PATH = "D:\\home\\site\\wwwroot"
def email_scrapper():
    import sys
    import os
    sys.path.append(SITE_PACKAGE_PATH)
    sys.path.append(CODE_PATH)
    import django
    from django.core.management import call_command

    os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE",
            "cis.settings"
        )

    django.setup()