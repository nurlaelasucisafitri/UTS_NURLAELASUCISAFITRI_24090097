jumlah_barang = int(input("Masukkan jumlah barang: "))
harga_barang_1 = float(input("Masukkan harga barang ke-1: "))
harga_barang_2 = float(input("Masukkan harga barang ke-2: "))
total_belanjaan = (jumlah_barang * harga_barang_1) + (jumlah_barang * harga_barang_2)
print(f"Total belanjaan Anda adalah: Rp {total_belanjaan:,.2f}")