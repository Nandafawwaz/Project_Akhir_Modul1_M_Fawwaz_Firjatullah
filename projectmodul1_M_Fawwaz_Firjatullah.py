# M Fawwaz Firjatullah

dictMobil = {
    1001: {'nama': 'Nissan R34 GT-R', 'tahun': 1999, 'warna': 'Biru', 'stock': 4, 'harga': 100000},
    1002: {'nama': 'Lamborghini Huracan', 'tahun': 2014, 'warna': 'Hijau', 'stock': 7, 'harga': 115000},
    1003: {'nama': 'Porsche 911 GT3 RS', 'tahun': 2016, 'warna': 'Putih', 'stock': 5, 'harga': 200000},
    1004: {'nama': 'Toyota Supra', 'tahun': 1994, 'warna': 'Merah', 'stock': 2, 'harga': 78000},
    1005: {'nama': 'Acura Integra Type-R', 'tahun': 1997, 'warna': 'Kuning', 'stock': 12, 'harga': 5000},
    1006: {'nama': 'Toyota Corolla AE86', 'tahun': 1984, 'warna': 'Putih', 'stock': 3, 'harga': 8000},
    1007: {'nama': 'Mitsubishi Lancer Evo VIII', 'tahun': 2003, 'warna': 'Hitam', 'stock': 9, 'harga': 10000},
    1008: {'nama': 'Mazda RX-7', 'tahun': 1979, 'warna': 'Orange', 'stock': 15, 'harga': 13000},
    1009: {'nama': 'Subaru WRX', 'tahun': 2002, 'warna': 'Biru', 'stock': 4, 'harga': 9500},
    1010: {'nama': 'Ferrari F40', 'tahun': 1987, 'warna': 'Merah', 'stock': 2, 'harga': 1000000}
}

def tampilkanMobil():
    print(f"|{'ID':<5}|{'Nama':<30}| {'Tahun':<6} | {'Warna':<10} | {'Stock':<5} | {'Harga':<8}")
    for id, data in dictMobil.items():
        print(f"|{id:<5}|{data['nama']:<30}| {data['tahun']:<6} | {data['warna']:<10} | {data['stock']:<5} | {data['harga']:<8}")

def tambahMobil():
    while True:
        id = int(input("Masukkan ID baru: "))
        if id in dictMobil:
            print("ID sudah ada! Masukkan ID yang unik.")
        else:
            break

    nama = input("Masukkan Nama Mobil: ")
    while True:
        tahun = int(input("Masukkan Tahun Mobil: "))
        if tahun < 1886 or tahun > 2025:
            print("Tahun tidak valid. Harus antara 1886 - 2025.")
        else:
            break
    warna = input("Masukkan Warna Mobil: ")
    stock = int(input("Masukkan Stock Mobil: "))
    harga = int(input("Masukkan Harga Mobil: "))

    dictMobil[id] = {
        'nama': nama,
        'tahun': tahun,
        'warna': warna,
        'stock': stock,
        'harga': harga
    }

    print("Mobil berhasil ditambahkan.")
    tampilkanMobil()

def hapusMobil():
    id = int(input("Masukkan ID mobil yang ingin dihapus: "))
    if id in dictMobil:
        del dictMobil[id]
        print(f"Mobil dengan ID {id} berhasil dihapus.")
    else:
        print("ID tidak ditemukan.")
    tampilkanMobil()

def updateMobil():
    id = int(input("Masukkan ID mobil yang ingin diupdate: "))
    if id in dictMobil:
        print(f"Mobil ditemukan: {dictMobil[id]['nama']}")
        print("Apa yang mau diupdate?\n1. Warna\n2. Harga\n3. Stock")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == '1':
            warnaBaru = input("Masukkan warna baru: ")
            dictMobil[id]['warna'] = warnaBaru
            print("Warna berhasil diupdate.")
        elif pilihan == '2':
            hargaBaru = int(input("Masukkan harga baru: "))
            dictMobil[id]['harga'] = hargaBaru
            print("Harga berhasil diupdate.")
        elif pilihan == '3':
            stockBaru = int(input("Masukkan stock baru: "))
            dictMobil[id]['stock'] = stockBaru
            print("Harga berhasil diupdate.")
        else:
            print("Pilihan tidak valid.")
    else:
        print("ID tidak ditemukan.")
    tampilkanMobil()

def beliMobil():
    cart = []
    while True:
        tampilkanMobil()
        idMobil = int(input("Masukkan ID mobil yang ingin dibeli (0 untuk selesai): "))
        if idMobil == 0:
            break
        if idMobil not in dictMobil:
            print("ID mobil tidak ditemukan.")
            continue

        stock_Mobil = dictMobil[idMobil]['stock']
        if stock_Mobil <= 0:
            print("Stock habis.")
            continue

        while True:
            jumlah = int(input("Jumlah mobil yang ingin dibeli: "))
            if jumlah <= stock_Mobil:
                break
            else:
                print("Stock tidak mencukupi.")

        nama_Mobil = dictMobil[idMobil]['nama']
        warna_Mobil = dictMobil[idMobil]['warna']
        harga_Mobil = dictMobil[idMobil]['harga']

        cart.append({'id': idMobil, 'nama': nama_Mobil, 'warna': warna_Mobil, 'jumlah': jumlah, 'harga': harga_Mobil})
        print(f"{jumlah} {nama_Mobil} ditambahkan ke keranjang.")

    if not cart:
        print("Keranjang kosong.")
    else:
        print("=== Daftar Belanja ===")
        print(f"|{'ID':<5}|{'Nama':<30}| {'Warna':<10} | {'Jumlah':<6} | {'Harga':<8} | {'Subtotal':<10}")
        total = 0
        for item in cart:
            subtotal = item['jumlah'] * item['harga']
            print(f"|{item['id']:<5}|{item['nama']:<30}| {item['warna']:<10} | {item['jumlah']:<6} | {item['harga']:<8} | {subtotal:<10}")
            total += subtotal
        print(f"Total yang harus dibayar: {total}")

        while True:
            uang = int(input("Masukkan jumlah uang: "))
            if uang < total:
                print(f"Uangnya kurang sebesar: {total - uang}")
            else:
                print("Terima kasih sudah berbelanja!")
                if uang > total:
                    print(f"Uang kembalian Anda: {uang - total}")
                break

        for item in cart:
            dictMobil[item['id']]['stock'] -= item['jumlah']


def menuUtama():
    while True:
        pilih = input('''
=== MENU UTAMA ===
1. Daftar Mobil
2. Tambah Mobil Baru
3. Hapus Mobil
4. Update data Mobil
5. Beli Mobil
6. Keluar
Masukkan pilihan: ''')
        if pilih == '1':
            tampilkanMobil()
        elif pilih == '2':
            tambahMobil()
        elif pilih == '3':
            hapusMobil()
        elif pilih == '4':
            updateMobil()
        elif pilih == '5':
            beliMobil()
        elif pilih == '6':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

menuUtama()