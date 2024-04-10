from flask import Flask, request
from flask_ngrok import run_with_ngrok

import json


app = Flask(__name__)
run_with_ngrok(app)

gamemode = {
    "Формулы": {
    },
    "Экзамены": {
    }
}


def pick_mode(user_id: str, req: dict, res: dict):
    """ Выбрать роежим. Формулы или Экзамены """
    pass


def pick_lesson(user_id: str, req: dict, res: dict):
    """ Выбрать урок. Матан..."""


def pick_class(user_id: str, req: dict, res: dict):
    """ Выбрать класс. 9 11..."""


def end_game(user_id: str, req: dict, res: dict):
    """конец игры, мб перенос на главный экран выбора мода и огласить результаты"""


@app.route("\post", methods=["POST"])
def get_alice_requests():
    response = {
        "session": request.json["session"],
        "version": request.json["version"],
        "response": {
            "end_session": False,
        }
    }
    handle_dialog(request.json, response)
    return json.dumps(response)


def handle_dialog(req: dict, res: dict):
    user_id = req["session"]["user_id"]
    if req["session"]["new"]:
        res["response"]["text"] = "Привет, с помощью этого навыка вы сможете выучить формулы и определения, которые " \
                                  "вас интересуют, проверить знания за заданиях из банка Фипи и поиграть в " \
                                  "интересную  игру про формулы. Что из этого вам интересует?"
        session_state["user_id"] = {
            "state": 1
        }
        return
    states[session_state[user_id]["state"]](user_id, req, res)


states = {
    1: pick_mode,
    2: pick_lesson,
    3: pick_class,
    4: end_game
}

session_state = {}

if __name__ == "__main__":
    app.run()
