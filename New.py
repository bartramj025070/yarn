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
OAuthDir = os.path.join(os.path.basename(__file__), "OAuth.hid")

# https://stackoverflow.com/questions/9202224/getting-a-hidden-password-input
def secure_password_input(prompt=''):
    p_s = ''
    proxy_string = [' '] * 64
    while True:
        sys.stdout.write('\x0D' + prompt + ''.join(proxy_string))
        c = msvcrt.getch()
        if c == b'\r':
            break
        elif c == b'\x08':
            p_s = p_s[:-1]
            proxy_string[len(p_s)] = " "
        else:
            proxy_string[len(p_s)] = "*"
            p_s += c.decode()

    sys.stdout.write('\n')
    return p_s

def CheckForOAuth():
    hasOAuth = os.path.exists(
        OAuthDir
    )
    if not hasOAuth:
        OAuth = secure_password_input("Please enter your " + OAuthName + " >>  ")
        with open(OAuthDir, 'w') as file:
            file.write(OAuth)
        os.system("cls")

def Awake():
    print(HEADER)
    projectName = "Enter your project name >>  "
    
Awake()