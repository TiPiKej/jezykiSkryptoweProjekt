from components.menu import menu_option

while True:
    # print menu
    n = 1
    for option in menu_option:
        print("{} : {}".format(n, option["name"]))
        n += 1
    del n
    print("{} : {}".format(0, "koniec programu"))

    # user choice
    while True:
        choice = int(input("Wybierz opcje: "))
        if 0 <= choice <= len(menu_option):
            break
    if choice == 0:
        break

    # call function
    menu_option[choice - 1]["function"]()
