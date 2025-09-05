#1

Jadwal_Piket_Hari_Ini=['Dika','Dihyah','Hanif']

print("Jadwal Piket Harian : ")

for santri in Jadwal_Piket_Hari_Ini:
    print(f"- {santri}")

#2
Rukun_Islam=('Syahadat','Sholat','Zakat','Puasa','Haji')

print("Rukun Islam Ada 5 :")

for RukIs in Rukun_Islam:
    print(f"- {RukIs}")


#3
Kitab_Bermanfaat={'Durusul Lughah','ABY','Tamhidus Sabil','Mukhtarot'}

print("Kitab-Kitab Yang Pernah Dipelajari")

for Book in Kitab_Bermanfaat:
    print(f"Kitab :{Book}")


#4 
biodata = {
    'nama': input("Masukkan nama santri: "),
    'kelas': input("Masukkan kelas santri: "),
    'hafalan_juz': int(input("Masukkan jumlah hafalan juz: "))
}


print("\nBiodata Santri:")
for kunci, nilai in biodata.items():
    print(f"{kunci}: {nilai}")
