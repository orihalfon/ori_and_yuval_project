#gets a word and returns a list of all anagrams of that word
def generate_anagrams(word:str)-> list: 
    lst=[]
    rec(word,lst)
    return lst

# helps generate_anagram
def rec(word:str,lst:list,x="":str)->None:
    if len(word)==0:
        lst.append(x)
        return
    for i in range(len(word)):
        rec(word[:i]+word[i+1:],lst,x+word[i])


# x=set(generate_anagrams("abcdefgh"))
# print(len(x))