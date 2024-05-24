def TampilData(ListData):
    for x, y in ListData.items():
        print("NPM : "+str(x)+" Nama: "+y['name']+" Angkatan: "+str(y['year'])+" Alamat: "+y['alamat'])

def tambah_data():
    npm = input("Inputkan NPM: ")
    if npm not in mahasiswa:
        nama = input("Inputkan Nama: ")
        angkatan = input("Angkatan: ")
        alamat = input("Alamat: ")
        dataupdate = {npm: {"name": nama, "year": int(angkatan), "alamat": alamat}}
        mahasiswa.update(dataupdate)
    else:
        print("NPM sudah terdaftar.")

def hapus_data():
    npm = input("Hapus data by NPM: ")
    if npm in mahasiswa:
        mahasiswa.pop(npm)
    else:
        print("NPM tidak ditemukan.")

def update_data():
    npm = input("Update data by NPM: ")
    if npm in mahasiswa:
        nama = input("Inputkan Nama: ")
        angkatan = input("Angkatan: ")
        alamat = input("Alamat: ")
        dataupdate = {npm: {"name": nama, "year": int(angkatan), "alamat": alamat}}
        mahasiswa.update(dataupdate)
    else:
        print("NPM tidak ditemukan.")

def tampil_menu():
    print("Tampil Data Mahasiswa")
    for x, y in mahasiswa.items():
        print("NPM : "+str(x)+" Nama: "+y['name']+" Angkatan: "+str(y['year'])+" Alamat: "+y['alamat'])
    print("\nPilih Menu")
    print("1. Tambah Data Baru")
    print("2. Hapus Data by NPM")
    print("3. Update Data by NPM")
    print("4. Exit")

mahasiswa = {
    "1": {"name": "Dea", "year": 2004, "alamat": "Jakarta"},
    "2": {"name": "Nabila", "year": 2004, "alamat": "Yogyakarta"},
    "3": {"name": "Sofi", "year": 2005, "alamat": "Lampung"},
}

while True:
    tampil_menu()
    pilihan = int(input("Pilih Menu: "))
    if pilihan == 1:
        tambah_data()
    elif pilihan == 2:
        hapus_data()
    elif pilihan == 3:
        update_data()
    elif pilihan == 4:
        break
    else:
        print("Pilihan tidak valid.")