from abc import ABC, abstractmethod

class Perpustakaan(ABC):
    @abstractmethod
    def Harga(self):
        pass

class Buku(Perpustakaan):
    def _init_(self, penulis, genre):
        self.penulis = penulis
        self.genre = genre

    def databuku(self):
        print("Buku ini ber genre:", self.genre, "dan nama penulisnya:", self.penulis)

    def Harga(self):
        return 50.000

class Majalah(Perpustakaan):
    def _init_(self, penerbit, tgl_terbit):
        self.penerbit = penerbit
        self.tgl_terbit = tgl_terbit

    def datamajalah(self):
        print("Majalah ini diterbitkan oleh:", self.penerbit, "dan diterbitkan pada:", self.tgl_terbit)

    def Harga(self):
        return 25.000

buku = Buku("Firda Febiola", "Fiksi Ilmiah")
buku.databuku()
buku.Harga()
print("Harga Buku:", buku.Harga())

majalah = Majalah("Febiola Firda", "2024-05-15")
majalah.Harga()
majalah.datamajalah()
print("Harga Majalah:", majalah.Harga())