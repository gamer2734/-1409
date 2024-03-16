import csv
a = open('history_mirror.csv', encoding='utf-8')#открываем Файл
b = a.readlines()
c = [] 
for i in b: #преобразовываем файл
    if i.count('\n') == 1:
        i = i.replace('\n', '')
        c.append(i.split(','))
a.close()
answer = []#создаём список с ответами
for j in range(len(c)): # ищем необходимые данные
    if (c[j])[2] == 'Победа над смертью':
        answer.append(f'{(c[j])[0]},{(c[j])[1]}\n')# записываем ответ
print(answer)
    

file = open('mirror_error.csv', encoding='utf8') # переписываем ответ в файл
for k in answer:
    file.write(k)
