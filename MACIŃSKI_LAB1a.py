# Fabian Maciński KY2S1
from __future__ import print_function

def publickey(g,p,key):
    publickey = (g^key)%p
    return publickey

def generator():
    p = previous_prime(2^b)
    n = (p-1)/2
    while is_prime(n):
        p = previous_prime(p)
        n = (p-1)/2
    return n,p

# ustalenie wartosci b
b = 42
# znalezienie liczby pierwszej mniejszej od 2^b oraz sprawdzenie czy jest liczba pierwsza
n,p=generator()
print("Czy liczba ", p, "jest liczba pierwsza", is_prime(p))
print("Rzad podgrupy cyklicznej n: ", n)
# zainicjowanie ciała GF(p)
F = GF(p)
# wylosowanie kluczy tajnych
Firstkey = F.random_element()
Secondkey = F.random_element()
print("Klucze prywatne: ", Firstkey, Secondkey)
# utworzenie publicznej podstawy
g = F.primitive_element()
print("Podstawa podgrupy cyklicznej g: ", g)
# Utworzenie kluczy publicznych
Firstpublic = publickey(g,p,Firstkey)
Secondpublic = publickey(g,p,Secondkey)
print("Klucze publiczne: ", Firstpublic, Secondpublic)
# Utworzenie klucza tajnego
Firstanswer = publickey(Secondpublic,p,Firstkey)
Secondanswer = publickey(Firstpublic,p,Secondkey)
print("Klucz tajny: ", Firstanswer, Secondanswer)
print("Klucze sa takie same") if Firstanswer == Secondanswer else print("Klucze sa rozne")
