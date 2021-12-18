FROM python:3.8.6-buster

COPY velibapi /velibapi
COPY velib /velib
COPY requirements.txt /requirements.txt
COPY data /data

RUN pip install -r requirements.txt

CMD uvicorn velibapi.fast:app --host 0.0.0.0 --port $PORT