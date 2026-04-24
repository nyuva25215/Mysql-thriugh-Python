from function import *


while True:
    query = input("enter your query(e to exit): ").strip().lower()

    if query == "e":
        print("Shuting down....")
        exit()

    elif query == "connect to databse" or query == "connect" or  query == "connect to the database":
        db_con()

    elif query == "show table" or query == "show tables":
        Show_table()



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



