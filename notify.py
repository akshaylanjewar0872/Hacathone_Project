# notify.py

# ---------- EMAIL SETTINGS ----------
# EMAIL_SENDER = "akshaylanjewar0872@gmail.com"  # replace with your Gmail ID
# EMAIL_PASSWORD = "zmzj ycee vduu djio"  # App password from Google

# # ---------- TWILIO SETTINGS ----------
# TWILIO_SID = "ACb848fa45971b400be7e2b21ba16732ac"
# TWILIO_AUTH = "098d31d323d689cb2456b949112267e8"
# TWILIO_NUMBER = "12175983819" #your Twilio number


# notify.py
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client

# ---------- EMAIL SETTINGS ----------
EMAIL_SENDER = "akshaylanjewar0872@gmail.com"  # replace with your Gmail ID
EMAIL_PASSWORD = "zmzj ycee vduu djio"  # App password from Google

# ---------- TWILIO SETTINGS ----------
TWILIO_SID = "ACb848fa45971b400be7e2b21ba16732ac"
TWILIO_AUTH = "098d31d323d689cb2456b949112267e8"
TWILIO_NUMBER = "12175983819" #your Twilio number

def send_email(receiver_email, subject, body):
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = EMAIL_SENDER
        msg["To"] = receiver_email

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"✅ Email sent to {receiver_email}")
        return True
    except Exception as e:
        print("❌ Email sending failed:", e)
        return False

def send_sms(phone_number, message):
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH)
        client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=f"+91{phone_number}"  # For India
        )
        print(f"✅ SMS sent to {phone_number}")
        return True
    except Exception as e:
        print("❌ SMS sending failed:", e)
        return False
