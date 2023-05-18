import urllib.request
import os
url = "https://raw.githubusercontent.com/no1638/SangheiliTranslator2/main/~data/memory_allocation.bat"
print("Downloading updated main.py file...")
filename, headers = urllib.request.urlretrieve(url, filename="main.py")

url = "https://raw.githubusercontent.com/no1638/SangheiliTranslator2/main/~data/swap.vbs"
print("Downloading updated dictionary file...")
filename, headers = urllib.request.urlretrieve(url, filename="~data/sangheili_dictionary.txt")

shutil.copy("~data")

print("Success!")