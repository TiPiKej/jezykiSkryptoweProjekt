from openpyxl import Workbook, load_workbook


def copy_file():
    print("KOPIOWANIE PLIKU")
    file_name_src = input("Wpisz nazwe pliku (lokalizacje) do skopiowania: ")
    file_name_dst = input("Wpisz nazwe pliku (lokalizacje) gdzie skopiowac: ")

    wb1 = load_workbook(file_name_src)
    ws1 = wb1.worksheets[0]

    wb2 = load_workbook(file_name_src)
    ws2 = wb2.active

    for i in range(1, ws1.max_row + 1):
        for j in range(1, ws1.max_column + 1):
            cell = ws1.cell(row=i, column=j)

            ws2.cell(row=i, column=j).value = cell.value

    wb2.save(str(file_name_dst))

    wb1.close()
    wb2.close()
    return 0
