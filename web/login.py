from flask import Flask, request, session, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/login_attempt', methods=['POST'])
def login_attempt():
    if request.method == 'POST':
        userID = request.form['id']
        userPWD = request.form['pwd']
