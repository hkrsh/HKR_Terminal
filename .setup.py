#!/usr/bin/env python3
import time
import sys
import os

os.system("clear")

# Author = HKR_SH
# Date - 25/03/2023
# Purpose ------------------------------------
# The tool is for change termux prompt automatically
# and it help to creat own prompt without getting trouble
# or yup you can add login system using this tool

os.system("pkg install figlet")
os.system("pip install lolcat")
os.system("pip install tqdm")

#that's for remove motd
os.chdir("/data/data/com.termux/files/usr/etc")
os.system("rm motd")
os.chdir("/data/data/com.termux/files/home/HKR_Terminal")


try:
  from tqdm.auto import tqdm
  for i in tqdm(range(100001)):
    print(" ", end='\r')
except:
  print("""\033[91mRequared packeges arn't installed
Make sure Divice is connected to the internet""")
  print("")
  for i in range(100000):
    print("Please restart project with internet connection")
    error = input("Do you want to restart [Y/N]\033[92m ")
    if error == "Y":
      os.system("python setup.py")
    elif error == "y":
      os.system("python setup.py")
    else:
      exit()

os.system("clear")
print("Starting HKR_Terminal >_ ………/")
time.sleep(5)
os.system("clear")
os.system("figlet HKR . SH | lolcat")
time.sleep(3)

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

print("\033[92m")
typewrite(
	" ",
	" ",
	" ",
	"```````````````````````````````````````````````",
	"THANK'S FOR USING MY TOOL                     ~",
	"SUPPORT ME : https://www.youtube.com/@hkrsh   ~",
	"~                                             ~",
	"~                                             ~",
	"~                                             ~",
	"~                                             ~",
	"~                                             ~",
	"~                                             ~",
	"[1] : ABOUT               [~]                 ~",
	"[2] : PROMPT         [TERMUX]                 ~",
	"[3] : BANNER         [TERMUX]                 ~",
	"[4] : LOGIN SYSTEM   [TERMUX]                 ~",
	"[5] : EXIT                [~]                 ~",
	"~                                             ~",
	"~                                             ~",
	"~                                             ~",
	"~                                             ~",
	"~                                             ~",
	"~                                             ~",
	"~                                             ~",
	"~                                             ~",
	"...............................................",
	"~",
	"~",
	"~",
)
for i in range(100):
  number = input("ENTER NO_: ")

  if number == "5":
    exit()

  if number == "3":
    os.system("clear")
    os.system("figlet T BANNER | lolcat")
    print("\033[32m")
    typewrite(
      "```````````````````````````````````````````````",
      "SUPPORT ME : https://www.youtube.com/@hkrsh   ~",
      "~                                             ~",
      "~                                             ~",
      "~                                             ~",
      "~                                             ~",
      "~                                             ~",
      "~                                             ~",
      "~                                             ~",
      "~                                             ~",
      "[1] : NEXT           [~]                      ~",
      "[2] : EXIT           [~]                      ~",
      "~                                             ~",
      "~                                             ~",
      "~                                             ~",
      "~                                             ~",
      "~                                             ~",
      "~                                             ~",
      "~                                             ~",
      "~.............................................~",
      "~",
      "~",
      "~",
    )
    op1 = input("ENTER NO : ")
    if op1 == "1":
      os.system("clear")
      os.system("figlet T BANNER | lolcat")
      print("\033[32m")
      typewrite(
        "```````````````````````````````````````````````",
        "SUPPORT ME : https://www.youtube.com/@hkrsh   ~",
        "~                                             ~",
        "~                                             ~",
        "~                                             ~",
        "~                                             ~",
        "~                                             ~",
        "~                                             ~",
        "~                                             ~",
        "~                                             ~",
        "~                                             ~",
        "~                                             ~",
        "~.............................................~",
        "~",
        "~",
        "~",
      )
      banner = input("WRITE YOUR NAME : ")
      with open(".bashrc", "w") as f:
        f.write('''figlet '''+banner+''' | lolcat
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
''')
      os.system("mv .bashrc ~/")
      print("\033[31mPLEASE EXIT AND REOPEN TERMUX")
    if op1 == "2":
            exit()


  if number == "4":
    os.system("clear")
    os.system("figlet T LOGIN | lolcat")
    typewrite(
      " ",
      " ",
      " ",
      " ",
      " ",
      " ",
      " ",
      " ",
      " ",
      " ",
    )

    user = input("SET YOUR USERNAME : ")
    pas = input("SET YOUR PASSWORD : ")
    print("")
    ban = input("SET YOUR BANNER NAME : ")


    with open(".login.py", "w") as f:
      f.write('''#!/usr/bin/env python3
import os

usr = "'''+user+'''"
pas = "'''+pas+'''"
ban = "'''+ban+'''"
os.system("figlet "+ban+" | lolcat")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

getuser = input("ENTER YOUR USERNAME: ")
getpas = input("ENTER YOUR PASSWORD : ")

if getuser == usr:
  if getpas == pas:
    os.system("clear")
  else:
    os.system("python .login.py") 
else:
  os.system("python .login.py")
''')

    os.system("mv .login.py ~/")
    os.chdir("/data/data/com.termux/files/home")
    with open(".bashrc", "w") as f:
      f.write('''
python .login.py

clear
''')
      f.write("figlet "+ban+" | lolcat")
      f.write('''
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""

''')
    print("\033[31mEXIT FROM TERMUX FOR SEE CHANGES")



