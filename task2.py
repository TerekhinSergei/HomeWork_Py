# 2 - Напишите программу для. проверки истинности утверждения
#     ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.

for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            result = not(x or y or z) == ((not x) and (not y) and (not z))
            print (f'x = {x}, y = {y}, z = {z}  Result = {result}')
        