FROM python:3.9-alpine
RUN apk update && apk add gcc libc-dev g++ libffi-dev make musl-dev python3-dev
RUN pip3 install gunicorn gevent
RUN pip3 install jinja2 bs4
WORKDIR /app
COPY ./templates/ /app/templates/
COPY ./static/ /app/static/
COPY experiment.py /app/
COPY render.py /app/
COPY fetchers.py /app/

COPY plot.py /app/
COPY start_hiplot_server.sh /app/

EXPOSE 8081
CMD ./start_hiplot_server.sh

