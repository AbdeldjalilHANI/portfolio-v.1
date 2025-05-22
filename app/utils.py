from app import mail
from flask_mail import Message
from flask import current_app

def send_email(subject, recipients, text_body, html_body=None):
    msg = Message(subject, recipients=recipients)
    msg.body = text_body
    if html_body:
        msg.html = html_body
    mail.send(msg)

def save_message_to_db(form):
    from app.models import Message
    from app import db
    
    message = Message(
        name=form.name.data,
        email=form.email.data,
        message=form.message.data
    )
    db.session.add(message)
    db.session.commit()
    return message