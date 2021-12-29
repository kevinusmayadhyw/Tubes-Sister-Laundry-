# Library
import paho.mqtt.client as mqtt
import datetime
import time
import os


# Function untuk publish data
def publish(nama, berat, tipe_paket):
    # Ip broker yang dituju
    ip_broker = 'localhost'
    # Buat client baru
    client = mqtt.Client('bandingwaktu', clean_session=False)
    # buat koneksi ke broker
    client.connect(ip_broker, port=4444)
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
    if tipe_paket == 'Hemat':
        plus_hours = t + \
            datetime.timedelta(
                days=3) + datetime.timedelta(minutes=5) + datetime.timedelta(minutes=10)
        Pengembalian_Cucian = str(plus_hours.strftime(
            '%d-%m-%y')) + ' ('+str(plus_hours.strftime('%H:%M:%S'))+') '
    # Waktu 2 hari 10 menit setelah penjemputan cucian
    elif tipe_paket == 'Standar':
        plus_hours = t + \
            datetime.timedelta(
                days=2) + datetime.timedelta(minutes=10) + datetime.timedelta(minutes=10)
        Pengembalian_Cucian = str(plus_hours.strftime(
            '%d-%m-%y')) + ' ('+str(plus_hours.strftime('%H:%M:%S'))+') '
    # Waktu 1 hari 5 menit setelah penjemputan cucian
    elif tipe_paket == 'Cepat':
        plus_hours = t + \
            datetime.timedelta(
                days=1) + datetime.timedelta(minutes=5) + datetime.timedelta(minutes=10)
        Pengembalian_Cucian = str(plus_hours.strftime(
            '%d-%m-%y')) + ' ('+str(plus_hours.strftime('%H:%M:%S'))+') '



    # Waktu pengembalian cucian Laundry Soang
    # Waktu 3 hari 50 menit setelah penjemputan cucian
    if tipe_paket == 'Hemat':
        plus_hours = t + \
            datetime.timedelta(
                days=3) + datetime.timedelta(minutes=50) + datetime.timedelta(minutes=15)
        Pengembalian_Cucian_t = str(plus_hours.strftime(
            '%d-%m-%y')) + ' ('+str(plus_hours.strftime('%H:%M:%S'))+') '
    # Waktu 2 hari 59 menit setelah penjemputan cucian
    elif tipe_paket == 'Standar':
        plus_hours = t + \
            datetime.timedelta(
                days=2) + datetime.timedelta(minutes=55) + datetime.timedelta(minutes=15)
        Pengembalian_Cucian_t = str(plus_hours.strftime(
            '%d-%m-%y')) + ' ('+str(plus_hours.strftime('%H:%M:%S'))+') '
    # Waktu 1 hari 45 menit setelah penjemputan cucian
    elif tipe_paket == 'Cepat':
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
    if tipe_paket == 'Hemat':
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
    elif tipe_paket == 'Standar':
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
    elif tipe_paket == 'Cepat':
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
    if tipe_paket == 'Hemat':
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
    elif tipe_paket == 'Standar':
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
    elif tipe_paket == 'Cepat':
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


# Main Program
loop = True
while loop:
    os.system('cls')
    print('')
    print('+-----------------------------------+')
    print('|       Inputkan data laundry       |')
    print('+-----------------------------------+')
    # 1. Nama
    Nama = input('Nama        : ')
    # 2. Berat
    Berat = input('Berat       : ')
    # 3. Jenis Paket
    print('+-----------------------------------+')
    print('|            Tipe Paket             |')
    print('|-----------------------------------|')
    print('| 1. Paket Hemat                    |')
    print('| 2. Paket Standar                  |')
    print('| 3. Paket Cepat                    |')
    print('+-----------------------------------+')
    Tipe_Paket = input('Jenis Paket : ')
    if Tipe_Paket == 'Hemat' or Tipe_Paket == 'Standar' or Tipe_Paket == 'Cepat':
        publish(Nama, Berat, Tipe_Paket)
        pil = input('Coba lagi ? [y/n] ')
        if pil == 'Y' or pil == 'y':
            time.sleep(3)
            loop = True
        else:
            loop = False
            time.sleep(3)
            print('')
            print('Program Selesai . . . . .')
    else:
        time.sleep(3)
        print('')
        print('+-----------------------------------+')
        print('|       Mohon maaf, input salah     |')
        print('+-----------------------------------+')
        pil = input('Coba lagi ? [Y/n] ')
        if pil == 'Y' or pil == 'y':
            time.sleep(3)
            loop = True
        else:
            loop = False
            time.sleep(3)
            print('')
            print('Program Selesai...')

