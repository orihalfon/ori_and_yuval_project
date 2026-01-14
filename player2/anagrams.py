def generate_anagrams(word):
    lst=[]
    rec(word,len(word),lst)
    return lst

def rec(word,l,lst,x=""):
    if len(x)==l:
        lst.append(x)
        return
    for i in range(len(word)):
        rec(word[:i]+word[i+1:],l,lst,x+word[i])


# x=set(generate_anagrams("abcdefgh"))
# print(len(x))