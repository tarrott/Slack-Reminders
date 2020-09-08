# Slack-Reminders

1. Rename `sample.reminders.txt` to `reminders.txt`
2. Format
3. Build Docker Image `docker build -t slack-reminders:latest`
4. Run with `docker run -d -e TIMEZONE="TIMEZONE" -e SLACK_WEBHOOK="URL" --name slack-reminders slack-reminders:latest`