#!/bin/sh
gunicorn -b :8081 plot:app --timeout 90 --worker-class gevent