# MULTIVERS STARTED FROM THEIR [:)]



  if number == "1":
#    os.system("python .loading.py")
    os.system("clear")
    os.system("figlet HKR SH | lolcat")
    print("\033[32m ")
    typewrite(
      " ",
      " ",
      "```````````````````````````````````````````````",
      "YOUTUBE   : https://www.youtube.com/@hkrsh    ~",
      "GITHUB    : https://github.com/hkrsh          ~",
      "FACEBOOK  : http                              ~",
      "INSTAGRAM : http                              ~",
      "~                                             ~",
      "~                                             ~",
      "~                                             ~",
      "~                                             ~",
      "~                                             ~",
      "~                                             ~",
      "1 : EXIT [~]                                  ~",
      "2 : PROMPT [TERMUX]                           ~",
      "3 : BANNER [TERMUX]                           ~",
      "4 : LOGIN_SYSTEM [TERMUX]                     ~",
      "~                                             ~",
      "~                                             ~",
      "~                                             ~",
      "~                                             ~",
      "~                                             ~",
      "~                                             ~",
      "~.............................................~",
      "~",
      "~",
      "~",
    )

    for i in range(100):
      numbera = input("ENTER NO_:")

      if numbera == "1":
        os.system("clear")
        exit()


      if numbera == "3":
        os.system("clear")
        os.system("figlet T BANNER | lolcat")
        print("\033[32m")
        typewrite(
          "```````````````````````````````````````````````",
          "SUPPORT ME : https://www.youtube.com/@hkrsh   ~",
          "~                                             ~",
          "~                                             ~",
          "~                                             ~",
          "~                                             ~",
          "~                                             ~",
          "~                                             ~",
          "~                                             ~",
          "[1] : NEXT           [~]                      ~",
          "[2] : EXIT           [~]                      ~",
          "~                                             ~",
          "~                                             ~",
          "~                                             ~",
          "~                                             ~",
          "~                                             ~",
          "~                                             ~",
          "~                                             ~",
          "~.............................................~",
          "~",
          "~",
          "~",
        )
        op2 = input("ENTER NO : ")
        if op2 == "1":
          os.system("clear")
          os.system("figlet T BANNER | lolcat")
          print("\033[32m")
          typewrite(
            "```````````````````````````````````````````````",
            "SUPPORT ME : https://www.youtube.com/@hkrsh   ~",
            "~                                             ~",
            "~                                             ~",
            "~                                             ~",
            "~                                             ~",
            "~                                             ~",
            "~                                             ~",
            "~                                             ~",
            "~                                             ~",
            "~                                             ~",
            "~                                             ~",
            "~.............................................~",
            "~",
            "~",
            "~",
          )
          banner = input("WRITE YOUR NAME : ")
          with open(".bashrc", "w") as f:
            f.write('''figlet '''+banner+''' | lolcat
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
''')
          os.system("mv .bashrc ~/")
          print("\033[31mPLEASE EXIT AND REOPEN TERMUX")
        if op2 == "2":
          exit()



      if numbera == "4":
        os.system("clear")
        os.system("figlet T LOGIN | lolcat")
        typewrite(
          " ",
          " ",
          " ",
          " ",
          " ",
          " ",
          " ",
          " ",
          " ",
          " ",
        )

        user = input("SET YOUR USERNAME : ")
        pas = input("SET YOUR PASSWORD : ")
        print("")
        ban = input("SET YOUR BANNER NAME : ")


        with open(".login.py", "w") as f:
          f.write('''#!/usr/bin/env python3
import os

usr = "'''+user+'''"
pas = "'''+pas+'''"
ban = "'''+ban+'''"
os.system("figlet "+ban+" | lolcat")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

getuser = input("ENTER YOUR USERNAME: ")
getpas = input("ENTER YOUR PASSWORD : ")

if getuser == usr:
  if getpas == pas:
    os.system("clear")
  else:
    os.system("python .login.py")
else:
    os.system("python .login.py")
''')

        os.system("mv .login.py ~/")
        os.chdir("/data/data/com.termux/files/home")
        with open(".bashrc", "w") as f:
          f.write('''
python .login.py

clear
''')
          f.write("figlet "+ban+" | lolcat")
          f.write('''
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""

''')
        print("\033[31mPLEASE EXIT FROM TERMUX")
                


      if numbera == "2":
