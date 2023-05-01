from time import ctime
from flask import Flask, render_template

from Utils import get_bitcoin_price

app = Flask(__name__)


@app.route('/news/')
def news_page():
    return "This is News Page"

@app.route('/')
def home_page():
    ct = ctime()
    return render_template('Home_page.html', ctm=ct)

@app.route('/time')
def time_page():
    return render_template("Time_page.html", my_current_time=ctime())

if __name__ == '__main__':
    app.run()
