from abc import ABC, abstractmethod

class Mobil(ABC):
    def fasilitas(self):
        pass
    def kecepatan(self):
        pass
    def harga(self):
        pass
    def kekuatan(self):
        pass

class BMW(Mobil):
    def fasilitas(self):
        return "Interior mewah dengan bahan premium"
    def kecepatan(self):
        return " 250 km/jam"
    def harga(self):
        return "Rp 900 juta hingga Rp 1,5 miliar"
    def kekuatan(self):
        return "Tenaga berkisar dari 184 hp "
    
class Avanza(Mobil):
    def fasilitas(self):
        return "Interior yang fungsional dan nyaman"
    def kecepatan(self):
        return " 180 km/jam"
    def harga(self):
        return "Rp 200 juta hingga Rp 250 juta"
    def kekuatan(self):
        return "Tenaga sekitar 104 hp pada mesin 1.5L"
    
class Ferrari(Mobil):
    def fasilitas(self):
        return "Interior mewah dengan kulit premium"
    def kecepatan(self):
        return " 330 km/jam"
    def harga(self):
        return "Rp 10 miliar hingga Rp 15 miliar"
    def kekuatan(self):
        return "Tenaga sekitar 661 hp pada mesin V8 3.9L twin-turbo"

    
def kelebihan_mobil(mobil: Mobil):
    print(f"Fasilitas: {mobil.fasilitas()}")
    print(f"Kecepatan: {mobil.kecepatan()}")
    print(f"Harga: {mobil.harga()}")
    print(f"Kekuatan: {mobil.kekuatan()}")

bmw = BMW();
avanza = Avanza();
ferrari = Ferrari();

print("BMW")
kelebihan_mobil(bmw);
print()
print("Avanza")
kelebihan_mobil(avanza);
print()
print("Ferrari")
kelebihan_mobil(ferrari);
