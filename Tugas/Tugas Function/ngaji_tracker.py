def total_mgaji(halaman_list):
    return sum(halaman_list)

def cek_target(total, target=20):
    if total >= target:
        return "tercapai 🎉"
    
    else:
        return "belum tercapai 😔"