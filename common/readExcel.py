import xlrd3, os

current_path = os.path.dirname(__file__)
data_path = os.path.join(current_path, '../Date/zengzhu1604.xlsx')


def read_excel(date_path=data_path, sheet_name='login_page'):
    wokebook = xlrd3.open_workbook(data_path)
    sheet = wokebook.sheet_by_name(sheet_name)
    data = {}
    for i in range(1, sheet.nrows):
        data_01 = {'elemen_name': sheet.cell_value(i, 1), 'locat_type': sheet.cell_value(i, 2),
                   'locate_value': sheet.cell_value(i, 3), 'time_out': sheet.cell_value(i, 4)}
        data[sheet.cell_value(i, 0)] = data_01
    return data


if __name__ == '__main__':
    print(read_excel(data_path, 'login_page'))
