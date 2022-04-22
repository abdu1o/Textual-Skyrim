from random import randint
import time


#Статы----------------------------------------------------------------------
class stats:
    hp = 100
    max_hp = 100

    mele_dam = 10

    mana = 80
    max_mana = 80

    mag_dam = 20
    
    stam = 100
    max_stam = 100

    xp = 0
    max_xp = 300

    skills = 0

    level = 1
    
player = stats()
#Вступление----------------------------------------------------------------------
   
print("""(Ралоф) Эй ты, не спишь?
        Ты нарушитель границы, так?
        Надо ж было тебе налететь прямо на имперскую засаду, они и нас поймали, и ворюгу этого.
 
          """)
time_count = 8
 
for i in range(time_count, 0, -1): 
    time.sleep(1)

print("""(Вор из Рорикстеда) Проклятые братья бури! В Скайриме было тихо пока вас сюда не принесло и империи ни до чего дела не было.
                    Если бы не вы, я бы сейчас украл вон ту лошадь и рванул в Хамерфел.
 
                      """)
time_count = 9
 
for i in range(time_count, 0, -1): 
    time.sleep(1)
    
print("""(Ралоф) Конечно, если бы мы уже не приехали.
 
          """)
time_count = 5
 
for i in range(time_count, 0, -1): 
    time.sleep(1)

print("""(Генерал легиона) А ну выходим из повозки, живо!
                  Итак, по списку: Ралоф из Ривервуда
                                   Локер из Рорикстеда
                  Постой ка, а кто ты?
 
                   """)

name = str(input("Меня зовут: "))
print(f"""{name} из Хамерфелла
 
""")
time_count = 3
 
for i in range(time_count, 0, -1): 
    print() 
    time.sleep(1)

print(f"""(Генерал легиона) Так, этих двух казнить,
                  а ты, {name} из Хамерфелла, иди за мной.
 
                """)

time_count = 10
 
for i in range(time_count, 0, -1): 
    print() 
    time.sleep(1)

print("""(Генерал легиона) Добро пожаловать на арену!
                 Я кстати не представился, меня Хадвар зовут,
                 а вот о тебе я бы хотел услышать по подробнее

                 """)

job = input("""Я был бравым воинон ордена Диагны [1]
            
Когда-то я был членом гильдии магов Обливиона, пока не захотел перебраться в Винтерхолд [2]
                                                            \n""")



#Класс-----------------------------------------------------------------------


if int(job) == 1:
    print("""(Хадвар) Мда, и как тебя только сюда занесло.
         Держи, тут набор лёгкой имперской брони и меч, думаю этого тебе хватит
         """)
    player.max_hp = player.max_hp + 20
    player.mele_dam = player.mele_dam + 20
    print(f"""Ваши показатели увелчены:
         Максимальное здоровье 100 --> {player.max_hp}
         Урон ближнего боя 10 --> {player.mele_dam}
         """)
elif int(job) == 2:
    print("""(Хадвар) О, так ты у нас волшебник, тогда держи мантию новичка,
         тебе она принесёт больше пользы
         """)
    player.max_mana = player.max_mana + 20
    player.mag_dam = player.mag_dam + 10
    print(f"""Ваши показатели увелчены:
         Максимальное кол-во маны 80 --> {player.max_mana}
         Магический урон 20 --> {player.mag_dam}
         """)

    
print("""(Хадвар) Пора бы тебя ввести в курс дела,
     Арена это место, где уголовники или случайно пойманные как ты могут попытаться
     выбить себе путь на свободу.
     Выбора у тебя нет, так что удачи!
         """)
print("Что ты будешь делать?")



#Арена--------------------------------------------------------------------------
           

