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
#  os.system("python .loading.py")
    with open("bash.bashrc", "w") as f:
      f.write('''shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

PROMPT_DIRTRIM=2
PS1='\033[1;91m
┍▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ƒ
\033[1;91m▌【\033[1;93m \@\033[1;91m 】☠
\033[1;91m▌【\033[1;92m\w\033[1;91m 】☠
\033[1;91m⌊▬▬▰➽➤\033[1;92m '

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
#    os.system("python .loading.py")
    with open("bash.bashrc", "w") as f:
      f.write('''shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

PROMPT_DIRTRIM=2
PS1='\033[1;92m
┍▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ƒ
\033[1;92m▌【\033[1;93m \@\033[1;92m 】☠
\033[1;92m▌【\033[1;91m\w\033[1;92m 】☠
\033[1;92m⌊▬▬▰➽➤\033[1;96m '

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
#    os.system("python .loading.py")
    with open("bash.bashrc", "w") as f:
      f.write('''shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

PROMPT_DIRTRIM=2
PS1='\033[1;93m
┍▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ƒ
\033[1;93m▌【\033[1;91m \@\033[1;93m 】☠
\033[1;93m▌【\033[1;32m\w\033[1;93m 】☠
\033[1;93m⌊▬▬▰➽➤\033[1;92m '

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
#    os.system("python .loading.py")
    with open("bash.bashrc", "w") as f:
      f.write('''shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

PROMPT_DIRTRIM=2
PS1='\033[1;94m
┍▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ƒ
\033[1;94m▌【\033[1;93m \@\033[1;94m 】☠
\033[1;94m▌【\033[1;92m\w\033[1;94m 】☠
\033[1;94m⌊▬▬▰➽➤\033[1;92m '

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
#    os.system("python .loading.py")
    with open("bash.bashrc", "w") as f:
      f.write('''shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

PROMPT_DIRTRIM=2
PS1='\033[1;95m
┍▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ƒ
\033[1;95m▌【\033[1;93m \@\033[1;95m 】☠
\033[1;95m▌【\033[1;92m\w\033[1;95m 】☠
\033[1;95m⌊▬▬▰➽➤\033[1;92m '

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
#    os.system("python .loading.py")
    with open("bash.bashrc", "w") as f:
      f.write('''shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

PROMPT_DIRTRIM=2
PS1='\033[1;96m
┍▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ƒ
\033[1;96m▌【\033[1;93m \@\033[1;96m 】☠
\033[1;96m▌【\033[1;92m\w\033[1;96m 】☠
\033[1;96m⌊▬▬▰➽➤\033[1;92m '

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
#    os.system("python .loading.py")
    with open("bash.bashrc", "w") as f:
      f.write('''shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

PROMPT_DIRTRIM=2
PS1='\033[1;97m
┍▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ƒ
\033[1;97m▌【\033[1;93m \@\033[1;97m 】☠
\033[1;97m▌【\033[1;92m\w\033[1;97m 】☠
\033[1;97m⌊▬▬▰➽➤\033[1;96m '

if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi''')
  os.system("mv bash.bashrc /data/data/com.termux/files/usr/etc")
#  os.system("python .loading.py")
  print('''\033[31mYOUR PROMPT CHANGED SUCCESFULLY
FOR SEE CHANGES CLOSE AND REOPEN TERMUX''')
