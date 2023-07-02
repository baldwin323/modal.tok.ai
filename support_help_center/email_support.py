```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from user_data_schema import User
from support_request_data_schema import SupportRequest

def provideEmailSupport(user_id, support_request_id):
    user = User.objects.get(id=user_id)
    support_request = SupportRequest.objects.get(id=support_request_id)

    # Email server setup
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to the email server
    server.login("your-email@gmail.com", "your-password")

    # Email content
    msg = MIMEMultipart()
    msg['From'] = "your-email@gmail.com"
    msg['To'] = user.email
    msg['Subject'] = "Support Request #" + str(support_request.id)
    body = "Dear " + user.name + ",\n\n" + support_request.response + "\n\nBest,\nYour Support Team"
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    text = msg.as_string()
    server.sendmail("your-email@gmail.com", user.email, text)

    # Close the server
    server.quit()
```