import os
import tkinter as tk
from tkinter import messagebox, scrolledtext

# Funkcje operujące na danych
def dodaj_znajomego():
    imie = imie_entry.get()
    nazwisko = nazwisko_entry.get()
    opis = opis_entry.get()
    numer_telefonu = numer_telefonu_entry.get()
    linki_media = linki_media_entry.get()

    if imie and nazwisko and opis:
        with open('data/resources.txt', 'a') as plik:
            plik.write(f"Imię: {imie}\n")
            plik.write(f"Nazwisko: {nazwisko}\n")
            plik.write(f"Opis: {opis}\n")
            if numer_telefonu:
                plik.write(f"Numer telefonu: {numer_telefonu}\n")
            if linki_media:
                plik.write(f"Linki do mediów społecznościowych: {linki_media}\n")
            plik.write("\n")
        messagebox.showinfo("Dodano znajomego", "Znajomy został dodany.")
        wyczysc_pola()
    else:
        messagebox.showerror("Błąd", "Imię, nazwisko i opis są wymagane.")

def pokaz_liste_znajomych():
    try:
        with open('data/resources.txt', 'r') as plik:
            zawartosc = plik.read()
            pokaz_okno_z_listą(zawartosc)
    except FileNotFoundError:
        messagebox.showinfo("Lista znajomych", "Nie masz jeszcze żadnych znajomych.")

def zapisz_i_zamknij():
    okno.destroy()

def wyczysc_pola():
    imie_entry.delete(0, tk.END)
    nazwisko_entry.delete(0, tk.END)
    opis_entry.delete(0, tk.END)
    numer_telefonu_entry.delete(0, tk.END)
    linki_media_entry.delete(0, tk.END)

def pokaz_okno_z_listą(zawartosc):
    okno_lista = tk.Toplevel(okno)
    okno_lista.title("Lista znajomych")

    pole_tekstowe = scrolledtext.ScrolledText(okno_lista, wrap=tk.WORD, width=40, height=20)
    pole_tekstowe.insert(tk.END, zawartosc)
    pole_tekstowe.configure(state='disabled')
    pole_tekstowe.pack(fill=tk.BOTH, expand=True)

# Tworzenie głównego okna aplikacji
okno = tk.Tk()
okno.title("Aplikacja Znajomi")

# Tworzenie etykiet i pól tekstowych
imie_label = tk.Label(okno, text="Imię:")
nazwisko_label = tk.Label(okno, text="Nazwisko:")
opis_label = tk.Label(okno, text="Opis:")
numer_telefonu_label = tk.Label(okno, text="Numer telefonu:")
linki_media_label = tk.Label(okno, text="Linki do mediów społecznościowych:")

imie_entry = tk.Entry(okno)
nazwisko_entry = tk.Entry(okno)
opis_entry = tk.Entry(okno)
numer_telefonu_entry = tk.Entry(okno)
linki_media_entry = tk.Entry(okno)

# Tworzenie przycisków
dodaj_przycisk = tk.Button(okno, text="Dodaj znajomego", command=dodaj_znajomego)
pokaz_przycisk = tk.Button(okno, text="Pokaż listę znajomych", command=pokaz_liste_znajomych)
zapisz_i_zamknij_przycisk = tk.Button(okno, text="Zapisz i zamknij", command=zapisz_i_zamknij)

# Umieszczenie elementów w oknie
imie_label.grid(row=0, column=0)
nazwisko_label.grid(row=1, column=0)
opis_label.grid(row=2, column=0)
numer_telefonu_label.grid(row=3, column=0)
linki_media_label.grid(row=4, column=0)

imie_entry.grid(row=0, column=1)
nazwisko_entry.grid(row=1, column=1)
opis_entry.grid(row=2, column=1)
numer_telefonu_entry.grid(row=3, column=1)
linki_media_entry.grid(row=4, column=1)

dodaj_przycisk.grid(row=5, column=0, columnspan=2)
pokaz_przycisk.grid(row=6, column=0, columnspan=2)
zapisz_i_zamknij_przycisk.grid(row=7, column=0, columnspan=2)

# Uruchomienie pętli głównej
okno.mainloop()
