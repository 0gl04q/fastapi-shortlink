from settings.config import settings
from celery import Celery
from celery.schedules import crontab
import sys

sys.path.append(settings.BASE_DIR)

app = Celery('worker', broker=settings.REDIS_URL, backend=settings.REDIS_URL)
app.conf.enable_utc = False
app.autodiscover_tasks(['links'])
app.conf.beat_schedule = {
    'clear_links': {
        'task': 'links.tasks.delete_links',
        'schedule': crontab(minute='0', hour='*')
    },
}
