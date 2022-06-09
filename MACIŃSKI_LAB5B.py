# Fabian Maciński KY2S1
from __future__ import print_function
import random

def genprime():
    temp = next_prime(random.randint(0,200))
    while temp % 4 != 3:
        temp = next_prime(random.randint(0,200))
    return temp

#-------------KROK 1---------------
#Uzytkownik A generuje liczbe Bluma n oraz x
#Generowanie p oraz q
p = genprime()
q = genprime()
print("Wygenerowane p i q:", p, q)
#Wyliczenie wartosci n
n = p * q
print("Uzytkownik A wygenerowal wartosc n:", n)
#Wylosowanie wartosci x wzglednie pierwszej z n
x = random.randint(0,3000)
while gcd(n,x)==1:
    x = random.randint(0,3000)
print("Uzytkownik A wygenerowal wartosc x:", x)

#-------------KROK 2---------------
#Uzytkownik A tworzy x0 i x1
x0 = (x^2) % n
x1 = (x0^2) % n
print("Wynik x0 i x1:",x0, x1)
#Uzytkownik A wysyla uzytkownikowi B wartosc n i x1
print("Uzytkownik A wysyla wartosc n i x1 do uzytkownika B:", n, x1)

#-------------KROK 3---------------
#Uzytkownik B odgaduje wartosc x0
pick = random.randint(0,1)
print("Uzytkownik B zgaduje, ze liczba x0 jest parzysta") if pick == 0 else print("Uzytkownik B zgaduje, ze liczba x0 jest nieparzysta")

#-------------KROK 4---------------
#Uzytkownik A wysyla uzytkownikowi B wartosc x oraz x0
print("Uzytkownik A wysyla wartosc x i x0 do uzytkownika B:", x, x0)

#-------------KROK 5---------------
#Użytkownik A wysyła czynniki do Użytkownika B
print("Uzytkownik A przesyla czynniki liczby n:", p, q)
#Uzytkownik B sprawdza czy n jest liczba calkowita Bluma
if p * q == n and p % 4 == 3 and q % 4 == 3 and p.is_prime() and q.is_prime():
    print("Liczba n jest liczba Bluma")
    test1 = true
else:
    print("Uzytkownik B zostal oszukany, liczba n nie jest liczba Bluma")
    test1 = false
#Uzytkownik B sprawdza czy x0 = x^2 (mod n) oraz x1 = x0^2 (mod n)
if x^2 % n == x0:
    print("Wartosc x0 zostala obliczona prawidlowo")
    test2 = true
else:
    print("Wartosc zostala obliczona niepoprawnie")
    test2 = false
if x0^2 % n == x1:
    print("Wartosc x1 zostala obliczona prawidlowo")
    test3 = true
else:
    print("Wartosc zostala obliczona niepoprawnie")
    test3 = false
#Sprawdzamy czy wszystko zostalo dobrze wyznaczone, jesli tak podajemy wynik rzutu moneta
if test1 == true and test2 == true and test3 == true:
    if x0 % 2 == 0 and pick == 0:
        print("Wylosowana wartosc to Orzel")
    elif x0 % 2 == 1 and pick == 1:
        print("Wylosowana wartosc to Orzel")
    else:
        print("Wylosowana wartosc to Reszka")
else:
    print("Wartosc x0, x1 lub liczba Bluma nie sa poprawne")