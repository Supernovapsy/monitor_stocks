import os

# Recipient email address.
RECIPIENT = "tony.wenbo.li@gmail.com"

# Program uses SSMTP to send out the email. Install it and put its path here.
SSMTP_PATH = "/usr/sbin/ssmtp"

# Name of the machine (will be the signature of the email message.
MACHINE_NAME = "wentron2"

# FORMAT - "stock name": (query on google finance, threshold spacing, last threshold # default)
# last threshold # default is used if file containing the lsat threshold does not already exist.
STOCKS = {
    "TSX": ("INDEXTSI%3AOSPTX&ei=qpqHV-G-NMSajAHZlYN4", 1000, 13100),
    "XBB": ("TSE%3AXBB&ei=bLeHV6zOJ8GM2AbQoL3gAg", 1, 31.1)
}

# Template for file to store each of the stocks' last threshold values.
LAST_THRESHOLD_FILE_TEMPLATE = "_monitor_stock_last_threshold_{}.txt"

# Folder to store the various files produced by the program.
FILES_FOLDER = "monitor_stocks_files"
EMAIL_FILE = "email.txt"
EMAIL_PATH = os.path.join(FILES_FOLDER, EMAIL_FILE)
