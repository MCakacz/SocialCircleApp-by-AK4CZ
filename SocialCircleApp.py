import os

# Sprawdź, czy folder 'data' istnieje, jeśli nie, to go utwórz
if not os.path.exists('data'):
    os.makedirs('data')

def dodaj_znajomego():
    imie = input("Podaj imię znajomego: ")
    nazwisko = input("Podaj nazwisko znajomego: ")
    opis = input("Podaj opis znajomego: ")
    numer_telefonu = input("Podaj numer telefonu (opcjonalnie): ")
    linki_media = input("Podaj linki do mediów społecznościowych (opcjonalnie): ")

    with open('data/resources.txt', 'a') as plik:
        plik.write(f"Imię: {imie}\n")
        plik.write(f"Nazwisko: {nazwisko}\n")
        plik.write(f"Opis: {opis}\n")
        if numer_telefonu:
            plik.write(f"Numer telefonu: {numer_telefonu}\n")
        if linki_media:
            plik.write(f"Linki do mediów społecznościowych: {linki_media}\n")
        plik.write("\n")

def pokaz_liste_znajomych():
    try:
        with open('data/resources.txt', 'r') as plik:
            zawartosc = plik.read()
            print(zawartosc)
    except FileNotFoundError:
        print("Nie masz jeszcze żadnych znajomych.")

def zapisz_i_zamknij():
    print("Zapisywanie i zamykanie aplikacji...")
    # Możesz dodać tu kod, który zapewni odpowiednie zapisywanie i zamykanie aplikacji, jeśli to konieczne

if __name__ == "__main__":
    while True:
        print("\nWybierz opcję:")
        print("1. Dodaj znajomego")
        print("2. Pokaż listę znajomych")
        print("3. Zapisz i zamknij")
        
        wybor = input("Wprowadź numer opcji: ")

        if wybor == "1":
            dodaj_znajomego()
        elif wybor == "2":
            pokaz_liste_znajomych()
        elif wybor == "3":
            zapisz_i_zamknij()
            break
        else:
            print("Nieprawidłowa opcja. Wybierz ponownie.")
