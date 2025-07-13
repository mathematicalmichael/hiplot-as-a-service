#!/bin/sh
gunicorn -b :8000 plot:app --timeout 90 -w 4
