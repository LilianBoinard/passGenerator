import os
from os import path
from colorama import init, Fore
init()

print(Fore.CYAN)
print(" _____  _____ _   _  ___________  ___ _____ ___________ ")
print("|  __ \|  ___| \ | ||  ___| ___ \/ _ \_   _|  _  | ___ \\")
print("| |  \/| |__ |  \| || |__ | |_/ / /_\ \| | | | | | |_/ /")
print("| | __ |  __|| . ` ||  __||    /|  _  || | | | | |    / ")
print("| |_\ \| |___| |\  || |___| |\ \| | | || | \ \_/ / |\ \ ")
print(" \____/\____/\_| \_/\____/\_| \_\_| |_/\_/  \___/\_| \_|")
print(Fore.WHITE)                                                               
                                                                

def add(append):
    theList.append(append)

def generate():
    global theList
    theList = []
    username = input("Username: ")
    add(username)
    add(username + "1")
    add(username + "123")
    add(username + "1234")
    add(str.capitalize(username))
    add(str.capitalize(username + "1"))
    add(str.capitalize(username + "123"))
    add(str.capitalize(username + "1234"))    
    name = input("Name (without capitalize): ")
    add(name)
    add(name + "1")
    add(name + "123")
    add(name + "1234")
    add(str.capitalize(name))
    add(str.capitalize(name + "1"))
    add(str.capitalize(name + "123"))
    add(str.capitalize(name + "1234"))    
    birthDay = input("Birth day: ")
    birthMonth = input("Birth month: ")
    birthYear = input("Birth year: ")
    add(birthDay + birthMonth + birthYear)
    add(username + birthDay)
    add(username + birthMonth)
    add(username + birthYear)
    add(username + birthDay + birthMonth)
    add(username + birthDay + birthMonth + birthYear)
    add(str.capitalize(username + birthDay))
    add(str.capitalize(username + birthMonth))
    add(str.capitalize(username + birthYear))
    add(str.capitalize(username + birthDay + birthMonth))
    add(str.capitalize(username + birthDay + birthMonth + birthYear))
    add(name + birthDay)
    add(name + birthMonth)
    add(name + birthYear)
    add(name + birthDay + birthMonth)
    add(name + birthDay + birthMonth + birthYear)
    add(str.capitalize(name + birthDay))
    add(str.capitalize(name + birthMonth))
    add(str.capitalize(name + birthYear))
    add(str.capitalize(name + birthDay + birthMonth))
    add(str.capitalize(name + birthDay + birthMonth + birthYear))
    hobby = input("Hobby: ")
    add(hobby)
    add(str.capitalize(hobby))
    add(username + "-" + hobby)
    add(str.capitalize(username) + "-" + hobby)
    add(username + "." + hobby)
    add(str.capitalize(username) + "." + hobby)
    add(name + "-" + hobby)
    add(str.capitalize(name) + "-" + hobby)
    add(name + "." + hobby)
    add(str.capitalize(name) + "." + hobby)

def main():
    print("Verification of the wordlist file...")
    filePath = "wordlist.txt"
    if path.exists(filePath):
        print(Fore.YELLOW + "File already exist.")
        def choiceDeleteData():
            choice = str(input("Do you want to delete existing data ? (y/n)\n" + Fore.WHITE))
            if choice == 'y':
                with open(filePath, 'w') as wordlist:
                    for i in range(47):
                        wordlist.write(theList[i] + '\n')
            elif choice == 'n': 
                with open(filePath, 'a') as wordlist:
                    for i in range(47):
                        wordlist.write(theList[i] + '\n')
            else:
                print("Choose y (yes) or n (no)")
                choiceDeleteData()
        choiceDeleteData()
    else:
        with open(filePath, 'w') as wordlist:
            for i in range(47):
                        wordlist.write(theList[i] + '\n')
        print("File created.")

generate()
main()
print(Fore.GREEN + "All passwords have been generated." + Fore.WHITE)
os.system("pause")