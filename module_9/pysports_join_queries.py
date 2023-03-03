# Title: pysports_join_queries.py
# Author: Rebecca Robinson
# Date: 02.06.23
# Description: Joining player team tables.


# Import statements
import mysql.connector
from mysql.connector import errorcode

# Configuration
config = {
    "user": "pysports_user",
     #insert root password
    "password": "",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# Try and catch to manage errors
try:

    db = mysql.connector.connect(**config)  

    cursor = db.cursor()

# Inner join  
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

# Get results  
    players = cursor.fetchall()

    print("\n  Showing Player Records")
    
# Print player data 
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press a key to continue... ")

except mysql.connector.Error as err:
# Manage errors

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  That username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  That database does not exist")

    else:
        print(err)

finally:

    db.close()
