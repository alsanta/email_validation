from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.email import Email

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/create_email', methods = ['POST','GET'])
def create_email():
    if not Email.validate_email(request.form):
        return redirect('/')
    Email.create_email(request.form)

    return redirect ('/success')

@app.route('/success')
def success():

    email = Email.get_all_emails()

    return render_template('success.html', email = email)

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }

    Email.delete(data)

    return redirect('/success')