from components.copyFile import copy_file
from components.search import search
from components.jsonInputOutput import save_xlsx_to_json, save_json_to_xlsx

menu_option = [
    {"name": "Kopiuj plik", "function": copy_file},
    {"name": "Przeszukaj plik", "function": search},
    {"name": "Eksportuj dane z pliku xlsx do pliku JSON", "function": save_xlsx_to_json},
    {"name": "Importuj dane z pliku JSON do pliku xlsx", "function": save_json_to_xlsx}
]

# to do
# mam 2 tabele -> szukam wpisow unikalnych 
# eksport tabeli do formatu bazodanowego
