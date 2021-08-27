from flask import Flask, render_template
import requests


app = Flask(__name__)

response = requests.get('https://api.npoint.io/60003338a24f652dcbbe').json()

@app.route("/")
def home():
    post1 = response[0]
    post2 = response[1]
    post3 = response[2]
    return render_template('index.html', fpost=post1, spost=post2, tpost=post3)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/post/<news_num>")
def post(news_num):
    news = response[int(news_num) - 1]
    return render_template('post.html', news_num=news)


@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
