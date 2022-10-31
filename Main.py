from bs4 import BeautifulSoup
from email.message import EmailMessage
import requests
import ssl 
import smtplib
from email.mime.text import MIMEText
import time


# This returns a list of all the article titles
def scrape_headlines():
    url = 'https://www.nytimes.com'
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, "html.parser")
    listArticles = (soup.find_all('h3'))
    return listArticles


# one-time password = ylobrkmtneyfozsu
#sends an email to myself containing the headlines
def send_email(headlines):
    email_sender = 'duckduckmongoose1@gmail.com'
    email_password = 'ivbptljvsyzcahiv'
    email_receiver = 'imscrol@gmail.com'

    port = 1025
    msg = MIMEText('This is test mail')
    msg['Subject'] = 'Test Mail'
    msg['From'] = 'duckduckmongoose1@gmail.com'

    subject = 'Email Sent From Python'
    for i in headlines:
        body += i.get_text()

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp@gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

print('hello')
time.sleep(5)
print('hello')