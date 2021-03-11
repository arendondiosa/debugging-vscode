from flask import Flask, render_template, redirect, url_for, request, jsonify


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("login.html", title="Some title")


@app.route("/success/<name>")
def success(name):
    return render_template("message.html", username=name)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("success", name=user))
    else:
        user = request.args.get("nm")
        return redirect(url_for("success", name=user))


@app.route("/test")
def test():
    return jsonify({"hello": "world"})


@app.route("/test/<some_param>")
def test_with_param(some_param):
    return jsonify({"hello": some_param})


if __name__ == "__main__":
    app.run()
