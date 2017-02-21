## Get Notifications from Stock Market Changes through crontab

## Setup

### Example Crontab (M-F 3:30 PM)
30 15 * * 1-5 python {repository location}/monitor_stocks.py

### INFO.py
These store the custom constants of the program.

Create one by using the INFO_TEMPLTE.py provided.

You have to AT LEAST change the RECIPIENT constant to your email address.

### Before you think you're finished:
Test by running monitor_stocks.py first before adding to your crontab. It
should send an email to your email address and output the command used. Use
this command to continuously test until you have it working.
