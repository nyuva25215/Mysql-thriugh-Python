from mysql.connector import errorcode as er
import mysql.connector as cr
import getpass

def db_con():
    while True:
        # turning varible to global variable
        global Host, User, Password, Database, con

        # take input from user
        Host = input("Enter host name: ").strip() or "localhost"
        User = input("Enter user name: ").strip() or "root"
        Password = getpass.getpass("Enter Password: ")
        Database = input("Enter database name: ").strip() or "exam"
        try:
            # Attempt to connect to the database
            con = cr.connect(
                host = Host,
                user = User,
                password = Password,
                database = Database
            )

            print(f"Connected to database '{Database}' successfully!")
            return Database, con
            # return con
            # Success! Return the connection object and exit loop

        except cr.Error as e:
            # Handle Erors 
            print("/n" + "="*40)
            if e.errno == er.ER_ACCESS_DENIED_ERROR:
                print("Invalid Username or Password")
            elif e.errno == er.ER_BAD_DB_ERROR:
                print(f"Database '{Database}' does not exist")
            else:
                print("An error occurred:", e)

            print("="*40)

            # asking for second looop
            retry = input("Try again? (y/n): ").strip().lower()
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
     

