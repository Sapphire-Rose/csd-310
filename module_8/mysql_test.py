"""
    Title: mysql_test.py
    Author: Rebecca Robinson
    Date: 02.03.23
    Description: Test Program for Joining Player and Team Tables
"""

# importing
import mysql.connector
from mysql.connector import errorcode

""" database config object """
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
    
    # connection status
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    # if error code

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()
