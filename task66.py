# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]
# нужно решить задачи с помощью лямбд, filter, map, zip, enumerate, list comprehension

import random

#numbers = [random.randint(1, 100) for _ in range(200)]
numbers = [0, 2, 2, 3, 3, 5, 5, 7, 7, 10, 10, 9, 11, 12, 13, 15]
# prod_list = list(filter(lambda x: x[0] != x[1], enumerate(numbers)))
print(f'список пар, где сумма кортежа кратна 5 -> {list(filter(lambda x: (x[0]+x[1])%5==0, enumerate(numbers)))}')
