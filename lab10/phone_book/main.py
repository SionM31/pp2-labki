import psycopg2
from config import *

def insert_console():
     with connection.cursor() as cursor:
        id = int(input())
        user = input()
        phone = int(input())
        cursor.execute("INSERT INTO phonebook (id, User_name, Phone_number) VALUES {};".format((id,user,phone)))
        print("[INFO] Inserted successfully!")

def select():
     with connection.cursor() as cursor:
        cursor.execute(
            "SELECT id, user_name, phone_number FROM phonebook;"     #Here I can select rows by user_name or phone_number or id
        )
        for x in cursor.fetchall():
            print(x)

def create():
     with connection.cursor() as cursor:
        cursor.execute(
            "CREATE TABLE PhoneBook (id BIGINT NOT NULL PRIMARY KEY,User_name VARCHAR(64) NOT NULL, Phone_number BIGINT NOT NULL);"
        )
        print("[INFO] Table created!")

def insert_csv():
     with connection.cursor() as cursor:
        file = open("lab10/phone_book/table.csv",'r')
        cursor.copy_from(file, "phonebook",sep = ',')
        print("[INFO] Inserted successfully!")

def update():
     with connection.cursor() as cursor:
         cursor.execute(
            "UPDATE phonebook SET phone_number = 87087193494 WHERE user_name = 'Nurs';")
         print("[INFO] Updated successfully!")
         
def delete():
    with connection.cursor() as cursor:
         cursor.execute(
            "DELETE FROM phonebook WHERE user_name = 'Nurs';")
         print("[INFO] Deleted successfully!")



try:
    #connect to exist database
    connection = psycopg2.connect(
        host = "localhost",
        user = "postgres",
        password = "20051337",
        database = "postgres"
    )
    connection.autocommit = True
    #the cursor for perfoming database operations


    #Choose request

    #insert_console()
    #insert_csv()
    #select()
    #create()
    # update()
    #delete()


except Exception as _ex:
    print("[INFO] Eror while working with PostgreSQL",_ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
