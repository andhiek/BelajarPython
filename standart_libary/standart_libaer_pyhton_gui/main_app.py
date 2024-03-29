# Standart python libary GUI

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
# window.resizable(False, False)

window.title("hello world")

NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()


# Frame input
input_frame = ttk.Frame(window)
# penempatam grid,Pack,Place
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# komponen - komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text="NAMA DEPAN:")
nama_depan_label.pack(padx=10, fill="x", expand=True)


# 2. ENTRY NAMA DEPAN
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, pady=5, fill="x", expand=True)

# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="NAMA BELAKANG:")
nama_belakang_label.pack(padx=10, pady=5, fill="x", expand=True)

# 4. ENTRY NAMA BELAKANG
NAMA_BELAKANG = tk.StringVar()
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)

# 5 . MEMBUAT TOMBOL
# fungsi tombol click


def tombol_click():
    '''fungsi ini akan dipanggil oleh tombol'''
    pesan = f"halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()},Terima kasih!!!"
    showinfo(title="Pesan!!", message=pesan)


tombol_submit = ttk.Button(input_frame, text="Submit", command=tombol_click)
tombol_submit.pack(padx=10, pady=10, fill='x', expand=True)
window.mainloop()
