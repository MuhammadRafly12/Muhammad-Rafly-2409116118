harga = int(input("Masukkan harga barang :"))
jumlah = int(input("Masukkan jumlah barang :"))

total = harga * jumlah 

if total >= 250000:
    potongan = total * 0.25
    set_potongan = total - potongan
    print("total harga: Rp", total)
    print("Mendapat diskon 25% Menjadi:", set_potongan)
else:
    print("Total harga: Rp.", total)