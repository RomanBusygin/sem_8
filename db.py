def save_data(data):
    with open(r'C:\Users\Roman\Desktop\GEEK block 2\Python\Seminar\Sem_8\directory.txt', 'a', encoding = 'utf8') as file:
        file.write(f'{data}\n')

def read_data():
    with open(r'C:\Users\Roman\Desktop\GEEK block 2\Python\Seminar\Sem_8\directory.txt', 'r', encoding = 'utf8') as file:
        return file.readlines()