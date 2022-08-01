from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello")
def hello_name():
    d = {"first_name": "Ali Haider", "last_name": "Rizvi"}
    return d

if __name__ == "__main__":
    app.run()
