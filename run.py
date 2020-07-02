#!/usr/bin/env python3.6
from user import User
from credential import Credentials

#create user
def create_user(username,password):
    """ 
    function is to register user into the system
    """

    new_user = User(username,password) 
    new_user.save_user()

def create_credential(name):
    """
    function is to create the credentials of the user
    """
    new_credential = Credential(name)
    new_credential.new_credential


def main():
    print("Hello and Welcome...Please enter your name")
    n_user=input()
    print("\n")
    print(f"Hello {n_user}...Please enter your password")
    n_password = input()
    print("Enter the your preferable username for your account ")
    name = input()
    print("Please enter the website name...")
    w_name = input()
    print("Please enter password...")
    pcode = input()
    print("Would you like the credentials to be displayed:Y/N")
    if input() == "Y":
       list_credentials()

    elif input() =="N":
        exit()

    create_user(n_user,n_password)

if __name__ == '__main__':

    main()