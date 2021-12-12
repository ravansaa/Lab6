print('=====================================')
print('|    PROGRAM NILAI DATA MAHASISWA   |')
print('=====================================')

dict = {}
while True:
    print("Pilih Menu Yang Disediakan".center(40))
    print('=====================================')
    print('Input Data Nilai Mahasiswa'.center(40))
    print('=====================================')
    print('| (T) Tambah Data                    |')
    print('| (L) Lihat Data Mahasiswa           |')
    print('| (U) Ubah Data Mahasiswa            |')
    print('| (H) Hapus Data Mahasiswa           |')
    print('| (K) Keluar                         |')
    print('=====================================')
    data = input("[Masukan Pilihan] : ")

    if data == "l" or data == "L":

        def tampilkan():
            if dict.items():
                print("Daftar Nilai")
                print("="*73)
                print("|No. |    Nama    |     NIM     |  Tugas  |  UTS  |  UAS  |  Akhir       |")
                print("="*73)
                i = 0 
                for y in dict.items():
                    i += 1
                    print("| {no:2} | {0:10} | {1:11} | {2:5} | {3:5} | {4:7} | {5:7} |".format
                    (y[0][:50], y[1][0], y[1][1], y[1][2], y[1][3], y[1][4], no=i))   
                    print("="*73)     
            else:
                print("Daftar Nilai")
                print("="*73)
                print("|No. |    Nama    |     NIM     |  Tugas  |  UTS  |  UAS  |  Akhir       |")
                print("="*73)
                print("|                           TIDAK ADA DATA                               |") 
                print("="*73)
        tampilkan()  

    elif data == 't' or data == 'T':

        def tambah():
            print("Tambah Data")
            nama = input("Masukan Nama        : ")
            nim = int(input("Masukan NIM         : "))
            tugas = int(input("Nilai Tugas         : "))
            uts = int(input("Nilai UTS           : "))
            uas = int(input("Nilai UAS           : "))
            hasil = tugas * 0.30 + uts * 0.35 + uas * 0.35
            dict[nama] = nim, tugas, uts, uas, hasil
        tambah()

    elif data == 'u' or data == 'U':

        def ubah():
            print("Ubah Data")
            nama = input("Masukan Nama            : ")
            if nama in dict.keys():
                nim = int(input("Masukan NIM         : "))
                tugas = int(input("Nilai Tugas         : "))
                uts = int(input("Nilai UTS           : "))
                uas = int(input("Nilai UAS           : "))
                hasil = tugas * 0.30 + uts * 0.35 + uas * 0.35                
                dict[nama] = nim, tugas, uts, uas, hasil
            else:
                print("Nama {0} Tidak di Tentukan".format(nama))
        ubah()

    elif data == 'h' or data == 'H':

        def hapus():
            print("Hapus Data")
            nama = input("Masukan Nama      : ")    
            if nama in dict.keys():
                del dict[nama]
            else:
                print("Nama {0} Tidak di Temukan".format(nama))
        hapus()

    elif data == 'k' or data == 'K':

        def keluar():
            print("Terima Kasih")
        keluar()

        break
        
    else:
        print("Pilih Menu Yang Disediakan")