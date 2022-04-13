from flask import render_template, request, redirect, session, url_for
from flask_app.models.email import Email
from flask_app import app

@app.route("/")
def main():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    if not Email.validate_email(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    # ... do other things
    Email.add_email(request.form)
    return redirect('/results')

@app.route('/results')
def results():
    emails=Email.get_email()
    return render_template('results.html', all_emails=emails)
