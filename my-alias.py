#!/usr/bin/env python3
# Welcome

import os
import sys
import mysql.connector



db = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "password", #password
	database = "myalias",
	auth_plugin = "mysql_native_password"
)
mycursor = db.cursor()
mycursor.execute("USE myalias")

welcome = "Welcome!\n"

rows, columns = os.popen('stty size', 'r').read().split()
center = int(float(columns)/2)
print("hello world".center(os.get_terminal_size().columns))
tab = " " * (center - 1)

os.system('ls')
os.system('./welcome-my-alias.sh')
print(
	(tab + "\tWelcome!\n") + 
	(tab + "1. List aliases\n") +
	(tab + "2. View alias\n") + 
	(tab + "3. Add alias\n") + 
	(tab + "4. Modify alias\n") + 
	(tab + "5. Remove alias\n") + 
	(tab + "6. Exit")
)
choice = input("Choose: ")


def listaliases():
   os.system("figlet -c -t -f standard 'LIST ALIASES' |lolcat")
   mycursor.execute("SELECT userID, username, systemname FROM Users INNER JOIN Systems ON Users.systemID = Systems.systemID")
   print(tab + "X------X--------------------X--------------------X")
   print(tab + "|  XX  |      Username      |       System       |")
   print(tab + "X------X--------------------X--------------------X")
   whitespaceUsername = ""
   whitespaceSystem = ""
   for user in mycursor:
      spacesUsername = 20 - int(len(user[1])) - 1
      spacesSystem = 20 - int(len(str(user[2]))) - 1
      for i in range(spacesUsername):
         whitespaceUsername += "‎‎‏‏‎ ‎"
      for i in range(spacesSystem):
         whitespaceSystem += "‎‎‏‏ ‎"
      print(tab + "|  0" + str(user[0]) + "  | " + user[1] + whitespaceUsername + "| " + str(user[2]) + whitespaceSystem + "|")
      whitespaceUsername = ""
      whitespaceSystem = ""
   print(tab + "X------X--------------------X--------------------X")


def viewalias():
   os.system("figlet -c -t -f standard 'VIEW ALIAS' |lolcat")

def createalias():
   os.system("figlet -c -t -f standard 'CREATE ALIAS' |lolcat")
   firstname = input("FIRST NAME: ")
   lastname = input("LAST NAME: ")
   username = input("USERNAME: ")
   systemname = input("SYSTEM: ")
   userID = 0
   systemID = 0
   mycursor.execute("SELECT * FROM Users")
   for user in mycursor:
      userID = user[2] + 1
   mycursor.execute("SELECT * FROM Systems")
   for system in mycursor:
      systemID = system[0] + 1
   mycursor.execute("INSERT INTO Systems(systemID, systemname) VALUES(%s, %s)", (systemID, systemname))
   mycursor.execute("INSERT INTO Users(userID, username, systemID) VALUES(%s, %s, %s)", (userID, username, systemID))
   db.commit()

   print("\n\n\n\n\n\n\n\n\n")

def modifyalias():
   os.system("figlet -c -t -f standard 'MODIFY ALIAS' |lolcat")

def removealias():
   os.system("figlet -c -t -f standard 'REMOVE ALIAS' |lolcat")
   username = input("USERNAME: ")
   mycursor.execute("SELECT * FROM Users")
   for user in mycursor:
      if user[1] == username:
         print(user)
         print(user[1])
         mycursor.execute("DELETE FROM Users WHERE username = 'B'") 
         #db.commit()

def exit():
   os.system("")



if (choice == "1"):
   listaliases()
elif (choice == "2"):
   viewalias()
elif (choice == "3"):
   createalias()
elif (choice == "4"):
   modifyalias()
elif (choice == "5"):
   removealias()
else:
   exit()
