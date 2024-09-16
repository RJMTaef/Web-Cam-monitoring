import smtplib
import mimetypes
from email.message import EmailMessage

PASSWORD = "Secret_Password"
SENDER = "nicoirons77@gmail.com"
RECEIVER = "nicoirons77@gmail.com"


def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New Customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    # Read the image content
    with open(image_path, "rb") as file:
        content = file.read()

    # Use mimetypes to guess the file type
    mime_type, _ = mimetypes.guess_type(image_path)
    maintype, subtype = mime_type.split('/')

    email_message.add_attachment(content, maintype=maintype, subtype=subtype)

    # Set up SMTP and send the email
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send_email function ended")
