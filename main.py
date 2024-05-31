import smtplib
import datetime as dt
from random import choice
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get email credentials & recipient email from environment variables
MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASS = os.environ["MY_PASS"]
RECIPIENT_EMAIL = os.environ["RECIPIENT_EMAIL"]

# Get the current day of the week and week number
now = dt.datetime.now()
weekday = now.weekday()
week_no = now.isocalendar()[1]


def get_quote():
    """
    Function to get a random quote from the quotes.txt file.
    Returns a random quote as a string.
    """
    with open("quotes.txt") as file:
        quotes = file.readlines()
    return choice(quotes)


def send_email(quote):
    """
        Function to send an email with the provided quote.
        Takes a quote as an argument.
    """
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECIPIENT_EMAIL,
            msg=f"Subject: Week {week_no} Motivational Quote\n\n{quote}"
        )


if __name__ == '__main__':
    # If the current day is Monday, send an email with a motivational quote
    if weekday == 0:
        send_email(get_quote())
