#a module that helps with text processing
import random

#simplifies the text by removing any non-alphabetic characters and making all letters uppercase
#it also removes duplicates and only keeps words with length between 3 and 5
def simplefy_text(text: str) -> list:
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
    return [i for i in words if len(i)<=5 and len(i)>=3] #find all words with length between 3 and 5

#gets a list of words and returns a random word from the list
def get_random_word(list_of_words:list)->str:
    return random.choice(list_of_words)

#saves the given word to a file called "word"
def save_word(word: str) -> None:
    with open("word","w") as f:
        f.write(word)

#retrieves the saved word from the file "word"
def get_word() -> str:
    with open("word","r") as f:
        return f.read()

