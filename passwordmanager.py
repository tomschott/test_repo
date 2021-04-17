import sqlite3

conn = sqlite3.connect('password.db')

c = conn.cursor()

import random

def create_password(length):
    pw = str()
    characters = "abcdefghijklmnopqrstuvwxyz123456789"
    for i in range(length):
        pw = pw + random.choice(characters)
    return(pw)

def insert_service(service):
    with conn:
        c.execute("INSERT INTO passwords VALUES (:service, :password)",{'service': service, 'password': "x"})

def update_password(service, password):
    with conn:
        c.execute("""UPDATE passwords SET password = :password
                     WHERE service = :service""",
                     {'service': service, 'password': password})

def get_password(service):
    c.execute("SELECT * FROM passwords WHERE service = :service", {'service': service})
    return c.fetchall()

def remove_password(service):
    with conn:
        c.execute("DELETE from passwords WHERE service = :service",
                  {'service': service})

admin_password = "1234"

connect = input("What is your admin password? ")

while connect != admin_password:
    connect = input("What is your admin password? ")
    if connect == "q":
        break

if connect == admin_password:
    try:
        c.execute("""CREATE TABLE passwords (
             service text,
             password text
             )""")
        print("Your safe has been created")
    except:
        print("you already have a safe")

    print("what would you like to do? ")
    print("*"*15)
    print("commands:")
    print("q = quit programm")
    print("gp = get password")
    print("sp = save password")
    print("*"*15)
    command = input(":")


    if command == "sp":
        new_password = str()
        new_service = str(input("what is the name of the service: "))
        old_service_wrong = get_password(new_service)
        try:
            old_service_wrong = old_service_wrong[0]
            old_service = old_service_wrong[0]
            if new_service == old_service:
                print("You already saved this service")
        except:
            insert_service(new_service)
            print("Would you like to create a password(cp),or save your own(op)?")
            choice = str(input(":"))
            if choice == "op":
                own_password = str(input("Enter your own password: "))
                update_password(new_service, own_password)
                print("your password has been saved")

            if choice == "cp":
                    length = int(input("length of the password: "))
                    created_password = create_password(length)
                    update_password(new_service, created_password)
                    print("your password has been saved")


    if command == "gp":
        service = input("what is the name of the service: ")
        asked_password_wrong = get_password(service)
        try:
            asked_password = asked_password_wrong[0]
            print("Your password is:", asked_password[1])
        except:
            print("You haven't saved this service")

    if command == "q":
        print("end")
