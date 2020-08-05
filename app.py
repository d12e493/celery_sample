import os
from celery import Celery

print(f'''
CELERY_NAME: {os.getenv('CELERY_NAME')}
CELERY_BROKER_URL: {os.getenv('CELERY_BROKER_URL')}
CELERY_RESULT_BACKEND_URL: {os.getenv('CELERY_RESULT_BACKEND_URL')}
''')

app = Celery(os.getenv('CELERY_NAME'))

app.conf.update(
    broker_url=os.getenv('CELERY_BROKER_URL'),
    result_backend=os.getenv('CELERY_RESULT_BACKEND_URL')
)
