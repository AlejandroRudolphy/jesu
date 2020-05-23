import re
from unicodedata import normalize

def son_anagramas(string1,string2):
    s1 = string1.lower()
    s2 = string2.lower()
    str1 = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize("NFD", s1), 0, re.I)
    str2 = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize("NFD", s2), 0, re.I)
    diccionario1=dict()
    diccionario2=dict()

    for v in str1:
        if v not in diccionario1:
            diccionario1[v]=0
        diccionario1[v]+=1
    
    for r in str2:
        if r not in diccionario2:
            diccionario2[r]=0
        diccionario2[r]+=1
    anagrama=True
    if len(str1)==len(str2):
        for key in diccionario1: #por cada llave (letra) del diccionario1
            if key in (diccionario1.keys() and diccionario2.keys()): #primero corroborar que la letra este en ambos strings
                if diccionario1[key]==diccionario2[key]: #si esa letra esta la misma cantidad de veces
                    continue
                else: # si una letra no esta la misma cantidad de veces, no es anagrama
                    anagrama=False
                    break
            else: #si alguna letra no esta en ambos strings, no es anagrama
                anagrama=False
                break
    else: 
        anagrama=False


    return anagrama

string1 = 'qwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnm'
string2 = 'mnbvcxzasdfghjklpoiuytrewqmnbvcxzasdfghjklpoiuytrewqmnbvcxzasdfghjklpoiuytrewqmnbvcxzasdfghjklpoiuytrewqmnbvcxzasdfghjklpoiuytrewqmnbvcxzasdfghjklpoiuytrewqmnbvcxzasdfghjklpoiuytrewqmnbvcxzasdfghjklpoiuytrewqmnbvcxzasdfghjklpoiuytrewqmnbvcxzasdfghjklpoiuytrewqmnbvcxzasdfghjklpoiuytrewq'
s = son_anagramas(string1, string2)
print(s)