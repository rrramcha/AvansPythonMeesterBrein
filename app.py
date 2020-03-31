from flask import Flask, render_template

from Controllers.MainController import GameController

app = Flask(__name__)

gameController = GameController()

@app.route('/')
def hello_world():
    return gameController.game_start()


if __name__ == '__main__':
    app.run(debug=True)

