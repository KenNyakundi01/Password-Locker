class Credentials:
    """
    Class that generates new instances of credential
    """
    credential_dict = []

    def __init__(self,first_name,last_name,number,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
         @classmethod
    def find_credential(cls, cred_name):
        '''
        find_credential: Method that checks if a credential exists
        '''
        if cred_name in cls.credential_dict:
            return True

    @classmethod
    def display_credentials(cls):
        '''
        display_credentials: Class method that returns all credentials in the dictionary
        '''
        return cls.credential_dict