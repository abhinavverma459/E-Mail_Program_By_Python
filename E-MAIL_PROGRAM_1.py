import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = '------'     # USE E-MAIL ADDRESS TO SEND ADDRESS
receiver_email = '-----'    # USE E-MAIL ADDRESS TO RECIVER ADDRESS
password = 'neel ipmt hhtw undg'  # HERE YOU USE SMTP PASSWORD WHICH YOU ARE GENERATE
subject = 'Python Email Test'

# Create a message object
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Email content
body = 'This is a test email sent from Python.'
message.attach(MIMEText(body, 'plain'))

# SMTP server configuration (for Gmail)
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Create a secure SSL context
context = smtplib.SMTP(smtp_server, smtp_port)
context.starttls()

# Login to your email account
context.login(sender_email, password)

# Send the email
text = message.as_string()
context.sendmail(sender_email, receiver_email, text)

# Close the SMTP connection
context.quit()

print('Email sent successfully!')
