from openpyxl import Workbook, load_workbook
from openpyxl.utils.exceptions import InvalidFileException
from components.basicFunctions import create_reg_exp_query, print_table, get_data
from components.jsonInputOutput import save_to_json
from components.basicConstants import confirm_query, reg_file_name_xlsx
import re


def search():
    file_name = input("Wpisz nazwe pliku (lokalizacje) do przeszukania: ")
    if not re.search(reg_file_name_xlsx, file_name):
        file_name = "{}.xlsx".format(file_name)

    result_arr = []
    wb = Workbook()
    try:
        wb = load_workbook(file_name, read_only=True)
        sheets = [wb.worksheets[i].title for i in range(len(wb.worksheets))]
        search_query = create_reg_exp_query()

        # pobieranie nazwy arkusza do przeszukiwania
        while True:
            temp_sheet = input("Podaj arkusz (dostepne: {}) w ktorym ma byc przeszukiwane wyrazenie ({}): "
                               .format(sheets, search_query))
            if temp_sheet in sheets:
                ws = wb.worksheets[sheets.index(temp_sheet)]
                break
            print("Niepoprawna nazwa arkusza!")

        result_arr = get_data(ws, search_query)

        print_table(result_arr)

        if len(result_arr) > 0:
            choice = input("Czy zapisac wynik wyszukiwania? (t - tak): ")
            if re.search(confirm_query, choice):
                save_to_json(result_arr)
    except FileNotFoundError:
        print("File not found!!")
    except InvalidFileException:
        print("File format not supported!!")
    finally:
        wb.close()
