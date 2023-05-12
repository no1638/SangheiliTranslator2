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

print("Success!")