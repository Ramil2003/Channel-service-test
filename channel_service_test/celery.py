import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channel_service_test.settings')
app = Celery('channel_service')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()