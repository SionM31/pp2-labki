import psycopg2
from config import *

def select_part_phone_number():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM phonebook;")
        for x in cursor.fetchall():
          t = str(x[2])
          if '8747' in t:
              print(x)
def select_part_name(): 
    with connection.cursor() as cursor:
        cursor.callproc('get_parts_phonebook')
        for x in cursor.fetchall():
            print(x)

def insert_new_users(): #Stored procedure
    with connection.cursor() as cursor:
      id = int(input())
      user_name = input()
      phone_number = int(input())
      cursor.execute('CALL add_new_part(%s,%s,%s)', (id,user_name, phone_number))
      print("[INFO] User inserted succesfully")

def delete_by_user_name():
    with connection.cursor() as cursor:
      user_name = input()
      cursor.execute('CALL delete_by_user(%s)', (user_name,))
      '''CREATE OR REPLACE PROCEDURE delete_by_user(new_user_name varchar)
         AS $$
         BEGIN
	       DELETE FROM phonebook WHERE phonebook.user_name = new_user_name;
	
         END;
         $$
         LANGUAGE PLPGSQL;'''
def delete_by_phone_number():
    with connection.cursor() as cursor:
        phone = int(input())
        cursor.execute('CALL delete_by_phone(%s)', (phone,))
        '''CREATE OR REPLACE PROCEDURE delete_by_phone(d_phone BIGINT)
           AS $$
           BEGIN
              DELETE FROM phonebook WHERE phonebook.phone_number = d_phone;
           END;
           $$
           LANGUAGE PLPGSQL;'''
   

def insert_many_users():
    with connection.cursor() as cursor:
      users = [
        (7, "John", 1234567890),
        (8, "Alice", 9876543210),
        (9, "Bob", 5555555555)
     ]
      for x in users:
        cursor.execute('CALL add_many_parts(%s,%s,%s)',x)
      print("[INFO] User inserted succesfully")




try:
    connection = psycopg2.connect(password = password,host= host, user = user,database = db_name)
    connection.autocommit = True
    #select_part_phone_number()
    #select_part_name()
    #insert_new_users()
    #insert_many_users()
    #delete_by_user_name()
    delete_by_phone_number()
except Exception as ex:
    print("[INFO] Something was wrong", ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")


#Code of stored procedure
'''CREATE OR REPLACE PROCEDURE add_new_part(
	new_id bigint,
	new_user_name varchar,
	new_phone_number bigint
	
) 
AS $$
BEGIN
	IF EXISTS(SELECT 1 FROM phonebook WHERE user_name = new_user_name)
	 THEN
		UPDATE phonebook SET phone_number = new_phone_number WHERE user_name = new_user_name;
	
	ELSE
		INSERT INTO phonebook(id,user_name,phone_number) 
		VALUES(new_id,new_user_name,new_phone_number); 
	END IF;
	
END;
$$
LANGUAGE PLPGSQL;
'''
#Code of function
'''CREATE OR REPLACE FUNCTION get_parts_phonebook()  RETURNS TABLE(id BIGINT,user_name VARCHAR,phone_number BIGINT) AS
$$
BEGIN RETURN QUERY
 SELECT phonebook.id,phonebook.user_name,phonebook.phone_number
 FROM phonebook WHERE phonebook.user_name LIKE '%ak%';
END;
$$
LANGUAGE plpgsql;
'''

