from flask import Flask, render_template,g
import sqlite3

PATH = "db/jobs.sqlite"

app = Flask(__name__)


def open_connection():
    connection = getattr(g, '_connection', None)
    if connection is None:
        connection = sqlite3.connect(PATH)
        g._connection = connection
    sqlite3.Row = connection.row_factory
    return connection


def execute_sql(sql, values=(), commit=False, single=False):
    connection = open_connection()
    cursor = connection.execute(sql, values)

    if commit:
        results = connection.commit()
    elif single:
        results = cursor.fetchone()
    elif not single:
        results = cursor.fetchall()

    cursor.close()
    return results


@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()


@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')


def url_for():
    return '../static/css/bulma.min.css'
