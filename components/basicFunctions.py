import random
import re
import pathlib

from typing import List
from openpyxl import Workbook
from prettytable import PrettyTable

from components.basicConstants import confirm_query, reg_file_name_xlsx


def check_if_file_exist(file_name, quiet=False):
    """

    :param file_name: string
    :param quiet: boolean; if is True -> nothing has prompt
    :return: if exist -> True, if not exist -> False
    """
    file = pathlib.Path(file_name)
    if file.exists():
        if quiet:
            return True

        confirm = input("Plik istnieje, czy chcesz go nadpisac? (t - tak): ")
        if not re.search(confirm_query, confirm):
            return True
    return False


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

    :param table: list of dictonary
    :param titles: optional parm, define titles of dictionary fields to output
    """
    # if titles are empty -> titles are filles by first row of table
    if len(table) == 0:
        print("Brak wynikow!")
        return None

    if len(titles) == 0:
        titles = table[0].keys()

    pretty_table = PrettyTable()

    pretty_table.field_names = [title for title in titles]  # add table's header

    for cell in table:
        pretty_table.add_row([cell[title] for title in titles])

    print(pretty_table)
    print("Liczba znalezionych elementow: {}".format(len(table)))


def add_sheet_to_workbook(table: List[dict], wb=Workbook(), title="Untitled", overwrite=False):
    """
    add sheet based on table list (row, column, value)

    :param table: list[dict] - data to be saved in new sheet
    :param wb: workbook - file where sheet will be added
    :param title: string - sheet's name
    :param overwrite: boolean - if is True -> it won't be created new sheet -> default sheet's title will be overwritted
    :return: new worksheet
    """
    if overwrite:
        ws = wb.worksheets[-1]
        ws.title = title
    else:
        ws = wb.create_sheet(title)
    # kopiowanie wartosci komorek
    for cell in table:
        ws.cell(row=cell['row'], column=cell['column']).value = cell['value']
    return ws


def new_static_file():
    wb = Workbook()
    file_name = input("Podaj nazwe pliku: ")
    if not re.search(reg_file_name_xlsx, file_name):
        file_name = "{}.xlsx".format(file_name)

    if check_if_file_exist(file_name):
        return "Nie utworzono pliku"

    ws = wb.active
    ws.title = "Tabliczka mnozenia"

    for row in range(1, 11):
        for column in range(1, 11):
            ws.cell(row=row, column=column).value = row * column

    ws = wb.create_sheet("pi")
    ws["A1"] = 3.14

    ws = wb.create_sheet("e")
    ws["A1"] = 2.718

    ws = wb.create_sheet("losowe liczby")

    for i in range(1, 100):
        ws["A{}".format(i)] = i
        ws["B{}".format(i)] = round(random.random() * 100000) / 1000

    wb.save(file_name)


def create_empty_file():
    file_name = input("Podaj nazwe pliku: ")
    if not re.search(reg_file_name_xlsx, file_name):
        file_name = "{}.xlsx".format(file_name)

    if check_if_file_exist(file_name):
        return "Nie utworzono pliku"

    wb = Workbook()
    wb.save(file_name)
