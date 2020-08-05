## Initial Setting
### Redis
```
sh redis/run.sh
```

### Python
```
pipenv install
pipenv shell
```
## Run Client
```
python client.py -c ${count}
```
## Run Worker
```
celery -A task worker -Q ${queue_name} -l ${log_level} -c ${concurrency} -n ${worker_name} --prefetch-multiplier=1

#sample
celery -A task worker -l info -Q email_task_queue_name -c 1 -n worker-1 --prefetch-multiplier=1
```
