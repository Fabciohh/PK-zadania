# FABIAN MACIŃSKI WCY20KY2S1 zad 2a
from __future__ import print_function
import hmac
import hashlib
import binascii
import random
#hashlib.algorithms_guaranteed

# Funkcja wykonujaca hmac
def function(word,keyh):
    temp = hmac.new(keyh,word.encode(),hashlib.sha3_512)
    code = temp.hexdigest()
    return code

# Funkcja porownujaca wartosci
def comparision(word1,word2):
    if(word1 == word2): 
        print("Wartosci sa rowne")
    else:
        print("Wartosci nie sa rowne")


# Generuje klucz
key = "1234567890ABCDEF"
keyh = binascii.unhexlify(key)
# Nazwyy uzytkownikow
UserA = "Agata"
UserB = "Bartosz"

#-------Krok 1---------
# Generujemy liczbe losowa Rand_A
Rand_A = random.randint(0,1500)

#-------Krok 2---------
# Generujemy liczbe losowa Rand_B
Rand_B = random.randint(0,1500)
# Laczymy 2 wylosowane wartosci wraz z nazwa uzytkownika B
connect_wordB = str(Rand_A) + str(Rand_B) + UserB
# Wykonujemy kodowanie
hmackB = function(connect_wordB,keyh)
print("Wynik HMACK(RandA,RandB,B) dla Uzytkownika B",hmackB)
# Wysylamy wynik do uzytkownika A

#-------Krok 3---------
# Uzytkownik A wykonuje kodowanie i porownuje wartosci
# Laczymy 2 wylosowane wartosci wraz z nazwa uzytkownika B
connect_wordB2 = str(Rand_A) + str(Rand_B) + UserB
# Wykonujemy kodowanie
hmackBtest = function(connect_wordB2,keyh)
print("Wynik HMACK(RandA,RandB,B) dla Uzytkownika A",hmackBtest)
# Porownujemy wartosci hmack
comparision(hmackB,hmackBtest)
# Laczymy wylosowana wartosc uzytkownika B z nazwa uzytkownika A
connect_wordA = str(Rand_B) + UserA
# Wykonujemy kodowanie hmack(Rand_B,A)
hmackA = function(connect_wordA,keyh)
print("Wynik HMACK(RandB,A) dla Uzytkownika A",hmackA)
# Wysylamy wynik do uzytkownika B

#-------Krok 4---------
# Uzytkownik B wykonuje kodowanie i porownuje wartosci
# Laczymy wylosowana wartosc uzytkownika B z nazwa uzytkownika A
connect_wordA2 = str(Rand_B) + UserA
# Wykonujemy kodowanie hmack(Rand_B,A)
hmackAtest = function(connect_wordA2,keyh)
print("Wynik HMACK(RandB,A) dla uzytkownika B",hmackAtest)
# Porownujemy wartosci hmack
comparision(hmackA,hmackAtest)