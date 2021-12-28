# Library
import paho.mqtt.client as mqtt
import time
from prettytable import PrettyTable
from tabulate import tabulate
from IPython.display import clear_output
import os

# Function untuk Main Menu
def menu():
    t = PrettyTable(['No', 'Menu'])
    t.add_row(['01', 'Subscribe ke Laundry Bojong (menggunakan port 2222)'])
    t.add_row(['02', 'Subscribe ke Laundry Soang  (menggunakan port 3333)'])
    t.add_row(['03', 'Subscribe untuk Perbandingan Waktu (menggunakan port 4444)'],)
    t.add_row(['04', 'Keluar'])
    t.align = 'l'
    print(t)

# Menu 1 untuk Laundry Bojong
def laundrybojong():
    # Simpan data laundry
    list = []

    # Function untuk memberikan pesan kepada client lain jika terconnect dengan laundry bojong
    def on_connect_laundrybojong(client, userdata, flags, rc):
        time.sleep(1.5)
        print('')
        print('Terhubung ke Laundry Bojong...')

    # Function untuk mengambil data dari laundry bojong, kemudian menampilkannya
    def on_message_laundrybojong(client, userdata, message):
        print('')
        data = str(message.payload.decode('utf-8')).split('|')
        list.append(data)
        clear_output(wait=True)
        os.system('cls')
        print('+----------------------------------------------------------------------------------------------------------------------------------------------+')
        print('|                                                              Data Laundry Bojong                                                             |')
        nomer_list = range(1, len(list)+1)
        print(tabulate(list, headers=[
            '    Nama    ', 'Tanggal & Waktu Pengajuan', '  Berat  ', 'Jenis Paket', 'Penjemputan Cucian', 'Pengembalian Cucian', '      Total Harga      '], tablefmt='pretty', showindex=nomer_list))

        # Membuat log
        # text_file = open('laundrybojong.txt', 'a')
        # # text_file.write(
        # #     '+----------------------------------------------------------------------------------------------------------------------------------------------+'+'\n')
        # # text_file.write(
        # #     '|                                                              DATA LAUNDRY-AN BOJONG                                                          |'+'\n')
        # # text_file.write(
        # #     '+----------------------------------------------------------------------------------------------------------------------------------------------+'+'\n')
        # # text_file.write('|     '+data[0]+'     |  '+data[1]+' |    '+data[2] + '    |    ' +
        # #                 data[3]+'    |  '+data[4]+' |  '+data[5]+' |   '+data[6]+'  |'+'\n')
        # text_file.write(data[0]+', '+data[1]+', '+data[2] + ', ' +
        #                 data[3]+', '+data[4]+', '+data[5]+', '+data[6]+'\n')
        # text_file.write(
        #     '----------------------------------------------------------------------------------------------------------------------------------'+'\n')
        # text_file.close()

    # Set ip_broker & buat client
    ip_broker = 'localhost'
    client = mqtt.Client('laundrybojong', clean_session=True)

    # Mengirim pesan ketika connect dan mengambil pesan dari Laundry Bojong
    client.on_connect = on_connect_laundrybojong
    client.on_message = on_message_laundrybojong
    client.connect(ip_broker, port=2222)

    client.loop_start()
    # Topik = datalaundry
    client.subscribe('datalaundry', qos=1)

    while True:
        time.sleep(1)

    client.loop_stop()



# Menu 2 untuk Laundry Soang
def laundrysoang():
    # Simpan data laundry
    list = []

    # Function untuk memberikan pesan kepada client lain jika terconnect dengan laundry soang
    def on_connect_laundrysoang(client, userdata, flags, rc):
        time.sleep(1.5)
        print('')
        print('Terhubung ke Laundry Soang')

    # Function untuk mengambil data dari laundry soang, kemudian menampilkannya
    def on_message_laundrysoang(client, userdata, message):
        print('')
        data = str(message.payload.decode('utf-8')).split('|')
        list.append(data)
        clear_output(wait=True)
        os.system('cls')
        print('+----------------------------------------------------------------------------------------------------------------------------------------------+')
        print('|                                                              Data Laundry Soang                                                              |')
        nomer_list = range(1, len(list)+1)
        print(tabulate(list, headers=[
            '    Nama    ', 'Tanggal & Waktu Pengajuan', '  Berat  ', 'Jenis Paket', 'Penjemputan Cucian', 'Pengembalian Cucian', '      Total Harga      '], tablefmt='pretty', showindex=nomer_list))

        # Membuat log
        # text_file = open('laundrysoang.txt', 'a')
        # # text_file.write(
        # #     '+----------------------------------------------------------------------------------------------------------------------------------------------+'+'\n')
        # # text_file.write(
        # #     '|                                                              DATA LAUNDRY-AN  SOANG                                                          |'+'\n')
        # # text_file.write(
        # #     '+----------------------------------------------------------------------------------------------------------------------------------------------+'+'\n')
        # # text_file.write('|     '+data[0]+'     |  '+data[1]+' |    '+data[2] + '    |    ' +
        # #                 data[3]+'    |  '+data[4]+' |  '+data[5]+' |   '+data[6]+'  |'+'\n')
        # text_file.write(data[0]+', '+data[1]+', '+data[2] + ', ' +
        #                 data[3]+', '+data[4]+', '+data[5]+', '+data[6]+'\n')
        # text_file.write(
        #     '----------------------------------------------------------------------------------------------------------------------------------'+'\n')
        # text_file.close()

    # Set ip_broker & buat client
    ip_broker = 'localhost'
    client = mqtt.Client('laundrysoang', clean_session=True)

    # Mengirim pesan ketika connect dan mengambil pesan dari laundry soang
    client.on_connect = on_connect_laundrysoang
    client.on_message = on_message_laundrysoang
    client.connect(ip_broker, port=3333)

    client.loop_start()
    # Topik = datalaundry
    client.subscribe('datalaundry', qos=1)

    while True:
        time.sleep(1)

    client.loop_stop()



