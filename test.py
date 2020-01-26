import os
from random import randrange

import mysql.connector as mariadb
import time
mariadb_connection = mariadb.connect(user="TAMUHack2020!", password='TAMUHack2020!', database='AssassinApp2', port=3316)
cursor = mariadb_connection.cursor()

cursor.execute("SELECT * FROM player")

for v in cursor:
    print(v)

#create game
#GET INPUT FROM WEBSITE
def createGame(name):
    nameOfGame = "Game 2"
    sql = "INSERT INTO games( game_id, game_status, game_name ) VALUES (%s, %s, %s)"
    val = ( 4, "OPEN", name)
    cursor.execute(sql, val)
    mariadb_connection.commit()

def addPlayer(name):
    sql = "INSERT INTO player( player_name ) VALUES ('" + name + "')"
    #val = ("Laure")
    cursor.execute(sql)
    mariadb_connection.commit()
    return cursor.lastrowid


#Start game
#REMINDER TO UPDATE WITH GAMEID
def startGame():
    sql1 = "UPDATE games SET game_status = 'IN PROGRESS' WHERE game_id = '2'"
    cursor.execute(sql1)
    mariadb_connection.commit()


#join game
#TODO check if id is valid player
def joinGame(player_id, game_id):
    #chwck if a valid name
    sql2 = "INSERT INTO participant( player_id, game_id, assassin, target, player_status) VALUES (%s, %s, %s, %s, %s)"
    val2 = (player_id, game_id, randrange(1000), randrange(1000), "ACTIVE")
    cursor.execute(sql2, val2)
    mariadb_connection.commit()


#My target
#PASS USER ID
def getTarget():
    sql3 = "SELECT target FROM participant WHERE player_id= '2' "
    cursor.execute(sql3)
    myresult = cursor.fetchone()
    return myresult[0]


#target terminated
def terminateTarget():
    sql4 = "UPDATE participant SET player_status='PENDING' WHERE player_id =" + str(getTarget())
    cursor.execute(sql4)
    mariadb_connection.commit()


#confirm termination


#view players and status
#UPDATE GAMEID
def viewPlayers(game_id):
    sql5 = "SELECT player_id, player_status FROM participant WHERE game_id = '"+game_id+"'"
    cursor.execute(sql5)
    myresult2 = cursor.fetchall()
        #Todo change the ids into full names
    return myresult2

def viewGames():
    sql5 = "SELECT * FROM games"
    cursor.execute(sql5)
    myresult2 = cursor.fetchall()
    return myresult2


def getPlayerName(playerId):
    sql6 = "SELECT player_name FROM player WHERE player_id=" + str(playerId)
    cursor.execute(sql6)
    myresult3 = cursor.fetchone()
    return myresult3

def getGameName(gameId):
    sql5 = "SELECT game_name FROM games WHERE game_id='"+gameId+"'"
    cursor.execute(sql5)
    myresult2 = cursor.fetchone()
    return myresult2

#print(viewGames())

def assignTargets():
    for i in range(0, len(userIDs) - 1):
        users.get(userIDs[i]).setTarget(userIDs[i + 1])
    users.get(userIDs[len(userIDs) - 1]).setTarget(userIDs[0])


def assignAssassins():
    for i in range((len(userIDs) - 1), 0, -1):
        users.get(userIDs[i]).setAssassin(userIDs[i - 1])
    users.get(userIDs[0]).setAssassin(userIDs[len(userIDs) - 1])
    #select count(*) from participants where id=game id


def incrementArray(arr):
    outarr = []
    for i in range(len(arr)):
       outarr.append(arr[i-1]);
    return outarr




print(incrementArray([1, 2, 3, 4, 5]))
print(viewPlayers('1'))


def assign(game_id):
    sql4 = "UPDATE participant SET target=NULL,assassin=NULL WHERE game_id=" + str(game_id)
    cursor.execute(sql4)
    mariadb_connection.commit()

    arr = []
    for i in viewPlayers(str(game_id)):
        arr.append(i[0])
    print(arr)
    inc = incrementArray(arr)
    print(inc)
    for j in range(0, len(inc)):
        sql4 = "UPDATE participant SET target='" + str(inc[j]) + "' WHERE game_id='"+str(game_id)+"' AND player_id =" + str(arr[j])
        cursor.execute(sql4)

    for j in range(0, len(inc)):
        sql4 = "UPDATE participant SET assassin='" + str(arr[j]) + "' WHERE game_id='"+str(game_id)+"' AND player_id =" + str(inc[j])
        cursor.execute(sql4)

    mariadb_connection.commit()


assign(4)