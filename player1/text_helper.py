import random
def simplefy_text(text):
    with open(text,"r") as f:
        x=f.read()
    words=[]
    temp=""
    for i in x:
        if i.isalpha():
           temp+=i.upper()
        else:
          if temp!="":
            words.append(temp)
          temp=""
    if temp!="":
        words.append(temp)
    words=set(words)
    return [i for i in words if len(i)<=5 and len(i)>=3]

def get_random_word(list_of_words:list)->str:
    return random.choice(list_of_words)

def save_word(word):
    with open("word","w") as f:
        f.write(word)

def get_word():
    with open("word","r") as f:
        return f.read()

def remove_from_l(char:str,list_1:list)->list:
    for i in range(len(list_1)):
        if char == list_1[i]:
            list_1.pop(i)
            break
