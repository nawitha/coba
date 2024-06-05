class Manusia:
    def __init__(self, nama, asal, penghasilan):
        self.nama = nama
        self.asal = asal
        self.penghasilan = penghasilan

    def tampilkan(self):
        print("Rincian: ",self.nama, self.asal, self.penghasilan)
    def biodatapertama(self):
        print("nama saya ", self.nama)
    def asalpertama(self):
        print("asal saya dari", self.asal)
    def hasilpertama(self):
        print("penghasilan saya sekitar ", self.penghasilan, "ribu")


#childern class   
class tentara(Manusia):
    def biodatakedua(self):
        print("nama saya ", self.nama)
    def asalkedua(self):
        print("asal saya dari", self.asal)
    def tugas1(self):
        print("saya adalah seorang tentara")
    def hasilkedua(self):
        print("penghasilan saya sekitar ", self.penghasilan, "rupiah")

class Dokter(Manusia):
    def biodataketiga(self):
        print("nama saya ", self.nama)
    def asalketiga(self):
        print("asal saya dari", self.asal)
    def tugas2(self):
        print("saya adalah seorang Dokter")
    def hasilketiga(self):
        print("penghasilan saya sekitar ", self.penghasilan, "rupiah")

class Petani(Manusia):
    def biodatakeempat(self):
        print("nama saya ", self.nama)
    def asalkeempat(self):
        print("asal saya dari", self.asal)
    def tugas3(self):
        print("saya adalah seorang Petani")
    def hasilkeempat(self):
        print("penghasilan saya sekitar ", self.penghasilan, "rupiah")


#memanggil fungsi dari parent class kendaraan 
Tentara = tentara("MIngyu", "Malang", 20000000)
Tentara.tampilkan()
Tentara.biodatapertama()
Tentara.asalpertama()
Tentara.tugas1()
Tentara.hasilkedua()

print()

dokter = Dokter("Wonwoo", "Surabaya", 30000000)
dokter.tampilkan()
dokter.biodataketiga()
dokter.asalketiga()
dokter.tugas2()
dokter.hasilketiga()

print()

petani = Petani("Vernon", "Pasuruan", 10000000)
petani.tampilkan()
petani.biodatakeempat()
petani.asalkeempat()
petani.tugas3()
petani.hasilkeempat()



