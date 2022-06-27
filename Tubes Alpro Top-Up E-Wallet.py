import tkinter as tk
from functools import partial

def topup1(label_result, saldo):
    while True:
        try:
            saldo = (saldo.get())
            result = int(saldo) + 25000
            label_result.config(text="Saldo Anda Sekarang Rp %d" % result)
            return
        except ValueError:
            tk.Label(root, text="Input Saldo Dalam Bentuk Angka").grid(row=7, column=1)

def topup2(label_result, saldo):
    while True:
        try:
            saldo = (saldo.get())
            result = int(saldo) + 50000
            label_result.config(text="Saldo Anda Sekarang Rp %d" % result)
            return
        except ValueError:
            tk.Label(root, text="Input Saldo Dalam Bentuk Angka").grid(row=7, column=1)

def topup3(label_result, saldo):
    while True:
        try:
            saldo = (saldo.get())
            result = int(saldo) + 100000
            label_result.config(text="Saldo Anda Sekarang Rp %d" % result)
            return
        except ValueError:
            tk.Label(root, text="Input Saldo Dalam Bentuk Angka").grid(row=7, column=1)

def topup4(label_result, saldo):
   while True:
        try:
            saldo = (saldo.get())
            result = int(saldo) + 250000
            label_result.config(text="Saldo Anda Sekarang Rp %d" % result)
            return
        except ValueError:
            tk.Label(root, text="Input Saldo Dalam Bentuk Angka").grid(row=7, column=1)

def topup5(label_result, saldo):
    while True:
        try:
            saldo = (saldo.get())
            result = int(saldo) + 500000
            label_result.config(text="Saldo Anda Sekarang Rp %d" % result)
            return
        except ValueError:
            tk.Label(root, text="Input Saldo Dalam Bentuk Angka").grid(row=7, column=1)

def topup6(label_result, saldo):
    while True:
        try:
            saldo = (saldo.get())
            result = int(saldo) + 1000000
            label_result.config(text="Saldo Anda Sekarang Rp %d" % result)
            return
        except ValueError:
            tk.Label(root, text="Input Saldo Dalam Bentuk Angka").grid(row=7, column=1)

root = tk.Tk()
root.geometry('500x200')
root.title('Top-Up E-Wallet Application')

saldo = tk.StringVar()

labelTitle = tk.Label(root, text="Aplikasi Top-Up Saldo E-Wallet").grid(row=0, column=1)
labelSaldo = tk.Label(root, text="Silakan Input Saldo E-Wallet Saat Ini").grid(row=1, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=7, column=1)

entrysaldo = tk.Entry(root, textvariable=saldo).grid(row=1, column=1)
topup1 = partial(topup1, labelResult, saldo)
button1 = tk.Button(root, text="Rp25.000", command=topup1).grid(row=3, column=0)
topup2 = partial(topup2, labelResult, saldo)
button2 = tk.Button(root, text="Rp50.000", command=topup2).grid(row=3, column=1)
topup3 = partial(topup3, labelResult, saldo)
button3 = tk.Button(root, text="Rp100.000", command=topup3).grid(row=3, column=2)
topup4 = partial(topup4, labelResult, saldo)
button4 = tk.Button(root, text="Rp250.000", command=topup4).grid(row=5, column=0)
topup5 = partial(topup5, labelResult, saldo)
button5 = tk.Button(root, text="Rp500.000", command=topup5).grid(row=5, column=1)
topup6 = partial(topup6, labelResult, saldo)
button6 = tk.Button(root, text="Rp1.000.000", command=topup6).grid(row=5, column=2)

pilihan = None
def top1():
    global pilihan
    pilihan == button1
def top2():
    global pilihan
    pilihan == button2
def top3():
    global pilihan
    pilihan == button3
def top4():
    global pilihan
    pilihan == button4
def top5():
    global pilihan
    pilihan == button5
def top6():
    global pilihan
    pilihan == button6

def choice():
    global choice
    if pilihan == button1:
        topup1()
    elif pilihan ==button2:
        topup2()
    elif pilihan ==button3:
        topup3()
    elif pilihan ==button4:
        topup4()
    elif pilihan ==button5:
        topup5()
    elif pilihan ==button6:
        topup6()
    else:
        tk.Label(root, text="Pilih Tombol yang Tersedia").grid(row=7, column=1)

root.mainloop()