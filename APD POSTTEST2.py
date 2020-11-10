# Program membuat kalkulator bangun ruang
import os

# cls adalah clearscreen
# nt untuk windows
# clear untuk linux dan unix

# Bersihin Layar
def bersihin_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menu
def kasih_liat_menu():
    bersihin_layar()
    print("2009106009_Hendi_POSTTEST2")
    print(20 * "-", "MENU", 20 * "-")
    print("Program Kalkulator Bangun Ruang Sederhana.")
    print(46 * "=")
    print("Silahkan pilih bangun ruang")
    print("[1] Kubus")
    print("[2] Balok")
    print("[3] Prisma Segitiga")
    print("[4] Limas Segitiga")
    print("[5] Limas Segiempat")
    print("[6] Tabung")
    print("[7] Kerucut")
    print("[8] Bola")
    print("[0] Exit")
    print(46 * "-")

    pilih = str(input("Masukan pilihan(1/2/3/4/5/6/7/8/0): "))

    if (pilih == "1"):
        Kubus()
    elif (pilih == "2"):
        Balok()
    elif (pilih == "3"):
        Prisma_Segitiga()
    elif (pilih == "4"):
        Limas_Segitiga()
    elif (pilih == "5"):
        Limas_Segiempat()
    elif (pilih == "6"):
        Tabung()
    elif (pilih == "7"):
        Kerucut()
    elif (pilih == "8"):
        Bola()
    elif (pilih == "0"):
        trims()

# Kubus
def Kubus():
    print("Pilih Operasi.")
    print("[1] Volume kubus")
    print("[2] Luas permukaan kubus")
    print("[3] Keliling kubus")
    print("[4] Kembali ke menu")
    print("[0] Exit")

    # Ambil input dari user
    pilih = str(input("Masukan pilihan(1/2/3/4/0): "))

    if (pilih == "1"):
        volume_kubus()
    elif (pilih == "2"):
        luas_permukaan_kubus()
    elif (pilih == "3"):
        keliling_kubus()
    elif (pilih == "4"):
        kembali_ke_menu()
    elif (pilih == "0"):
        trims()
    else:
        print("Input salah")
        kembali_ke_menu()

# Balok
def Balok():
    print("Pilih Operasi.")
    print("[1] Volume balok")
    print("[2] Luas permukaan balok")
    print("[3] Diagonal ruang")
    print("[4] Keliling balok")
    print("[5] Kembali ke menu")
    print("[0] Exit")

    # Ambil input dari user
    pilih = str(input("Masukan pilihan(1/2/3/4/5/0): "))

    if (pilih == "1"):
        volume_balok()
    elif (pilih == "2"):
        luas_permukaan_balok()
    elif (pilih == "3"):
        diagonal_ruang_balok()
    elif (pilih == "4"):
        keliling_balok()
    elif (pilih == "5"):
        kembali_ke_menu()
    elif (pilih == "0"):
        trims()
    else:
        print("Input salah")
        kembali_ke_menu()

# Prisma Segitiga
def Prisma_Segitiga():
    print("Pilih Operasi.")
    print("[1] Volume prisma segitiga")
    print("[2] Luas permukaan prisma segitiga")
    print("[3] Kembali ke menu")
    print("[0] Exit")

    # Ambil input dari user
    pilih = str(input("Masukan pilihan(1/2/3/0): "))

    if (pilih == "1"):
        volume_prisma_segitiga()
    elif (pilih == "2"):
        luas_permukaan_prisma_segitiga()
    elif (pilih == "3"):
        kembali_ke_menu()
    elif (pilih == "0"):
        trims()
    else:
        print("Input salah")
        kembali_ke_menu()


# Limas Segitiga
def Limas_Segitiga():
    print("Pilih Operasi.")
    print("[1] Volume limas segitiga")
    print("[2] Luas permukaan limas segitiga")
    print("[3] Kembali ke menu")
    print("[0] Exit")

    # Ambil input dari user
    pilih = str(input("Masukan pilihan(1/2/3/0): "))

    if (pilih == "1"):
        volume_limas_segitiga()
    elif (pilih == "2"):
        luas_permukaan_limas_segitiga_sembarang()
    elif (pilih == "3"):
        kembali_ke_menu()
    elif (pilih == "0"):
        trims()
    else:
        print("Input salah")
        kembali_ke_menu()

