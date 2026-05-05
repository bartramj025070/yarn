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
and use run the Push and Pull files respectively in the
Yarn project.

The entire project is written in Python, for ease-of-use,
readability, and to alleviate my specific circumstances:
my school doesn't allow any other programming language
on the computers.
"""

OAuthName = "PAT (Personal Access Token)"

filePath = os.path.dirname(__file__)
OAuthDir = os.path.join(filePath, "OAuth.csv")
gitIgnoreDir = os.path.join(filePath, ".gitignore")

def CheckForOAuth():
    hasOAuth = os.path.exists(OAuthDir) and os.path.exists(gitIgnoreDir)
    if not hasOAuth:
        with open(gitIgnoreDir, 'w') as gitIgnore:
            gitIgnore.writelines([
                'projects',
                os.path.basename(OAuthDir)
            ])
        
        githubUsername = input("Please enter your GitHub username >>  ")
        print("\nIf you don't have a PAT, go to: https://github.com/settings/personal-access-tokens")
        OAuth = input("Please enter your " + OAuthName + " >>  ")
        with open(OAuthDir, 'w') as file:
            file.write(f"{githubUsername},{OAuth}")
        os.system("cls")
        print(HEADER)

def Awake():
    print(HEADER)
    CheckForOAuth()
    
    projectName = input("Enter your project name >>  ")
    projectDir = os.path.join(filePath, projectName)
    
    if os.path.exists(projectDir):
        print("This project already exists!")
        input()
        return
    os.mkdir(projectDir)
    
Awake()