# the point of this program is to kind organize and store the passwords
# store all of the passwords along with the username of the account they are associated with any text file, but we are not going to store the passwords in plaintext
# we are going to encrypt the passwords

from cryptography.fernet import Fernet

master_pwd = input("what is the master password? ")

def view():
    '''
    loop through the lines of the file and just print them.
    '''
    with open('passwords.txt', 'r') as f: 
        for line in f.readlines():
            data = line.rstrip()  # I want to seperate name and pass
            user , passw = data.split("|")
            print("User:" , user , "," , "Password:" , passw)

# rstrip : will strip off the carriage return from our line..  use this method to not print new empty line // becuse we use \n in add method   
# "noor|jojo|yes|5".split("|") = ["noor","jojo","yes","5"]

def add():
    '''
    create a new file, if the file storing our password is doesn't already exist and add the password into it
    we need to do is get the username and then the password and add it into the file.
    '''

    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f: 
        f.write(name + "|" + pwd + "\n")


# when use with will automatically close the file for us.
# w : write mode : will do is create a new file or override this file if it already exists, means w mode clear the last file and make new one.
# r : read mode : open the file and read it. 
# a : a mode : most flexible mode , allows you to add something to the end of an existing file or create a new file if that file dosn't exist.

while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()

    if mode == "q":
        break

    elif mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode.")
        continue


# pip install cryptography -> we use this packege to encrypt he password
# this module to encrypt texts    
