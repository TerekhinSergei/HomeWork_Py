def create_dict(lines_fio, lines_oklad):
    salary=dict()
    for key in lines_fio:        
        for value in lines_oklad:
            salary[key] = value
            lines_oklad.remove(value)
            break  
    return salary

def create_itogo_file(dict, data):
    for name, oklad  in salary.items():
        if name.count('Lisa Montgomery') or name.count('Nancy Jones'):
            name = name.upper()
            oklad = str(int(oklad)*2.0)                
        else:
            oklad= str(int(oklad)*1.5)            
        string = name +', '+ oklad +'\n'           
        data_itogo.write(string) 


data_fio = open('fio.txt', 'r') 
data_oklad = open('oklad.txt', 'r') 
data_itogo = open('itogo.txt', 'w+') 

lines_fio = data_fio.readlines()
lines_oklad = data_oklad.readlines()

lines_fio = list(map(str.rstrip,lines_fio)) # удаление перевода строки
lines_oklad = list(map(str.rstrip,lines_oklad))


salary= create_dict(lines_fio, lines_oklad)
#print(salary)
create_itogo_file(salary, data_itogo)

data_fio.close
data_oklad.close    
data_itogo.close

# data_itogo = open('itogo.txt', 'r') 
# lines_itogo = data_itogo.readlines()
# print(lines_itogo)
# data_itogo.close
