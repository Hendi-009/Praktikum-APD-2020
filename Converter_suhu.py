# Program membuat converter suhu
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
    print("Selamat datang di converter suhu!")
    print("Program ini dibuat oleh:")
    print("Kelompok 15 - Informatika 20 - Universitas Mulawarman")

    print(20 * "-", "MENU", 20 * "-")
    print("Pilih satuan suhu yang akan dikonversikan.")
    print("[1] Celcius")
    print("[2] Fahrenheit")
    print("[3] Kelvin")
    print("[4] Reamur")
    print("[0] Exit")
    print(46 * "-")

    pilih = str(input("Masukan pilihan(1/2/3/4/0): "))

    if (pilih == "1"):
        Celcius()
    elif (pilih == "2"):
        Fahrenheit()
    elif (pilih == "3"):
        Kelvin()
    elif (pilih == "4"):
        Reamur()
    elif (pilih == "0"):
        trims()


# Celcius ke suhu lain
def Celcius():
    print("Pilih Operasi.")
    print("[1] Celcius ke Fahrenheit")
    print("[2] Celcius ke Kelvin")
    print("[3] Celcius ke Reamur")
    print("[4] Kembali ke menu")
    print("[0] Exit")

    # Ambil input dari user
    pilih = str(input("Masukan pilihan(1/2/3/4/0): "))

    if (pilih == "1"):
        celsius_ke_fahrenheit()
    elif (pilih == "2"):
        celsius_ke_kelvin()
    elif (pilih == "3"):
        celsius_ke_reamur()
    elif (pilih == "4"):
        kembali_ke_menu()
    elif (pilih == "0"):
        trims()
    else:
        print("Input salah")
        kembali_ke_menu()


# Fahrenheit ke suhu lain
def Fahrenheit():
    print("Pilih Operasi.")
    print("[1].Fahrenheit ke Celcius")
    print("[2].Fahrenheit ke Kelvin")
    print("[3].Fahrenheit ke Reamur")
    print("[4] Kembali ke menu")
    print("[0] Exit")

    # Ambil input dari user
    pilih = str(input("Masukan pilihan(1/2/3/4/0): "))

    if (pilih == "1"):
        fahrenheit_ke_celcius()
    elif (pilih == "2"):
        fahrenheit_ke_kelvin()
    elif (pilih == "3"):
        fahrenheit_ke_reamur()
    elif (pilih == "4"):
        kembali_ke_menu()
    elif (pilih == "0"):
        trims()
    else:
        print("Input salah")
        kembali_ke_menu()


# Kelvin ke suhu lain
def Kelvin():
    print("Pilih Operasi.")
    print("[1].Kelvin ke Celcius")
    print("[2].Kelvin ke Fahrenheit")
    print("[3].Kelvin ke Reamur")
    print("[4] Kembali ke menu")
    print("[0] Exit")

    # Ambil input dari user
    pilih = str(input("Masukan pilihan(1/2/3/4/0): "))

    if (pilih == "1"):
        kelvin_ke_celcius()
    elif (pilih == "2"):
        kelvin_ke_fahrenheit()
    elif (pilih == "3"):
        kelvin_ke_reamur()
    elif (pilih == "4"):
        kembali_ke_menu()
    elif (pilih == "0"):
        trims()
    else:
        print("Input salah")
        kembali_ke_menu()


# Reamur ke suhu lain
def Reamur():
    print("Pilih Operasi.")
    print("[1].Reamur ke Celcius")
    print("[2].Reamur ke Fahrenheit")
    print("[3].Reamur ke Kelvin")
    print("[4] Kembali ke menu")
    print("[0] Exit")

    # Ambil input dari user
    pilih = str(input("Masukan pilihan(1/2/3/4/0): "))

    if (pilih == "1"):
        reamur_ke_celcius()
    elif (pilih == "2"):
        reamur_ke_fahrenheit()
    elif (pilih == "3"):
        reamur_ke_kelvin()
    elif (pilih == "4"):
        kembali_ke_menu()
    elif (pilih == "0"):
        trims()
    else:
        print("Input salah")
        kembali_ke_menu()


# Terimakasih
def trims():
    print("Terimakasih Telah Menggunakaan converter suhu")
    input("Tekan Enter untuk keluar")
    exit()


# Kembali ke menu
def kembali_ke_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    kasih_liat_menu()

# Rumus Celcius
def celsius_ke_fahrenheit():
    celcius = float(input("Masukan suhu: "))
    fahrenheit = celcius * 9 / 5 + 32

    print("fahrenheit =", fahrenheit, "℉")
    kembali_ke_menu()

def celsius_ke_kelvin():
    celcius = float(input("Masukan suhu: "))
    kelvin = celcius + 273

    print("kelvin =", kelvin, "K")
    kembali_ke_menu()

def celsius_ke_reamur():
    celcius = float(input("Masukan suhu: "))
    reamur = celcius * 4 / 5

    print("reamur =", reamur, "°R")
    kembali_ke_menu()


# Rumus Fahrenheit
def fahrenheit_ke_celcius():
    fahrenheit = float(input("Masukan suhu: "))
    celcius = (5 / 9) * (fahrenheit - 32)

    print("Celcius =", celcius, "℃")
    kembali_ke_menu()


def fahrenheit_ke_kelvin():
    fahrenheit = float(input("Masukan suhu: "))
    kelvin = (fahrenheit - 32) * (5 / 9) + 273

    print("kelvin =", kelvin, "K")
    kembali_ke_menu()


def fahrenheit_ke_reamur():
    fahrenheit = float(input("Masukan suhu: "))
    reamur = (fahrenheit - 32) * (4 / 9)

    print("reamur =", reamur, "°R")
    kembali_ke_menu()


# Rumus Kelvin
def kelvin_ke_celcius():
    kelvin = float(input("Masukan suhu: "))
    celcius = (kelvin - 273)

    print("Celcius =", celcius, "℃")
    kembali_ke_menu()


def kelvin_ke_fahrenheit():
    kelvin = float(input("Masukan suhu: "))
    fahrenheit = (((kelvin - 273) * 9 / 5 + 32))

    print("fahrenheit =", fahrenheit, "°F")
    kembali_ke_menu()


def kelvin_ke_reamur():
    kelvin = float(input("Masukan suhu: "))
    reamur = (4 / 5) * (kelvin - 273)

    print("reamur =", reamur, "°R")
    kembali_ke_menu()


# Rumus Reamur
def reamur_ke_celcius():
    reamur = float(input("Masukan suhu: "))
    celcius = (5 / 4) * reamur

    print("Celcius =", celcius, "℃")
    kembali_ke_menu()


def reamur_ke_fahrenheit():
    reamur = float(input("Masukan suhu: "))
    fahrenheit = reamur * (9 / 4) + 32

    print("fahrenheit =", fahrenheit, "°F")
    kembali_ke_menu()


def reamur_ke_kelvin():
    reamur = float(input("Masukan suhu: "))
    kelvin = reamur * (5 / 4) + 273

    print("kelvin =", kelvin, "K")
    kembali_ke_menu()


kasih_liat_menu()