import json
#tambahkan module 'json' dengan 'import'
print("Materi 12  JSON File Handling")
print("READ JSON")
file_path_json= r"D:\Dika\Folder Baru\Tugas\materi.json"
with open(file_path_json, "r") as file_materi:
    #json.load() -> membaca isi file json
    data_materi= json.load(file_materi)
    #akses data json dengan key
    print(f"Judul Berkas: {data_materi['tittle']}")
    print(f"Total Santri kelas A: {data_materi['total']}")
    print(f"Status Santri: {data_materi['status_santri']}")
    print(f"Status Kelulusan: {data_materi['status_lulus']}")
    #ekstrak data list for loop
    for pelajaran in data_materi['pelajaran']:
        print(f"--> {pelajaran}")

print("-"*50)
print("|No|Nama Surah|Ayat|Tempat Turun|")
print("-"*50)
for surah in data_materi['surah']:
    print(f"| {surah['No']} | {surah['Nama']} |{surah['Ayat']} | {surah['Turun']}")