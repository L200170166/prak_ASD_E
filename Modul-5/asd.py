class Manusia(object):
    """Class manusia dengan inisiasi 'nama'"""
    keadaan='Hungry'
    def __init__(self,nama):
        self.nama = nama
    def ucapSalam(self):
        print("Hello my name: ", self.nama)
    def makan(self,s):
        print("I'm just ate ", s)
        self.keadaan = 'Satisfied'
    def olah(self,k):
        print("I'm just got training", k)
        self.keadaan='Hungry'
    def kali(self,n):
return n*2
