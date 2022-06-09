# Fabian Maciński KY2S1
from __future__ import print_function

def arraygenerate(k,a):
#generuje losowe wartosci dla a(i)
    for i in range(0, k-1):
        temp = F.random_element()
        a.append(temp)
    return a

def fun_f_gen(k,a,M):
#tworze wielomian f
    f = M
    for i in range(1,k):
        f=a[k-1-i]*x**(i)+f
    print("Otrzymany wielomian:")
    return f

def decoding(l,F,k,n):
    B=vector(F,l)
    print("Utworzony wektor B: ")
    print(B)
    A=zero_matrix(F,k,k)
    for i in range (0,k):
        A[i,k-1]=1
    for i in range (0,k):
        for j in range (0,k):
            A[i,j]=(i+1)**(j)
    print("Macierz A:")
    print(A)
    Ainv=A.inverse()
    print("Transponowana macierz A:")
    print(Ainv)
    X=Ainv*B
    print("Wektor X:", X)
    return X


Message = 21
#pobieram wielkosc k i n od wielkosci wiadomosci
k = sys.getsizeof(Message)/16
n = (sys.getsizeof(Message)/16)*2
#generuje wartosc p po wartosci wiadomosci
p=next_prime(Message)
print("Nasze wartosci k=", k, "n=", n,"p=",p)
#tworze cialo proste
F=GF(p)
P.<x>=F[]
#alokuje pamiec dla a
a = []
print("Wylosowane wartosci a:")
#losowanie wartosci dla wspolczynnikow a
arraygenerate(k,a)
#tworze wielomian stopnia k-1
f=fun_f_gen(k,a,Message)
print(f)
#alokuje pamiec dla wynikow f(xi)
l = []
#wyznaczam cienie
print("Wysylanie cieni do uczestnikow:")
for i in range (0,k):
    l.append(f(i+1))
#wysylamwartosci do uczestnikow
    print("Uczestnik nr",i+1,"otrzymuje wartosc xi, li oraz p:",i+1,l[i],p)
#dekoduje wartosc M z l
X = decoding(l,F,k,n)
print("Wartosc M i odtworzona wartosc X[k-1] sa takie same") if X[0] == Message else print("Operacja nie udala sie")