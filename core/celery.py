import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core',broker = os.environ.get('REDIS_HOST','redis://localhost:7055/0'))

app.config_from_object('django.conf:settings', namespace="CELERY")
task_apps = ['web.tasks']

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS + task_apps)