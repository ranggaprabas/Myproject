#SELEKSI BEASISWA POLINES
nama = input("Masukkan nama: ")
nim = input("Masukkan nim: ")
kelas = input("Masukkan kelas: ")
nilai = input("Masukkan nilai: ")

min_nilai = 3.7

if float(nilai) > min_nilai :
    print("\n\nSelamat " + nama + ", Anda berhak mendapatkan Beasiswa POLINES!")
else :
    print("\n\nMohon Maaf " + nama + ", Anda belum bisa mendapatkan Beasiswa POLINES")