import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import traceback

class EmailSender:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, receiver_email, subject, body):
        try:
            # Create message container
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject

            # Attach body to the message
            msg.attach(MIMEText(body, 'plain'))

            # Connect to SMTP server and send email
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, receiver_email, msg.as_string())

            print(f"Email sent successfully to {receiver_email}")
        except Exception as e:
            print(f"Failed to send email to {receiver_email}: {e}")
            traceback.print_exc()

# Example usage:
# sender = EmailSender("smtp.example.com", 465, "your_email@example.com", "your_password")
# sender.send_email("receiver@example.com", "Test Subject", "This is a test email.")
