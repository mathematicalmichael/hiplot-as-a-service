#FROM python:3.9-alpine
#RUN apk update && apk add gcc libc-dev g++ libffi-dev make musl-dev python3-dev
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY templates/ ./templates
COPY static/ ./static
COPY experiment.py ./
COPY render.py ./
COPY fetchers.py ./

COPY plot.py /app/
COPY start_hiplot_server.sh /app/

EXPOSE 8000
CMD ["./start_hiplot_server.sh"]

