from copyFile import copy_file

menu_option = [
    {"name": "Kopiuj plik", "function": copy_file}
]


def menu():
    n = 1
    for option in menu_option:
        print("{} : {}".format(n, option["name"]))
        n += 1
    print("{} : {}".format(0, "koniec programu"))
    while True:
        choice = int(input("Wybierz opcje: "))
        if 0 <= choice <= len(menu_option):
            break
    if choice == 0:
        return -1
    print("-----------------------------")
    menu_option[choice - 1]["function"]()
    return choice - 1

