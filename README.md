## Get Notifications from Stock Market Changes through crontab.

### Example Crontab (M-F 3:30 PM)
30 15 * * 1-5 python <repo location>/monitor_stocks.py

### INFO.py
These store the custom constants of the program.

Make sure you change the RECIPIENT constant to your email address.

## Note:
Test by running monitor_stocks.py first before adding to your crontab.
