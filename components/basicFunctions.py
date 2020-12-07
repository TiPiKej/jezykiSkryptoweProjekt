import pathlib
import re
import json
from typing import List

from prettytable import PrettyTable

from components.basicConstants import confirm_query


def create_reg_exp_query():
    """
    Function getting reg exp from a user

    :return: reg exp query
    """

    print("""Opcje:
        1 - podstawowe wyszukiwanie (mozna uzyc wyrazenia regularnego)
        2 - wyszukiwanie zaawansowane z pomoca""")

    while True:
        choice = input("Wybor: ")
        if re.search("^[12]$", choice):
            break
        print("Podales bledna wartosc!")

    choice = int(choice)

    if choice == 1:
        return input("Podaj szukane haslo: ")

    # zaawansowane wyrazenie query
    query = ""

    if re.search(confirm_query, input("Czy mam szukac slow zaczynajacych sie od wyrazenia? (t - tak) ")):
        query = "^" + query

    query += input("Podaj zestaw znakow (np. [a-e]), lub szukane slowo (np. abc): ")

    while True:
        n = input("Ile mam szukac wystapien (np. 4), \
jezeli ma zawierac conajmniej x znakow dodaj po tej liczbie przecinek (np. 4,): ")
        if re.search("^[0-9]+[,]*$", n):
            break
        print("Podales nieprawidlowe dane!")
    query += "{" + n + "}"

    if re.search(confirm_query, input("Czy mam szukac slow konczoncych sie wyrazeniem? (t - tak) ")):
        query += "$"

    return query


def print_table(table: List[dict], *titles: str):
    """
    function only print list of dictionary

    :param table: dictonary of list
    :param titles: optional parm, define titles of dictionary fields to output
    """
    # if titles are empty -> titles are filles by first row of table
    if len(titles) == 0:
        titles = table[0].keys()

    pretty_table = PrettyTable()

    pretty_table.field_names = [title for title in titles]  # add table's header

    for cell in table:
        pretty_table.add_row([cell[title] for title in titles])

    print(pretty_table)
    print("Liczba znalezionych elementow: {}".format(len(table)))


def save_to_file(table: List[dict]):
    file_name = input("Podaj nazwe pliku (bez rozszerzenia) gdzie zapisac wynik: ")

    # check if file exist
    file = pathlib.Path(file_name)
    if file.exists():
        confirm = input("Plik istnieje, czy chcesz go nadpisac? (t - tak): ")
        if not re.search(confirm_query, confirm):
            return "Nie zapisano pliku"

    # saving file
    if not re.search("^[A-Za-z_-]+$", file_name):
        return "Nie zapisano pliku"

    try:
        with open("{}.json".format(file_name), "w") as json_file:
            json.dump(table, json_file)
            print("Wynik polecenia zapisano w {}.json".format(file_name))
    except IOError as e:
        print("Nie mozna zapisac pliku: ", e)
        if re.search(confirm_query, input("Czy chcesz sprobowac zapisac raz jeszcze? (t - tak) ")):
            return save_to_file(table)
