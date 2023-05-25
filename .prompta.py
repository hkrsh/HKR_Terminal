#!/usr/bin/env python3
import os
import time
import sys

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


os.system("clear")

RED = "\033[1;91m"
GREEN = "\033[1;92m"
YELLOW = "\033[1;93m"
BLUE = "\033[1;94m"
MAGENTA = "\033[1;95m"
CYAN = "\033[1;96m"
WHITE = "\033[1;97m"
codet = "'"

print(GREEN)
typewrite(
  "THISE SECSION IS FOR CREAT OWN PROMPT`````````~",
  "YOU CAN CREAT YOUR OWN PROMPT                 ~",
  "SMARTLY WITHOUT GATTING TROUBLE               ~",
  "~                                             ~",
  "USE OF THISE TOOL IS VERY SIMPLE              ~",
  "WRITE YOUR PROMPT IN THERE                    ~",
  "FOR MAKE YOUR PROMPT COLORFULL                ~",
  "JUST WRITE YOUR COLOR CODE WHERE YOU WANT     ~",
  "THEN HIT ENTER                                ~",
  "FOR SEE FULL TUTORIAL WATCH MY VIDEO          ~",
  "~                                             ~",
  "VIDEO LINK :                                  ~",
  "~                                             ~",
  "~                                             ~",
  "~                                             ~",
  "~                                             ~",
  "~                                             ~",
  "~                                             ~",
  "~                                             ~",
  "1 === NEXT                                    ~",
  "~.............................................~",
  "~",
  "~",
  "~",
)
for i in range(100):
	next = input("TYPE THIRE : ")
	if next == "1":
		os.system("clear")
		print("```````````````````````````````````````````````")
		print("~HOW MANY LINES YOU WANT TO ADD IN YOUR PROMPT'")
		print("~TYPE THERE YOU CAN WRITE HIGHEST 5 LINES     ~")
		print("~PROMPT I THINK THAT'S ENOUGH FOR YOU. IF YOU ~")
		print("~NEED MORE PLEASE CONTACT WITH ME             ~")
		print("~                                             ~")
		print("~                                             ~")
		print("~                                             ~")
		print("~                                             ~")
		print("~                                             ~")
		print("~                                             ~")
		print("~                                             ~")
		print("~                                             ~")
		print("~                                             ~")
		print("~                                             ~")
		print("...............................................")

#      "```````````````````````````````````````````````",
#      "~HOW MANY LINES YOU WANT TO ADD IN YOUR PROMPT'",
#      "~TYPE THERE YOU CAN WRITE HIGHEST 5 LINES     ~",
#      "~PROMPT I THINK THAT'S ENOUGH FOR YOU. IF YOU ~",
#      "~NEED MORE PLEASE CONTACT WITH ME             ~",
#      "~                                             ~",
#      "~                                             ~",
#      "~                                             ~",
  #    "~                                             ~",
   #   "~                                             ~",
  #    "~                                             ~",
 #     "~                                             ~",
     # "~                                             ~",
   #   "~                                             ~",
    #  "~                                             ~",
    #  "...............................................",
		#  "~",
		  #"~",
	#	  "~",
 #   )
		for i in range(100):
			ines = input("TYPE THIRE : ")
			if ines == "1":
				os.system("clear")
#				os.system("python .loading.py")
				print("")
				print("")
				print("")
				print("")
				print("")
				print("")
				print("")
				print("")
				prompt = input("TYPE YOUR PROMPT THIRE : ")
#				os.system("python .loading.py")
				with open("bash.bashrc", "w") as f:
					f.write('''shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

PROMPT_DIRTRIM=2''')
					f.write('''
''')
					f.write("PS1='"+prompt+codet)
					f.write('''
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi''')

				os.system("mv bash.bashrc /data/data/com.termux/files/usr/etc")
				os.system("python .loading.py")
				print('''\033[31mYOUR PROMPT CHANGED SUCCESFULLY
FOR SEE CHANGES CLOSE AND REOPEN TERMUX''')


			if ines == "2":
				aa = input("WRITE FIRST LINE THIRE :")
				ba = input("WRITE SECOND LINE THIRE :")

				with open("bash.bashrc", "w") as f:
					f.write('''shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

PROMPT_DIRTRIM=2''')
					f.write('''
''')
					f.write("PS1='"+aa)
					f.write('''
''')
					f.write(ba+codet)
					f.write('''
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi''')

				os.system("mv bash.bashrc /data/data/com.termux/files/usr/etc")
#				os.system("python .loading.py")
				print('''\033[31mYOUR PROMPT CHANGED SUCCESFULLY
FOR SEE CHANGES CLOSE AND REOPEN TERMUX''')


			if ines == "3":
				ab = input("WRITE FIRST LINE THIRE :")
				bb = input("WRITE SECOND LINE THIRE :")
				cb = input("WRITE THIRD LINE THIRE :")

				with open("bash.bashrc", "w") as f:
					f.write('''shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

PROMPT_DIRTRIM=2''')
					f.write('''
''')
					f.write("PS1='"+ab)
					f.write('''
''')
					f.write(bb)
					f.write('''
''')
					f.write(cb+codet)
					f.write('''
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi''')

				os.system("mv bash.bashrc /data/data/com.termux/files/usr/etc")
#				os.system("python .loading.py")
				print('''\033[31mYOUR PROMPT CHANGED SUCCESFULLY
 EXIT AND REOPEN TERMUX FOR SEE CHANGES''')


			if ines == "4":
				ac = input("WRITE FIRST LINE THIRE :")
				bc = input("WRITE SECOND LINE THIRE :")
				cc = input("WRITE THIRD LINE THIRE :")
				dc = input("WRITE FOUR LINE THIRE :")

				with open("bash.bashrc", "w") as f:
					f.write('''shopt -s histappend
shopt -s histverify
eport HISTCONTROL=ignoreboth

PRO#MPT_DIRTRIM=2''')
					f.write('''
''')
					f.write("PS1='"+ac)
					f.write('''
''')
					f.write(bc)
					f.write('''
''')
					f.write(cc)
					f.write('''
''')
					f.write(dc+codet)
					f.write('''
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-fou>
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command>
        }
fi''')

				os.system("mv bash.bashrc /data/data/com.termux/files/usr/etc")
#				os.system("python .loading.py")
				print('''\033[31mYOUR PROMPT CHANGED SUCCESFULLY
EXIT AND REOPEN TERMUX FOR SEE CHANGES''')

			if ines == "5":
				ad = input("WRITE FIRST LINE THIRE :")
				bd = input("WRITE SECOND LINE THIRE :")
				cd = input("WRITE THIRD LINE THIRE :")
				dd = input("WRITE FOUR LINE THIRE :")
				ed = input("WRITE FIVE LINE THIRE :")

				with open("bash.bashrc", "w") as f:
					f.write('''shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

PROMPT_DIRTRIM=2''')
					f.write('''
''')
					f.write("PS1='"+ad)
					f.write('''
''')
					f.write(bd)
					f.write('''
''')
					f.write(cd)
					f.write('''
''')
					f.write(dd)
					f.write('''
''')
					f.write(ed+codet)
					f.write('''
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-fou>
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command>
        }
fi''')

				os.system("mv bash.bashrc /data/data/com.termux/files/usr/etc")
#				os.system("python .loading.py")
				print('''\033[31mYOUR PROMPT CHANGED SUCCESFULLY
EXIT AND REOPEN TERMUX FOR SEE CHANGES''')
