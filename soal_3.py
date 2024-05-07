def hitung_total_harga(jumlah_barang):
    total_harga = 0
    for i in range(jumlah_barang):
        harga_barang = float(input(f"Masukkan harga barang ke-{i+1}: "))
        total_harga += harga_barang
    return total_harga

jumlah_barang = int(input("Masukkan jumlah barang: "))
total_harga = hitung_total_harga(jumlah_barang)

print(f"Total harga belanjaan: Rp{total_harga}")