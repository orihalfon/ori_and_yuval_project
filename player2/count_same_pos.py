def count_same_pos(word1,word2):
    count=0
    for i in range(len(word1)):
        if word1[i]==word2[i]:
            count+=1
    return count

def filter_candidats(candidats,word,num):
    new_candidats=[]
    for i in candidats:
        diff=count_same_pos(i,word)
        if diff==num:
            new_candidats.append(i)
    return new_candidats