# Menu 3 untuk Banding Waktu
def bandingwaktu():
    # Simpan data banding waktu
    list = []

    # Function untuk memberikan pesan kepada client lain jika terconnect dengan banding waktu
    def on_connect_bandingwaktu(client, userdata, flags, rc):
        time.sleep(1.5)
        print('')
        print('Terhubung ke Perbandingan Waktu')

    # Function untuk mengambil data dari banding waktu, kemudian menampilkannya
    def on_message_bandingwaktu(client, userdata, message):
        print('')
        data = str(message.payload.decode('utf-8')).split('|')
        list.append(data)
        clear_output(wait=True)
        os.system('cls')
        print('+------------------------------------------------------------------------------------------------------------------------------------------------------+')
        print('|                                                                  Perbandingan Waktu Laundry                                                          |')
        print(tabulate(list, headers=[' Laundry ', '    Nama    ', 'Tanggal & Waktu Pengajuan', '  Berat  ',
              'Jenis Paket', 'Penjemputan Cucian', 'Pengembalian Cucian', '      Total Harga      '], tablefmt='pretty'))
        print('')

        # Membuat log
        # text_file = open('bandingwaktu.txt', 'a')
        # # text_file.write(
        # #     '+----------------------------------------------------------------------------------------------------------------------------------------------+'+'\n')
        # # text_file.write(
        # #     '|                                                              DATA LAUNDRY-AN BOJONG                                                          |'+'\n')
        # # text_file.write(
        # #     '+----------------------------------------------------------------------------------------------------------------------------------------------+'+'\n')
        # # text_file.write('|     '+data[0]+'     |  '+data[1]+' |    '+data[2] + '    |    ' +
        # #                 data[3]+'    |  '+data[4]+' |  '+data[5]+' |   '+data[6]+'  |'+'\n')
        # text_file.write(data[0]+', '+data[1]+', '+data[2] + ', ' +
        #                 data[3]+', '+data[4]+', '+data[5]+', '+data[6]+', '+data[7]+'\n')
        # text_file.write(
        #     '----------------------------------------------------------------------------------------------------------------------------------'+'\n')
        # text_file.close()

    # Set ip_broker & buat client
    ip_broker = 'localhost'
    client = mqtt.Client('BandingWaktu', clean_session=True)

    # Mengirim pesan ketika connect dan mengambil pesan dari kedua laundry
    client.on_connect = on_connect_bandingwaktu
    client.on_message = on_message_bandingwaktu
    client.connect(ip_broker, port=4444)

    client.loop_start()
    # Topik = datalaundry
    client.subscribe('datalaundry', qos=1)

    while True:
        time.sleep(1)

    client.loop_stop()



# Menu 4 untuk keluar dari program
def exit():
    time.sleep(3)
    print('')
    print('Keluar dari program...')


# Akses menuju main program, untuk memilih pilihan Laundry Bojong, Laundry Soang, Perbandingan Waktu, dan keluar dari program
os.system('cls')
menu()
loop = True
while loop:
    pil = input('Masukan pilihan anda : ')
    if pil == '01':
        laundrybojong()
    elif pil == '02':
        laundrysoang()
    elif pil == '03':
        bandingwaktu()
    elif pil == '04':
        loop = False
        exit()
    else:
        time.sleep(3)
        print('')
        print('+-------------------------------+')
        print('|    Mohon maaf, input salah    |')
        print('+-------------------------------+')
        pil = input('Coba lagi? [Y/n] ')
        time.sleep(3)
        if pil == 'Y' or pil == 'y':
            os.system('cls')
            menu()
        else:
            loop = False
            time.sleep(3)
            print('')
            print('Program berhenti')
