import os

from apscheduler.schedulers.blocking import BlockingScheduler
from tzlocal import get_localzone
import requests

webhook = os.environ["SLACK_WEBHOOK"]
timezone = os.environ["TIMEZONE"]

def parse_reminder(lines):
    reminders = []

    for line in lines:
        if line[-1:] == '\n':
            line = line[:-1]
        line = line.split()
        reminder = {
            "message": line[0],
            "weekday": line[1],
            "hour": line[2],
            "minute": line[3]
        }
        reminders.append(reminder)

    return reminders


def send_reminder(message):
    data = f'{{"text": "{message}"}}'

    try:
        response = requests.post(webhook, data)
    except Exception as e:
        print(f"{str(response.status_code)}: {response.text}")
        print(e)


def schedule_reminders(reminders):
    scheduler = BlockingScheduler(timezone=timezone)

    for id,reminder in enumerate(reminders, 1):
        scheduler.add_job(
            send_reminder,
            args=[reminder["message"]],
            trigger='cron',
            day_of_week=reminder["weekday"],
            hour=reminder["hour"],
            minute=reminder["minute"],
            id=str(id)
        )
    scheduler.start()


if __name__ == "__main__":
    local_timezone = get_localzone()
    print(f"The local timezone is {local_timezone}")

    with open('reminders.txt', 'r') as f:
        lines = f.readlines()
    reminders = parse_reminder(lines)
    schedule_reminders(reminders)
