''' root web page '''
import os
import smtplib, ssl
from flask import Flask, render_template, send_from_directory, url_for, request, redirect
from logger_settings import api_logger


app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    ''' serve favicon '''
    return send_from_directory(os.path.join(app.root_path, 'static/img/'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route("/submit_contact_form", methods=["POST","GET"])
def submit_contact_form():
    ''' using form data send email to notify communications of request'''
    if request.method == 'POST':
        data = request.form.to_dict()
        res = send_contact_email(data['name'], data['email'], data['message'])    
        if res == 'success':
            return redirect('/thankyou.html')
        else:
            return render_template('/error.html'), 500
    
def send_contact_email(contact_name, contact_email, contact_message):
    ''' send the email from the contact to the comunication person'''
    try:
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "gd.7.communications@gmail.com"
        password = '*****************'
        message = 'Subject: Web Site Contact Form Submitted\n'
        message += contact_name + ' has sent a contact request, please respond appropriately/n'
        message += contact_message + '/n'
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, contact_email, message)
            return 'success'
    except smtplib.SMTPAuthenticationError as send_exception:
        api_logger.error('Error at %s', 'Error sending contact email to ' + contact_email, exc_info=send_exception)        
    except Exception as ex_general:  
        api_logger.error('Error at %s', 'Error sending contact email to ' + contact_email, exc_info=ex_general)  
