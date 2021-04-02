import csv
import os

#buat file catatan pengeluaran
if not os.path.exists('Catatan.csv'):
    with open('Catatan.csv', 'w') as csv_file:
        akun = []
        fieldnames = ['HARI', 'BULAN', 'TAHUN', 'NOMOR', 'KETERANGAN', 'NOMINAL']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in akun:
            writer.writerow({'HARI': new_data['HARI'], 'BULAN': new_data['BULAN'], 'TAHUN': new_data['TAHUN'],
                            'NOMOR': new_data['NOMOR'], 'KETERANGAN': new_data['KETERANGAN'],
                            'NOMINAL': new_data['NOMINAL']})
#buat file akun buat login
if not os.path.exists('akun.csv'):
    with open('akun.csv', 'w') as csv_file:
        akun = []
        fieldnames = ['USERNAME', 'PASS']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in akun:
            writer.writerow(
                {'USERNAME': new_data['USERNAME'], 'PASSWORD': new_data['PASS']})

def bersihin_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

csv_filename = 'Catatan.csv'

#Menu utama
def liat_menu():
    bersihin_layar()
    print("-" * 42, "SELAMAT DATANG DI EXPENSE TRACKER!", 42 * "-")
    print("-" * 48, "Projek ini dibuat oleh", 48 * "-")
    print("-" * 36, "Kelompok 16 - IF A 20 - Universitas Mulawarman", 36 * "-")
    print("-" * 57, "MENU", 57 * "-")
    print(" " * 45, "[1] Lihat Daftar Pengeluaran", 45 * " ")
    print(" " * 45, "[2] Total Pengeluaran", 52 * " ")
    print(" " * 45, "[3] Tambah Pengeluaran", 51 * " ")
    print(" " * 45, "[4] Edit Pengeluaran", 53 * " ")
    print(" " * 45, "[5] Hapus Pengeluaran", 52 * " ")
    print(" " * 45, "[6] Cari Pengeluaran", 53 * " ")
    print(" " * 45, "[0] Exit", 65 * " ")
    print(" " * 120, )
    #imput unser memilih menu pakai str supaya user hanya bisa input angka
    selected_menu = str(input(" " * 54 + "Pilih MENU:"))

    if (selected_menu == "1"):
        liat_catatan()
    elif (selected_menu == "2"):
        total_pengeluaran()
    elif (selected_menu == "3"):
        buat_catatan()
    elif (selected_menu == "4"):
        edit_catatan()
    elif (selected_menu == "5"):
        hapus_catatan()
    elif (selected_menu == "6"):
        cari_catatan()
    elif (selected_menu == "0"):
        exit()
    else:
        print(" " * 45, "Kamu memilih menu yang salah")
        balik_menu()


def mulai():
    print("\n"*5)
    pilih = input(" " * 45 + "Apakah anda memilik akun?y/t : ")
    if (pilih == "y"):
        login()
    elif (pilih == "t"):
        buat_akun()
    else:
        print(" " * 120)
        print(" " * 48, "Pilihan hanya y atau t")
        print(" " * 120)
        mulai()


def buat_akun():
    bersihin_layar()
    csv_filename = 'akun.csv'

    with open(csv_filename, mode='a') as csv_file:
        fieldnames = ['USERNAME', 'PASS']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        print(" " * 55 + 'BUAT AKUN')
        print(" " * 47 + '_' * 26)
        u = (input(" " * 54 +"Username: "))
        p = (input(" " * 54 +"Password: "))
        print(" " * 47 + '_' * 26)
        print(" " * 46, "Berhasil disimpan!")
        print("\n")
        writer.writerow({'USERNAME': u, 'PASS': p})
    input(" " * 47 + "Tekan Enter untuk login...")
    login()


def login():
    bersihin_layar()
    csv_filename = 'akun.csv'
    akun = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akun.append(row)

    print('=' * 120)
    print("-" * 56, "LOGIN!", 56 * "-")
    print(" " * 55, "USERNAME", 55 * " ")
    u = input(" " * 56)
    print(' ' * 120)
    print(" " * 55, "PASSWORD", 55 * " ")
    p = input(" " * 56)
    print(' ' * 120)
    data_found = []
    indeks = 0
    for data in akun:
        if (data['USERNAME'] == u):
            data_found = akun[indeks]

        indeks = indeks + 1
        if len(data_found) > 0:
            if (data['PASS'] == p):
                print(' ' * 51, 'Login Berhasil!!', 51 * ' ')
                liat_menu()
            else:
                print(' ' * 47, 'Login gagal coba lagi...', 47 * ' ')
                mulai()

