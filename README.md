# Slack-Reminders

1. Rename `sample.reminders.txt` to `reminders.txt`
2. Each line in `reminders.txt` is a separate reminder. The format is space-delimited `Reminder-message Weekday(0-6 or sun-sat Hour(0-23) Minute(0-59)`. Use `*` to send reminder at every interval.
3. Build Docker Image `docker build -t slack-reminders:latest`
4. Run with `docker run -d -e TIMEZONE="TIMEZONE" -e SLACK_WEBHOOK="URL" --name slack-reminders slack-reminders:latest`