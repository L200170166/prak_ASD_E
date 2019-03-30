from fgh import Mahasiswa
import sys
a=Mahasiswa('Alan',210,'Magelang',213000)
b=Mahasiswa('Telo',737,'Sarangan',321000)
c=Mahasiswa('Markonah',242,'Slumbung',120000)
d=Mahasiswa('Item',864,'Udel',540000)
e=Mahasiswa('Yonglex',243,'Dadapan',720000)
f=Mahasiswa('Pino',123,'Gladak',110000)
g=Mahasiswa('Usri',234,'Kleco',320000)
h=Mahasiswa('Helda',312,'Suronatan',230000)
i=Mahasiswa('Freya',180,'Sukoharjo',123000)
j=Mahasiswa('Unto',314,'Solo',120000)

mahasiswa = [a,b,c,d,e,f,g,h,i,j]

def urutkan(A):
    baru = {}
    for i in range(len(A)):
        baru[A[i].nama] = A[i].NIM
    listofTuples = sorted(baru.items(), key=lambda x: x[1])
    for elem in listofTuples :
        print(elem[0] , ":" , elem[1] )

urutkan(mhss)
