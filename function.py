from inter_funct import name_data, surname_data, phone_data, adress_data
import os


def input_contact():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input('В каком формате совершить\n'
          '1. все данные на отдельных строках\n'
          '2. все в одной строчке через пробел'))
    while var < 1 or var > 2:
        print('Введите число от 1 до 4')
        var = int(input('В каком формате совершить\n'
          '1. все данные на отдельных строках\n'
          '2. все в одной строчке через пробел'))
    if var == 1:
        with open('data_y.txt', 'a', encoding ='utf-8') as f:
            f.write(f'{name.capitalize()} \n {surname.capitalize()} \n {phone} \n {adress}\n\n')
    else:
        with open('data_x.txt', 'a', encoding='utf-8') as f:
            f.write(f'{name.capitalize()}  {surname.capitalize()}  {phone}  {adress}\n\n')



def view_contact():
    with open('data_y.txt', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        print(*data_first)
    with open('data_x.txt', 'r', encoding='utf-8') as file:
        data_second = file.readlines()
        print(*data_second)
    return data_first, data_second




def del_contact():
    
    file_var = int(input('С Какого файла хотите удалить контакт? 1 или 2'))  
    while file_var < 1 or file_var > 2:
        file_var = int(input('Введите 1 для удаления из гаризонтально записанных и 2 из вертикально записанных'))

    if file_var == 1:                                                            
         with open('data_x.txt', 'r', encoding='utf-8') as d: 
            data = d.readlines()
            data_strip = [line.strip() for line in data]
            sata = input("Какой контакт хотите удалить (Введите ИМЯ или ФАМИЛИЯ или НОМЕР ТЕЛЕФОНА)?\n")
            if any(sata.lower() in line.lower() for line in data_strip):
                with open('data_x.txt', 'w', encoding='utf-8') as b:
                    lst = []
                    for i in range(len(data)):
                        if data[i] == '\n':
                            plus = data[i-1] + data[i]
                            if sata  not in plus:
                                lst.append(plus)
                    b.writelines(lst)
                    print('Контакт удалён')
    
            else:
                print('Контакт не найден')

   
    else:
       with open('data_y.txt', 'r', encoding='utf-8') as d:
            data = d.readlines()
            data_strip = [line.strip() for line in data]  
            sata = input("Какой контакт хотите удалить (Введите ИМЯ или ФАМИЛИЯ или НОМЕР ТЕЛЕФОНА)?\n")
            if any(sata.lower() in line.lower() for line in data_strip):
                with open('data_y.txt', 'w', encoding='utf-8') as b:
                    lst = []
                    for i in range(len(data)):
                        if data[i] == '\n':
                            plus = data[i-4] + data[i-3] + data[i-2] + data[i-1] + data[i]  
                            if sata not in plus:
                                lst.append(plus)
                    b.writelines(lst)
                    print('Контакт удалён')
            
            else:
                print('Контакт не найден')
 

def restart_contact():
    
    file_var = int(input('С Какого файла хотите изменить контакт? 1 или 2')) 
    while file_var < 1 or file_var > 2:
        file_var = int(input('Введите 1 для удаления из гаризонтально записанных и 2 из вертикально записанных'))

    if file_var == 1:
        with open('data_x.txt', 'r', encoding = 'utf=8') as d:
            data = d.readlines()
            sata = input("Введите ИМЯ или ФАМИЛИЯ или НОМЕР контакта для изменения")     #находим контакт по имени или фамилию или номер
            if any(sata.lower() in line.lower() for line in data):                       
                with open('data_x.txt', 'w', encoding='utf-8') as files:
                    for i in range(len(data)):
                        if sata in data[i]:
                            new_name = input('новое имя')
                            new_surname = input('новое фамилия')
                            new_contact = input('новый номер')
                            new_adress = input('Новый адрес')
                            data[i] = f'{new_name}  {new_surname}  {new_contact}  {new_adress}\n\n'
                            files.writelines(data)
            else:
                print('Контакт не найден')

    
    else:

        with open('data_y.txt', 'r', encoding = 'utf-8') as d:
            data = d.readlines()
            sata = input("Введите ИМЯ или ФАМИЛИЯ или НОМЕР контакта для изменения")
            if any(sata.lower() in line.lower() for line in data):
                with open('data_y.txt', 'w', encoding='utf-8') as files:
                    lst = []
                    for i in range(len(data)):
                        if data[i] == '\n':
                            rev = data[i-4] + data[i-3] + data[i-2] + data[i-1] + data[i]
                            lst.append(rev)
                    for i in range(len(lst)):
                        if sata in lst[i]:
                            new_name = input('новое имя')
                            new_surname = input('новое фамилия')
                            new_contact = input('новый номер')
                            new_adress = input('Новый адрес')
                            lst[i] = f'{new_name} \n {new_surname} \n {new_contact} \n {new_adress}\n\n'
                    files.writelines(lst)
            else:
                print('Контакт не найден')



# def renamed_contact():
#     file_var = input('Какой файл открыть')
#     if file_var == 1:
#         with open('data_x.txt', 'r', encoding = 'utf=8') as v g:
#             data = g.readlines()
#             sat = input('Введите ИМЯ или ФАМИЛИЯ или НОМЕР контакта для изменения')
#         with open('data_x.txt', 'r', encoding = 'utf=8') as d:
#             for i in range(len(data)):
#               if sata in data[i]:
#                   data.split = ' '.split(data[i])
#                   sat2 = intut('изменяем имя фамилия номер или адрес(введите их)')
#                   for i in renge(len(data.split)):
#                       if sat2 in data.split:
#                           data.split[i] = input('введите новые данные')