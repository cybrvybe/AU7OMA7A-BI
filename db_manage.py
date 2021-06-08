
from django.db import connection
import os
from django.db.migrations.migration import Migration
from django.db.migrations.recorder import MigrationRecorder

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_dir.settings')

application = get_wsgi_application()
def drop_create_db():
    with connection.cursor() as cursor:
        cursor.execute("DROP DATABASE personal_business;")
        cursor.execute("CREATE DATABASE business;")

def squash_migrations():
    apps = [
        "analytics",
        "budgeting",
        "career",
        "content",
        "forecasting",
        "general_business",
        "marketing",
        "processes",
        "product",
        "project",
        "reporting",
        "sales",
        "time_manage"
    ]
    migration_objects = MigrationRecorder.Migration.objects.all()
    for migration_obj in migration_objects:

        for app in apps:
            os.system("python manage.py squashmigrations " + app + " " + migration_obj.name)
            print("AU70MA7A-BI: Unapplying all migrations...")

def master():
    drop_create_db()
    squash_migrations()

master()