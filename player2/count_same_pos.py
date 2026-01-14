
#counts the number of same positions chars between two words
def count_same_pos(word1: str, word2: str) -> int:
    count=0
    for i in range(len(word1)):
        if word1[i]==word2[i]:
            count+=1
    return count

# filters the list of candidats by keeping only those that have the same number  of same positions as given
def filter_candidats(candidats: list, word: str, num: int) -> list:
    new_candidats=[]
    for i in candidats:
        diff=count_same_pos(i,word)
        if diff==num:
            new_candidats.append(i)
    return new_candidats
