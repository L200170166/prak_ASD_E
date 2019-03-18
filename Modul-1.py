#L200170166
#1
def cetakSiku(x):
  for i in range(x+1):
     for j in range(i):
        print('*', end='')
     print()
cetakSiku(5)
print( )
print( )
#2
def gambarlahPesegiEmpat(a,b):
    i=1
    print("@"*b)
    while(i<a):
       print("@"+" "*(b-2)+"@")
       i+=1
    print("@"*b)
gambarlahPesegiEmpat(4,5)
print( )
print( )
#3
def jumlahHurufVokal(a):
    v="aiueoAIUEO"
    vokal=0
    jumlahhuruf=0
    for i in a:
        jumlahhuruf+=1
        if i in v:
            vokal+=1
    return (jumlahhuruf,vokal)
print(jumlahHurufVokal("Surakarta"))
def jumlahHurufKonsonan(a):
    v="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnopqrstvwxyz"
    konsonan=0
    jumlahhuruf=0
    for i in a:
        jumlahhuruf+=1
        if i in v:
            konsonan+=1
    return (jumlahhuruf,konsonan)
print(jumlahHurufKonsonan("Surakarta"))
print( )
print( )
#4
def rerata(b=[]):
    x=0
    n=0
    if b != []:
        for i in b:
            x+=i
            n+=1
        return x/n
    return "illegal"
print(rerata([2,2]))
print( )
print( )
#5
from math import sqrt as sq
def apakahPrima(n):
    n=int(n)
    assert n>=0
    primaKecil=[2, 3, 5, 7, 11]
    bukanPrima=[0, 1, 4, 6, 8, 9, 10]
    if n in primaKecil:
        return True
    elif n in bukanPrima:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if(n%i==0):
                return False
    return True
print(apakahPrima(17))
print(apakahPrima(97))
print(apakahPrima(123))
print( )
print( )
#6
def cetakBilanganPrima():
    prima=list()
    for i in range(2,100):
        a = True
        for iter in prima:
            if(i%iter==0):
                a=False
                break
        if(a):
            print(i)
            prima.append(i)
cetakBilanganPrima()
print( )
print( )
#7
def faktorPrima(n):
    prima=list()
    for i in range(2,n):
        a = True
        for iter in prima:
            if(i%iter==0):
                a=False
                break
        if a and n%i==0:
            prima.append(i)
    return prima
print(faktorPrima(10))
print(faktorPrima(120))
print(faktorPrima(19))
print( )
print( )
#8
def apakahTerkandung(a,b):
    return a in b
print(apakahTerkandung("do","Indonesia tanah air beta"))
print(apakahTerkandung("pusaka","Indonesia raya"))
print( )
print( )
#9
def iterasi():
    for i in range(1,100):
        if (i%3)!=0 and (i%5)!=0:
            print(i)
        else:
            if (i%15)==0:
                print("Python UMS")
            elif (i%3)==0:
                print("Python")
            elif (i%5)==0:
                print("UMS")
iterasi()
print( )
print( )
#10
def selesaikanABC(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    D=(b**2)-(4*a*c)
    if D<0:
        return "determinan negatif"
    return  "determinan positif"
print(selesaikanABC(1,2,3))
print( )
print( )
#11
def apakahKabisat(a):
    if(a%400==0):
        return True
    if(a%100==0):
        return False
    if(a%4==0):
        return True
    return False
print(apakahKabisat(100))
print( )
print( )
#12
import random
def permainan():
    a=random.randrange(0, 100)
    while(True):
        b=int(input("Masukan angka: "))
        if(b>a):
            print("Angka ini terlalu besar, Coba lagi!")
        elif(b<a):
            print("Angka ini terlalu kecil, Coba lagi!")
        else:
            print("Ya, Anda Benar")
            break
permainan()
print( )
print( )
#13
def katakan(a):
    x={"0":"","1":"Se","2":"Dua ","3":"Tiga ","4":"Empat ","5":"Lima ","6":"Enam ","7":"Tujuh ","8":"Delapan ","9":"Sembilan "}
    y={-1:"",-2:"puluh ",-3:"ratus ",-4:"ribu ",-5:"puluh ",6:"ratus ",7:"juta ",8:"puluhjuta "}
    b=str(a)
    c=""
    i=-1
    while i>= -len(b):
        c=x[b[i]]+y[i]+c
        i-=1
    return c
print(katakan(123))
print( )
print( )
#14
def formatRupiah(a):
    b=str(a)
    c=""
    i = -1
    while i>= -len(b):
        if((i+1)%3==0 and (i+1)!=0):
            c="."+c
        c=b[i]+c
        i-=1
    return "Rp "+c
print(formatRupiah(1500))
print(formatRupiah(2560000))
