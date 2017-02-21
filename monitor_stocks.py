"""Script to monitor portfolio of stocks for big changes."""
import os
import urllib
import cPickle
import subprocess
from INFO import * # Import constants used by this file.

def run_cmd(cmd, dryrun=False):
    if not dryrun:
        subprocess.call(cmd, shell=True)

# NOTE: Do not use _stock_data as this is overwritten by
# get_current_quote_finance.
def get_current_quote_google_finance(query):
    """Gets the current quote of a stock from google finance using an url."""
    url = "https://www.google.com/finance/info?q=" + query
    stock = urllib.urlopen(url)
    stock_exec = "_stock_data = "
    for line in stock.readlines():
        if ":" in line or "{" in line or "}" in line:
            stock_exec += line
    exec(stock_exec)
    return _stock_data

def monitor_stock(
        name, stock_query, stock_threshold_spacing, last_threshold_default):
    """send an email if there has been a big change in a stock's valuation."""
    stock_data = get_current_quote_google_finance(stock_query)
    stock_current = float(stock_data["l_fix"])
    stock_file_name = LAST_THRESHOLD_FILE_TEMPLATE.format(name)
    stock_file_path = os.path.join(FILES_FOLDER, stock_file_name)
    if not os.path.isfile(stock_file_path):
        with open(stock_file_path, 'w') as stock_file:
            pickler = cPickle.Pickler(stock_file, cPickle.HIGHEST_PROTOCOL)
            pickler.dump(last_threshold_default)

    with open(stock_file_path, 'r') as stock_file:
        unpickler = cPickle.Unpickler(stock_file)
        stock_last_threshold = unpickler.load()
    if (stock_current <= stock_last_threshold - stock_threshold_spacing or
            stock_current >= stock_last_threshold + stock_threshold_spacing):
        # Update last threshold variable.
        step_changes = int(
            (stock_current - stock_last_threshold) / stock_threshold_spacing)
        stock_new_threshold = (
            stock_last_threshold + step_changes * stock_threshold_spacing)
        with open(stock_file_path, 'w') as stock_file:
            pickler = cPickle.Pickler(stock_file, cPickle.HIGHEST_PROTOCOL)
            pickler.dump(stock_new_threshold)
        with open(EMAIL_PATH, 'w') as email_file:
            lines = list()
            lines.append("Subject: {}: {}, last threshold: {}\n".format(
                name, stock_current, stock_last_threshold))
            lines.append("stock monitor daemon on {}\n".format(MACHINE_NAME))
            email_file.writelines(lines)
        cmd = "{} -s {} < {}".format(SSMTP_PATH, RECIPIENT, EMAIL_PATH)
        print cmd
        run_cmd(cmd)

if __name__ == "__main__":
    if not os.path.isdir(FILES_FOLDER):
        os.mkdir(FILES_FOLDER)
    for stock_name, stock_info in STOCKS.iteritems():
        monitor_stock(stock_name, *stock_info)
