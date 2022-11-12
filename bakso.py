import datetime
import os
def clear(): #fungsi membersihkan layar
    os.system('cls') 
    
def pemesanan_bakso(): #fungsi pemesanan bakso

    print("selamat datang di toko bakso")
    nama = input("\nmasukan nama: ")
    waktu = datetime.datetime.now()
    pesanan = {}
    while True: #untuk perulangan program
        print('\n')
        print("1. bakso urat  Rp.10.000\n2. bakso telur  Rp.12.000\n3. mie ayam  Rp.10.000\n4. mie ayam bakso  Rp.15.000")
        nama_bakso = input("pesan bakso apa? ")

        if(nama_bakso == "bakso urat" or nama_bakso == "1"):
            print("bakso urat")
            jumlah1 = int(input("masukan jumlahnya:")) #masukan jumlahnya
            pesanan ['bakso urat'] = jumlah1
            total = int(jumlah1*10.000)
        elif (nama_bakso == "bakso telur" or nama_bakso == "2"):
            print("bakso telur")
            jumlah2 = int(input("masukan jumlahnya: "))
            pesanan  ['bakso telur'] = jumlah2
            total = int(jumlah2*12.000)
        elif (nama_bakso == "mie ayam" or nama_bakso == "3"):
            print("mie ayam")
            jumlah3 = int(input("masukan jumlahnya: "))
            pesanan  ['mie ayam'] = jumlah3
            total = int(jumlah3*10.000)
        elif (nama_bakso == "mie ayam bakso" or nama_bakso == "4"):
            print("mie ayam bakso")
            jumlah4 = int(input("masukan jumlahnya: "))
            pesanan ["mie ayam bakso"] = jumlah4
            total = int(jumlah4*15.000)
        print("\nPesanan saat ini: ", pesanan)
        ulang = input('apakah anda ingin pesan yang lain? (y)') #pertanyaan apakah anda ingin mengulang program

        if ulang == "y": #lanjutkan bila diketik y
            continue
        else:
            break
    print("\nAtas nama: ",nama)
    print("waktu pemesanan",waktu.strftime("tanggal: %d-%m-%Y jam: %H:%M:%S"))
    print("pesanan",pesanan)
    print("total", total)
clear()
pemesanan_bakso() 