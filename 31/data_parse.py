from string import *
import requests

def parse_char():
    with open("chinese.txt") as file:
        data = file.read()
        new_string = ""
        for i in data:
            if i not in ascii_letters and i not in digits:
                new_string += i
        
    with open("new_chinese.txt", "w") as new_file:
        new_file.write(new_string)

# parse_char()

def parse_pinyin():
    with open("new_chinese.txt") as file:
        data = file.read()
        new_list = []
        for char in data:
            pinyin_data = requests.get(f"https://helloacm.com/api/pinyin/?cached&s={char}&t=1")
            pinyin = pinyin_data.json()["result"]
            new_list.append(pinyin)
        print(new_list)
    with open("pinyin.txt", "w") as new_file:
        new_file.write(new_list)

# parse_pinyin()

# test = requests.get("https://helloacm.com/api/pinyin/?cached&s=你好&t=1")
# print(test.json()["result"])