# TODO
"""
- Create adv mode and smpl mode
- Update dictionary (DONE)
"""

import os
import sqlite3
import json
import os, signal
from os import name as os_name, system
import shutil
import time
import subprocess
from colorama import init, Fore as cc
import psutil
import re
import string
import random
# s = "testzhi"
# indices = [-3]
# parts = [s[i:j] for i,j in zip(indices, indices[1:]+[None])]
# print(parts)
#exit()
"""
This is V2 of my sangheili translator that is a LOT more streamlined, probably faster and uses proper programming techniques, the old translator would just split input and run a bunch of if statements (of every word in the dictionary which i prepared those if statements using ANOTHER python script XD) V2 uses an SQL database with words + counterparts and it translates both ways, you can also string together english and sangheili words in 1 input and it will translate them accordingly!
"""

# ENABLE/DISABLE CHOICE FOR ADV MODE, ONLY USE IF YOU HAVE AN ADVANCED VERSION OF YOUR DICTIONARY!
enable_adv = 0

clear = lambda: system('cls') if os_name == 'nt' else system('clear')
init()
dr = DR = r = R = cc.LIGHTRED_EX
g = G = cc.LIGHTGREEN_EX
b = B = cc.LIGHTBLUE_EX
m = M = cc.LIGHTMAGENTA_EX
c = C = cc.LIGHTCYAN_EX
y = Y = cc.LIGHTYELLOW_EX
w = W = cc.RESET

conn = sqlite3.connect(f'~data/words.db')
c = conn.cursor()

if not os.path.exists("~data/created.txt"):
  c.execute("""CREATE TABLE words(
        word text,
        counter text
    )""")
  conn.commit()
  c.execute("""CREATE TABLE suffix(
        word text,
        counter text
    )""")
  conn.commit()
  with open("~data/created.txt", "w") as f:
    f.close()

mainlogo = f'''{g}
=-------------------------------------------=
Dictionary may be updated at any time!
To make / add your own language please
clone this replit and then create a 
text file in ~data named-
sangheili_translator.txt
1 word / translation per line, format as so:

english; translated word

example:
your; k'e

=-------------------------------------------=

{w}'''
choices = [
  0,
  0,
  0,
  0,
  0,
  1,
  0,
  0,
  0,
  0,
  0,
  0,
]
cho = random.choice(choices)
if cho == 0:
  print(f"{r}Deleting current SQL rows...")
  c.execute("DELETE FROM words")
  print(f"{g}\nSuccess!\n{w}")
  print(f"{y}Loading new words...")
if cho == 1:
  print(f"{r}Hacking into the mainframe...")
  c.execute("DELETE FROM words")
  print(f"{g}\nSuccess!\n{w}")
  print(f"{y}Loading new configs...")
with open("~data/sangheili_dictionary.txt", "r", encoding="utf-8") as f:
  content = f.readlines()
  f.close()
colors = [f"{r}", f"{g}", f"{b}", f"{m}", f"{c}", f"{y}", f"{w}"]
currentcolor = 0
for line in content:

  line = line.strip()
  print(f"{colors[currentcolor]}{line}")
  try:
    ind = line.index(";")
  except:
    print(line)
  mainword = line[:ind]
  translated = line[ind + 2:]
  c.execute(f"""INSERT INTO words VALUES ("{mainword}", "{translated}")""")
  conn.commit()
  currentcolor = currentcolor + 1
  if currentcolor >= 6:
    currentcolor = 0
c.execute("DELETE FROM suffix")
print("Deleted all Suffixes")

with open("~data/suffix.txt", "r", encoding="utf-8") as f:
  content = f.readlines()
  f.close()
colors = [f"{r}", f"{g}", f"{b}", f"{m}", f"{c}", f"{y}", f"{w}"]
currentcolor = 0
for line in content:

  line = line.strip()
  print(f"{colors[currentcolor]}{line}")
  try:
    ind = line.index(";")
  except:
    print(line)
  mainword = line[:ind]
  translated = line[ind + 2:]
  c.execute(f"""INSERT INTO suffix VALUES ("{mainword}", "{translated}")""")
  conn.commit()
  currentcolor = currentcolor + 1
  if currentcolor >= 6:
    currentcolor = 0
    
    
print(f"\n{g}Success!\n{w}")


def main():
  clear()
  print(mainlogo)

  def inputPrime(text):
    print(text, end='')
    return input()

  phrase = inputPrime(f"{y}Input Phrase To Translate > {w}")
  finphrase = ""

  #phrase = phrase.translate(str.maketrans('', '', string.punctuation))

  def translate(phrase):
      translated = []
      splitted = phrase.split()
      for word in splitted:
        c.execute(f"""SELECT * FROM words WHERE word LIKE "{word}" """)
        output = c.fetchone()
        if not output is None:
            translated.append(output[-1])
        if output is None:
            c.execute(f"""SELECT * FROM words WHERE counter LIKE "{word}" """)
            output = c.fetchone()
            if not output is None:
                translated.append(output[0])
            if output is None:
                s = f"{word}"
                indices = [-3]
                parts = [s[i:j] for i,j in zip(indices, indices[1:]+[None])]
                suffix = parts[0]
                base = word[:-3]
                c.execute(f"""SELECT * FROM suffix WHERE counter LIKE "{suffix}" """)
                output2 = c.fetchone()
                if not output2 is None:
                    c.execute(f"""SELECT * FROM words WHERE counter LIKE "{base}" """)
                    output3 = c.fetchone()
                    if not output3 is None:
                        translated.append(f"{output2[0]} {output3[0]}")
                        #print(translated)
                if output2 is None:
                    c.execute(f"""SELECT * FROM suffix WHERE word LIKE "{word}" """)
                    output2 = c.fetchone()
                    if not output2 is None:
                        indbase = splitted.index(word)
                        base = splitted[indbase+1]
                        c.execute(f"""SELECT * FROM words WHERE word LIKE "{base}" """)
                        output3 = c.fetchone()
                        if not output3 is None:
                            translated.append(f"{output3[-1]}{output2[-1]}")
                            splitted.remove(f"{base}")
                            # print(translated)
                            # print(output3)
                            # print(output2)
                
                if output2 is None:
                    translated.append(f"{r}[{word}]{g}")
      joined = " ".join(translated)
      print(f"{g}{joined}{w}")
      input(f"{m}\n\nPress enter to continue...{w}")
      main()

  translate(phrase)


main()
