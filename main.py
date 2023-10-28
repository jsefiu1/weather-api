from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html") 

@app.route("/api/v1/<station>/<data>  ")
def about(station, date):
    return render_template("home.html") 


if __name__ == "__name__":
    app.run(debug=True)