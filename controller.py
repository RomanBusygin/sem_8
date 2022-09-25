from itertools import count
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

    print(dir_list)

def button_click():
    mod = int(ui.input_data('1 - запись данных;\n2 - чтение данных\n3 - удаление данных '))
    if mod == 1:
        directory_add()
    elif mod == 2:
        directory_read()
    elif mod == 3:
        delete_rec()

def delete_rec():
    dir_list = db.read_data()
    fam = ui.input_data('Кого удалить? ')
    count = 0
    while count != len(dir_list):
        if fam in dir_list[count]:
            dir_list.pop(count)
        count += 1
    db.delete_save()
    for i in (dir_list):
        db.save_data(i)
    