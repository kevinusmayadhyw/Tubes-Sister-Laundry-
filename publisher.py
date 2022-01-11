# Library
import paho.mqtt.client as mqtt
import datetime
import time
import os

# Function untuk publish data
def publishBojong(nama, berat, paket):
    # IP broker yang akan dituju

    ip = 'broker.emqx.io'

    # Buat client baru
    client = mqtt.Client('Bojong', clean_session=False)
    # Buat koneksi ke broker
    client.connect(ip, port=1883)
    # Proses komunikasi
    client.loop_start()
    print('')
    print('Melakukan publishing data kepada subscriber')
    time.sleep(3)
    print('')

    # waktu pengajuan cucian
    waktu_pengajuan = datetime.datetime.now()
    waktu_pengajuan_str = str(waktu_pengajuan.strftime('%d-%m-%y')) + \
        ' ('+str(waktu_pengajuan.strftime('%H:%M:%S'))+') '

    # waktu penjemputan cucian Laundry Bojong
    waktu_pengajuan_jemput = waktu_pengajuan + datetime.timedelta(minutes=10)
    waktu_pengajuan_jemput_str = str(waktu_pengajuan_jemput.strftime(
        '%d-%m-%y')) + ' ('+str(waktu_pengajuan_jemput.strftime('%H:%M:%S'))+') '

    # waktu Pengembalian cucian Laundry Bojong
    # waktu 3 hari 5 menit setelah penjemputan cucian
    if paket == 'hemat':
        waktu_pengembalian = waktu_pengajuan + \
            datetime.timedelta(
                days=3) + datetime.timedelta(minutes=5) + datetime.timedelta(minutes=10)
        waktu_pengembalian_str = str(waktu_pengembalian.strftime(
            '%d-%m-%y')) + ' ('+str(waktu_pengembalian.strftime('%H:%M:%S'))+') '
    # waktu 2 hari 10 menit setelah penjemputan cucian
    elif paket == 'standar':
        waktu_pengembalian = waktu_pengajuan + \
            datetime.timedelta(
                days=2) + datetime.timedelta(minutes=10) + datetime.timedelta(minutes=10)
        waktu_pengembalian_str = str(waktu_pengembalian.strftime(
            '%d-%m-%y')) + ' ('+str(waktu_pengembalian.strftime('%H:%M:%S'))+') '
    # waktu 1 hari 5 menit setelah penjemputan cucian
    elif paket == 'cepat':
        waktu_pengembalian = waktu_pengajuan + \
            datetime.timedelta(
                days=1) + datetime.timedelta(minutes=5) + datetime.timedelta(minutes=10)
        waktu_pengembalian_str = str(waktu_pengembalian.strftime(
            '%d-%m-%y')) + ' ('+str(waktu_pengembalian.strftime('%H:%M:%S'))+') '

    # Berat
    berat_float = float(berat)
    berat_str = str(berat_float) + ' Kg'

    # Harga Laundry Bojong
    # Jika menggunakan paket Hemat
    if paket == 'hemat':
        # Berat kurang dari atau sama dengan 1kg = berat x 6000 + 500
        if berat_float <= 1:
            harga_int = int(berat_float * 6000)
            harga_str = str(harga_int) + ' + 500 = ' + str((harga_int) + 500)
        # Berat lebih dari 1kg dan kurang dari atau sama dengan 2kg = berat x 9000 + 1000
        elif berat_float > 1 and berat_float <= 2:
            harga_int = int(berat_float * 9000)
            harga_str = str(harga_int) + ' + 1000 = ' + str((harga_int) + 1000)
        # Berat lebih dari 2kg = berat x 11000 + 1500
        else:
            harga_int = int(berat_float * 11000)
            harga_str = str(harga_int) + ' + 1500 = ' + str((harga_int) + 1500)

    # Jika menggunakan paket Standar
    elif paket == 'standar':
        # Berat kurang dari atau sama dengan 1kg = berat x 7000 + 1000
        if berat_float <= 1:
            harga_int = int(berat_float * 7000)
            harga_str = str(harga_int) + ' + 1000 = ' + str((harga_int) + 1000)
        # Berat lebih dari 1kg dan kurang dari atau sama dengan 2kg =  berat x 10000 + 1500
        elif berat_float > 1 and berat_float <= 2:
            harga_int = int(berat_float * 10000)
            harga_str = str(harga_int) + ' + 1500 = ' + str((harga_int) + 1500)
        # Berat lebih dari 2kg = berat x 12000 + 2000
        else:
            harga_int = int(berat_float * 12000)
            harga_str = str(harga_int) + ' + 2000 = ' + str((harga_int) + 2000)

    # Jika menggunakan paket Cepat
    elif paket == 'cepat':
        # Berat kurang dari atau sama dengan 1kg = berat x 10000 + 1500
        if berat_float <= 1:
            harga_int = int(berat_float * 10000)
            harga_str = str(harga_int) + ' + 1500 = ' + str((harga_int) + 1500)
        # Berat lebih dari 1kg dan kurang dari atau sama dengan 2kg = berat x 13000 + 2000
        elif berat_float > 1 and berat_float <= 2:
            harga_int = int(berat_float * 13000)
            harga_str = str(harga_int) + ' + 2000 = ' + str((harga_int) + 2000)
        # Berat lebih dari 2kg = berat x 15000 + 2500
        else:
            harga_int = int(berat_float * 15000)
            harga_str = str(harga_int) + ' + 2500 = ' + str((harga_int) + 2500)

    # Mempublish data ke client
    client.publish('datalaundry', ''+nama+'|'+waktu_pengajuan_str+'|'+berat_str+'|'+paket +
                   '|'+waktu_pengajuan_jemput_str+'|'+waktu_pengembalian_str+'|'+harga_str+'', qos=1, retain=False)

    client.loop_stop()

