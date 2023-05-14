import urllib.request
url = "https://raw.githubusercontent.com/no1638/SangheiliTranslator2/main/main.py"
print("Downloading updated main.py file...")
filename, headers = urllib.request.urlretrieve(url, filename="main.py")

url = "https://raw.githubusercontent.com/no1638/SangheiliTranslator2/main/~data/sangheili_dictionary.txt"
print("Downloading updated dictionary file...")
filename, headers = urllib.request.urlretrieve(url, filename="~data/sangheili_dictionary.txt")

url = "https://raw.githubusercontent.com/no1638/SangheiliTranslator2/main/~data/suffix.txt"
print("Downloading updated suffix file...")
filename, headers = urllib.request.urlretrieve(url, filename="~data/suffix.txt")

url = "https://raw.githubusercontent.com/no1638/SangheiliTranslator2/main/real_time_translator.py"
print("Downloading updated R-T-Translator.py file...")
filename, headers = urllib.request.urlretrieve(url, filename="real_time_translator.py")

url = "https://raw.githubusercontent.com/no1638/SangheiliTranslator2/main/updater.py"
print("Downloading updated updater file...")
filename, headers = urllib.request.urlretrieve(url, filename="updater.py")

print("Success!")