from abc import ABC, abstractclassmethod
class Penerbit(ABC):
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang =  pengarang
        self.tahun_terbit = tahun_terbit
    @abstractclassmethod
    def TampilkanInfoPenerbit028(self): #kelas Abstrak
        pass
class Idbuku:
    def __init__(self, isbn):
        self.isbn = isbn
    def TampilkanIsbn028(self):
        return f"Isbn :{self.isbn}"
class Buku(Penerbit, Idbuku): #Multiple inheritance
    def __init__(self, isbn, judul, pengarang, tahun_terbit):
       Idbuku.__init__(self, isbn)
       Penerbit.__init__(self, judul, pengarang, tahun_terbit)
    def TampilkanInfoPenerbit028(self): #pemanggilan abstrac 
        return f"Judul Buku :{self.judul} \nPengarang :{self.pengarang} \nTahun Terbit :{self.tahun_terbit}"
    def __TampilkanInfoBuku028(self): #private method
        return f"{self.TampilkanIsbn028()} \n{self.TampilkanInfoPenerbit028()}"
    def AksesBuku028(self): #akeses private
        return self.__TampilkanInfoBuku028()
a = input("Masukkan Isbn Buku :")
b = input("Masukkan Judul Buku :")
c = input("Masukkan pengarang Buku :")
d = input("Masukkan tahun terbit Buku :")
buku1 = Buku(a, b, c, d)
print(buku1.AksesBuku028())
