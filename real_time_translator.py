from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard
import keyboard as kboard
import sqlite3
import string
import win32clipboard
import pyautogui
import pyperclip




conn = sqlite3.connect("~data/words.db", check_same_thread=False)
c = conn.cursor()


kb = Controller()

enabled = False
keylist = []

cmb = [{keyboard.Key.home}]
current = set()

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
        output = c.fetchall()
        if not len(output) == 0:
            #print(output)
            if len(output) > 1:
                newlist = []
                for item in output:
                  newlist.append(f"{item[-2]}")
                  #output.remove(item)
                  #print(newlist)
                newjoined = "/".join(newlist)
                #print(newjoined)
                translated.append(newjoined)
            if not len(output) > 1:
              output1 = output[0]
              translated.append(output1[-2])
        if len(output) == 0:
            s = f"{word}"
            indices = [-4]
            parts = [s[i:j] for i,j in zip(indices, indices[1:]+[None])]
            suffix = parts[0]
            base = word[:-4]
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
                    try:
                        base = splitted[indbase+1]
                        c.execute(f"""SELECT * FROM words WHERE word LIKE "{base}" """)
                        output3 = c.fetchone()
                        if not output3 is None:
                            translated.append(f"{output3[-1]}{output2[-1]}")
                            splitted.remove(f"{base}")
                            # print(translated)
                            # print(output3)
                            # print(output2)
                    except:
                        #print(base)
                        translated.append(output2[-1])
            if output2 is None:
                translated.append(f"[{word}]")
  joined = " ".join(translated)
  print(f"{joined}")
  return joined
        
        
        
def execute():
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
    data = pyperclip.paste()
    #print(data)
    phrase = data
    phrase2 = translate(phrase)
    pyperclip.copy(phrase2)
    pyautogui.hotkey('ctrl', 'v')
    




# def on_press(key):
    # global enabled
    # backspace = Key.backspace
    # spacebar = Key.space
    # forbidden = [Key.alt, Key.space, Key.cmd_l, Key.cmd_r, Key.alt_r, Key.alt_l, Key.ctrl_l, Key.ctrl_r, Key.shift_l, Key.shift_r, Key.backspace, Key.caps_lock, Key.cmd, Key.ctrl, Key.delete, Key.down, Key.enter, Key.end, Key.esc, Key.f1, Key.f2, Key.f3, Key.f4, Key.f5, Key.f6, Key.f7, Key.f8, Key.f9, Key.f10, Key.f11, Key.f12, Key.f13, Key.f14, Key.f15, Key.f16, Key.f17, Key.f18, Key.f19, Key.f20, Key.f21, Key.f22, Key.f23, Key.f24, Key.home, Key.left, Key.page_down, Key.page_up, Key.right, Key.shift, Key.tab, Key.up]
    # if enabled == True:
        # if not key in forbidden:
            # keylist.append(str(key))
            # print(f"PRINTING KEYLIST {keylist}")
        # if key == spacebar:
            # phrase = "".join(keylist)
            # keylist.clear()
            # print("JOINED KEYLIST")
            # phrase = phrase.translate(str.maketrans('', '', string.punctuation))
            # #print(phrase)
            # joined = translate(phrase)
            # print("TRANSLATED PHRASE")
            # for char in phrase:
                # kboard.press_and_release("backspace")
                
            # kboard.press_and_release("backspace")
            # for char in joined:
                # kboard.write(char)
                # keylist.clear()
            # kboard.write(" ")
            # keylist.clear()
            # print("CLEARED KEYLIST")

        
        
       
        
    # if key == Key.f9:
        # print("detected f9")
        # enabled = not enabled
        # if enabled == False:
            # print("Disabled")
        # if enabled == True:
            # print ("Enabled")
        
        
    # if key == Key.end:
        # exit()
        
def on_press(key):
  if key == Key.end:
    exit()
  if any([key in z for z in cmb]):
    current.add(key)
    if any(all(k in current for k in z) for z in cmb):
      execute()
 
def on_release(key):
  print(current)
  if any([key in z for z in cmb]):
    try:
        current.remove(key)
    except:
        pass
    print(current)
        
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    
    
    
    