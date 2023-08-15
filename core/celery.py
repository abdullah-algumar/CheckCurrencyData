import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core',broker = os.environ.get('REDIS_HOST'))

app.config_from_object('django.conf:settings')
task_apps = ['web.tasks']

CELERYBEAT_SCHEDULE = {
    'run-every-30-seconds': {
        'task': 'web.tasks.fetch_currency_data',
        'schedule': 30.0,
    },
}
app.conf.timezone = 'Europe/Istanbul'

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS + task_apps)