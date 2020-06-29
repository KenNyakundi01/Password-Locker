import unittest
from user import user # Importing the user class

class Testuser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = user("username","websitename","passcode") 

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username)
        self.assertEqual(self.new_user.websitename)
        self.assertEqual(self.new_user.passcode)

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = user("username","websitename","passcode") 
            test_user.save_user()
            self.assertEqual(len(user.user_list),2)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            user.user_list = []

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = user("username","websitename","passcode")
            test_user.save_user()
            self.assertEqual(len(user.user_list),2)
     def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = user("username","websitename","passcode")
            test_user.save_user()

            self.new_user.delete_user()
            self.assertEqual(len(user.user_list),1)

if __name__ == '__main__':
    unittest.main()