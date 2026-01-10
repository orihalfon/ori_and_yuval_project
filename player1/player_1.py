from player1.text_helper import save_word, simplefy_text, get_word, get_random_word, remove_from_l

def start_game():
    text="/Users/orihalfon/PycharmProjects/ori_and_yuval_project/player1/story"
    new_text = simplefy_text(text)
    word = get_random_word(new_text)
    save_word(word)

def evaluate (guess:str,word:str)->int:
    num = 0
    for i in range (len(word)):
        if guess[i]==word[i]:
            num+=1
    return num

def ret_len():
    return len(get_word())

def send_word(word):
    og_word=get_word()
    return min_change_anagram(word, og_word)

def ask_answer(word):
    og_word=get_word()
    return evaluate(word, og_word)

def min_change_anagram(guess: str, real_w: str) -> str:
    #נייצר שני רשימות של מילת המטרה
    list_1 = list(real_w)
    list_2 = list(real_w)
    #
    for char in guess:
        if char in list_1:
            remove_from_l(char,list_1)

    res = ""
    for char in guess:
        if char not in list_2 :
            res+=list_1[0]
            remove_from_l(list_1[0],list_2)
            list_1.pop(0)
        else:
            res+=char
            remove_from_l(char,list_2)
    return res