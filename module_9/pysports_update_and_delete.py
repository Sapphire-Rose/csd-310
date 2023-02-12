# Title: pysports_update_and_delete.py
# Author: Rebecca Robinson
# Date: 02.06.23
# Description: Insert, update, and delete records from pysports database.

# Import statements
import mysql.connector
from mysql.connector import errorcode


# Configuration
config = {
    "user": "pysports_user",
    "password": "M662Lhmi2U!-BK&B",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}


def show_players(cursor, title):

# Perform inner join 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

# Get the results 
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    
# Print player data
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

# Try and catch to manage errors
try:

# Database connector
    db = mysql.connector.connect(**config) 

# Get cursor 
    cursor = db.cursor()

# Insert player 
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")

# Player data 
    player_data = ("Ash", "Tyler", 1)

# Insert a new player record
    cursor.execute(add_player, player_data)

# Insert into database 
    db.commit()

# Show player table
    show_players(cursor, "*Displaying Players After Update*")

# Update the inserted record 
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Voq', last_name = 'Torchbearer' WHERE first_name = 'Ash'")

# Execute the update 
    cursor.execute(update_player)

# Show player table 
    show_players(cursor, "*Displaying Players After Update*")

# delete query 
    delete_player = ("DELETE FROM player WHERE first_name = 'Voq'")

    cursor.execute(delete_player)

# delete query 
    delete_player = ("DELETE FROM player WHERE first_name = 'Ash'")

    cursor.execute(delete_player)

# Show player table
    show_players(cursor, "*Displaying Players After Deletion*")

    input("\n\n  Press a key to continue... ")

except mysql.connector.Error as err:
 # Error management

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  That username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  That database does not exist")

    else:
        print(err)

finally:

    db.close()
