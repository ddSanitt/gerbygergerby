import matplotlib.pyplot as plt

#разделителем записей считается точка с запятой, пробелы разделяют строку и число
file_path = 'test.txt'  #имя файла
file = open(file_path)
all_records = {} #пустой словарь для хранения пар строка:число
for line in file: #перебираем строки файла (это на случай, если в файле несколько строк)
    line = line.strip('; \n') #строку очищаем по краям справа и слева от ненужных символов (точки с запятой, пробелы и символы перехода строки)
    records_in_line = line.split(';') #делим строку на список подстрок, разделенных точками с запятой
    for record in records_in_line: #перебираем подстроки
        if record != '':
            key, value = tuple(record.split()) #делим подстроки еще на две подстроки (пробел - разделитель). Преобразовываем список в кортеж с помощью tuple() для удобства записи в левой стороне выражения.
            all_records[key]  = int(value) #заносим очередную пару строка:число в словарь

#таким образом получили словарь пар строка:число из файла


        
#готовим таблицу

cell_content = [] #пустой список для содержимого ячеек таблицы
for key in all_records.keys():   #перебираем пары слово:число в словаре
    cell_content.append([key, str(all_records[key])]) 


fig1 = plt.figure(1)  #создаем окно для таблицы и диаграммы





#убираем ось X полученной диаграммы, вместо нее будет
plt.table(cellText = cell_content, loc = 'best')
plt.axis('off')


#столбовая диаграмма по полученнным данным:
plt.figure(2)
bars_loc = range(len(all_records)) #range(len(all_records)) дает равномерные координаты столбцов по оси y в соответствии с количеством записей
plt.barh(bars_loc, all_records.values()) #all_records.values() - список чисел из словаря all_records

plt.yticks(bars_loc, list(all_records.keys())) #уточняем настройки вертикальной оси - тики располагаем по положению столбцов, добавляем надписи из списка слов в словаре all_records

plt.show()
