import asyncio

from celery import Celery

from parsing import fetch_currency_rates

celery_app = Celery(
    'currency_tasks',
    broker='redis://localhost:6379/0',  # Redis as the message broker
)

@celery_app.task
def update_currency_task():
    asyncio.run(fetch_currency_rates())