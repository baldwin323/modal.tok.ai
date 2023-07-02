```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from user_data_schema import User
from subscription_data_schema import Subscription
from content_data_schema import Content

class NotificationSender:
    def __init__(self, server, port, email, password):
        self.server = server
        self.port = port
        self.email = email
        self.password = password

    def send_email(self, to_email, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP(self.server, self.port)
        server.starttls()
        server.login(self.email, self.password)
        text = msg.as_string()
        server.sendmail(self.email, to_email, text)
        server.quit()

    def send_notification(self, user_id, message_name):
        user = User.get(user_id)
        if message_name == 'transaction-complete':
            subject = 'Transaction Complete'
            message = 'Your transaction has been completed successfully.'
        elif message_name == 'subscription-update':
            subscription = Subscription.get(user.subscription_id)
            subject = 'Subscription Update'
            message = f'Your subscription has been updated to {subscription.subscription_type}.'
        elif message_name == 'content-update':
            content = Content.get(user.content_id)
            subject = 'Content Update'
            message = f'New content "{content.content_type}" has been uploaded.'
        elif message_name == 'new-notification':
            subject = 'New Notification'
            message = 'You have a new notification.'
        elif message_name == 'admin-alert':
            subject = 'Admin Alert'
            message = 'An admin alert has been issued.'
        else:
            return

        self.send_email(user.email, subject, message)
```