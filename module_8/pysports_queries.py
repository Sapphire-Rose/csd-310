"""
    Title: mysql_test.py
    Author: Rebecca Robinson
    Date: 02.03.23
    Description: Test Program for Joining Player and Team Tables
"""

# importing
import mysql.connector
from mysql.connector import errorcode

# database configuration
config = {
    "user": "pysports_user",
    "password": "M662Lhmi2U!-BK&B",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    # try catch for errors 

    db = mysql.connector.connect(**config) # connect to the pysports database 
    
    cursor = db.cursor()

    # pull from team table 
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    # get the results  
    teams = cursor.fetchall()

    print("\n  -- DISPLAYING TEAM RECORDS --")
    
    # print team results 
    for team in teams: 
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

    # pull from player table 
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    # get the results  
    players = cursor.fetchall()

    print ("\n  -- DISPLAYING PLAYER RECORDS --")

    # print player results
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    # if error code

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
# close MySQL

    db.close()
