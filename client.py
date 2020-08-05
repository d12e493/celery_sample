from argparse import ArgumentParser

import random
import names
import json
import time

from task import execute, TaskContext

parser = ArgumentParser()
parser.add_argument("-c", "--count", help="how many task send", dest="count", default=1)

client_name = names.get_first_name()

args = parser.parse_args()
print(f'client will send task by {args.count} times')

for i in range(int(args.count)):
    random_name = f'{client_name}____{names.get_full_name()}___{i}____'
    task_context = TaskContext(
        name=random_name,
        email=random_name.replace(' ', '_').lower()+'@gmail.com'
    )
    execute.delay(json.dumps(task_context.__dict__))
    print(f'task_context random_name : {random_name}')
    # FIXME test random consumer
    time.sleep(random.randrange(100, 1000) / 1000)

print(f'client execute finish')
