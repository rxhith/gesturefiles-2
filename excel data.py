import re
import time
from openpyxl import load_workbook


def read_data():
    book = load_workbook('dynamic csv.xlsx')
    sheet = book.active
    all_rows = []
    column_averages = {}

    for row_num in range(17, 22):  # Loop through rows 17 to 21
        data = {}
        value_b = sheet[f'B{row_num}'].value
        if isinstance(value_b, str):
            numeric_value_b = re.findall(r'\d+', value_b)
            if numeric_value_b:
                data['B'] = int(numeric_value_b[0])

        data['C'] = sheet[f'C{row_num}'].value
        data['D'] = sheet[f'D{row_num}'].value
        all_rows.append(data)

        # Calculate individual column averages
        for key, value in data.items():
            if isinstance(value, (int, float)):
                if key not in column_averages:
                    column_averages[key] = [value]
                else:
                    column_averages[key].append(value)

    # Calculate column averages
    for key, values in column_averages.items():
        column_averages[key] = sum(values) / len(values)

    print(all_rows)
    print('---------------------')
    print(column_averages)


while True:
    read_data()
    time.sleep(10)
