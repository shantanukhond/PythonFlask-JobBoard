from flask import Flask, redirect, url_for, render_template, request, flash

#__name__ = 'Flask App'

app = Flask(__name__)


@app.route('/')
def jobs():
    return render_template('index.html')
