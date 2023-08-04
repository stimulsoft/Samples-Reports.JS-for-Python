from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/viewer")
def viewer():
    return render_template("viewer.html")

@app.route("/designer")
def designer():
    return render_template("designer.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)