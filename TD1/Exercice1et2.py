tirage = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']
mots_possibles = ['sacre', 'sabre', 'baser', 'cabre', 'garce', 'crase', 'brase', 'barge', 'caser', 'jaser', 'crabe', 'scare', 'aber', 'gare', 'sage', 'gars', 'rase', 'arec', 'acre', 'jars', 'case', 'base', 'cage', 'rage', 'jase', 'bras', 'race', 'ars', 'sac', 'arc', 'are', 'jar', 'jas', 'bar', 'bas', 'ace', 'cas', 'car', 'age', 'bac', 'cab', 'as', 'ra', 'sa', 'a']

def motlepluslong(tirage,mots_possibles):
    mot=mots_possibles[0]
    n=len(mots_possibles)
    for i in range (1,n):
        if len (mots_possibles[i]) > len(mot):
            for lettres in mots_possibles[i]:
                if lettres in tirage:
                        mot=mots_possibles[i]
    return mot

#print(motlepluslong(tirage,mots_possibles))

available_words=[]
file= open("frenchssaccent.dic",'r')
for ligne in file:
     available_words.append(ligne[0:len(ligne)-1])
file.close()

print(motlepluslong(tirage,file))
