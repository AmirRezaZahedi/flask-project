from flask import Flask, redirect, url_for, render_template, request, flash, session
import sqlite3
import secrets
import smtplib
import ssl
from datetime import datetime
from email.message import EmailMessage
import time
import os


app = Flask(__name__)
# Generate a random secret key
app.secret_key = secrets.token_hex(16)
def send_email(email, password):
    current_date_and_time = datetime.now()
    email_sender = '*'  # Enter provider server's email
    email_password = '*'  # Enter provider's password
    email_receiver = str(email)  # Enter admin email.
    subject = 'Forget password... ' 
    body = "current date and time : \n" + str(current_date_and_time)
    body = "\nDon't send this email to someone⚠"
    body = body + f"\npassword is : {password}"
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # SQLite3

        connection = sqlite3.connect("user_data.db")
        cursor = connection.cursor()

        email = request.form['email']
        password = request.form['password']

        query = "SELECT email, password FROM users WHERE email=? AND password=?"
        cursor.execute(query, (email, password))
        result = cursor.fetchall()


        if len(result) == 0:
            return redirect(url_for('login'))
        else:
            # Save user info in session
            session['email'] = email
            session['password'] = password
            return redirect(url_for('unique'))

    # Check if the user is already logged in
    if 'email' in session and 'password' in session:
        return redirect(url_for('unique'))

    return render_template("index.html")

@app.route('/unique')
def unique():
    email = session.get('email')
    password = session.get('password')

    connection = sqlite3.connect("user_data.db")
    query = "SELECT name FROM users WHERE email = ? AND password = ?"

    
    cursor = connection.cursor()
    cursor.execute(query, (email, password))
    name = cursor.fetchone()
    cursor.close()
    connection.close()

    connection = sqlite3.connect("user_content.db")
    cursor = connection.cursor()
    cursor.execute("SELECT users.title, users.content, users.name FROM users")
    posts = cursor.fetchall()
    connection.close()

    # Check if the user is logged in
    logged_in = 'email' in session and 'password' in session
    logged_out = not logged_in
    return render_template('main.html', name=name, posts=posts, logged_in=not logged_in, logged_out=logged_out)


    
@app.route('/createPost')
def create_post():
    if 'email' in session and 'password' in session:
        return render_template('createPost.html')
    else:
        return redirect(url_for('index'))


@app.route('/submit_post', methods=['POST'])
def submit_post():
    if 'email' in session and 'password' in session:
        title = request.form['title']
        content = request.form['content']
        connection = sqlite3.connect("user_data.db")
        cursor = connection.cursor()
        print(session['email'])
        cursor.execute("SELECT name FROM users WHERE email=? AND password=?", (session['email'],
                                                                                        session['password']))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        nameTmp = result[0]
        connection = sqlite3.connect('User_Content.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (name, email, title, content) VALUES (?, ?, ?, ?)",
                   (nameTmp, session['email'], title, content))
        connection.commit()
        return render_template('post_success.html', title=title)

    else:
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.clear()  
    return redirect(url_for('index'))


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['pwd']

    query = "SELECT email FROM users where email = '" + email + "'"
    connection = sqlite3.connect("user_data.db")
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    if len(result) == 0:
        cursor.execute("INSERT INTO users (name, password, email, phone) VALUES (?, ?, ?, ?)",
                   (username, password, email, phone))
        connection.commit()
    else:
        session['error'] = 'Email already exists.'
        return redirect(url_for('index'))

    connection.close()

    return redirect(url_for('index'))

@app.route('/search')
def search():
    search_query = request.args.get('search', '')  
    connection = sqlite3.connect("user_content.db")
    cursor = connection.cursor()
    cursor.execute("SELECT title, content, name FROM users WHERE title LIKE ?", ('%' + search_query + '%',))
    search_results = cursor.fetchall()
    connection.close()
    return render_template('search.html', search_query=search_query, results=search_results)


@app.route('/user_count')
def user_count():
    connection = sqlite3.connect("user_data.db")
    cursor = connection.cursor()

    
    cursor.execute("SELECT COUNT(*) FROM users")
    result = cursor.fetchone()
    connection.close()
    return {'userCount': result[0]}

@app.route('/forgetpassword', methods=['GET', 'POST'])
def forget_password():
    if request.method == 'POST':
        email = request.form['gmail']

        connection = sqlite3.connect("user_data.db")
        cursor = connection.cursor()

        query = "SELECT password FROM users WHERE email=?"
        cursor.execute(query, (email,))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        if result:
            password = result[0]
            
            flash("An email with your password has been sent to your email address.")
            send_email(email, password)
            time.sleep(5)
        else:
            flash("The entered email was not found.")
            time.sleep(5)

        return redirect(url_for('index'))

    return render_template("forgetpassword.html")



if __name__ == '__main__':
    app.run(debug=True)
