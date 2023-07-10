from tkinter import *
from tkinter import ttk


window = Tk()
window.title("Kalkulator Sederhana") #kamu bisa mengubah judul aplikasimu disini
window.resizable(False,False)
window.geometry('350x400') #ukuran window

input_frame = ttk.Frame()
input_frame.pack(padx=5,pady=0,fill="x",anchor=N,expand=True)

judul = ttk.Label(input_frame, text="SELAMAT DATANG COY",anchor=N,width=43)
judul1 = ttk.Label(input_frame, text="DI KALKULATOR SEDERHANA\n\n",anchor=N,width=43)
judul.pack(padx=5,pady=0,fill="x",anchor=N,expand=True)
judul1.pack(padx=5,pady=0,fill="x",anchor=N,expand=True)

# USER INPUT 1
isi1 = ttk.Label(input_frame, text="Masukkin Angkanya Coy:",anchor=N,width=43)
isi1.pack(padx=5,pady=1,fill="x",anchor=N,expand=True)

# KOLOM ENTRY 1
NILAI1 = StringVar()
angka1 = ttk.Entry(input_frame,textvariable=NILAI1)
angka1.pack(padx=0,pady=0,fill="none",expand=True)

# USER INPUT 2
isi2 = ttk.Label(input_frame, text="Masukkan Angkanya Lagi Coy:",anchor=N,width=43)
isi2.pack(padx=5,pady=1,fill="y",anchor=N,expand=True)

# KOLOM ENTRY 2
NILAI2 = StringVar()
angka2 = ttk.Entry(input_frame,textvariable=NILAI2)
angka2.pack(padx=0,pady=1,fill="y",expand=True)

# HASIL INPUT
isi3 = ttk.Label(input_frame, text=" Nih Hasilnya Coy :",anchor=N,width=43)
isi3.pack(padx=5,pady=1,fill="y",anchor=N,expand=True)

hasil = ttk.Label(input_frame, text="0",anchor=N,width=43)
hasil.pack(padx=5,pady=1,fill="y",anchor=N,expand=True)

warning = ttk.Label(input_frame, text="Woro-Woro: Untuk Pembagian 0 gak Bisa Ya Coy ",anchor=N,width=43,font=('Times',7))
warning.pack(padx=5,pady=1,fill="y",anchor=N,expand=True)

# OPERASI MATEMATIKA
def tambah():
    hasil.configure(text=(int(angka1.get())+int(angka2.get())))
 
def kurang():
    hasil.configure(text=(int(angka1.get())-int(angka2.get())))
 
def kali():
    hasil.configure(text=(int(angka1.get())*int(angka2.get())))
 
def bagi():
    hasil.configure(text=(int(angka1.get())/int(angka2.get())))


# TOMBOL
tombol_tambah = ttk.Button(input_frame,text="+",command=tambah)
tombol_tambah.pack(fill="x",expand=True,padx=5,pady=0)

tombol_kurang = ttk.Button(input_frame,text="-",command=kurang)
tombol_kurang.pack(fill="x",expand=True,padx=5,pady=0)

tombol_kali = ttk.Button(input_frame,text="X",command=kali)
tombol_kali.pack(fill="x",expand=True,padx=5,pady=0)

tombol_bagi = ttk.Button(input_frame,text=":",command=bagi)
tombol_bagi.pack(fill="x",expand=True,padx=5,pady=0)

pembuat = ttk.Label(input_frame, text="Ciptaan:\nRuspian Majid ",anchor=S,width=43,font=('Times',7))
pembuat.pack(padx=5,pady=20,fill="y",anchor=N,expand=True)

window.mainloop()