def balik_menu():
    print("\n")
    input(' '*47 + "Tekan Enter untuk kembali...")
    liat_menu()

def liat_catatan():
    bersihin_layar()
    global table
    catatan = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            catatan.append(row)

    print(" " * 54 + "List catatan")
    print(" " * 47 + '_' * 26)
    d = input(" " * 54 + "Tanggal(00): ")
    m = input(" " * 54 + "Bulan(00): ")
    y = input(" " * 54 + "Tahun(0000): ")
    print(" " * 47 + '_' * 26)
    data_found = []

    indeks = 0
    for data in catatan:
        if (data['HARI'] == d and data['BULAN'] == m and data['TAHUN'] == y):
            data_found = catatan[indeks]
        indeks = indeks + 1

    if len(data_found) > 0:
        print(' ' * 26, "-" * 68)
        print(' ' * 26, "HARI  BULAN   TAHUN   NOMOR   KETERANGAN              NOMINAL")
        print(' ' * 26, "-" * 68)
        for data in catatan:
            print(' ' * 26,
                  f"{data['HARI']} \t {data['BULAN']} \t {data['TAHUN']} \t {data['NOMOR']} \t {data['KETERANGAN']} \t\t {data['NOMINAL']}")
        print(' ' * 26, "-" * 68)
        balik_menu()
    else:
        print(" " * 46, "Tidak ada data ditemukan")
    balik_menu()


def total_pengeluaran():
    bersihin_layar()
    print("-" * 120)
    print(" " * 54, "[1] Hari")
    print(" " * 54, "[2] Bulan")
    print(" " * 54, "[3] Tahun")
    print(" " * 54, "[4] Kembali ke menu")
    print("_" * 120)
    selected_menu = str(input(" " * 55 + "Pilih menu: "))
    if (selected_menu == "1"):
        Hari()
    elif (selected_menu == "2"):
        Bulan()
    elif (selected_menu == "3"):
        Tahun()
    elif (selected_menu == "4"):
        balik_menu()
    else:
        print("Kamu memilih menu yang salah!")
        total_pengeluaran()

def Hari():
    bersihin_layar()
    catatan = []
    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            catatan.append(row)

    print(" " * 54 + 'Total Harian')
    print(" " * 47 + '_' * 26)
    d = input(" " * 54 + "Hari(00): ")
    m = input(" " * 54 + "Bulan(00): ")
    y = input(" " * 54 + "Tahun(0000): ")
    print(" " * 47 + '_' * 26)

    data_found = []
    indeks = 0
    sum = 0
    for data in catatan:
        if (data['HARI'] == d and data['BULAN'] == m and data['TAHUN'] == y):
            data_found = catatan[indeks]

        indeks = indeks + 1
        if len(data_found) > 0:
            sum += int(data_found["NOMINAL"])
    print(" " * 46, "Total Pengeluaran Harian: Rp.", sum)
    balik_menu()

def Bulan():
    bersihin_layar()
    catatan = []
    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            catatan.append(row)

    print(" " * 54 + 'Total Bulanan')
    print(" " * 47 + '_' * 26)
    m = input(" " * 54 + "Bulan(00): ")
    y = input(" " * 54 + "Tahun(0000): ")
    print(" " * 47 + '_' * 26)

    data_found = []
    indeks = 0
    sum = 0
    for data in catatan:
        if (data['BULAN'] == m and data['TAHUN'] == y):
            data_found = catatan[indeks]

        indeks = indeks + 1
        if len(data_found) > 0:
            sum += int(data_found["NOMINAL"])
    print(" " * 46, "Total Pengeluaran Bulanan: Rp.", sum)
    balik_menu()

