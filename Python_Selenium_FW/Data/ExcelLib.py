from Data import *
from Library import *


def read_data(sheetname, testcase):
    workbook = xlrd.open_workbook(Config.DATA_FILE_PATH)
    worksheet = workbook.sheet_by_name(sheetname)
    data = []
    headers = None
    rows = worksheet.get_rows()
    for rowno, row in enumerate(rows):
        if row[0].value == testcase:
            headers = worksheet.row_values(rowno - 1, start_colx=2)
            headers = [item for item in headers if item]
            headers = ','.join(headers)
            break

    rows = worksheet.get_rows()  # Re-initialising iterator

    for rowno, row in enumerate(rows):
        if row[0].value == "test_shopping":
            # Get the row values of the existing row from column-1
            temp_data = worksheet.row_values(rowno, start_colx=1)
            temp_data = [item for item in temp_data if item]
            # Append the list only if the execute column is "Yes"
            if temp_data[0] == "Yes":
                data.append(tuple(temp_data))
    return [headers, data]


def read_locators(sheetname):
    workbook = xlrd.open_workbook(Config.OBJECTS_FILE_PATH)
    worksheet = workbook.sheet_by_name(sheetname)
    rows = worksheet.get_rows()
    next(rows)     # Skip Headers
    return {row[0].value: (row[1].value, row[2].value) for row in rows}
