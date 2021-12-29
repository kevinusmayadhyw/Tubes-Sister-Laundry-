import paho.mqtt.client as mqtt
import time
from prettytable import PrettyTable
from IPython.display import clear_output
from tabulate import tabulate
import os

def laundrybojong():
    databojong = []

    def on_connect_laundrybojong(client, userdata, flags, rc):
        print("Menghubungkan ke Laundry Bojong dalam 3 detik")
        for i in range(3):
            print("...")
            time.sleep(1)
        print('Terhubung ke Laundry Bojong...')

    def on_message_laundrybojong(client, userdata, message):
        print('')
        data = str(message.payload.decode('utf-8')).split('|')
        databojong.append(data)
        clear_output(wait=True)
        os.system('cls')
        print("====================================================================================================================================================")
        print("==                                                                Data Laundry Bojong                                                             ==")
        print("====================================================================================================================================================")
        no = range(1, len(databojong)+1)
        print("")
        header=['    Nama    ', '     Waktu Pengajuan     ', '  Berat  ', 'Jenis Paket', '    Penjemputan   ', '    Pengembalian   ', '      Total Harga      ']
        print(tabulate(data, header, tablefmt='fancy_grid', showindex=no))

    broker_address = 'localhost'
    client = mqtt.Client('laundrybojong', clean_session=True)

    client.on_connect = on_connect_laundrybojong
    client.on_message = on_message_laundrybojong
    client.connect(broker_address, port=2222)

    client.loop_start()
    client.subscribe('datalaundry', qos=1)

    while True:
        time.sleep(1)

    client.loop_stop()

def laundrysoang():
    datasoang = []

    def on_connect_laundrysoang(client, userdata, flags, rc):
        print("Menghubungkan ke Laundry Soang dalam 3 detik")
        for i in range(3):
            print("...")
            time.sleep(1)
        print('Terhubung ke Laundry Soang...')

    def on_message_laundrysoang(client, userdata, message):
        print('')
        data = str(message.payload.decode('utf-8')).split('|')
        datasoang.append(data)
        clear_output(wait=True)
        os.system('cls')
        print("====================================================================================================================================================")
        print("==                                                                Data Laundry Soang                                                              ==")
        print("====================================================================================================================================================")
        no = range(1, len(datasoang)+1)
        print("")
        header=['    Nama    ', '     Waktu Pengajuan     ', '  Berat  ', 'Jenis Paket', '    Penjemputan   ', '    Pengembalian   ', '      Total Harga      ']
        print(tabulate(datasoang, header, tablefmt='fancy_grid', showindex=no))

    broker_address = 'localhost'
    client = mqtt.Client('laundrysoang', clean_session=True)

    client.on_connect = on_connect_laundrysoang
    client.on_message = on_message_laundrysoang
    client.connect(broker_address, port=3333)

    client.loop_start()
    client.subscribe('datalaundry', qos=1)

    while True:
        time.sleep(1)

    client.loop_stop()

def perbandingan():
    dataperbandingan = []

    def on_connect_bandingwaktu(client, userdata, flags, rc):
        print("Menghubungkan ke perbandingan dalam 3 detik")
        for i in range(3):
            print("...")
            time.sleep(1)
        print('Terhubung ke Perbandingan Laundry Bojong dan Soang...')

    def on_message_bandingwaktu(client, userdata, message):
        print('')
        data = str(message.payload.decode('utf-8')).split('|')
        dataperbandingan.append(data)
        clear_output(wait=True)
        os.system('cls')
        print("====================================================================================================================================================")
        print("==                                                       Perbandingan Laundry Bojong dan Soang                                                    ==")
        print("====================================================================================================================================================")
        print("")
        header=['    Nama    ', '     Waktu Pengajuan     ', '  Berat  ', 'Jenis Paket', '    Penjemputan   ', '    Pengembalian   ', '      Total Harga      ']
        print(tabulate(dataperbandingan, header, tablefmt='fancy_grid'))
        print('')

    broker_address = 'localhost'
    client = mqtt.Client('BandingWaktu', clean_session=True)

    client.on_connect = on_connect_bandingwaktu
    client.on_message = on_message_bandingwaktu
    client.connect(broker_address, port=4444)

    client.loop_start()
    client.subscribe('datalaundry', qos=1)

    while True:
        time.sleep(1)

    client.loop_stop()


def menu():
    berhenti = False
    while not(berhenti):
        print("=================================================")
        print("==                   Laundry                   ==")
        print("=================================================")
        print("== NO |                  Menu                  ==")
        print("== 1  | Laundry Bojong                         ==")
        print("== 2  | Laundry Soang                          ==")
        print("== 3  | Perbandingan Laundry Bojong dan Soang  ==")
        print("== 4  | Keluar                                 ==")
        print("=================================================")
        pilihan = input("Masukan pilihan anda : ")
        if pilihan == "1":
            laundrybojong()
        elif pilihan == "2":
            laundrysoang()
        elif pilihan == "3":
            perbandingan()
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
            

os.system('cls')
menu()
