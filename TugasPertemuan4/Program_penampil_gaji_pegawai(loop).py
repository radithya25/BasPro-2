#Program penampil gaji pegawai(loop)
status_pegawai = ["tetap", "honor"]
golongan_list = ["A", "B", "C"]

gaji_pokok = {
    "tetap": 1000000,
    "honor": 750000
}

bonus_golongan = {
    "tetap": {"A": 200000, "B": 400000, "C": 550000},
    "honor": {"A": 150000, "B": 275000, "C": 480000}
}

print("\n==== Daftar Gaji Pegawai ====")
for status in status_pegawai:
    for golongan in golongan_list:
        gaji = gaji_pokok[status]
        bonus = bonus_golongan[status][golongan]
        total_gaji = gaji + bonus
        print(f"| Status: {status} | Golongan: {golongan} | Gaji Pokok: {gaji} | Bonus: {bonus} | Total Gaji: {total_gaji}")
