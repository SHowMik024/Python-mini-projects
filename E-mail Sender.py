import smtplib

sender = "md.golam.shahnewaz@g.bracu.ac.bd"
receiver = "showmikshahnewaz@gmail.com"
password = "mybruthur213"
subject = "just a test"
body = "just checking bruv"

message = f"""From: Big Dawg{sender}
To: Small Dawg{receiver}
subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Got In...")
    server.sendmail(sender, receiver, message)
    print("GOOD job It's done")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")
