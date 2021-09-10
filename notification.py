import smtplib
import datetime

MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "lazytestmail@gmail.com"
MY_PASSWORD = "lazytest21"


class NotificationManager:

    def send_email(self, name, email, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs='lazyboyprogrammer@gmail.com',
                msg=f"Subject: Gig From Website {datetime.datetime.today()} {name} \n"
                    f"Name: {name} \n"
                    f"email: {email}\n"
                    f"Message: {message}"
            )

