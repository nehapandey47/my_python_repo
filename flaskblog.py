from flask import Flask,render_template
from random import randrange
app = Flask(__name__)

response = [
    "If someone says you can do it. Do it twice and take pictures",
    "You are doing really good.",
    "Everything is possible if you don't make a choice",
    "Whatever happens life has to Go On",
    "Winter is Coming",
    "Stay hungry...stay foolish"
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',response=response[randrange(len(response))])

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form")
def form():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)