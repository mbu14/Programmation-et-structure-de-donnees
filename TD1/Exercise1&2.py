#Exercise 1
draw = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']
possible_words = ['sacre', 'sabre', 'baser', 'cabre', 'garce', 'crase', 'brase', 'barge', 'caser', 'jaser', 'crabe', 'scare', 'aber', 'gare', 'sage', 'gars', 'rase', 'arec', 'acre', 'jars', 'case', 'base', 'cage', 'rage', 'jase', 'bras', 'race', 'ars', 'sac', 'arc', 'are', 'jar', 'jas', 'bar', 'bas', 'ace', 'cas', 'car', 'age', 'bac', 'cab', 'as', 'ra', 'sa', 'a']

import copy
def longest_word(draw,possible_words):
    word=possible_words[0]
    n=len(possible_words)
    available = {} #one use per letter of draw
    for letter in draw :
        if letter in available:
             available[letter]+=1
        available[letter]=1
    for i in range (1,n):
        if len (possible_words[i]) > len(word):
            m=len(possible_words[i])
            changing_available=copy.deepcopy(available)
            for letter in possible_words[i]:
                if letter not in changing_available:
                     break
                elif changing_available[letter]>=1:
                        changing_available[letter]=changing_available[letter]-1
                        m=m-1
            if m==0:
                word=possible_words[i]
    return word

print(longest_word(draw,possible_words))

#Exercise 2
available_words=[]
file= open('mots.sansaccent.txt','r')
for ligne in file:
     available_words.append(ligne[0:len(ligne)-1])
file.close()

#print (available_words)
print(longest_word(draw,available_words))

