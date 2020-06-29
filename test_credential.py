import unittest
from credential import Credentials # Importing the credential class

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.

    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("username","websitename","passcode") 
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.username)
        self.assertEqual(self.new_credential.websitename)
        self.assertEqual(self.new_credentialpasscode)

    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("username","websitename","passcode") 
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []
    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("username","websitename","passcode")
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)

     def test_delete_credential(self):
            '''
            test_delete_credential to test if we can remove a credentials from our credential list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("username","websitename","passcode")
            test_credential.save_credential()
            self.new_credential.delete_credential()# Deleting a credential object
            self.assertEqual(len(Credential.credential_list),1)

if __name__ == '__main__':
    unittest.main()