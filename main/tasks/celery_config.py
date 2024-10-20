from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'generate-inventory-report-every-hour': {
        'task': 'main.tasks.inventory_report.generate_inventory_report',
        'schedule': crontab(minute=0, hour='*'),  # This runs every hour
    },
}
