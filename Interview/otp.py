import random as rd
import smtplib
from email.message import EmailMessage

otp =  ""

for i in range(6):
    num = rd.randint(0,9)
    otp += str(num)


SMTP_HOST = "smtp.mailtrap.io"
SMTP_PORT = 587
SMTP_USERNAME = "OTP Service <no-reply@test.com>"
SMTP_PASSWORD = "d1777c8129325682bcaf38b69652ebb4"

server = smtplib.SMTP(SMTP_HOST,SMTP_PORT)
server.starttls()

msg = EmailMessage()
msg["subject"] = "OTP Test"
msg["from"] = "test@mailtrap.io"
msg["To"] = "patadiyavardan@gmail.com"
msg.set_content(f"Your OTP is {otp}")
server.login(SMTP_USERNAME,SMTP_PASSWORD)

server.send_message(msg)

server.quit()
userOTP = input("Enter a OTP : ")

if (userOTP == otp):
    print("Your OTP is Right")
else:
    print("wronge")
