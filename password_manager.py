from re import M
from unicodedata import name
from cryptography.fernet import Fernet
     



def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key" , "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("what is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open('Password.txt', 'r') as f:
        for line in f.readlines():
            data=(line.rstrip())
            user , passw =data.split("|")
            print("User:", user , ", Password:" , str(fer.decrypt(passw.encode())))

            
def add():
    name = input("Account Name: ")
    pwd =  input("Password: ")
    
    with open('Password.txt', 'a') as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode())) + "\n")

while True:
    mode =input("would you like to add a nwe password or view existging ones (view/ add)? and q for quit(q)  ").lower()
    if mode =="q":
       break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
       print("invalid mode! ")
       continue