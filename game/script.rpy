# Вы можете расположить сценарий своей игры в этом файле.
define n = Character(None, kind=nvl)

define pass1_correct = "98"
define pass2_correct = "03"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:

label start:
    play music "default.mp3" loop

    call introduction 
    call matvey_home
    call valdic_home
    call colobok_home

    return 


label introduction:
    scene bg start

    n """
    Вы оказались в стране Никландия, в городе Волейленд

    Попав в канон нового года, вы решаете отправиться по городу и познакомится с местными жителями.

    Но все оказывается не так просто, жители города, совершенно пренебрегая вашей фигурой, 
    заставляют съесть пирожное перед тем как радушно принять вас в своём доме. 

    Итак, вы направляетесь к ближайшему дому ...

    """
    nvl clear
    nvl hide

    return


label matvey_home:
    scene home 1

    "Дом Матвиуса"

    n """
    Первое пирожное за сегдоня вы съедите в доме Матвиуса.

    На каждом пирожном есть порядковый номер. В данном случае съедайте пирожное под номером 1 
    и вписывайте пароль, спрятаный под пирожным
    """

    nvl clear
    nvl hide

    $ pass1 = renpy.input("Введите пароль от первого пирожного: ").strip().lower()

    while pass1 != pass1_correct:
        "Видимо вы ошиблись, поробуйте еще раз"
        $ pass1 = renpy.input("Введите пароль от первого пирожного: ")

    "Все верно!"
    $ renpy.movie_cutscene("matvey.ogv")

    return


label valdic_home:
    scene street

    "Вы чудесно посидели у Матвиуса, но аппетит после первого перожного только больше разыгрался. Поэтому вы двигаетесь прямо по улице к следоющему дому"

    scene home 2
    "Дом Владельгольца"

    $ pass2 = renpy.input("Введите пароль от второго пирожного: ").strip().lower()

    while pass2 != pass2_correct:
        "Видимо вы ошиблись, поробуйте еще раз"
        $ pass1 = renpy.input("Введите пароль от второго пирожного: ")

    "Все верно!"
    $ renpy.movie_cutscene("vladic.ogv")


label colobok_home:
    scene street

    "Вы чудесно посидели у Матвиуса, но аппетит после первого перожного только больше разыгрался. Поэтому вы двигаетесь прямо по улице к следоющему дому"

    scene home 2
    "Дом Владельгольца"

    $ pass2 = renpy.input("Введите пароль от второго пирожного: ").strip().lower()

    while pass2 != pass2_correct:
        "Видимо вы ошиблись, поробуйте еще раз"
        $ pass1 = renpy.input("Введите пароль от второго пирожного: ")

    "Все верно!"
    $ renpy.movie_cutscene("vladic.ogv")

