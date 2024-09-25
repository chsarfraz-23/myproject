import os

import pytest


os.environ["DJANGO_SETTINGS_MODULE"] = "MyProject.tests_settings"

@pytest.fixture(autouse=True)
def enable_db_for_all_tests(db):
    pass
