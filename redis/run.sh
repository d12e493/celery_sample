#!/bin/bash

docker run -v ~/celery_sample/redis/data:/data \
-p 6379:6379 \
--name redis-service \
-d redis redis-server \
--appendonly yes