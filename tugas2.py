#no1
kendaraan=["B 564 yu", "Yamaha", "160", "biru"]
#no2
kendaraan.append("RP.19.000.000")
kendaraan.append(2)
kendaraan.insert(2, "Honda")
kendaraan.insert(3, "CB150R")
print (kendaraan)
#no3
#3 buat program dengan bahasa pyhton dengan match case untuk menghitung luas bangun datar 
luas= input("Masukan luas (1. persegi, 2. lingkaran, 3. segitiga)")

match luas:
    case "1"|"persegi":
        sisi=int(input("masukan nilai sisi persegi"))
        luas=sisi*sisi
        print(luas) 
    case "2"|"lingkaran":
        jarijari=int(input("masukan nilai jarijari"))
        luas=3.14*jarijari**2
        print(luas)
    case "3"|"segitiga"|"segitiga":
        alas=int(input("masukan nilai alas:"))
        tinggi=int(input("masukan nilai tinggi:"))
        luas=alas*tinggi/2
        print(luas)
    case _:
        print("coba lagi")