from function import *


while True:
    query = input("enter your query(e to exit): ").strip().lower()

    if query == "e":
        print("Shuting down....")
        exit()

    elif query == "connect":
        global Host, User, Password, Database
        Host = input("Enter host name: ").strip() or "localhost"
        User = input("Enter user name: ").strip() or "root"
        Password = getpass.getpass("Enter Password: ") or "say my name 38"
        Database = input("Enter database name: ") or "exam"
        
        db_con()

    elif query == "show table":
        Show_table()

    elif query == "help":
        print("Available commands:")
        print("- connect: Connect to a MySQL database")
        print("- show table: Show tables in the connected database")
        print("- help: Show this help message")
        print("- e: Exit the program")



# import mysql.connector as cr
# from mysql.connector import errorcode as er
# import getpass

# Host = input("Enter host name: ").strip() or "localhost"
# User = input("Enter user name: ").strip() or "root"
# Password = getpass.getpass("Enter password: ").strip() 
# Database = input("Enter database name: ").strip()

# con = cr.connect(host=Host,
#                  user=User,
#                  password=Password, 
#                  database=Database)



# if con.is_connected():
#     print("connected to database", Database, "successfully")
# else:
#     print("Not connected to database", Database, "successfully")



