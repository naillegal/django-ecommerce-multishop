# multishop/celery.py

import os
import dotenv
from celery import Celery



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "multishop.settings")
dotenv.load_dotenv()
app = Celery("multishop")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()