from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    env = os.environ.get("FLASK_ENV","development")
    db_url = os.environ.get("DATABASE_URL","sqlite:///test.db")
    return f"<h1> Hello from flask <br> Environemnt: {env} <br> DB: {db_url}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)