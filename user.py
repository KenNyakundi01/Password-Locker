class User:
    ''' 
    This is the user class where the user is persisted to disk in a plain file
    '''
    user_list = []  # empty user list

    def __init__(self, username, password):
        '''
        __init__ method that helps us define properties for our objects
        Args:
                username: New user's username
                password: New user's password
        '''
        self.username = username
        self.password = password
    def save_user(self):
        '''
        save_user method: saves user to user list as an append
        '''
        User.user_list.append(self)
    def delete_user(self):
        '''
        delete_user method: deletes the last user saved to the user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_name(cls, name):
        '''
        find_by_name class method: Method that takes in a name and returns a user with that name
        '''
        for user in cls.user_list:
            if user.username == name:
                return user
    @classmethod
    def user_exist(cls, name):
        '''
         Method that checks if a user exists from the user list
        '''
        for user in cls.user_list:
            if user.username == name:
                return True

        return False

    