import count_same_pos
import anagrams
import random

from player1.player_1 import start_game, ret_len, send_word, ask_answer

start_game()
length=ret_len()
word=input("write a word with length: "+str(length))
word=send_word(word)
candidats= anagrams.generate_anagrams(word)
answer=random.choice(candidats)
count=0
while len(candidats)!=1:
    count+=1
    # send to player1 word and get number
    num=ask_answer(answer)
    candidats= count_same_pos.filter_candidats(candidats, answer, num)
    answer=random.choice(candidats)
print(candidats)
print(count)
