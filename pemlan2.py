class kendaraan:
    def __init__(self, nama, warna, harga):
        self.nama = nama
        self.warna = warna
        self.harga = harga

    def tampilkan(self):
            print("Rincian: ",self.nama, self.warna, self.harga)

    def kecepatanmaxpertama(self):
            print("kecepatan maximum kendaraan: ", self.nama, "adalah 150km/jam")

    def gantigearpertama(self):
            print("Gantigear maximum kendaraan adalah sampai 6 ")


#childern class   
class Mobil(kendaraan):
    def kecepatanmaxkedua(self):
        print("kecepatan maximum kendaraan:", self.nama, "adalah 200km/jam")

    def gamtigearkedua(self):
        print("gantigear maximum kendaraan adalah sampai 7")

#memanggil fungsi dari parent class kendaraan 
Avanza = Mobil("Avanza", "Putih", 200000000)
Avanza.tampilkan()
Avanza.kecepatanmaxpertama()
Avanza.gantigearpertama()

#memanggil fungsi dari parent class kendaraan  dan childern class mobil
Jeep = Mobil("jeep", "coklat", 300000000)
Jeep.tampilkan()
Jeep.kecepatanmaxpertama()
Jeep.gantigearpertama()

