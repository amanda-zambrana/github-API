""" 
This code is designed to interface with an external REST-based API. 
I used the following public GitHub API: https://api.github.com/users/<ID>/repos

The code includes a function that takes an input from the user for a GitHub user ID. Then, it interfaces with
GitHub in order to extract and display useful information about the user and their repositories. (Please note
that it only grabs information about the user's public repositories, not their private ones.) 
The function communicates using the RESTful services APIs provided by GitHub. 

The output of the function is a list of the names of all of the public repositories that the user has, as well
as the number of commits that are in each of the listed repositories. Note that if the username inputted does not
exist as a GitHub account, the function displays an error message. Also, if the username does correlate with an 
account but that user has no public repositories, the function displays a message indicating that as well. 

WARNING: With this GitHub API, if you make too many API requests of GitHub then you may reach a limit and then 
GitHub will start to give errors. You can only perform so many tests of GitHub APIs within some period of time, 
so realize that if your tests are passing fine and then all of a sudden they start to fail, then it may be 
because you have exceeded the limits on GitHub. You will need to stop testing and wait for a period of time 
before GitHub will allow further requests.

@author: amanda-zambrana 
"""

# NOTE: I had to change the python interpreter from 3.9.6 64-bit to 3.8.x because it was not recognizing the requests module import (coding in VS Code)
import requests  
import json


def githubapi(githubID):
    # Using the following GitHub API to retrieve a user's list of repositories (input from the user in the <ID> position of the API)
    results = requests.get("https://api.github.com/users/" + githubID + "/repos")

    if results.status_code != 200:
        # If the username entered does not correspond with an existing GitHub account, display this message
        print("Sorry, there is no GitHub account with this username.")
        return False

    accountRepos = results.json()

    # If the username entered corresponds with an existing account, but that account has no public repositories, then dispaly this message 
    if len(accountRepos) == 0:
        print("This account has no repositories.")
        return False

    for repository in accountRepos:
        repositoryResult = requests.get(repository['commits_url'].split("{")[0])
        repositoryResult = repositoryResult.json()
        print("Repository Name: " + repository['name'] + ",  Number Of Commits: " + str(len(repositoryResult)))

    return True


if __name__ == "__main__":
    username = input("Please enter your Github username: ")
    githubapi(username)