import requests
import json

def shiritori(word):
    url = "https://xxxxx.com/"
    payload = {'word': word}
    response = requests.request("POST", url, data = payload)
    data = response.json()
    return data["word"]

words = []
komoji_list = ["ァ","ィ","ゥ","ェ","ォ","ッ","ャ","ュ","ョ"]

while True:
    print("あなたの番です(カタカナで入力してね) >> ")
    input_str = input()
    if input_str[-1] == "ー":
        input_str = input_str[:-1]
    if input_str[-1] in komoji_list:
        list_str = list(input_str)
        list_str[-1] = chr(ord(list_str[-1])+1)
        input_str = ''.join(list_str)
    if input_str in words or input_str[-1] == "ン":
        print("あいての勝ちです")
        break
    words.append(input_str)
    resp = shiritori(input_str)
    words.append(resp)
    if resp[len(resp)-1] == "ン":
        print("あいて: " + resp)
        print("あなたの勝利です")
        break
    else:
        print("あいて: " + resp)
print('=>'.join(words))