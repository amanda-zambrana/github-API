"""
The primary goal of this python file is to demonstrate a simple unittest implementation for testing the
githubAPI.py file. 

(NOTE: for the third test, I found a random GitHub account with no repos to use. Here is the link to double check
that there are no repositories in that account when we run the tests to ensure accurate test results:
https://github.com/AmandaZamora)

@author: amanda-zambrana
"""

import unittest
from githubAPI import githubapi

class testGithubAPI(unittest.TestCase):
    # This test case is for testing when there is no user account with the inputted name 
    def testNoAccount(self):
        self.assertEqual(githubapi('amanda-zambrana123456789'), False)

    # This test case is for when a username inputted does correlate with an account in GitHub that does exist 
    def testExistingAccount(self): 
        self.assertEqual(githubapi('amanda-zambrana'), True)
    
    # This test case is for when the user input does correspond with an existing account, but there is no public repos.
    def testNoRepos(self):
        self.assertEqual(githubapi('AmandaZamora'), False) # Please note that I found a random GitHub account that exists with no repos just for this test

   # def testNoInput(self):
   #     self.assertEqual(githubapi(''), False,'There is no input')

if __name__ == '__main__':
    print("Running unit tests.")
    unittest.main()

