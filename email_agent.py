import os
from typing import Dict

#Sendgrid
import sendgrid
from sendgrid.helpers.mail import Email, Mail, Content, To
from agents import Agent, function_tool

#SMTP
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# @function_tool
# def send_email(subject: str, html_body: str) -> Dict[str, str]:
#     """ Send an email with the given subject and HTML body """
#     sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
#     from_email = Email("ed@edwarddonner.com") # put your verified sender here
#     to_email = To("ed.donner@gmail.com") # put your recipient here
#     content = Content("text/html", html_body)
#     mail = Mail(from_email, to_email, subject, content).get()
#     response = sg.client.mail.send.post(request_body=mail)
#     print("Email response", response.status_code)
#     return {"status": "success"}

@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """
    Send an HTML email using SMTP with the given subject and HTML content.
    """
    smtp_server = "smtp.gmail.com"   # or your SMTP server
    smtp_port = 587
    sender_email = "dsdd0511@gmail.com"
    receiver_email = "dsharma7_be22@thapar.edu"
    sender_password = os.getenv("EMAIL_APP_PASSWORD")  # Use App Password for Gmail (or real SMTP password)

    # Create MIME message
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Add HTML body
    html_part = MIMEText(html_body, "html")
    message.attach(html_part)

    try:
        # Connect to SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

INSTRUCTIONS = """You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the 
report converted into clean, well presented HTML with an appropriate subject line."""

email_agent = Agent(
    name="Email agent",
    instructions=INSTRUCTIONS,
    tools=[send_email],
    model="gpt-4o-mini",
)