from flask import Flask
import random

app = Flask(__name__)

num = random.randint(0, 9)


@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<iframe src="https://giphy.com/embed/13RcbHeXlLNysE" width="480" height="304" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/i-love-lucy-lucille-ball-13RcbHeXlLNysE">via GIPHY</a></p>'


@app.route("/<int:guess>")
def hl_game(guess):
    if int(guess) > num:
        return f'<h1>Too High, Try again {str(num)}</h1>' \
            '<iframe src="https://giphy.com/embed/2cei8MJiL2OWga5XoC" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/johnlegend-john-legend-so-high-2cei8MJiL2OWga5XoC">via GIPHY</a></p>'
    elif int(guess) < num:
        return f'<h1>Too Low, Try again {str(num)}</h1>' \
            '<iframe src="https://giphy.com/embed/xjUdSMOFVQ5o1X47sM" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/starterpack-meme-atthellolab-xjUdSMOFVQ5o1X47sM">via GIPHY</a></p>'
    else:
        return '<h1>Just Right</h1>' \
            '<iframe src="https://giphy.com/embed/Sw7EmPJy8Ttulcv8v7" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/OneDayAtATime-poptv-one-day-at-a-time-odaat-Sw7EmPJy8Ttulcv8v7">via GIPHY</a></p>'


if __name__ == "__main__":
    app.run(debug=True)
