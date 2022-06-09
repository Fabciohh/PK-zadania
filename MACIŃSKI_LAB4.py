# Fabian Maciński KY2S1
from __future__ import print_function
import random

#---Algorytm generacji podpisu---

#generujemy p, F, g oraz m
m = random.randint(0,1500)
temp = random.randint(0,1500)
p = next_prime(temp)
F=GF(p)
g = F.primitive_element()
#generujemy x oraz X
x = previous_prime(temp)
#gdy generuje x, ktory jest liczba pierwsza nwd(x,p-1) zawsze jest rowne 1
X = (g^x) % p
#Użytkownik A wyznacza podpis z
z = (m^x) % p
#X to klucz publiczny, wiec kazdy ma do niego dostep
print("Wartosc klucza prywatnego x: ", x)
print("Wiadomosc m: ",m)
print("Wartosc g: ",g)
print("Wartosc p: ",p)
print("Wyznaczony podpis przez uzytkownika A: ",z)
#---Protokół weryfikacji podpisu---

#-------------KROK 1---------------
#Użytkownik B losuje liczby a i b mniejsze od p
a=random.randint(1,p-1)
b=random.randint(1,p-1)
print("Wylosowane wartosci a i b", a, b)
#obliczamy c
c = ( m**a * g**b ) % p
print("Wartosc c: ", c)
print("Wysylamy wartosc c do uzytkownika A")
#--Użytkownik B wysyła do użytkownika A wynik obliczeń--
#--Użytkownik A i B zna p oraz g

#-------------KROK 2-----------------
#losujemy liczbe q
q = F.random_element()
print("wartosc q: ",q)
#Użytkownik A wykonuje obliczenia s1 oraz s2
s1 = (c * g^q) % p 
s2 = ((c*g^q)^x) % p
print("Obliczone wartosci s1 i s2 obliczone przez uzytkownika A", s1, s2)
#Uzytkownik A wysyla wynik s1 i s2 do uzytkownika B

#-------------KROK 3-----------------
#użytkownik b przesyłą wartość a i b do użytkownika A
#Użytkownik A sprawdza czy nie został oszukany
ctemp = (m^a * g^b) % p
print("Wartosc c obliczona przez uzytkownika A", ctemp)
print("Porownujemy wartosci obliczonych c")
print ("Uzytkownik A nie zostal oszukany") if c == ctemp else print("Uzytkownik A zostal oszukany")

#-------------KROK 4-----------------
#użytkownik A przesyła do użytkownika B wartość q oraz z
#użytkownik B oblicza s1_B i s2_B
s1_B = (c* g^q) % p
s2_B = (X^(b+q)*z^a) % p
print("Obliczone wartosci ^s1 i ^s2 przez uzytkownika B", s1, s2)
#porownujemy wartosci s1_B z s1 oraz s2_B z s2
print("Porownujemy wartosci s1, s2 z ^s1 i ^s2")
print("Wartosci sa takie same, podpis jest poprawny") if s1 == s1_B and s2 == s2_B else print("Wartosci sa rozne, podpis nie jest poprawny")