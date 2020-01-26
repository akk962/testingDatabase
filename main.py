# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
import flask
from flask import Flask, request, render_template, url_for
#from dictDatabase import *
from test import *

current = "Not Signed In"
# addUser(User("Anna", "Kolodziejcyk"))

'''

users = {}
def addUser(userId, first, last, status, target, assassin):
    users[userId] = [first, last, status, target, assassin]

def getTarget(userId):
    return users[userId][3]

def getName(userId):
    return users[userId][0] + " " + users[userId][1]

def getStatus(userId):
    return users[userId][2]

def getAssassin(userId):
    return users[userId][4]

addUser(2321, "Anna", "Kolodziejcyk", "Active", "Lauren", "Jonathan")
print(users)
print(getTarget(2321))
print(getName(2321))
print(getStatus(2321))
print(getAssassin(2321))



print(users.get("10"))
'''

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    return flask.redirect(url_for("view_games"))


@app.route("/games")
def view_games():
    return render_template("games.html", games=viewGames(), user=current)


@app.route('/games', methods=['POST'])
def add_game():
    text = request.form['text']
    createGame(text)
    # return processed_text
    return flask.redirect(url_for("view_games"))


@app.route("/game/<gameId>")
def view_game(gameId):
    # get players of specified gameId
    #players = {"Julian": 25, "Bob": 26, "Dan": 47, gameId: 3}
    gameName = getGameName(gameId)[0]
    return render_template("game.html", players=viewPlayers(gameId), user=current, name=gameName)


@app.route('/game/<gameId>', methods=['POST'])
def add_to_game(gameId):
    global current
    joinGame(current, gameId)
    # return processed_text
    gameName = getGameName(gameId)[0]
    return render_template("game.html", players=viewPlayers(gameId), user=current, name=gameName)

@app.route("/newplayer")
def view_new_player():
    return render_template("newPlayer.html", user=current)


@app.route('/newplayer', methods=['POST'])
def add_player():
    name = request.form['name']
    global current
    current = str(addPlayer(name))
    return flask.redirect(url_for("view_games"))


@app.route("/signin")
def sign_in():
    return render_template("signin.html", user=current)


@app.route('/signin', methods=['POST'])
def sign_in_token():
    id = request.form['id']
    # TODO check if user is valid

    global current
    current = id

    # return processed_text
    return flask.redirect(url_for("view_games"))


@app.route('/user')
def userData():
    global current

    if(current == "Not Signed In"):
        return flask.redirect(url_for("sign_in"))

    user =  current

    name = getPlayerName(user)[0]
    target = getPlayerName(getPlayerTarget(user)[0])[0]

    # return processed_text
    return render_template("user.html", target=target, name=name, user=current)

@app.route('/user', methods=['POST'])
def terminate_user():
    global current
    terminate(current)

    # return processed_text
    return flask.redirect(url_for("view_games"))


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    port = os.getenv("PORT", 8080)
    app.run(host='0.0.0.0', port=port, debug=True)
# [END gae_python37_app]

'''
Views
All games
    list games
    
Specific game
    list of users
    status of users

Specific User
    name
    target
    status
    game
'''
