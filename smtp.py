import smtplib

# Set up the SMTP server
smtp_server = 'smtp.gmail.com'
port = 587
server = smtplib.SMTP(smtp_server, port)
server.starttls() 

# Go to the email sending gmail account, go to app passwords section, create creds for an app, use that password here
username = 'sanandrosingh@gmail.com'
password = 'ziff ssno vyju krmn'
server.login(username, password)

# Compose the email
from_address = 'sanandrosingh@gmail.com'
to_address = 'simranbanwait02@gmail.com'
subject = 'SMTP NIGGA...'
body = 'Mail Sent from an EC2 Jammy Ubuntu System'

# Send the email
server.sendmail(from_address, to_address, f'Subject: {subject}\n\n{body}')

# Close the server connection
server.quit()
