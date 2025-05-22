from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.forms import ContactForm
from app.models import Project
from app.utils import send_email, save_message_to_db
from app import db

from datetime import datetime
from flask import Blueprint, render_template



main = Blueprint('main', __name__)

@main.context_processor
def inject_now():
    return {'now': datetime.now()}

@main.route('/')
def home():
    projects = Project.query.order_by(Project.created_at.desc()).limit(3).all()
    return render_template('index.html', projects=projects)

@main.route('/projects')
def projects():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template('projects.html', projects=projects)

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        try:
            # Save to database
            save_message_to_db(form)
            
            # Send email notification
            email_subject = f"New message from {form.name.data}"
            email_body = f"""
            From: {form.name.data} <{form.email.data}>
            Message:
            {form.message.data}
            """
            send_email(
                subject=email_subject,
                recipients=['your-email@example.com'],
                text_body=email_body
            )
            
            flash('Your message has been sent! I will get back to you soon.', 'success')
            return redirect(url_for('main.home'))
        except Exception as e:
            flash('Something went wrong. Please try again later.', 'danger')
    
    return render_template('contact.html', form=form)