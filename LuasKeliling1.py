#jobsheet 4 Program Menghitung Luas dan Keliling Bangun Datar
def lbs(x): # fungsi luas bujur sangkar
   return x * x
def kbs(x): # fungsi keliling bujur sangkar
   return 4 * x 
def lpp(x, y): # fungsi luas persegi panjang
   return x * y
def kpp(x, y): # fungsi keliling persegi panjang
   return 2 * (x + y)
def ls(x, y): # fungsi luas segitiga
   return (x * y) / 2
def ks(x): # fungsi keliling segitiga
   return 3 * x
def ll(x): # fungsi luas lingkaran
   return 22/7 * x * x
def kl(x): # fungsi keliling lingkaran
   return 2 * 22/7 * x 
def ljg(x,y): # fungsi luas jajar genjang
   return x * y
def kjg(x, y): # fungsi keliling jajar genjang
   return 2 * (x + y)
# menu operasi
print("Pilih Operasi.")
print("1.mencari luas bujur sangkar")
print("2.mencari keliling bujur sangkar")
print("3.mencari luas persegi panjang")
print("4.mencari keliling persegi panjang")
print("5.mencari luas segitiga")
print("6.mencari keliling segitiga")
print("7.mencari luas lingkaran")
print("8.mencari keliling lingkaran")
print("9.mencari luas jajar genjang")
print("10.mencari keliling jajar genjang")
choice = input("Masukkan pilihan(1/2/3/4/5/6/7/8/9/10): ") # Meminta input dari user
if choice == '1':
    num1 = int(input("Masukkan sisi: "))
elif choice == '2':
    num1 = int(input("Masukkan sisi: "))
elif choice == '3':
    num1 = int(input("Masukkan panjang: "))
    num2 = int(input("Masukkan lebar: "))
elif choice == '4':
    num1 = int(input("Masukkan panjang: "))
    num2 = int(input("Masukkan lebar: "))
elif choice == '5':
    num1 = int(input("Masukkan alas: "))
    num2 = int(input("Masukkan tinggi: "))
elif choice == '6':
    num1 = int(input("Masukkan bilangan pertama: "))
elif choice == '7':
    num1 = int(input("Masukkan jari - jari: "))
elif choice == '8':
    num1 = int(input("Masukkan jari - jari: "))
elif choice == '9':
    num1 = int(input("Masukkan alas: "))
    num2 = int(input("Masukkan tinggi: "))
elif choice == '10':
    num1 = int(input("Masukkan alas: "))
    num2 = int(input("Masukkan tinggi: "))
else :
    print("salah")
if choice == '1':
   print(num1,"*",num1,"=", lbs(num1))
elif choice == '2':
   print("4","*",num1,"=", kbs(num1))
elif choice == '3':
   print(num1,"*",num2,"=", lpp(num1,num2))
elif choice == '4':
   print("2*(",num1,"+", num2,") =", kpp(num1, num2))
elif choice == '5':
   print("(", num1,"*", num2,")/2 =", ls(num1, num2))
elif choice == '6':
   print("3","*",num1,"=", ks(num1))
elif choice == '7':
   print("3,14","",num1,"",num1,"=", ll(num1))
elif choice == '8':
   print("2 * 3,14","*",num1,"=", kl(num1))
elif choice == '9':
   print(num1,"*",num2,"=", ljg(num1,num2))
elif choice == '10':
   print("2 (", num1,"+", num2,") =", kjg(num1, num2))
else:
    print("Maaf, Anda salah memasukkan angka")