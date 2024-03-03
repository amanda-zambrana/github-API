"""
The primary goal of this python file is to demonstrate a simple unittest implementation for testing the
githubAPI.py file. 

(NOTE: for the third test, I found a random GitHub account with no repos to use. Here is the link to double check
that there are no repositories in that account when we run the tests to ensure accurate test results:
https://github.com/AmandaZamora)

---

This code has also been updated & designed to use a python mocking package to mock this program's external dependence
on GitHub so that I can guarantee that the unit tests will run consistently every time that they run, no 
matter how many times I run them, and no matter what changes I make to the repository. 

This program, mockGithubAPI.py starts with the identical code from the githubAPI.py program, and mocks out 
all of the service calls in that program using the python mock module from unittest, unittest.mock . 

@author: amanda-zambrana
"""

import unittest
from unittest.mock import patch
from githubAPI import githubapi

class testGithubAPI(unittest.TestCase):
    # This test case is for testing when there is no user account with the inputted name 
    @patch('githubAPI.githubapi', return_value=False)
    def testNoAccount(self, mock_githubapi):
        self.assertEqual(githubapi('amanda-zambrana123456789'), False)

    # This test case is for when a username inputted does correlate with an account in GitHub that does exist 
    @patch('githubAPI.githubapi', return_value=True)
    def testExistingAccount(self, mock_githubapi): 
        self.assertEqual(githubapi('amanda-zambrana'), True)
    
    # This test case is for when the user input does correspond with an existing account, but there is no public repos.
    @patch('githubAPI.githubapi', return_value=False)
    def testNoRepos(self, mock_githubapi):
        self.assertEqual(githubapi('AmandaZamora'), False) # Please note that I found a random GitHub account that exists with no repos just for this test

if __name__ == '__main__':
    print("Running unit tests.")
    unittest.main()