# Function untuk publish data
def publishSoang(nama, weight, package_type ):
    # IP broker yang akan dituju
    ip_broker = 'broker.emqx.io'
    # Buat client baru
    client = mqtt.Client('Soang', clean_session=False)
    # Buat koneksi ke broker
    client.connect(ip_broker, port=1883)
    # Proses komunikasi
    client.loop_start()
    print('')
    print('Melakukan publishing data terhadap subscriber')
    time.sleep(3)
    print('')

    # Waktu pengajuan cucian
    t = datetime.datetime.now()
    submission = str(t.strftime('%d-%m-%y')) + \
        ' ('+str(t.strftime('%H:%M:%S'))+') '

    # Waktu penjemputan cucian Laundry Soang
    plus_minutes = t + datetime.timedelta(minutes=15)
    laundry_pickup  = str(plus_minutes.strftime(
        '%d-%m-%y')) + ' ('+str(plus_minutes.strftime('%H:%M:%S'))+') '

    # Waktu pengembalian cucian
    # Waktu 3 hari 50 menit setelah penjemputan cucian
    if package_type == 'hemat':
        plus_hours = t + \
            datetime.timedelta(
                days=3) + datetime.timedelta(minutes=50) + datetime.timedelta(minutes=15)
        Pengembalian_Cucian = str(plus_hours.strftime(
            '%d-%m-%y')) + ' ('+str(plus_hours.strftime('%H:%M:%S'))+') '
    # Waktu 2 hari 55 menit setelah penjemputan cucian
    elif package_type == 'standar':
        plus_hours = t + \
            datetime.timedelta(
                days=2) + datetime.timedelta(minutes=55) + datetime.timedelta(minutes=15)
        Pengembalian_Cucian = str(plus_hours.strftime(
            '%d-%m-%y')) + ' ('+str(plus_hours.strftime('%H:%M:%S'))+') '
    # Waktu 1 hari 45 menit setelah penjemputan cucian
    elif package_type == 'cepat':
        plus_hours = t + \
            datetime.timedelta(
                days=1) + datetime.timedelta(minutes=45) + datetime.timedelta(minutes=15)
        Pengembalian_Cucian = str(plus_hours.strftime(
            '%d-%m-%y')) + ' ('+str(plus_hours.strftime('%H:%M:%S'))+') '

    # Berat cucian
    float_weight = float(weight)
    str_weight = str(float_weight) + 'Kg'

    # Harga Laundry Soang
    # Jika menggunakan paket Hemat
    if package_type == 'hemat':
        # Berat kurang dari atau sama dengan 1kg = berat x 5000 + 500
        if float_weight <= 1:
            price_int = int(float_weight * 5000)
            price_str = str(price_int) + ' + 500 = ' + str((price_int) + 500)
        # Berat lebih dari 1kg dan kurang dari atau sama dengan 2kg = berat x 7000 + 1000
        elif float_weight > 1 and float_weight <= 2:
            price_int = int(float_weight * 7000)
            price_str = str(price_int) + ' + 1000 = ' + str((price_int) + 1000)
        # Berat lebih dari 2kg = berat x 9000 + 1500
        else:
            price_int = int(float_weight * 9000)
            price_str = str(price_int) + ' + 1500 = ' + str((price_int) + 1500)

    # Jika menggunakan paket Standar
    elif package_type == 'standar':
        # Berat kurang dari atau sama dengan 1kg = berat x 6000 + 1000
        if float_weight <= 1:
            price_int = int(float_weight * 6000)
            price_str = str(price_int) + ' + 1000 = ' + str((price_int) + 1000)
        # Berat lebih dari 1kg dan kurang dari atau sama dengan 2kg = berat x 9000 + 1500
        elif float_weight > 1 and float_weight <= 2:
            price_int = int(float_weight * 9000)
            price_str = str(price_int) + ' + 1500 = ' + str((price_int) + 1500)
        # Berat lebih dari 2kg = berat x 11000 + 2000
        else:
            price_int = int(float_weight * 11000)
            price_str = str(price_int) + ' + 2000 = ' + str((price_int) + 2000)

    # Jika menggunakan paket Cepat
    elif package_type == 'cepat':
         # Berat kurang dari atau sama dengan 1kg = berat x 8000 + 1500
        if float_weight <= 1:
            price_int = int(float_weight * 8000)
            price_str = str(price_int) + ' + 1500 = ' + str((price_int) + 1500)
        # Berat lebih dari 1kg dan kurang dari atau sama dengan 2kg = berat x 10000 + 2000
        elif float_weight > 1 and float_weight <= 2:
            price_int = int(float_weight * 10000)
            price_str = str(price_int) + ' + 2000 = ' + str((price_int) + 2000)
        # Berat lebih dari 2kg = berat x 13000 + 2500
        else:
            price_int = int(float_weight * 13000)
            price_str = str(price_int) + ' + 2500 = ' + str((price_int) + 2500)

    # Melakukan publish data ke client
    client.publish('datalaundry', ''+nama+'|'+submission+'|'+str_weight+'|'+ package_type +
                   '|'+laundry_pickup+'|'+Pengembalian_Cucian+'|'+price_str+'', qos=1, retain=False)

    client.loop_stop()

    # Function untuk publish data
