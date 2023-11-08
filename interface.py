from function import input_contact, view_contact,  del_contact, restart_contact 

press = int(input('введите действие которое хотите соверщить \n'
          '1. Ввести контакт\n'
          '2. Изменить контакт\n'
          '3. Удалить контакт\n'
          '4. Вывести контакт\n'))
while press < 1 or press > 5:
    print('Введите число от 1 до 4') 
    press = int(input('введите действие которое хотите соверщить \n'
          '1. Ввести контакт\n'
          '2. Изменить контакт\n'
          '3. Удалить контакт\n'
          '4. Вывести контакт\n'))
         # '5. Изменить контакт (версия 2'))
    
if press == 1:
    input_contact()
if press == 2:
    restart_contact()
if press == 3:
    del_contact()
if press == 4:
    view_contact()
#if press == 5:
#    renamed_contact()
        
