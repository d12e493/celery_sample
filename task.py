import logging
import time
import json
import random

from app import app
from collections import namedtuple

TASK_NAME = 'send_email_task_name'
QUEUE_NAME = 'email_task_queue_name'

app.conf.update({
    'task_routes': {
        TASK_NAME: {'queue': QUEUE_NAME},
    },
})


class TaskContext:
    def __init__(self,
                 name: str,
                 email: str):
        self.name = name
        self.email = email


@app.task(queue=QUEUE_NAME, task=TASK_NAME)
def execute(context_json):

    context = json.loads(context_json, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

    logging.info(f'execute email : {context.email}')

    # FIXME test random & multiple worker
    time.sleep(random.randrange(100, 1000)/1000)

    # FIXME test error handler
    # raise KeyError('test')

    return 'SUCCESS'