def publishBanding(nama, berat, tipe_paket):
    # Ip broker yang dituju
    ip_broker = 'broker.emqx.io'
    # Buat client baru
    client = mqtt.Client('bandingwaktu', clean_session=False)
    # buat koneksi ke broker
    client.connect(ip_broker, port=1883)
    # Proses komunikasi
    client.loop_start()
    print('')
    print('Melakukan upload data terhadap subscriber')
    time.sleep(3)
    print('')


    # Waktu Pengajuan Laundry Bojong dan Soang
    t = datetime.datetime.now()
    TW_Pengajuan = str(t.strftime('%d-%m-%y')) + \
        ' ('+str(t.strftime('%H:%M:%S'))+') '

    # Waktu penjemputan cucian Laundry Bojong
    plus_minutes = t + datetime.timedelta(minutes=10)
    jemput_Cucian = str(plus_minutes.strftime(
        '%d-%m-%y')) + ' ('+str(plus_minutes.strftime('%H:%M:%S'))+') '

    # Waktu penjemputan cucian Laundry Soang
    plus_minutes = t + datetime.timedelta(minutes=15)
    jemput_Cucian_t = str(plus_minutes.strftime(
        '%d-%m-%y')) + ' ('+str(plus_minutes.strftime('%H:%M:%S'))+') '



    # Waktu pengembalian cucian Laundry Bojong
    # Waktu 3 hari 5 menit setelah penjemputan cucian
    if tipe_paket == 'hemat':
        plus_hours = t + \
            datetime.timedelta(
                days=3) + datetime.timedelta(minutes=5) + datetime.timedelta(minutes=10)
        Pengembalian_Cucian = str(plus_hours.strftime(
            '%d-%m-%y')) + ' ('+str(plus_hours.strftime('%H:%M:%S'))+') '
    # Waktu 2 hari 10 menit setelah penjemputan cucian
    elif tipe_paket == 'standar':
        plus_hours = t + \
            datetime.timedelta(
                days=2) + datetime.timedelta(minutes=10) + datetime.timedelta(minutes=10)
        Pengembalian_Cucian = str(plus_hours.strftime(
            '%d-%m-%y')) + ' ('+str(plus_hours.strftime('%H:%M:%S'))+') '
    # Waktu 1 hari 5 menit setelah penjemputan cucian
    elif tipe_paket == 'cepat':
        plus_hours = t + \
            datetime.timedelta(
                days=1) + datetime.timedelta(minutes=5) + datetime.timedelta(minutes=10)
        Pengembalian_Cucian = str(plus_hours.strftime(
            '%d-%m-%y')) + ' ('+str(plus_hours.strftime('%H:%M:%S'))+') '



    # Waktu pengembalian cucian Laundry Soang
    # Waktu 3 hari 50 menit setelah penjemputan cucian
    if tipe_paket == 'hemat':
        plus_hours = t + \
            datetime.timedelta(
                days=3) + datetime.timedelta(minutes=50) + datetime.timedelta(minutes=15)
        Pengembalian_Cucian_t = str(plus_hours.strftime(
            '%d-%m-%y')) + ' ('+str(plus_hours.strftime('%H:%M:%S'))+') '
    # Waktu 2 hari 59 menit setelah penjemputan cucian
    elif tipe_paket == 'standar':
        plus_hours = t + \
            datetime.timedelta(
                days=2) + datetime.timedelta(minutes=55) + datetime.timedelta(minutes=15)
        Pengembalian_Cucian_t = str(plus_hours.strftime(
            '%d-%m-%y')) + ' ('+str(plus_hours.strftime('%H:%M:%S'))+') '
    # Waktu 1 hari 45 menit setelah penjemputan cucian
    elif tipe_paket == 'cepat':
        plus_hours = t + \
            datetime.timedelta(
                days=1) + datetime.timedelta(minutes=45) + datetime.timedelta(minutes=15)
        Pengembalian_Cucian_t = str(plus_hours.strftime(
            '%d-%m-%y')) + ' ('+str(plus_hours.strftime('%H:%M:%S'))+') '



    # Berat Laundry Bojong dan Soang
    float_berat = float(berat)
    str_berat = str(float_berat) + ' Kg'


    # Harga Laundry Bojong
    # Jika menggunakan paket Hemat
    if tipe_paket == 'hemat':
        # Berat kurang dari atau sama dengan 1kg = berat x 6000 + 500
        if float_berat <= 1:
            int_harga = int(float_berat * 6000)
            str_harga = str(int_harga) + ' + 500 = ' + str((int_harga) + 500)
        # Berat lebih dari 1kg dan kurang dari atau sama dengan 2kg = berat x 10000 + 1000
        elif float_berat > 1 and float_berat <= 2:
            int_harga = int(float_berat * 9000)
            str_harga = str(int_harga) + ' + 1000 = ' + str((int_harga) + 1000)
        # Berat lebih dari 2kg = berat x 12000 + 1500
        else:
            int_harga = int(float_berat * 11000)
            str_harga = str(int_harga) + ' + 1500 = ' + str((int_harga) + 1500)


    # Jika menggunakan paket Standar
    elif tipe_paket == 'standar':
        # Berat kurang dari atau sama dengan 1kg = berat x 8000 + 1000
        if float_berat <= 1:
            int_harga = int(float_berat * 7000)
            str_harga = str(int_harga) + ' + 1000 = ' + str((int_harga) + 1000)
        # Berat lebih dari 1kg dan kurang dari atau sama dengan 2kg =  berat x 11000 + 1500
        elif float_berat > 1 and float_berat <= 2:
            int_harga = int(float_berat * 10000)
            str_harga = str(int_harga) + ' + 1500 = ' + str((int_harga) + 1500)
        # Berat lebih dari 2kg = berat x 13000 + 2000
        else:
            int_harga = int(float_berat * 12000)
            str_harga = str(int_harga) + ' + 2000 = ' + str((int_harga) + 2000)


    # Jika menggunakan paket cepat
    elif tipe_paket == 'cepat':
        # Berat kurang dari atau sama dengan 1kg = berat x 9000 + 1500
        if float_berat <= 1:
            int_harga = int(float_berat * 10000)
            str_harga = str(int_harga) + ' + 1500 = ' + str((int_harga) + 1500)
        # Berat lebih dari 1kg dan kurang dari atau sama dengan 2kg = berat x 12000 + 2000
        elif float_berat > 1 and float_berat <= 2:
            int_harga = int(float_berat * 13000)
            str_harga = str(int_harga) + ' + 2000 = ' + str((int_harga) + 2000)
        # Berat lebih dari 2kg = berat x 14000 + 2500
        else:
            int_harga = int(float_berat * 15000)
            str_harga = str(int_harga) + ' + 2500 = ' + str((int_harga) + 2500)



   # Harga Laundry Soang
    # Jika menggunakan paket Hemat
    if tipe_paket == 'hemat':
        # Berat kurang dari atau sama dengan 1kg = berat x 7500 + 500
        if float_berat <= 1:
            int_harga = int(float_berat * 5000)
            str_harga_t = str(int_harga) + ' + 500 = ' + str((int_harga) + 500)
        # Berat lebih dari 1kg dan kurang dari atau sama dengan 2kg = berat x 11000 + 1000
        elif float_berat > 1 and float_berat <= 2:
            int_harga = int(float_berat * 7000)
            str_harga_t = str(int_harga) + ' + 1000 = ' + str((int_harga) + 1000)
        # Berat lebih dari 2kg = berat x 13000 + 1500
        else:
            int_harga = int(float_berat * 9000)
            str_harga_t = str(int_harga) + ' + 1500 = ' + str((int_harga) + 1500)


    # Jika menggunakan paket Standar
    elif tipe_paket == 'standar':
        # Berat kurang dari atau sama dengan 1kg = berat x 8500 + 1000
        if float_berat <= 1:
            int_harga = int(float_berat * 8000)
            str_harga_t = str(int_harga) + ' + 1000 = ' + str((int_harga) + 1000)
        # Berat lebih dari 1kg dan kurang dari atau sama dengan 2kg = berat x 12500 + 1500
        elif float_berat > 1 and float_berat <= 2:
            int_harga = int(float_berat * 9000)
            str_harga_t = str(int_harga) + ' + 1500 = ' + str((int_harga) + 1500)
        # Berat lebih dari 2kg = berat x 13500 + 2000
        else:
            int_harga = int(float_berat * 11000)
            str_harga_t = str(int_harga) + ' + 2000 = ' + str((int_harga) + 2000)


    # Jika menggunakan paket Cepat
    elif tipe_paket == 'cepat':
         # Berat kurang dari atau sama dengan 1kg = berat x 9500 + 1500
        if float_berat <= 1:
            int_harga = int(float_berat * 8000)
            str_harga_t = str(int_harga) + ' + 1500 = ' + str((int_harga) + 1500)
        # Berat lebih dari 1kg dan kurang dari atau sama dengan 2kg = berat x 13000 + 2000
        elif float_berat > 1 and float_berat <= 2:
            int_harga = int(float_berat * 10000)
            str_harga_t = str(int_harga) + ' + 2000 = ' + str((int_harga) + 2000)
        # Berat lebih dari 2kg = berat x 15000 + 2500
        else:
            int_harga = int(float_berat * 13000)
            str_harga_t = str(int_harga) + ' + 2500 = ' + str((int_harga) + 2500)


    # Mempublish data ke client
    client.publish('datalaundry', ''+'Bojong'+'|'+nama+'|'+TW_Pengajuan+'|'+str_berat+'|'+tipe_paket +
                   '|'+jemput_Cucian+'|'+Pengembalian_Cucian+'|'+str_harga+'', qos=1, retain=False)
    client.publish('datalaundry', ''+'Soang'+'|'+nama+'|'+TW_Pengajuan+'|'+str_berat+'|'+tipe_paket +
                   '|'+jemput_Cucian_t+'|'+Pengembalian_Cucian_t+'|'+str_harga_t+'', qos=1, retain=False)
    client.loop_stop()

