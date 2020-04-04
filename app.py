from flask import Flask, render_template, request

from Controllers.MainControllerClass import MainController

app = Flask(__name__)
app.config['SECRET_KEY'] = '8044110391c54ba91493bdaa564b0073'

mainController = MainController()


@app.route('/', methods=['GET', 'POST'])
def new_game():
    return mainController.new_game()


@app.route('/game', methods=['GET', 'POST'])
def game():
    numbers = request.forms[]
    return mainController.handle_answer()

@app.route('/newgame', methods=['GET', 'POST'])
def initgame():
    return render_template('newgame.jinja')

if __name__ == '__main__':
    app.run(debug=True)
