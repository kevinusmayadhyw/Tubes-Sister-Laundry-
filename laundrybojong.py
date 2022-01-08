# Library
import paho.mqtt.client as mqtt
import datetime
import time
import os

# Function untuk publish data
def publish(nama, berat, paket):
    # IP broker yang akan dituju

    ip = '26.106.194.199'

    # Buat client baru
    client = mqtt.Client('Bojong', clean_session=False)
    # Buat koneksi ke broker
    client.connect(ip, port=2222)
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
    if paket == 'Hemat':
        waktu_pengembalian = waktu_pengajuan + \
            datetime.timedelta(
                days=3) + datetime.timedelta(minutes=5) + datetime.timedelta(minutes=10)
        waktu_pengembalian_str = str(waktu_pengembalian.strftime(
            '%d-%m-%y')) + ' ('+str(waktu_pengembalian.strftime('%H:%M:%S'))+') '
    # waktu 2 hari 10 menit setelah penjemputan cucian
    elif paket == 'Standar':
        waktu_pengembalian = waktu_pengajuan + \
            datetime.timedelta(
                days=2) + datetime.timedelta(minutes=10) + datetime.timedelta(minutes=10)
        waktu_pengembalian_str = str(waktu_pengembalian.strftime(
            '%d-%m-%y')) + ' ('+str(waktu_pengembalian.strftime('%H:%M:%S'))+') '
    # waktu 1 hari 5 menit setelah penjemputan cucian
    elif paket == 'Cepat':
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
    if paket == 'Hemat':
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
    elif paket == 'Standar':
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
    elif paket == 'Cepat':
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
    paket = input('Jenis Paket : ')

    if paket == 'Hemat' or paket == 'Standar' or paket == 'Cepat':
        publish(Nama, Berat, paket)
        pil = input('Coba lagi? [Y/n] ')
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
        pil = input('Coba lagi? [Y/n] ')
        if pil == 'Y' or pil == 'y':
            time.sleep(3)
            loop = True
        else:
            loop = False
            time.sleep(3)
            print('')
            print('Program Selesai...')