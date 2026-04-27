from mysql.connector import errorcode as er
import mysql.connector as cr
import getpass

def db_con(Host ,User, Password, Database):
    # turning varible to global variable
    global con
    # Trying to COnnect to database
    try:
        con = cr.connect(
            host=Host,
            user=User,
            password=Password, 
            database=Database
            )
        
        if con.is_connected():
            print("connected to database", Database, "successfully")
            print
        else:
            print("Not connected to database", Database, "successfully")
    except cr as e:
        if e.rrrno == er.ER_ACCESS_DENIED_ERROR:
            print("Invalid username or password")
        elif e.errno == er.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(f"An error occurred: {e}")

        print("="*40)

        retry = input("Do you want to retry? (y/n): ").strip().lower()
        if retry != "y":
            print("Exiting...")
            exit()        
                



def Show_table():
    db = input("Enter database name: ") or "student"

    # turning varible to global variable
    global cursor
    
    cursor = con.cursor()
    query = "select * from {}".format(db)
    cursor.execute(query)
    data = cursor.fetchall()
    # print(data)
    for i in data:
        print(i)
     

