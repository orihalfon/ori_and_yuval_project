from player1.text_helper import save_word, simplefy_text, get_word, get_random_word



#starts the game by getting a random word from the story and saving it
def start_game(file_name: str ) -> None:

    text="/Users/orihalfon/PycharmProjects/ori_and_yuval_project/player1/story"
    new_text = simplefy_text(file_name)
    word = get_random_word(new_text)
    save_word(word)


# asks the user for an answer and evaluates it against the saved word
def ask_answer(word: str) -> int: 
    og_word=get_word()
    return evaluate(word, og_word)



# evaluates the guess by comparing it to the real word and counting correct positions
def evaluate (guess:str,word:str)->int:
    num = 0
    for i in range (len(word)):
        if guess[i]==word[i]:
            num+=1
    return num


# returns the length of the saved word
def ret_len() -> int:
    return len(get_word())


# given a word, returns an anagram with minimal changes from the saved word
def send_word(word: str) -> str:
    og_word=get_word()
    return min_change_anagram(word, og_word)

#removes the first occurrence of char from list_1
def remove_from_l(char:str,list_1:list)->list:
    for i in range(len(list_1)):
        if char == list_1[i]:
            list_1.pop(i)
            break

# given a guess and the real word, returns an anagram of the real word
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
