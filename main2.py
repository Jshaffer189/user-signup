from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


#only renders and displays signup template
@app.route("/")
def signup():
    return render_template('signup.html')

#valid submission and welcome page
@app.route('/valid-welcome')
def valid_welcome():
    return render_template('welcome.html')

#errors testing
def empty_input(z):
    if z:
        return True
    else:
        return False

def length_input(z):
    if len(z) > 2 and len(z) < 21:
        return True
    else:
        return False

def at_mail(z):
    if z.count('@') == 1:
        return True
    else: 
        return False

def dot_mail(z):
    if z.count('.') == 1:
        return True
    else:
        return False

def space_error(z):
    if z.count(' ') == 0:
        return True
    else:
        return False

def password_match(z, b):
    if z == b:
        return True
    else:
        return False

#--------------------------------------

#if/elif/else testing        
#verification of signup
@app.route("/", methods=['POST'])
def validate_signup():
    username = request.form['username']
    password = request.form['password']
    retype = request.form['retype']
    mail = request.form['mail']

    #empty error messages
    username_error = ''
    password_error = ''
    retype_error = ''
    mail_error = ''

    #error messages
    space_error_msg = 'please do not include any spaces'
    emptyinput_error_msg = 'please input'
    length_error_msg = 'please keep characters between 3 and 20'
    period_error_msg = 'please use only one (.) symbol for email'
    atmail_error_msg = 'please use only one (@) symbol for email'
    password_match_error_msg = 'passwords must match'

   
    #username testing
    if not empty_input(username):
        username_error = emptyinput_error_msg
        password = ''
        retype = ''
    elif not length_input(username):
        username_error = length_error_msg
        username = username
        password = ''
        retype = ''
    elif not space_error(username):
        username_error = space_error_msg
        username = username
        password = ''
        retype = ''
       

    #password testing    
    if not password_match(password, retype):
        password_error = password_match_error_msg
        retype_error = password_match_error_msg
        password = ''
        retype = ''
    elif not empty_input(password):
        password_error = emptyinput_error_msg
        retype_error = emptyinput_error_msg
        password = ''
        retype = ''
    elif not length_input(password):
        password_error = length_error_msg
        retype_error = length_error_msg
        password = ''
        retype = ''

    #email testing
    if empty_input(mail):
        if not length_input(mail):
            mail = mail
            mail_error = length_error_msg
            password = ''
            retype = ''
        elif not at_mail(mail):
            mail = mail 
            mail_error = atmail_error_msg        
            password = ''
            retype = ''
        elif not dot_mail(mail):
            mail = mail
            mail_error = period_error_msg
            password = ''
            retype = ''
        elif not space_error(mail):
            mail = mail
            mail_error = space_error_msg
            password = ''
            retype = ''
    
    if not username_error and not password_error and not retype_error and not mail_error:
        username=username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup.html', username_error = username_error, password_error = password_error, retype_error = retype_error, mail_error = mail_error, username=username, password=password, retype=retype, mail=mail)

@app.route('/welcome')
def login_success():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()