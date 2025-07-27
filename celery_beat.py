from celery.schedules import crontab

from tasks import celery_app


celery_app.conf.beat_schedule = {
    'update-currency-daily': {
        'task': 'tasks.update_currency_task',
        'schedule': crontab(hour=9, minute=0),  # Every day at 9:00 AM
    },
}