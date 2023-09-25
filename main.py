from flask import Flask
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
  return 'Hello from Flask! Tks'


app.run(host='0.0.0.0', port=81)
