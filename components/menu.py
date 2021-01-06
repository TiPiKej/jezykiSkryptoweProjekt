from components.copyFile import copy_file
from components.search import search
from components.jsonInputOutput import save_xlsx_to_json, save_json_to_xlsx
from components.basicFunctions import new_static_file, create_empty_file

menu_option = [
    {"name": "Nowy plik z szablonu", "function": new_static_file},
    {"name": "Nowy pusty plik xlsx", "function": create_empty_file},
    {"name": "Kopiuj plik", "function": copy_file},
    {"name": "Przeszukaj plik", "function": search},
    {"name": "Eksportuj dane z pliku xlsx do pliku JSON", "function": save_xlsx_to_json},
    {"name": "Importuj dane z pliku JSON do pliku xlsx", "function": save_json_to_xlsx}
]
