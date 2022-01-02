# CSU33012 - Software Engineering GitHub API Assignment
This is my submission repository for the GitHub API assignment for the Software Engineering Module (CSU33012).

# Program Explenation
**JSON** - Generates a JSON file of the scraped information for any future use.
**Graphs** 
- Line graph of the number of commits by a user for each of their public repositories.
My own profile: <img src="" width=400> Friends profile: <img src="" width=400>
- Multi-series pie chart of the languages used by the user, secondly broken down into how much of a language was used in different repositories.
My own profile: <img src="" width=400> Friends profile: <img src="" width=400>
- Bar chart of the amount of followers and the amount of people the user follows.
My own profile: <img src="" width=400> Friends profile: <img src="" width=400>

# How to Run
**NOTE**: Make sure that you have Python installed on your system and have a valid GitHub Access Token.
- First you will need to download this project from my GitHub.
- Using cmd or any other command prompt, navigate to the downloaded project path.
- To install all the necessary packages, we will need to install pip:
```
python get-pip.py
```
- Now we can install of the packages
```
pip install -r packages.txt
```
- Now we can run the program
```
python GitHubApi.py
```