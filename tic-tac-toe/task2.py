import TicTacToe3 as TTT3


check = input("Привет!\nПредлагаю сыграть в крестики-нолики\nВведи 'Д' or 'Y' если согласен, иначе просто нажми <интер>: ")

if check.lower() == 'д' or check.lower() == 'y':
    game = True
    while game:
        try:
            TTT3.play()
        except:  # в скачанной библиотеке есть ошибки, поэтому обернул
            print('что-то пошло не так, заходи ещё')
        check = input("Еще разок?! Усли согласен просто нажми <интер>\nиначе 'Н' или 'N' : ")
        if check.lower() == 'н' or check.lower() == 'n':
            game = False
else:
    check = input("Желаете ознакомиться со своей статистикой - 'Д' or 'Y', нет - просто <интер>: ")
    if check.lower() == 'д' or check.lower() == 'y':
        TTT3.showProbability()

print('Программа завершена. Приходи ещё.')
