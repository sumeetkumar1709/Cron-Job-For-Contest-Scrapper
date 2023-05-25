import smtplib
import ssl
from email.message import EmailMessage
import os
from dotenv import load_dotenv
import requests
from flask import Flask
from flask import request

app = Flask(__name__)

load_dotenv() # Loading the environment variables

@app.route('/__space/v0/actions', methods=['POST'])
def actions():
  data = request.get_json()
  event = data['event']
  if event['id'] == 'scrape':
    master()



def master():
    base_url = os.getenv('BASE_URL')

    # codechef requests
    res = None
    x=0
    while res!=200 and x<200:
        res = requests.post((base_url+'/codechef'))
        x+=1
        res = res.status_code
    print(f" Codechef done after {x} tries")

    # atcoder requests
    res = None
    x=0
    while res!=200 and x<200:
        res = requests.post((base_url+'/atcoder'))
        x+=1
        res = res.status_code
    print(f" Atcoder done after {x} tries")


    # leetcode requests
    res = None
    x=0
    while res!=200 and x<200:
        res = requests.post((base_url+'/leetcode'))
        x+=1
        res = res.status_code
    print(f" Leetcode done after {x} tries")


    email_sender = 'ninja.coolprojects@gmail.com'
    email_password = os.getenv('GMAIL_PASS')
    email_receiver = ['sumeetkumar1709@gmail.com','khchoudhary08@gmail.com']

    subject = 'POST REQUESTS SUCCESSFUL'
    body = """
    HEY! JUST WANTED TO LET YOU KNOW THAT THE DB IS UPDATED 😁 !!!!!!!!
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

