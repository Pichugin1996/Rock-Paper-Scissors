import random
#Камень = 1
#Ножницы = 2
#Бумага = 3
balans = 150
def start():
    global play, ii, iitem, balans, stavka, i
    if balans == 0:
        print("Ты проиграл, последний ход!")
        i = 1000
    print ("Ваш баланс {}$".format(balans))
    stavka = int(input("Ваша ставка: "))
    if balans < stavka:
        print("Ошибка! Баланс не может быть меньше ставки")
        start()
    play = int(input("Выберай: Камень, ножницы или бумага: "))
    if play != 1:
        if play != 2:
            if play !=3:
                print("Ошибка! Вводи цыфры от 1 до 3 (1=камень, 2=ножницы, 3=бумага)")
                start()
    ii = random.randint(1, 3)
    iitem = ["", "камень", "ножницы", "бумага"]

    print("Компьютер выбрал", iitem[ii], ", а ты выбрал", iitem[play])

    gamestart()

def gamestart():
    if play == ii:
        print("Ничья")
    else:
        game1()
        game2()
        game3()
def game1():
    global play, ii, iitem, balans, stavka
    if play == 1:
        if ii == 2:
            print ("Ты победил")
            balans += stavka
        else:
            print ("Ты проиграл")
            balans -= stavka

def game2():
    global play, ii, iitem, balans, stavka
    if play == 2:
        if ii == 3:
            print ("Ты победил")
            balans += stavka
        else:
            print ("Ты проиграл")
            balans -= stavka

def game3():
    global play, ii, iitem, balans, stavka
    if play == 3:
        if ii == 1:
            print ("Ты победил")
            balans += stavka
        else:
            print ("Ты проиграл")
            balans -= stavka

print("Игра: Камень, Ножницы, Бумага")
gamelong = int(input("Сколько игр будешь играть?: "))
i = 1
while i <= gamelong:
    start()
    i += 1
print ("Конец игры!")




