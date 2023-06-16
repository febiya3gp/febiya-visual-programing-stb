import tkinter
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo

#inisialisasi
window = tkinter.Tk()
window.configure(bg="#E7A1B0")
icon_img = PhotoImage(file='C:\\latihanpython\\asset\\ramen.png')
window.iconphoto(False, icon_img)
window.geometry("500x300")
window.resizable(False,False)
window.title("Pendaftaran Mukbang")

#header
header_label = ttk.Label(window, text="Pengisian Formulir", font=(20), background="#B89773", foreground="white")
header_label.pack(pady=20)

#Variable dan Function
NAMA_LENGKAP = tkinter.StringVar()
ALAMAT_RUMAH = tkinter.StringVar()
HOBI = tkinter.StringVar()
MAKANAN_FAVORIT = tkinter.StringVar()
MINUMAN_FAVORIT = tkinter.StringVar()

#fungsi tombol
def tombol_click():
    if not NAMA_LENGKAP.get() or not ALAMAT_RUMAH.get() or not HOBI.get() or not MAKANAN_FAVORIT.get() or not MINUMAN_FAVORIT.get():
        showinfo(title="Error!", message="Mohon lengkapi semua form!")

    else:
        pesan = f"Hallo {NAMA_LENGKAP.get()}, Kamu sudah terdaftar!"
        showinfo(title="Selamat",message=pesan)

#frame input
style = ttk.Style()
style.configure("Custom.TEntry", fieldbackground="green")
input_frame = ttk.Frame(window)

#penempatan grid, pack, place
input_frame.pack(padx=10,pady=10,fill="x", expand=True)

#KOMPONEN nama lengkap
nama_depan_label = ttk.Label(input_frame, text="Nama Lengkap :")
nama_depan_label.pack(padx=10,fill="x", expand=True)
nama_depan_entry = ttk.Entry(input_frame, textvariable= NAMA_LENGKAP, style="Custom.TEntry")
nama_depan_entry.pack(padx=10,fill="x",expand=True)

#komponen alamat rumah
alamat_rumah_label = ttk.Label(input_frame, text="Alamat :")
alamat_rumah_label.pack(padx=10,fill="x", expand=True)
alamat_rumah_entry = ttk.Entry(input_frame, textvariable= ALAMAT_RUMAH)
alamat_rumah_entry.pack(padx=10,fill="x",expand=True)

#komponen hobi
hobi_label = ttk.Label(input_frame, text="Hobi :")
hobi_label.pack(padx=10,fill="x", expand=True)
hobi_entry = ttk.Entry(input_frame, textvariable= HOBI)
hobi_entry.pack(padx=10,fill="x",expand=True)

#komponen makanan favorit
makanan_label = ttk.Label(input_frame, text="Makanan Favorit :")
makanan_label.pack(padx=10,fill="x", expand=True)
makanan_entry = ttk.Entry(input_frame, textvariable= MAKANAN_FAVORIT)
makanan_entry.pack(padx=10,fill="x",expand=True)

#komponen minuman favorit
minuman_label = ttk.Label(input_frame, text="Minuman Favorit :")
minuman_label.pack(padx=10,fill="x", expand=True)
minuman_entry = ttk.Entry(input_frame, textvariable= MINUMAN_FAVORIT)
minuman_entry.pack(padx=10,fill="x",expand=True)

#TOMBOL
tombol_daftar = ttk.Button(input_frame,text="Daftar",command=tombol_click)
tombol_daftar.pack(fill="x",padx=10,pady=10, expand=True)

window.mainloop()