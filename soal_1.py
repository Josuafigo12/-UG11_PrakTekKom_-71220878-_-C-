def penjumlahan(bilangan_pertama,bilangan_kedua):
    penjumlahan = bilangan_pertama + bilangan_kedua
    return penjumlahan
def pengurangan(bilangan_pertama,bilangan_kedua):
    pengurangan = bilangan_pertama - bilangan_kedua
    return pengurangan
def perkalian(bilangan_pertama,bilangan_kedua):
    pembaguan = bilangan_pertama * bilangan_kedua
    return perkalian
def pembagian(bilangan_pertama,bilangan_kedua):
    pembagian = bilangan_pertama / bilangan_kedua
    return pembagian

print("====================")
print("1. penjumlahan [+]")
print("2. pengurangan [-]")
print("3. perkalian [*]")
print("4. pembagian [/]")
print("====================")
operasi = (input("pilih operasi (1/2/3/4) :"))
bilangan_pertama = int(input("masukan bilangan pertama :"))
bilangan_kedua = int(input("masukan bilangan kedua :"))
if operasi == "1":
    print("hasil dari operasi",bilangan_pertama,"+",bilangan_kedua,"=",penjumlahan(bilangan_pertama,bilangan_kedua))
elif operasi == "2":
    print("hasil dari operasi",bilangan_pertama,"-",bilangan_kedua,"=",penjumlahan(bilangan_pertama,bilangan_kedua))
elif operasi == "3":
    print("hasil dari operasi",bilangan_pertama,"*",bilangan_kedua,"=",penjumlahan(bilangan_pertama,bilangan_kedua))
elif operasi == "4":
    print("hasil dari operasi",bilangan_pertama,"/",bilangan_kedua,"=",penjumlahan(bilangan_pertama,bilangan_kedua))

