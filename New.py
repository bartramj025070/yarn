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

OAuthName = "SSH Key"
OAuthDir = os.path.join(os.path.dirname(__file__), "OAuth.hid")

def CheckForOAuth():
    hasOAuth = os.path.exists(OAuthDir)
    if not hasOAuth:
        OAuth = input("Please enter your " + OAuthName + " >>  ")
        with open(OAuthDir, 'w') as file:
            file.write(OAuth)
        os.system("cls")
        print(HEADER)

def Awake():
    print(HEADER)
    CheckForOAuth()
    projectName = "Enter your project name >>  "
    
Awake()