while player.hp > 0:
    menu = int(input("""Пойти на арену [1]
Посмотреть характеристики [2]\n"""))
    if menu == 2:
        print(f"{player.max_hp} здоровья")
        print(f"{player.max_mana} маны")
        print(f"{player.max_stam} выносливости")
        print(f"{player.mele_dam} урона в ближнем бою")
        print(f"{player.mag_dam} магического урона")
        input("Нажмите enter что бы продолжить")
        print("---------------------")

    if menu == 1:
        enemy_hp = 20 * randint(5, 20)
        enemy_dam = 10 * randint(2, 10)
        player.hp = player.max_hp
        player.mana = player.max_mana
        player.stam = player.max_stam
        while enemy_hp > 0:
            print(f"Здоровье врага: {enemy_hp} ")
            print(f"""Урон врага: {enemy_dam}
""")
            print(f"Что вы будете делать:")
            fight = int(input("""[1] Удар в ближнем бою
[2] Урон магией
[3] Силовая атака\n"""))
            if fight == 1:
                miss = randint(1, 2)
                if miss == 1:
                    enemy_hp = enemy_hp - player.mele_dam
                    print("Вы ударили врага")
                    print("---------------------")
                    print(f"Ваше здоровье: {player.hp}")
                    print("---------------------")
                if miss == 2:
                    player.hp = player.hp - enemy_dam
                    print("Враг смог уклониться от вашего удара и проатаковать в ответ")
                    print("---------------------")
                    print(f"Ваше здоровье: {player.hp}")
                    print("---------------------")
                    if player.hp <= 0:
                        print("Вы проиграли")
                        print("---------------------")
                        print("Хотите попробовать заново?")
                        n = int(input("[1] - да   [2] - нет\n"))
                        if n == 1:
                            enemy_hp = 20 * randint(5, 20)
                            enemy_dam = 10 * randint(2, 10)
                            player.hp = player.max_hp
                            player.mana = player.max_mana
                            player.stam = player.max_stam
                            if player.xp > 0:
                                player.xp = player.xp - 50
                        else:
                            exit()
                    if enemy_hp <= 0:
                        print("Вы выиграли")
                        print("---------------------")
                        player.xp = player.xp + 150
            if player.xp >= player.max_xp:
                player.xp = 0
                player.max_xp = player.max_xp + 100
                player.skills = player.skills + 1
                if player.skills > 0:
                    print(f"""Что вы хотите улучшить? Очков навыков: {player.skills}
                          """)
                    print("[1] Сила атаки")
                    print("[2] Здоровье")
                    print("[3] Интелект")
                    up = int(input())
                    if up == 1:
                        player.level = player.level + 1
                        player.mele_dam = player.mele_dam + 5
                        print(f"Сила атаки увеличина 10 --> {player.mele_dam}")
                        print(f"Ваш уровень: {player.level}")
                        print("---------------------")
                        player.skills = player.skills - 1
                        player.max_xp = player.max_xp + 100
                        player.xp = 0
                    if up == 2:
                        player.level = player.level + 1
                        player.max_hp = player.max_hp + 10
                        print(f"Максимальное здоровье увеличино 100 --> {player.max_hp}")
                        print(f"Ваш уровень: {player.level}")
                        print("---------------------")
                        player.skills = player.skills - 1
                        player.max_xp = player.max_xp + 100
                        player.xp = 0
                    if up == 3:
                        player.level = player.level + 1
                        player.max_mana = player.max_mana + 10
                        player.mag_dam = player.mag_dam + 5
                        print(f"Кол-во маны увеличино 100 --> {player.max_mana}")
                        print(f"Магический урон увеличен 20 --> {player.mag_dam}")
                        print(f"Ваш уровень: {player.level}")
                        print("---------------------")
                        player.skills = player.skills - 1
                        player.max_xp = player.max_xp + 100
                        player.xp = 0
                
                    
                        
            if fight == 2:
                if player.mana <= 0:
                    print("Вы не можете использовать магию")
                    print("---------------------")
                else:
                    enemy_hp = enemy_hp - player.mag_dam
                    player.mana = player.mana - 20
                    print("Вы ударили врага магией")
                    print("---------------------")
                    print(f"Ваше здоровье: {player.hp}")
                    print(f"Ваша мана: {player.mana}")
                    print("---------------------")
                    if enemy_hp <= 0:
                        print("Вы выиграли")
                        print("---------------------")
                        player.xp = player.xp + 150
            if player.xp >= player.max_xp:
                player.xp = 0
                player.max_xp = player.max_xp + 100
                player.skills = player.skills + 1
                if player.skills > 0:
                    print(f"""Что вы хотите улучшить? Очков навыков: {player.skills}
                          """)
                    print("[1] Сила атаки")
                    print("[2] Здоровье")
                    print("[3] Интелект")
                    up = int(input())
                    if up == 1:
                        player.level = player.level + 1
                        player.mele_dam = player.mele_dam + 5
                        print(f"Сила атаки увеличина 10 --> {player.mele_dam}")
                        print(f"Ваш уровень: {player.level}")
                        print("---------------------")
                        player.skills = player.skills - 1
                        player.max_xp = player.max_xp + 100
                        player.xp = 0
                    if up == 2:
                        player.level = player.level + 1
                        player.max_hp = player.max_hp + 10
                        print(f"Максимальное здоровье увеличино 100 --> {player.max_hp}")
                        print(f"Ваш уровень: {player.level}")
                        print("---------------------")
                        player.skills = player.skills - 1
                        player.max_xp = player.max_xp + 100
                        player.xp = 0
                    if up == 3:
                        player.level = player.level + 1
                        player.max_mana = player.max_mana + 10
                        player.mag_dam = player.mag_dam + 5
                        print(f"Кол-во маны увеличино 100 --> {player.max_mana}")
                        print(f"Магический урон увеличен 20 --> {player.mag_dam}")
                        print(f"Ваш уровень: {player.level}")
                        print("---------------------")
                        player.skills = player.skills - 1
                        player.max_xp = player.max_xp + 100
                        player.xp = 0
                

                
            if fight == 3:
                if player.stam <= 0:
                    print("Вы не можете провести силовую атаку")
                    print("---------------------")
                else:
                    enemy_hp = enemy_hp - (player.mele_dam + 15)
                    player.stam = player.stam - 25
                    print("Вы успешно провели силовую атаку")
                    print("---------------------")
                    print(f"Ваше здоровье: {player.hp}")
                    print(f"Ваша энергия: {player.stam}")
                    print("---------------------")
                    if enemy_hp <= 0:
                        print("Вы выиграли")
                        print("---------------------")
                        player.xp = player.xp + 150
            if player.xp >= player.max_xp:
                player.xp = 0
                player.skills = player.skills + 1
                if player.skills > 0:
                    print(f"""Что вы хотите улучшить? Очков навыков: {player.skills}
                          """)
                    print("[1] Сила атаки")
                    print("[2] Здоровье")
                    print("[3] Интелект")
                    up = int(input())
                    if up == 1:
                        player.level = player.level + 1
                        player.mele_dam = player.mele_dam + 5
                        print(f"Сила атаки увеличина 10 --> {player.mele_dam}")
                        print(f"Ваш уровень: {player.level}")
                        print("---------------------")
                        player.skills = player.skills - 1
                        player.max_xp = player.max_xp + 100
                        player.xp = 0
                    if up == 2:
                        player.level = player.level + 1
                        player.max_hp = player.max_hp + 10
                        print(f"Максимальное здоровье увеличино 100 --> {player.max_hp}")
                        print(f"Ваш уровень: {player.level}")
                        print("---------------------")
                        player.skills = player.skills - 1
                        player.max_xp = player.max_xp + 100
                        player.xp = 0
                    if up == 3:
                        player.level = player.level + 1
                        player.max_mana = player.max_mana + 10
                        player.mag_dam = player.mag_dam + 5
                        print(f"Кол-во маны увеличино 100 --> {player.max_mana}")
                        print(f"Магический урон увеличен 20 --> {player.mag_dam}")
                        print(f"Ваш уровень: {player.level}")
                        print("---------------------")
                        player.skills = player.skills - 1
                        player.max_xp = player.max_xp + 100
                        player.xp = 0
                
                


        







                
                

            
            
                
         
        

        
        
        
        
                
    
            
























    


        
        
       

