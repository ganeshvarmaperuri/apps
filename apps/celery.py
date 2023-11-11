from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

from apps import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apps.settings')

app = Celery('apps')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()