#        os.system("python .loading.py")
        os.system("clear")
        os.system("figlet T PROMPT | lolcat")
        print("\033[32m")
        typewrite(
          " ",
          " ",
          " ",
          "THANKS FOR USING MY TOOL",
          "SUPPORT ME : https://www.youtube.com/@hkrsh"
          "SELECT YOUR PROMPT",
          " ",
          " ",
          " ",
          " ",
          " ",
          " ",
          " ",
          "1 === MAKE OWN [~]"
          " ",
          )
        print('''2 === \033[31m┌⟼⟻⟼[D.A.T.E]⟻[]⟼[T.I.M.E]⟻⟼⟻⟼⟻⟼#")
      \033[31m├─[ \033[33mMon Mar 27 \033[31m][ \033[33m12:00 PM \033[31m]")
      \033[31m├─[~\033[32m/Termux_Prompt\\033[31m ]")
      \033[31m└─>[][CY.BE.R.SH][][~]:❯❯❯\033[32m''')
        print("")
        print('''3 === \033[31m┍▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ƒ")
      ▌【 \033[33m12:00 PM \033[31m】☠")
      ▌【\033[32m ~/Termux_Prompt\ \033[31m】☠")
      ⌊▬▬▬▰➽➤\033[32m''')
        print('')
        print('''\033[32m4 === \033[31m┌▬▬▬【D▬A▬T▬E]▬▬▬▬[T▬I▬M▬E]▬▬▬▬▬▬▬▬【\033[33mHKR_Terminal_Prompt\033[31m】
      ├▬【 \033[33mMon Apr 03  11:17 PM \033[31m】
      └>【s】:>>>>>
\033[32m''')
        typewrite(
           " ",
           " ",
           " ",
           " ",
           " ",
           " ",
           " ",
        )
        for i in range(100):
          numberb = input("ENTER NO_: ")

          if numberb == "1":
#            os.system("python .loading.py")
            os.system("python .prompta.py")

          if numberb == "2":
#            os.system("python .loading.py")
            os.system("python .promptb.py")

          if numberb == "3":
#            os.system("python .loading.py")
            os.system("python .promptc.py")

          if numberb == "4":
#            os.system("python .loading.py")
            os.system("python .promptd.py")



  if number == "2":
    os.system("clear")
    os.system("figlet HKR SH | lolcat")
    print("\033[32m")
    typewrite(
      " ",
      " ",
      " ",
      "THANKS FOR USING MY TOOL",
      "SUPPORT ME : https://www.youtube.com/@hkrsh"
      "SELECT YOUR PROMPT",
      " ",
      " ",
      " ",
      " ",
      " ",
      " ",
      " ",
      "1 === MAKE OWN [~]"
      " ",
    )
    print('''2 === \033[31m┌⟼⟻⟼[D.A.T.E]⟻[]⟼[T.I.M.E]⟻⟼⟻⟼⟻⟼#")
      \033[31m├─[ \033[33mMon Mar 27 \033[31m][ \033[33m12:00 PM \033[31m]")
      \033[31m├─[~\033[32m/Termux_Prompt\\033[31m ]")
      \033[31m└─>[][CY.BE.R.SH][][~]:❯❯❯\033[32m''')
    print("")
    print('''3 === \033[31m┍▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ƒ")
      ▌【 \033[33m12:00 PM \033[31m】☠")
      ▌【\033[32m ~/Termux_Prompt\ \033[31m】☠")
      ⌊▬▬▰➽➤\033[32m''')
    print('')
    print('''\033[32m4 === \033[31m┌▬▬▬【D▬A▬T▬E]▬▬▬▬[T▬I▬M▬E]▬▬▬▬▬▬▬▬【\033[33mTermux_Prompt\033[31m】
      ├▬【 \033[33mMon Apr 03  11:17 PM \033[31m】
      └>【s】:>>>>>
''')
    typewrite(
      " ",
      " ",
      " ",
      " ",
      " ",
      " ",
      " ",
    )
    for i in range(100):
      numberc = input("ENTER NO_: ")

      if numberc == "1":
#        os.system("python .loading.py")
        os.system("python .prompta.py")

      if numberc == "2":
#        os.system("python .loading.py")
        os.system("python .promptb.py")

      if numberc == "3":
#        os.system("python .loading.py")
                os.system("python .promptc.py")

      if numberc == "4":
#        os.system("python .loading.py")
        os.system("python .promptd.py")


