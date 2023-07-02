```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Importing the Support Request Data Schema
from shared_dependencies import SupportRequestDataSchema

def emailSupport(support_request):
    # Extracting details from the support request
    support_data = SupportRequestDataSchema.load(support_request)

    # Email settings
    sender_address = 'admin@ourapp.com'
    sender_pass = 'AdminPassword'
    receiver_address = support_data.user_email

    # Setup MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Support Request Response'   # Subject line

    # The body and the attachments for the mail
    mail_content = f"Hello {support_data.user_name},\n\nWe have received your support request. Our team will get back to you shortly.\n\nBest,\nOurApp Support Team"
    message.attach(MIMEText(mail_content, 'plain'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # Use gmail with port
    session.starttls()  # Enable security

    # Login with mail_id and password
    session.login(sender_address, sender_pass)

    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    print(f'Mail Sent to {receiver_address} regarding their support request.')
```