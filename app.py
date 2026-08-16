<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    print("🎂 SURYA Birthday Website Starting...")
    app.run(host="127.0.0.1", port=5000, debug=True)
>>>>>>> 08e097ad8ab38ed5c8589eee2c6d966d339a2b83
