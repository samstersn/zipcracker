#1/usr/bin/python
import os
import sys
os.system("clear")
print("\033[91m ")
os.system("figlet zipcracker")
print("\033[93m ")
os.system("cowsay created by @khacker...")
print("\033[36m ")
import zipfile

from tqdm import tqdm
# the password list path you want to use, must be available in the current directory
wordlist = "/data/data/com.termux/files/home/pass.txt"
# the zip file you want to crack its password
zip_file = "/data/data/com.termux/files/home/0.zip"
# initialize the Zip File object
zip_file = zipfile.ZipFile(zip_file)
# count the number of words in this wordlist
n_words = len(list(open(wordlist, "rb")))
# print the total number of passwords

print("Total passwords to test:", n_words)

with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)
print("[!] Password not found, try other wordlist.")
print("Created by @khacker...")
