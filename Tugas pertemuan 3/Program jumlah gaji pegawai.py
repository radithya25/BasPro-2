#Program jumlah gaji pegawai
nama=str(input("Masukkan Nama: "))
nik=int(input("Masukkan NIK: "))
status=str(input("Masukkan Status pegawai(tetap/honor): "))
golongan=str(input("Masukkan Golongan: "))

if status == "tetap":
    gaji = 1000000
    if golongan == "A":
        bonus = 200000
    elif golongan == "B":
        bonus = 400000
    elif golongan == "C":
        bonus = 550000
    else:
        print("Golongan yang di input tidak valid")
        exit()
elif status == "honor":
    gaji = 750000
    if golongan == "A":
        bonus = 150000
    elif golongan == "B":
        bonus = 275000
    elif golongan == "C":
        bonus = 480000
    else:
        print("Golongan yang di input tidak valid")
        exit()
else:
    print("Status pegawai tidak valid")
    exit()

TotalGaji=gaji+bonus

print("\n====Rincian====")
print("Nama: ",nama)
print("NIK: ",nik)
print("Status: ",status)
print("Golongan: ",golongan)
print("Gaji pokok: ",gaji)
print("Bonus: ",bonus)
print("Gaji total: ",TotalGaji)