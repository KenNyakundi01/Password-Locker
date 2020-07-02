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

 

def main():
    print("Please enter your name")
    n_user=input()
    print("\n")
    print("Please enter your password")
    n_password = input()

    create_user(n_user,n_password)

if __name__ == '__main__':

    main()