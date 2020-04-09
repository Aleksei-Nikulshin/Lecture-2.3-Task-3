


#Я работаю секретарем и мне постоянно приходят различные документы. Я должен быть очень внимателен чтобы не потерять ни один документ. Каталог документов хранится в следующем виде:

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
# Перечень полок, на которых находятся документы хранится в следующем виде:
#
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': []
      }


# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:\nd – delete – команда,
# которая спросит номер документа и удалит его из каталога и из перечня полок;\nm – move – команда, которая спросит
# номер документа и целевую полку и переместит его с текущей полки на целевую;

command_list = str('p – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;\np_all - команда, которая выведет имена всех владельцев документов;\nl – команда, которая выведет список всех документов;\ns – команда, которая спросит номер документа и выведет номер полки, на которой он находится;\na – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться;\nq - команда для завершения работы программы.')



def choice_data_people():
  input_2 = input('Введите "y",  если хотите ввести другой номер документа, или "q", если хотите закончить работу с программой, или любое другое значение, если хотите продолжить работу с другими командами программы: ')
  if input_2 == 'y':
    data_people()
  elif input_2 == 'q':
    print("Программа остановлена")
  elif input_2 != 'q':
    print()
    main()

def data_people():
  input_1 = input('Введите номер документа: ')
  i = 0
  for document in documents:
    # print(document.values())
    if input_1 in document.values():
     print(f"Согласно введенному Вами номеру документа есть совпадение - {document['name']}")
     print()
    else:
     i += 1
  if i == len(documents):
    print(f'Согласно введенному Вами номеру документа нет совпадений.')
    print()
    choice_data_people()



def data_print():
  for document in documents:
    print(f"{document['type']} '{document['number']}' '{document['name']}' ")
  print()
  input_2 = input('Введите "q", если хотите закончить работу с программой или любое другое значение, если хотите продолжить работу с другими командами программы: ')
  if input_2 == 'q':
    print("Программа остановлена")
  elif input_2 != 'q':
    print()
    main()


def shelf_print():
  input_data_people = input('Введите номер документа: ')
  i = 0
  for row in directories:
    # print(row)
    if input_data_people in directories[row]:
      print(f'Согласно введенному Вами номеру документа обнаружен документ на полке {row}')
    else:
      i += 1
  if i == len(directories):
    print(f'Согласно введенному Вами номеру документа не обнаружено документов на полках.')
    print()

def add_data():
  input_new_type = input('Введите тип нового документа: ')
  input_new_number = input('Введите номер нового документа: ')
  input_new_name = input('Введите имя и фамилию владельца нового документа: ')
  input_new_key = input('Введите номер полки для нового документа: ')
  new_dict = {"type": input_new_type, "number": input_new_number, "name": input_new_name }
  documents.append(new_dict)
  # print(documents)
  d = 0
  for k in directories.keys():
    # print(k)
    if input_new_key == k:
      # print('Такая полка уже есть!')
      old_value = directories[k]
      # print(f'old value = {old_value}')
      old_value.append(input_new_number)
      print(old_value)
    else:
      d += 1
  # print(d)
  if d == len(directories.keys()):
    print(f'Такой полки ранее не было. Поэтому создана новая полка с обозначением {input_new_key}')
    new_list = []
    new_list.append(input_new_number)
    directories[input_new_key] = new_list
    print(directories)

def unworked():
  input_delete_number = input('Введите номер документа для удаления: ')
  new_documents = documents.copy()
  # print(f'new_documents   {new_documents}')
  # print(f'len(new_documents)   {len(new_documents)}')
  for i in range(len(new_documents)):
    if new_documents[i]['number'] == input_delete_number:
      print(f"Согласно введенному Вами номеру документа есть совпадение - {new_documents[i]['name']}")
      del documents[i]
  # print(documents)
  # print(directories.values())
  # k = 0
  # print(len(directories.values())
  # del_dict = directories.copy()
  # for key, value in del_dict.items():
  #   # print(f'value {value}')
  #   # print(f'key {key}')
  #   # print(f'len(value) {len(value)}')
  #   k = 0
  #   for i in range(len(value)):
  #     if value[i] == input_delete_number:
  #       # print(f'value[i] {value[i]}')
  #       result = {c:[vi for vi in v if vi != input_delete_number] for c,v in directories.items()}
  #       print(f'result {result}')
  #     else:
  #       k += 1
  #       print(k)
  # if k == len(directories.values()):
  #   print(f"Согласно введенному Вами номеру документа нет совпадений")
  #   print()
  # print(f'В documents сейчас {documents}')
  # print(f'В directories сейчас {directories}')
  # print()
  # main()

def print_all_names():
  # print(documents)
  for document in documents:
    try:
      print(f"Владелец - {document['name']} ")
    except KeyError:
      print('У документа не обнаружен владелец')


def main():
    print(command_list)
    print()
    input_main = input('Введите команду из списка: ')
    if input_main == 'p':
      data_people()
    elif input_main == 'l':
      data_print()
    elif input_main == 's':
      shelf_print()
    elif input_main == 'a':
      add_data()
    elif input_main == 'p_all':
      print_all_names()
    elif input_main == 'q':
      print('Выполнение программы остановлено')
      break
    else:
      print('Вы ввели команду не из списка. Перезапустите программу')
    return

main()