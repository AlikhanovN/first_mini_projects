# импортируем библиотеки
from datetime import datetime, timedelta, date
import pandas

# открываем первую страницу файла с шифтами
shift = pandas.read_excel(r'files/shifts.xlsx', sheet_name='Sheet1')

# задаем формат времени
time_format = '%H:%M:%S'

# создаем пустой столбец для вычисления с какого часа можно назначать агента на смену
shift.insert(8, 'Avltime', '')

# цикл по всем строкам  с вычислением 12 часовой разницы после окончания смены
n = 0
for i in shift['End']:
    datetime.strptime(str(i), time_format) - datetime.strptime('12:00:00', time_format)
    shift['Avltime'][n] = i
    n += 1

# сохраняем как новый файл без индексов
with pandas.ExcelWriter(r'result/shifts_new.xlsx') as writer:
    shift.to_excel(writer, index=False)

print(shift)