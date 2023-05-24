#!/usr/bin/env python3
import os
import sys
import time

os.system("clear")
from time import sleep
from typing import Tuple

DELAY: float = .01


def typewrite(*paragraph: str) -> None:
	for sentence in paragraph:
		for char in sentence:
			sys.stdout.write(char)
			sys.stdout.flush()
			sleep(DELAY)
		print()
		sleep(DELAY)

os.system("figlet HKR SH | lolcat")
print('\033[32m")
typewrite(
  " ",
  " ",
  " ",
  "'''''''''''''''''''''''''''''''''''''''''''''''",
  "SELECT YOUR PROMPT COLOUR                     ~",
  "~                                             ~",
  "~                                             ~",
  "~                                             ~",
  "~                                             ~",
  "~                                             ~",
  "~                                             ~",
  "~                                             ~",
  "[1] : RED                                     ~",
  "[2] : GREEN                                   ~",
  "[3] : YELLOW                                  ~",
  "[4] : BLUE                                    ~",
  "[5] : MAGENTA                                 ~",
  "[6] : CYAN                                    ~",
  "[7] : WHITE                                   ~",
  "~                                             ~",
  "~                                             ~",
  "~                                             ~",
  "~.............................................~",
  "~",
  "~",
  "~",
)
for i in range(100):
  color = input("ENTER NO_: ")
  if color == "1":
    name = input("TYPE YOUR NAME : ")
    with open("bash.bashrc", "w") as f:
      f.write('''shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

PROMPT_DIRTRIM=2
PS1='\033[1;91m
┌⟼⟻⟼[D.A.T.E]⟻[]⟼[T.I.M.E]⟻⟼⟻⟼⟻⟼#
\033[1;91m├─[\033[1;93m \d\033[1;91m ][\033[1;93m \@\033[1;91m ]
\033[1;91m├─[\033[1;92m\w\033[1;91m\ ]
\033[1;91m└>[]['''+name+'''][][~]:❯❯❯ \033[1;92m'

if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi''')
    os.system("mv bash.bashrc /data/data/com.termux/files/usr/etc")
#    os.system("python .loading.py")
    print('''\033[31mYOUR PROMPT CHANGED SUCCESFULLY
FOR SEE CHANGES CLOSE AND REOPEN TERMUX''')


  if color == "2":
    name = input("TYPE YOUR NAME : ")
    with open("bash.bashrc", "w") as f:
      f.write('''shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

PROMPT_DIRTRIM=2
PS1='\033[1;92m
┌⟼⟻⟼[D.A.T.E]⟻[]⟼[T.I.M.E]⟻⟼⟻⟼⟻⟼#
\033[1;92m├─[\033[1;93m \d\033[1;92m ][\033[1;93m \@\033[1;92m ]
\033[1;92m├─[\033[1;91m\w\033[1;92m\ ]
\033[1;92m└>[]['''+name+'''][][~]:❯❯❯ \033[1;91m'

if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi''')
    os.system("mv bash.bashrc /data/data/com.termux/files/usr/etc")
#    os.system("python .loading.py")
    print('''\033[31mYOUR PROMPT CHANGED SUCCESFULLY
FOR SEE CHANGES CLOSE AND REOPEN TERMUX''')


  if color == "3":
    name = input("TYPE YOUR NAME : ")
    with open("bash.bashrc", "w") as f:
      f.write('''shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

PROMPT_DIRTRIM=2
PS1='\033[1;93m
┌⟼⟻⟼[D.A.T.E]⟻[]⟼[T.I.M.E]⟻⟼⟻⟼⟻⟼#
\033[1;93m├─[\033[1;91m \d\033[1;93m ][\033[1;91m \@\033[1;93m ]
\033[1;93m├─[\033[1;92m\w\033[1;93m\ ]
\033[1;93m└>[]['''+name+'''][][~]:❯❯❯ \033[1;92m'

if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi''')
    os.system("mv bash.bashrc /data/data/com.termux/files/usr/etc")
#    os.system("python .loading.py")
    print('''\033[31mYOUR PROMPT CHANGED SUCCESFULLY
FOR SEE CHANGES CLOSE AND REOPEN TERMUX''')


  if color == "4":
    name = input("TYPE YOUR NAME : ")
    with open("bash.bashrc", "w") as f:
      f.write('''shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

PROMPT_DIRTRIM=2
PS1='\033[1;94m
┌⟼⟻⟼[D.A.T.E]⟻[]⟼[T.I.M.E]⟻⟼⟻⟼⟻⟼#
\033[1;94m├─[\033[1;93m \d\033[1;94m ][\033[1;93m \@\033[1;94m ]
\033[1;94m├─[\033[1;92m\w\033[1;94m\ ]
\033[1;94m└>[]['''+name+'''][][~]:❯❯❯ \033[1;92m'

if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi''')
    os.system("mv bash.bashrc /data/data/com.termux/files/usr/etc")
#    os.system("python .loading.py")
    print('''\033[31mYOUR PROMPT CHANGED SUCCESFULLY
FOR SEE CHANGES CLOSE AND REOPEN TERMUX''')


  if color == "5":
    name = input("TYPE YOUR NAME : ")
    with open("bash.bashrc", "w") as f:
      f.write('''shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

PROMPT_DIRTRIM=2
PS1='\033[1;95m
┌⟼⟻⟼[D.A.T.E]⟻[]⟼[T.I.M.E]⟻⟼⟻⟼⟻⟼#
\033[1;95m├─[\033[1;93m \d\033[1;95m ][\033[1;93m \@\033[1;95m ]
\033[1;95m├─[\033[1;92m\w\033[1;95m\ ]
\033[1;95m└>[]['''+name+'''][][~]:❯❯❯ \033[1;92m'

if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi''')
    os.system("mv bash.bashrc /data/data/com.termux/files/usr/etc")
#    os.system("python .loading.py")
    print('''\033[31mYOUR PROMPT CHANGED SUCCESFULLY
FOR SEE CHANGES CLOSE AND REOPEN TERMUX''')


  if color == "6":
    name = input("TYPE YOUR NAME : ")
    with open("bash.bashrc", "w") as f:
      f.write('''shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

PROMPT_DIRTRIM=2
PS1='\033[1;96m
┌⟼⟻⟼[D.A.T.E]⟻[]⟼[T.I.M.E]⟻⟼⟻⟼⟻⟼#
\033[1;96m├─[\033[1;93m \d\033[1;96m ][\033[1;93m \@\033[1;96m ]
\033[1;96m├─[\033[1;92m\w\033[1;96m\ ]
\033[1;96m└>[]['''+name+'''][][~]:❯❯❯ \033[1;92m'

if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi''')
    os.system("mv bash.bashrc /data/data/com.termux/files/usr/etc")
#    os.system("python .loading.py")
    print('''\033[31mYOUR PROMPT CHANGED SUCCESFULLY
FOR SEE CHANGES CLOSE AND REOPEN TERMUX''')


  if color == "7":
    name = input("TYPE YOUR NAME : ")
    with open("bash.bashrc", "w") as f:
      f.write('''shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

PROMPT_DIRTRIM=2
PS1='\033[1;97m
┌⟼⟻⟼[D.A.T.E]⟻[]⟼[T.I.M.E]⟻⟼⟻⟼⟻⟼#
\033[1;97m├─[\033[1;93m \d\033[1;97m ][\033[1;93m \@\033[1;97m ]
\033[1;97m├─[\033[1;92m\w\033[1;97m\ ]
\033[1;97m└>[]['''+name+'''][][~]:❯❯❯ \033[1;92m'

if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi''')
    os.system("mv bash.bashrc /data/data/com.termux/files/usr/etc")
#    os.system("python .loading.py")
    print('''\033[31mYOUR PROMPT CHANGED SUCCESFULLY
FOR SEE CHANGES CLOSE AND REOPEN TERMUX''')


