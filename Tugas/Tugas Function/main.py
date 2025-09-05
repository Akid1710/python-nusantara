import Hitung_Uang

data = input("masukan daftar uang jajan mu:")

jajan = list(map(int, data.split()))


print("Data Asli:", jajan)
print("Ditambah Bonus:", Hitung_Uang.tambah_bonus(jajan))
print("Yang Boros:", Hitung_Uang.filter_boros(jajan))


import ranking

nilai = [95, 98, 99, 100, 90]

print("Daftar Nilai:", nilai)
print("Nilai Urut:", ranking.urutkan_nilai(nilai))
print("Nilai Tertinggi:", ranking.nilai_tertinggi(nilai))
print("Nilai Terendah:", ranking.nilai_terendah(nilai))



import Emoji_mood

moods= ["senang", "sedih", "biasa", "semangat", "Ngantuk"]

print("Data Mood:", moods)
print("Hasil Convert:", Emoji_mood.convert_mood(moods))



import ngaji_tracker


halaman = [1,5,3,8,6,9,7,4,2]
total = ngaji_tracker.total_mgaji(halaman)

print("DataNgaji:", halaman)
print("Total Halaman:", total)
print("Status:", ngaji_tracker.cek_target(total))