# Limas Segiempat
def Limas_Segiempat():
    print("Pilih Operasi.")
    print("[1] Volume limas segiempat")
    print("[2] Luas permukaan limas segiempat")
    print("[3] Kembali ke menu")
    print("[0] Exit")

    # Ambil input dari user
    pilih = str(input("Masukan pilihan(1/2/3/0): "))

    if (pilih == "1"):
        volume_limas_segiempat()
    elif (pilih == "2"):
        luas_permukaan_limas_segiempat()
    elif (pilih == "3"):
        kembali_ke_menu()
    elif (pilih == "0"):
        trims()
    else:
        print("Input salah")
        kembali_ke_menu()

# Tabung
def Tabung():
    print("Pilih Operasi.")
    print("[1] Volume tabung")
    print("[2] Luas permukaan tabung")
    print("[3] Kembali ke menu")
    print("[0] Exit")

    # Ambil input dari user
    pilih = str(input("Masukan pilihan(1/2/3/0): "))

    if (pilih == "1"):
        volume_tabung()
    elif (pilih == "2"):
        luas_permukaan_tabung()
    elif (pilih == "3"):
        kembali_ke_menu()
    elif (pilih == "0"):
        trims()
    else:
        print("Input salah")
        kembali_ke_menu()

# Kerucut
def Kerucut():
    print("Pilih Operasi.")
    print("[1] Volume kerucut")
    print("[2] Luas permukaan kerucut")
    print("[3] Kembali ke menu")
    print("[0] Exit")

    # Ambil input dari user
    pilih = str(input("Masukan pilihan(1/2/3/0): "))

    if (pilih == "1"):
        volume_kerucut()
    elif (pilih == "2"):
        luas_permukaan_kerucut()
    elif (pilih == "3"):
        kembali_ke_menu()
    elif (pilih == "0"):
        trims()
    else:
        print("Input salah")
        kembali_ke_menu()

# Bola
def Bola():
    print("Pilih Operasi.")
    print("[1] Volume bola")
    print("[2] Luas permukaan bola")
    print("[3] Kembali ke menu")
    print("[0] Exit")

    # Ambil input dari user
    pilih = str(input("Masukan pilihan(1/2/3/0): "))

    if (pilih == "1"):
        volume_bola()
    elif (pilih == "2"):
        luas_permukaan_bola()
    elif (pilih == "3"):
        kembali_ke_menu()
    elif (pilih == "0"):
        trims()
    else:
        print("Input salah")
        kembali_ke_menu()

# Terimakasih
def trims():
    print("Terimakasih Telah Menggunakaan Kalkulator Bangun Ruang Sederhana")
    input("Tekan Enter untuk keluar")
    exit()

# Kembali ke menu
def kembali_ke_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    kasih_liat_menu()

# Rumus kubus
def volume_kubus():
    s = float(input("Masukan panjang sisi: "))
    V = pow(s, 3)

    print("Volume kubus =", V, "cm³")
    kembali_ke_menu()

def luas_permukaan_kubus():
    s = float(input("Masukan panjang sisi: "))
    L = 6 * pow(s, 2)

    print("Luas permukaan kubus =", L, "cm²")
    kembali_ke_menu()

def keliling_kubus():
    s = float(input("Masukan panjang sisi: "))
    Kel = 12 * s

    print("Keliling kubus =", Kel, "cm")
    kembali_ke_menu()


# Rumus balok
def volume_balok():
    p = float(input("Masukan panjang:  "))
    l = float(input("Masukan lebar:  "))
    t = float(input("Masukan tinggi:  "))
    V = p * l * t

    print("Volume balok =", V, "cm³")
    kembali_ke_menu()

def luas_permukaan_balok():
    p = float(input("Masukan panjang: "))
    l = float(input("Masukan lebar: "))
    t = float(input("Masukan tinggi: "))
    L = 2 * (p * l + l * t + p * t)

    print("Luas permukaan balok =", L, "cm²")
    kembali_ke_menu()

def diagonal_ruang_balok():
    from math import sqrt as akar
    p = float(input("Masukan panjang: "))
    l = float(input("Masukan lebar: "))
    t = float(input("Masukan tinggi: "))
    Dia = akar(pow(p, 2) + pow(l, 2) + pow(t, 2))

    print("Diagonal ruang balok =", Dia, "cm")
    kembali_ke_menu()

def keliling_balok():
    p = float(input("Masukan panjang: "))
    l = float(input("Masukan lebar: "))
    t = float(input("Masukan tinggi: "))
    Kel = 4 * (p + l + t)

    print("Keliling balok =", Kel, "cm")
    kembali_ke_menu()