def Tahun():
    bersihin_layar()
    catatan = []
    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            catatan.append(row)

    print(" " * 54 + 'Total Tahunan')
    print(" " * 47 + '_' * 26)
    y = input(" " * 54 + "Tahun(0000): ")
    print(" " * 47 + '_' * 26)

    data_found = []
    indeks = 0
    sum = 0
    for data in catatan:
        if (data['TAHUN'] == y):
            data_found = catatan[indeks]

        indeks = indeks + 1
        if len(data_found) > 0:
            sum += int(data_found["NOMINAL"])
    print(" " * 46, "Total Pengeluaran Tahunan: Rp.", sum)
    balik_menu()

def buat_catatan():
    bersihin_layar()
    csv_filename = 'Catatan.csv'

    with open(csv_filename, mode='a') as csv_file:
        fieldnames = ['HARI', 'BULAN', 'TAHUN', 'NOMOR', 'KETERANGAN', 'NOMINAL']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        try:
            print(" " * 54 + "Buat Catatan")
            print(" " * 47 + '_' * 26)
            d = int(input(" " * 54 + "Hari(00): "))
            m = int(input(" " * 54 + "Bulan(00): "))
            y = int(input(" " * 54 + "Tahun(0000): "))
            no = int(input(" " * 54 + "Nomor(00): "))
            ket = input(" " * 54 + "Keterangan: ")
            jum = int(input(" " * 54 + "Nominal: "))
            print(" " * 47 + '_' * 26)
        except ValueError:
            print(" " * 46, "Ups sepertinya ada kesalahan memasukan data")
            print("\n")
            input(" " * 46 + "Tekan Enter untuk kembali...")
            buat_catatan()

        writer.writerow({'HARI': d, 'BULAN': m, 'TAHUN': y, 'NOMOR': no, 'KETERANGAN': ket, 'NOMINAL': jum})
        print(" " * 46, "Berhasil disimpan!")
    balik_menu()

def edit_catatan():
    bersihin_layar()
    catatan = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            catatan.append(row)

    print(" " * 54 + "Ubah Catatan")
    print(" " * 47 + '_' * 26)
    d = input(" " * 54 + "Tanggal(00): ")
    m = input(" " * 54 + "Bulan(00): ")
    y = input(" " * 54 + "Tahun(0000): ")
    no = input(" " * 54 + "Nomor(00): ")
    print(" " * 47 + '_' * 26)
    data_found = []

    indeks = 0
    for data in catatan:
        if (data['HARI'] == d and data['BULAN'] == m and data['TAHUN'] == y and data['NOMOR'] == no):
            data_found = catatan[indeks]
        indeks = indeks + 1

    if len(data_found) > 0:
        print(" " * 46, "DATA DITEMUKAN: ")
        print(" " * 46, f"Hari: {data_found['HARI']}")
        print(" " * 46, f"Bulan: {data_found['BULAN']}")
        print(" " * 46, f"Tahun: {data_found['TAHUN']}")
        print(" " * 46, f"Nomor: {data_found['NOMOR']}")
        print(" " * 46, f"Keterangan: {data_found['KETERANGAN']}")
        print(" " * 46, f"Nominal: {data_found['NOMINAL']}")
        print(" " * 47 + '_' * 26)
        ket = input(" " * 54 + "Keterangan baru: ")
        jum = input(" " * 54 + "Nominal baru: ")
        print(" " * 47 + '_' * 26)
        print(" " * 46, "Data diperbarui")
        indeks = 0
        for data in catatan:
            if (data['HARI'] == d and data['BULAN'] == m and data['TAHUN'] == y and data['NOMOR'] == no):
                catatan[indeks]['KETERANGAN'] = ket
                catatan[indeks]['NOMINAL'] = jum
            indeks = indeks + 1

        # Menulis data baru ke file CSV (tulis ulang)
        with open(csv_filename, mode="w") as csv_file:
            fieldnames = ['HARI', 'BULAN', 'TAHUN', 'NOMOR', 'KETERANGAN', 'NOMINAL']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for new_data in catatan:
                writer.writerow({'HARI': new_data['HARI'], 'BULAN': new_data['BULAN'], 'TAHUN': new_data['TAHUN'],
                                 'NOMOR': new_data['NOMOR'], 'KETERANGAN': new_data['KETERANGAN'],
                                 'NOMINAL': new_data['NOMINAL']})
        balik_menu()
    else:
        print(" " * 46, "Tidak ada data ditemukan")
    balik_menu()

