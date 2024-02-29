import os
import shutil

def find_file(nazwa_pliku, katalog):
    for root, dirs, files in os.walk(katalog):
        if nazwa_pliku in files:
            return os.path.join(root, nazwa_pliku)
    return None

def cp_linuxowe(nazwa_pliku, katalog_zrodlowy, sciezka_docelowa):
    sciezka_pliku = find_file(nazwa_pliku, katalog_zrodlowy)
    if sciezka_pliku:
        shutil.copy(sciezka_pliku, sciezka_docelowa)
        print(f"Plik {nazwa_pliku} został skopiowany do {sciezka_docelowa}")
    else:
        print(f"Nie można znaleźć pliku {nazwa_pliku} w {katalog_zrodlowy}")

nazwa_pliku = input("Podaj nazwę pliku, który chcesz skopiować: ")
katalog_zrodlowy = input("Podaj pełną ścieżkę do katalogu źródłowego: ")
sciezka_docelowa = input("Podaj pełną ścieżkę pliku docelowego: ")

cp_linuxowe(nazwa_pliku, katalog_zrodlowy, sciezka_docelowa)
