#
#       _                        
#       \`*-.                    
#        )  _`-.                 
#       .  : `. .                
#       : _   '  \               
#       ; *` _.   `*-._          
#       `-.-'          `-.       
#         ;       `       `.     
#         :.       .        \    
#         . \  .   :   .-'   .   
#         '  `+.;  ;  '      :   
#         :  '  |    ;       ;-. 
#         ; '   : :`-:     _.`* ;
#[bug] .*' /  .*' ; .*`- +'  `*' 
#      `*-*   `*-*  `*-*'
#this code is protected by milo the cat

import os

HEADER = """
Yarn is a tool for developing and maintaining
consistent development on github on computers where
you can't consistently validate your account's auth
tokens, or for where you don't have access to the
git shell.

This file creates a new Yarn project, follow it as such
and run the Push and Pull files respectively in the
Yarn project.

The entire project is written in Python, for ease-of-use,
readability, and to alleviate my specific circumstances:
my school doesn't allow any other programming language
on the computers.
"""

OAuthName = "PAT (Personal Access Token)"

filePath = os.path.dirname(__file__)
OAuthDir = os.path.join(filePath, ".pat.csv")
gitIgnoreDir = os.path.join(filePath, ".gitignore")

# Filled in CheckForOAuth()
OAuth = {
    "username": "mrrp :3",
    "token": "mrrp :3",
}

def CheckForOAuth():
    global OAuth
    hasOAuth = os.path.exists(OAuthDir) and os.path.exists(gitIgnoreDir)
    
    if not hasOAuth:
        with open(gitIgnoreDir, 'w') as gitIgnore:
            gitIgnore.writelines([
                'projects\n',
                os.path.basename(OAuthDir)
            ])
        
        githubUsername = input("Please enter your GitHub username >>  ")
        
        print("\nIf you don't have a PAT, go to: https://github.com/settings/personal-access-tokens")
        PAToken = input("Please enter your " + OAuthName + " >>  ")
        
        with open(OAuthDir, 'w') as file:
            file.write(f"{githubUsername},{PAToken}")
        
        os.system("cls")
        print(HEADER)
    
    with open(OAuthDir, 'r') as file:
        contents = file.read().split(',')
        
        username = contents[0]
        token = contents[1]
        
        OAuth["username"] = username
        OAuth["token"] = token

def Awake():
    print(HEADER)
    CheckForOAuth()
    
    projectName = input("Enter your project name >>  ")
    
    projectsDir = os.path.join(filePath, "projects")
    projectDir = os.path.join(projectsDir, projectName)
    
    if not os.path.exists(projectsDir):
        os.mkdir(projectsDir)
    
    if os.path.exists(projectDir):
        print("This project already exists!")
        input()
        return
    os.mkdir(projectDir)
    
    
Awake()