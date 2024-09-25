import os

from MyProject.settings import BASE_DIR

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / os.getenv("TEST_DB_NAME", default="db.sqlite3")
    }
}

class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(selfself, item):
        return "notmigrations"

MIGRATION_MODULES = DisableMigrations()
TEST_ENV=True