def hapus_catatan():
    bersihin_layar()
    catatan = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            catatan.append(row)

    print(" " * 53 + "Hapus Catatan")
    print(" " * 47 + '_' * 26)
    d = input(" " * 54 + "tanggal(00): ")
    m = input(" " * 54 + "bulan(00): ")
    y = input(" " * 54 + "tahun(0000): ")
    no = input(" " * 54 + "nomor(00): ")
    print(" " * 47 + '_' * 26)
    data_found = []

    indeks = 0
    for data in catatan:
        if (data['HARI'] == d and data['BULAN'] == m and data['TAHUN'] == y and data['NOMOR'] == no):
            data_found = catatan[indeks]
        indeks = indeks + 1

    if len(data_found) > 0:
        print(" " * 46, "DATA DITEMUKAN: ")
        print(" " * 46, f"Hari: {data_found['HARI']}")
        print(" " * 46, f"Bulan: {data_found['BULAN']}")
        print(" " * 46, f"Tahun: {data_found['TAHUN']}")
        print(" " * 46, f"Nomor: {data_found['NOMOR']}")
        print(" " * 46, f"Keterangan: {data_found['KETERANGAN']}")
        print(" " * 46, f"Nominal: {data_found['NOMINAL']}")
        print(" " * 47 + '_' * 26)
        pilih = input(" " * 46 + " Hapus? y/t : ")
        if (pilih == "y"):
            indeks = 0
            for data in catatan:
                if (data['HARI'] == d and data['BULAN'] == m and data['TAHUN'] == y and data['NOMOR'] == no):
                    catatan.remove(catatan[indeks])
                indeks = indeks + 1

            with open(csv_filename, mode="w") as csv_file:
                fieldnames = ['HARI', 'BULAN', 'TAHUN', 'NOMOR', 'KETERANGAN', 'NOMINAL']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for new_data in catatan:
                    writer.writerow({'HARI': new_data['HARI'], 'BULAN': new_data['BULAN'], 'TAHUN': new_data['TAHUN'],
                                     'NOMOR': new_data['NOMOR'], 'KETERANGAN': new_data['KETERANGAN'],
                                     'NOMINAL': new_data['NOMINAL']})
            print(" " * 47 + '_' * 26)
            print(" " * 46, "Data dihapus")
            balik_menu()
        else:
            print(" " * 120)
            print(" " * 48, "Pilihan hanya y atau t")
            print(" " * 120)
            balik_menu()
    else:
        print(" " * 46, "Tidak ada data ditemukan")
    balik_menu()

def cari_catatan():
    bersihin_layar()
    catatan = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            catatan.append(row)

    print(" " * 54 + "Cari Catatan")
    print(" " * 47 + '_' * 26)
    d = input(" " * 54 + "Tanggal(00): ")
    m = input(" " * 54 + "Bulan(00): ")
    y = input(" " * 54 + "Tahun(0000): ")
    no = input(" " * 54 + "Nomor(00): ")
    print(" " * 47 + '_' * 26)
    data_found = []

    indeks = 0
    for data in catatan:
        if (data['HARI'] == d and data['BULAN'] == m and data['TAHUN'] == y and data['NOMOR'] == no):
            data_found = catatan[indeks]

        indeks = indeks + 1

    if len(data_found) > 0:
        print(" " * 46, "DATA DITEMUKAN: ")
        print(" " * 46, f"Hari: {data_found['HARI']}")
        print(" " * 46, f"Bulan: {data_found['BULAN']}")
        print(" " * 46, f"Tahun: {data_found['TAHUN']}")
        print(" " * 46, f"Nomor: {data_found['NOMOR']}")
        print(" " * 46, f"Keterangan: {data_found['KETERANGAN']}")
        print(" " * 46, f"Nominal: {data_found['NOMINAL']}")
    else:
        print(" " * 46, "Tidak ada data ditemukan")
    balik_menu()


if __name__ == "__main__":
    while True:
        mulai()