import json
import os
import smtplib
from email.message import EmailMessage

from src import settings


def notification(message):
    try:
        message = json.loads(message)
        print(f"Decoded message: {message}")
        mp3_fid = message["mp3_fid"]
        sender = settings.email_address
        sender_pass = settings.email_password
        receiver = message["email"]

        msg = EmailMessage()
        msg.set_content(f"mp3 file: {mp3_fid} is ready for download")
        msg["Subject"] = "MP3 DOWNLOAD"
        msg["From"] = sender
        msg["To"] = receiver

        session = smtplib.SMTP("smtp.gmail.com", 587)
        session.starttls()
        session.login(sender, sender_pass)
        session.send_message(msg, sender, receiver)
        session.quit()
        print("email sent")

    except Exception as err:
        print(f"Error while sending email: {err}")
        return err
    return None
