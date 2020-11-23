from copyFile import copy_file


def load_file():
    print("PLIK WCZYTYWANY")


def save_file():
    print("PLIK ZAPISYWANY")


menu_option = [
    {"name": "Wczytaj plik", "function": load_file},
    {"name": "Zapisz plik", "function": save_file},
    {"name": "Kopiuj plik", "function": copy_file}
]


def menu():
    n = 0
    for option in menu_option:
        print(n, ": ", option["name"])
        n += 1
    choice = int(input())
    return menu_option[choice]["function"]
