from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def firstRoute():
    #return "My first GET request"
    return render_template("index.html") #message="My first GET request")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
