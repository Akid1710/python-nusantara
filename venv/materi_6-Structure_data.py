#list (Berurutan, Bisa Diganti, Bisa Di Duplikat)
DaftarBelanjaThisWeek=["Tahu Bakso Idola","Cakwe","Risol","Es Teh Desa"]
print("Isi Tas Belanja:", DaftarBelanjaThisWeek)
#Mengakses List Lewat Index
print("Isi Tas Belanja", DaftarBelanjaThisWeek)
print("Item Ke-1", DaftarBelanjaThisWeek[0])
print("Item Ke-2", DaftarBelanjaThisWeek[1])
print("Item Ke-2", DaftarBelanjaThisWeek[2])
#append() Menambah Item Baru Ke List
DaftarBelanjaThisWeek.append("Es Doger")
DaftarBelanjaThisWeek.append("Mie Ayam")
print("Isi Tas Belanja Sekarang:", DaftarBelanjaThisWeek)
#Remove () Menghapus Item Dari List
DaftarBelanjaThisWeek.remove("Mie Ayam")
print("Isi Tas Belanja Akhir", DaftarBelanjaThisWeek)


#tuple (Urut , Tidak Bisa Diubah , Boleh Duplikat)
#Penulisannya Menggunakan ()
print("-------------------TUPLE----------------")
TTL =("Karawang",19, "January", 2010)
print("Tanggal Lahir Dika:", TTL)
print("Tanggal:", TTL[1])
print("Bulan:", TTL[2])
print("Tahun:", TTL[3])
print("Tempat:", TTL[0])
#Akses Index (posisi index) :lalu batas akhir item nya
print("Bulan Tahun:", TTL[2:4])
#unpacking tuple ke variable baru
#mengikuti urutan itemnya
Tempat_Lahir, Tanggal_Lahir, Bulan_Lahir, Tahun_Lahir =TTL
print(Tempat_Lahir)

#manipulasi list lanjutan
Jajan_Dika =("Batagor", "Pempek")
Jajan_Qila =("Siomay", "Cimol")
Jajan_DiSha = Jajan_Dika + Jajan_Qila
print(Jajan_DiSha)
#List Multi-Dimensi
List_Makanan =[
    ["Mie Ayam", "Mie Goreng", "Mie Tek-tek"],
    ["Nasi Goreng", "Nasi Kuning", "Nasi Uduk"],
    ["Ayam Goreng", "Ayam Panggang", "Ayam Bakar"]
]
print(List_Makanan)
print(List_Makanan [1][2])