def menu_laundry():
    loop = True
    l = []
    os.system('cls')
    print('')
    print('+-----------------------------------+')
    print('|       Inputkan data laundry       |')
    print('+-----------------------------------+')
    nama = input('Nama        : ')
    berat = input('Berat       : ')
    print('+-----------------------------------+')
    print('|            Tipe Paket             |')
    print('|-----------------------------------|')
    print('| 1. Paket Hemat                    |')
    print('| 2. Paket Standar                  |')
    print('| 3. Paket Cepat                    |')
    print('+-----------------------------------+')
    tipe = input('Jenis Paket : ')
    tipe = tipe.lower()
    if tipe == 'hemat' or tipe == 'standar' or tipe == 'cepat':
        l = [nama, berat, tipe]
    elif tipe == '1':
        l = [nama, berat, 'hemat']
    elif tipe == '2':
        l = [nama, berat, 'standar']
    elif tipe == '3':
        l = [nama, berat, 'cepat']
    return l
    os.system('cls')

def ulang():
    pil = input('Input lagi? [Y/n] ')
    pil = pil.lower()
    if pil == 'y':
        time.sleep(3)
        return True
    elif pil == 'n':
        time.sleep(3)
        print('')
        print('Program Selesai . . . . .')
        return False
    

def menu():
    berhenti = False
    while not(berhenti):
        print("=================================================")
        print("==               Publish Laundry               ==")
        print("=================================================")
        print("== NO |                  Menu                  ==")
        print("== 1  | Laundry Bojong                         ==")
        print("== 2  | Laundry Soang                          ==")
        print("== 3  | Perbandingan Laundry Bojong dan Soang  ==")
        print("== 4  | Keluar                                 ==")
        print("=================================================")
        pilihan = input("Masukan pilihan anda : ")
        loop = True
        if pilihan == "1":
            while loop:
                nama, berat, tipe = menu_laundry()
                publishBojong(nama, berat, tipe)
                loop = ulang()
            os.system('cls')
        elif pilihan == "2":
            while loop:
                nama, berat, tipe = menu_laundry()
                publishSoang(nama, berat, tipe)
                loop = ulang()
            os.system('cls')
        elif pilihan == "3":
            while loop:
                nama, berat, tipe = menu_laundry()
                publishBanding(nama, berat, tipe)
                loop = ulang()
            os.system('cls')
        elif pilihan == "4":
            berhenti = True
            print("...")
            os.system("cls")
            print("=================================================")
            print("==             Anda Berhasil Keluar            ==")
            print("=================================================")
            print("Mematikan program dalam 5 detik")
            for i in range(5):
                print(i+1)
                time.sleep(1)

            os.system("cls")
        else:
            print("Input yang anda masukan tidak tersedia")
            print("Mengembalikan ke menu utama dalam 2 detik")
            for i in range(2):
                print(i+1)
                time.sleep(1)
            os.system("cls")

# Main Program
os.system('cls')
menu()