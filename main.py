from flask import Flask

app = Flask(__name__)


@app.route('/username')
def home():
    return "<h1>Good Morning</h1>" % username


if __name__ == "__main__":
    app.run()
