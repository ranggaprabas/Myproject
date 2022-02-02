#Membuat List Kosong Untuk Menampung Hobi
nama = []
hobi = []
stop = False
i = j = 1
n = 0

#Input Nama & Hobi
while(not stop):
    nama_baru = input("Masukkan nama ke-"+ format(i) +" : ")
    nama.append(nama_baru)
    hobi_baru= input("Masukkan hobi ke-"+ format(j) +" : ")
    hobi.append(hobi_baru)
    print ("")

#Increment & Pengecualian
    konfirmasi = input("Apakah ingin menambahkan data lagi? (y/t) = ")
    if(konfirmasi == "y") :
        i += 1
        j += 1
        n += 1
        continue
    elif(konfirmasi == "t") :
        stop = True
    else :
        print ("Inputan salah")
        nama.pop (n)
        hobi.pop (n)
        continue
        
#Cetak Jumlah Data (Nama dan Jenis Hobi)
print ("")
print ("==================== DATA TEREKAM ====================")
print ("Terdapat " +format(len(nama)) + " Mahasiswa yang sudah memasukkan datanya")

#Cetak Data Terekam
print ("")
cetak = input("Apakah hendak menampilkan data? (y/t) = ")
if (cetak == "y") : 
        print ("Berikut adalah data nama mahasiswa :")
        for nm in nama :
            print ("- " + format(nm))
        print ("")
        print ("Berikut adalah data hobi mahasiswa :")
        for hb in hobi :
            print ("- " + format(hb))
        print ("")
elif (cetak == "t") :
    print ("Tidak menampilkan data")
else :
    print ("Inputan salah")
