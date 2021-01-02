from openpyxl import Workbook, load_workbook
from openpyxl.utils.exceptions import InvalidFileException
from components.basicFunctions import create_reg_exp_query, print_table
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
            print("Podaj arkusz (dostepne: {}) w ktorym ma byc przeszukiwane wyrazenie ({}): "
                  .format(sheets, search_query))
            temp_sheet = input()
            if temp_sheet in sheets:
                ws = wb.worksheets[sheets.index(temp_sheet)]
                break
            print("Niepoprawna nazwa arkusza!")

        for i in range(1, ws.max_row + 1):
            for j in range(1, ws.max_column + 1):
                temp_value = ws.cell(row=i, column=j).value
                if temp_value is None:
                    continue
                if re.search(search_query, str(temp_value)):  # wyrazenie regularne (wyrazenie, sprawdzana wartosc)
                    result_arr.append({
                        "row": i,
                        "column": j,
                        "value": temp_value
                    })

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
