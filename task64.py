# 4 - Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.
# нужно решить задачи с помощью лямбд, filter, map, zip, enumerate, list comprehension


url_list = ['https://dzen.ru/suite/a6424a0f-4fdb-44a1-95a0-9945e6f0a699',
            'https://disk.yandex.ru/i/o42lR-XVcSk3KA',
            'https://gb.ru/lessons/284811/homework',
            'https://www.youtube.com/watch?v=5g-MHZ0MzZY&t=18602s',
            'https://docs.google.com/presentation/d/1Q6ZiqwpNtd0BcSL0GmNH6CjNOOgc3JO9jpvolIwHmx8/edit#slide=id.g1500622f28c_0_43',
            'https://pythonist.ru/10-priemov-dlya-preobrazovaniya-i-dekompoziczii-strok-v-python/',
            'https://pythonworld.ru/tipy-dannyx-v-python/kortezhi-tuple.html',            
            'https://proproprogs.ru/python_base/chtenie-i-zapis-v-fayl',
            'https://docs-python.ru/tutorial/metody-fajlovogo-obekta-potoka-python/metod-file-readline/',
            'https://www.rulit.me/data/programs/resources/pdf/Kolcov_Python-Sozdaem-programmy-i-igry_RuLit_Me_721945.pdf',
            'https://github.com/TerekhinSergei']
            

domen_list = list(map(lambda i: i[:i.find('/')], [i for i in map(lambda i: i.replace('https://',''), url_list)]))
print(domen_list)