# Rumus prisma segitiga
def volume_prisma_segitiga():
    a = float(input("Masukan alas segitiga: "))
    t = float(input("Masukan tinggi segitiga: "))
    T = float(input("Masukan tinggi prisma: "))
    V = 1 / 2 * a * t * T

    print("Volume prisma segitiga =", V, "cm³")
    kembali_ke_menu()

def luas_permukaan_prisma_segitiga():
    s1 = float(input("Masukan panjang sisi miring segitiga:  "))
    s2 = a = float(input("Masukan panjang alas segitiga:  "))
    s3 = t = float(input("Masukan panjang tinggi segitiga:  "))
    T = float(input("Masukan tinggi prisma:  "))
    L = T * (s1 + s2 + s3) + (2 * 1 / 2 * a * t)

    print("Luas permukaan prisma segitiga =", L, "cm²")
    kembali_ke_menu()


# Rumus limas segitiga
def volume_limas_segitiga():
    T = float(input("Masukan tinggi limas segitiga:  "))
    a = float(input("Masukan panjang alas segitiga:  "))
    t = float(input("Masukan panjang tinggi segitiga:  "))
    V = 1 / 3 * (1 / 2 * a * t) * T

    print("Volume limas segitiga =", V, "cm³")
    kembali_ke_menu()

def luas_permukaan_limas_segitiga_sembarang():
    a1 = float(input("Masukan panjang alas segitiga alas:  "))
    t1 = float(input("Masukan panjang tinggi segitiga alas:  "))
    a2 = float(input("Masukan panjang alas segitiga 1:  "))
    t2 = float(input("Masukan panjang tinggi segitiga 1:  "))
    a3 = float(input("Masukan panjang alas segitiga 2:  "))
    t3 = float(input("Masukan panjang tinggi segitiga 2:  "))
    a4 = float(input("Masukan panjang alas segitiga 3:  "))
    t4 = float(input("Masukan panjang tinggi segitiga 3:  "))
    L = (1 / 2 * a1 * t1) + (1 / 2 * a2 * t2) + (1 / 2 * a3 * t3) + (1 / 2 * a4 * t4)

    print("Luas permukaan limas segitiga =", L, "cm²")
    kembali_ke_menu()


# Rumus limas segiempat
def volume_limas_segiempat():
    p = float(input("Masukan panjang: "))
    l = float(input("Masukan lebar: "))
    t = float(input("Masukan tinggi: "))
    V = 1 / 3 * p * l * t

    print("Volume limas segiempat =", V, "cm³")
    kembali_ke_menu()

def luas_permukaan_limas_segiempat():
    from math import sqrt as akar
    s = a = float(input("Masukan panjang sisi persegi:  "))
    T = float(input("Masukan tinggi limas:  "))
    L = (s * s) + 4 * (1 / 2 * a * akar(pow(T, 2) + pow(1/2 * s, 2)))

    print("Luas permukaan limas segitiga =", L, "cm²")
    kembali_ke_menu()


# Rumus tabung
def volume_tabung():
    phi = 3.14
    r = float(input("Masukan radius: "))
    t = float(input("Masukan tinggi: "))
    V = phi * pow(r, 2) * t

    print("Volume tabung =", V, "cm³")
    kembali_ke_menu()

def luas_permukaan_tabung():
    phi = 3.14
    r = float(input("Masukan radius: "))
    t = float(input("Masukan tinggi:  cm"))
    L = 2 * phi * r * (r + t)

    print("Luas permukaan tabung =", L, "cm²")
    kembali_ke_menu()


# Rumus kerucut
def volume_kerucut():
    phi = 3.14
    r = float(input("Masukan radius: "))
    t = float(input("Masukan tinggi: "))
    V = 1 / 3 * phi * pow(r, 2) * t

    print("Volume kerucut =", V, "cm³")
    kembali_ke_menu()

def luas_permukaan_kerucut():
    phi = 3.14
    r = float(input("Masukan radius: "))
    s = float(input("Masukan tinggi: "))
    L = phi * pow(r, 2) + phi * r * s

    print("Luas permukaan kerucut =", L, "cm²")
    kembali_ke_menu()


# Rumus bola
def volume_bola():
    phi = 3.14
    r = float(input("Masukan radius: "))
    V = 4 / 3 * phi * pow(r, 2)

    print("Volume bola =", V, "cm³")
    kembali_ke_menu()

def luas_permukaan_bola():
    phi = 3.14
    r = float(input("Masukan radius: "))
    L = 4 * phi * pow(r, 2)

    print("Luas permukaan bola =", L, "cm²")
    kembali_ke_menu()

kasih_liat_menu()