import ui
import db


def directory_add():
    second_name = ui.input_data('Введите фамилию: ')
    first_name = ui.input_data('Введите имя: ')
    tel = ui.input_data('Введите телефон: ')

    record = second_name + '; ' + first_name + '; ' + tel
    db.save_data(record)

def directory_read():
    global dir_list
    dir_list = db.read_data()

def button_click():
    mod = int(ui.input_data('1 - запись данных;\n2 - чтение данных: '))
    if mod == 1:
        directory_add()
    elif mod == 2:
        directory_read()