# По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого. 
# При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, 
# остальные получили по две монеты. Далее человек, на котором остановился счет, 
# отдает все свои монеты следующему по счету человеку, а сам выбывает из круга. 
# Процесс продолжается с места остановки аналогичным образом до последнего человека в 
# круге. Составьте алгоритм, который проводит эту игру. Если хотите делать паузы, 
# то импортируйте библиотеку time и используйте оттуда функцию sleep. 
# Определите номер этого человека и количество монет, 
# которые оказались у него в конце игры.

#### Для поверки записывал в файл каждый цикл счета на выбывание, потом закоментировал
path = 'result.txt'
data = open(path, 'w') 

people = int(input('Количество человек в кругу: '))
count = int(input('Какое число счета (для выбывания)? '))
data.write(f'Количество человек в кругу {people}\n')
data.write(f'Выбывает каждый {count}\n\n')
list_of_people = list(range(1, people + 1))

out_index = 0 
for i in range(people - 1):
    data.write(f'Текущий круг людей {list_of_people}\n')
    start_index = out_index % len(list_of_people)    
    out_index = (start_index + count - 1) % len(list_of_people)            
    data.write(f'Выбывает человек под номером {list_of_people[out_index]}\n\n')
    list_of_people.remove(list_of_people[out_index])

print(f'Остался человек под номером {list_of_people[0]}')
data.write(f'Остался человек под номером {list_of_people[0]}\n')

money = 0
while (people != 1):
    if (people > count):
        money += count + (people - count) * 2        
    else:
        money += people       
    people -=1 

print(f'Количество монет -> {money}')

data.write(f'Количество монет -> {money}')
data.close