FROM python:3.8-slim-buster

RUN mkdir /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt

COPY reminders.txt /app
COPY reminders.py /app

CMD python reminders.py