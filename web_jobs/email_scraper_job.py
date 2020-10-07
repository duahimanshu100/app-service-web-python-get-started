SITE_PACKAGE_PATH = "D:\\home\\site\\wwwroot\\env\\Lib\\site-packages"
CODE_PATH = "D:\\home\\site\\wwwroot"

def setup_django():
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
def email_scrapper():
    print("Inside email scrapper web job")
    setup_django()
    print("Setup Django complete")
    from emailscraper.utils.email_processors import email_processing
    print("Imported email processing")
    email_processing()
    print("Comple email processing")

email_scrapper()