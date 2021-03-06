# Library
import paho.mqtt.client as mqtt
import datetime
import time
import os

# Function untuk publish data
def publish(name, weight, package_type ):
    # IP broker yang akan dituju
    ip_broker = 'localhost'
    # Buat client baru
    client = mqtt.Client('Soang', clean_session=False)
    # Buat koneksi ke broker
    client.connect(ip_broker, port=3333)
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
    if package_type == 'Hemat':
        plus_hours = t + \
            datetime.timedelta(
                days=3) + datetime.timedelta(minutes=50) + datetime.timedelta(minutes=15)
        Pengembalian_Cucian = str(plus_hours.strftime(
            '%d-%m-%y')) + ' ('+str(plus_hours.strftime('%H:%M:%S'))+') '
    # Waktu 2 hari 55 menit setelah penjemputan cucian
    elif package_type == 'Reguler':
        plus_hours = t + \
            datetime.timedelta(
                days=2) + datetime.timedelta(minutes=55) + datetime.timedelta(minutes=15)
        Pengembalian_Cucian = str(plus_hours.strftime(
            '%d-%m-%y')) + ' ('+str(plus_hours.strftime('%H:%M:%S'))+') '
    # Waktu 1 hari 45 menit setelah penjemputan cucian
    elif package_type == 'Cepat':
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
    if package_type == 'Hemat':
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
    elif package_type == 'Standar':
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
    elif package_type == 'Cepat':
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
    client.publish('datalaundry', ''+Nama+'|'+submission+'|'+str_weight+'|'+ package_type +
                   '|'+laundry_pickup+'|'+Pengembalian_Cucian+'|'+price_str+'', qos=1, retain=False)

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
    weight = input('Berat       : ')
    # 3. Jenis Paket
    print('+-----------------------------------+')
    print('|            Tipe Paket             |')
    print('|-----------------------------------|')
    print('| 1. Paket Hemat                    |')
    print('| 2. Paket Standar                  |')
    print('| 3. Paket Cepat                    |')
    print('+-----------------------------------+')
    package_type = input('Jenis Paket : ')
    if package_type == 'Hemat' or package_type == 'Standar' or package_type == 'Cepat':
        publish(Nama, weight, package_type)
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
