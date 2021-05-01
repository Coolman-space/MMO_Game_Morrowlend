import os
import re
import sys
import random
import time
import text as t
import Quests
from character import Character

# Player Characters
pc_Lucznik = Character("łucznik",100,100,60, 50 ,1,1 )
pc_Mag = Character("Mag",100,100, 30, 70, 1,1, )
pc_Assasine = Character("Assasine",100,100, 60, 40 ,1,1)
# Game Initialization
players = [pc_Lucznik,pc_Mag,pc_Assasine]
def check_stats(stat):
    stat = str(stat)
    if len(stat) < 3 and len(stat) > 1:
        stat = stat + " "
    elif len(stat) < 2:
        stat = stat + "  "
    return stat
def matrix():

    symbols = ["1", "0", " ", " "]
    line = []
    counter = 0
    for i in range(118):
        x = random.randint(0, 3)
        line.append(symbols[x])
        counter += 1

    for i in range(150):
        if counter % 5 == 0:
            r_symbols = [random.randint(0, 117)for x in range(10)]
            for i in r_symbols:
                line[i] = symbols[random.randint(0, 3)]
        print(*line)
        time.sleep(0.03)
        counter += 1



    return None
def pressenter():
    print("╔══════════════════════════════════════════╗")
    print("║     PRESS ENTER TO SHOW ANOTHER HERO     ║")
    print("╚══════════════════════════════════════════╝")
    input()
def Tor():
    print("██████████████████████████████████████████████████████")
    print("█          PLEASE WRITHE YOUR NICKNAME               █")
    print("██████████████████████████████████████████████████████")
def display_stats():
    print("\n")
    print("╔═══════════════╗          ╔══════════════════╗          ╔════════════════╗")
    print("║     Names     ║          ║      Health      ║          ║      Mana      ║")
    print("╚═══════════════╝          ╚══════════════════╝          ╚════════════════╝")
    for player in players:
        print(player.name + "           " + check_stats(player.health) + "                           " + check_stats(player.mana))
    print("\n")
def save_game_1():
    plik = open('save_level.txt', 'w' )
    plik.write(str('1'))
    plik.close()
#def save_game_defolt_0():
 #   plik = open('save_level.txt','w')
  #  plik.write(str('0'))
  #  plik.close()
  ######START#########

def Start_normal():
    t.print_Logo()
    matrix()
    os.system('cls')
    for i in t.Welcome_Menu:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.000001)
    loop = input(":>>>> ")
    if loop in ("Play","play","PLAY"):
        os.system("cls")
        Global_Start()
    elif loop in ("Load","load","LOAD"):
        Quests.Load()
        file = open('save_level.txt', 'r').read()
        int(file)
        if file == str(0):
            Quests.print_for_sumbols(" ██ ██ ██ Niestety jeszcze nie masz zapisanej gry. PRESS ENTER to NEW GAME!) ██ ██ ██ ")
            input()
            os.system("cls")
            Start_normal()
        elif file == str(1):
            for i in range(10):
                print(t.Load)
                time.sleep(0.8)
                os.system("cls")
            Quests.General_Level_1()
        elif file == str(2):
            for i in range(10):
                print(t.Load)
                time.sleep(0.8)
                os.system("cls")
            Quests.General_Level_2()
        elif file == str(3):
            for i in range(10):
                print(t.Load)
                time.sleep(0.8)
                os.system("cls")
            Quests.General_Level_3()
    elif  loop == "Exit":
          sys.exit()
    else:
        Start_normal()
def Global_Start():
    t.print_First_story()
    t.print_chage()
    #####Lucznik#######
    #t.print_Info_Lucznik()
    print("\n")
    print("╔═══════════════╗          ╔══════════════════╗          ╔════════════════╗          ╔════════════════╗")
    print("║     Names     ║          ║      Health      ║          ║      Mana      ║          ║     defense    ║")
    print("╚═══════════════╝          ╚══════════════════╝          ╚════════════════╝          ╚════════════════╝")
    print("\n")
    print("     "+pc_Lucznik.name + "                        " + check_stats(pc_Lucznik.health) + "                        " + check_stats(pc_Lucznik.mana)+ "                           " + check_stats(pc_Lucznik.defense))
    print("\n")
    print("\n")
    pressenter()
    os.system('cls')
    ########Mag########
   # t.print_Info_Mag()
    print("\n")
    print("╔═══════════════╗          ╔══════════════════╗          ╔════════════════╗          ╔════════════════╗")
    print("║     Names     ║          ║      Health      ║          ║      Mana      ║          ║     defense    ║")
    print("╚═══════════════╝          ╚══════════════════╝          ╚════════════════╝          ╚════════════════╝")
    print("\n")
    print("     "+pc_Mag.name + "                              " + check_stats(pc_Mag.health) + "                        " + check_stats(pc_Mag.mana)+ "                           " + check_stats(pc_Mag.defense))
    print("\n")
    print("\n")
    pressenter()
    os.system('cls')
    #######assasine#########
   # t.print_Info_Assasine()
    print("\n")
    print("╔═══════════════╗          ╔══════════════════╗          ╔════════════════╗          ╔════════════════╗")
    print("║     Names     ║          ║      Health      ║          ║      Mana      ║          ║     defense    ║")
    print("╚═══════════════╝          ╚══════════════════╝          ╚════════════════╝          ╚════════════════╝")
    print("\n")
    print("     "+pc_Assasine.name + "                        " + check_stats(pc_Assasine.health) + "                        " + check_stats(pc_Assasine.mana)+ "                           " + check_stats(pc_Assasine.defense))
    print("\n")
    print("\n")
    pressenter()
    os.system('cls')
    print("╔═══════════════╗          ╔══════════════════╗          ╔════════════════╗")
    print("║  1. łucznik   ║          ║      2. Mag      ║          ║  3. ASSASINE   ║")
    print("╚═══════════════╝          ╚══════════════════╝          ╚════════════════╝")
    print("╔═══════════════════════════════════════════════════════════════════╗")
    print("║                         PRESS 1,2,3 FOR CHOICE                    ║")
    print("╚═══════════════════════════════════════════════════════════════════╝")


    Hero_Choise = int(input()) - 1
    if Hero_Choise == 0:
        players.remove(pc_Mag)
        players.remove(pc_Assasine)
        print("\n")
        print("████████████████████████████████████████████")
        print("█     You choises " + pc_Lucznik.name + "                  ")
        print("████████████████████████████████████████████")
        print("\n")
        Tor()
        pc_Lucznik.name = input(">>")
        print("\n")
        print("█████████████████████████████████████████████████████████████████████")
        print("█                    HELLO        " + pc_Lucznik.name + "                              ")
        print("█████████████████████████████████████████████████████████████████████")
        print("\n")
        time.sleep(2)
        os.system('cls')
        save_game_1()
        for i in range(10):
            print(t.Save)
            time.sleep(0.8)
            os.system("cls")
        Quests.General_Level_1()
    elif Hero_Choise == 1:
        players.remove(pc_Lucznik)
        players.remove(pc_Assasine)
        print("\n")
        print("████████████████████████████████████████████")
        print("█     You choises " + pc_Mag.name + "                  ")
        print("████████████████████████████████████████████")
        print("\n")
        Tor()
        pc_Mag.name = input(">>")
        print("\n")
        print("█████████████████████████████████████████████████████████████████████")
        print("█                    HELLO    " + pc_Mag.name + "                            ")
        print("█████████████████████████████████████████████████████████████████████")
        print("\n")
        time.sleep(2)
        os.system('cls')
        save_game_1()
        for i in range(10):
            print(t.Save)
            time.sleep(0.8)
            os.system("cls")
        Quests.General_Level_1()
    else:
        players.remove(pc_Mag)
        players.remove(pc_Lucznik)
        print("\n")
        print("████████████████████████████████████████████")
        print("█     You choises " + pc_Assasine.name + "                  ")
        print("████████████████████████████████████████████")
        print("\n")
        Tor()
        pc_Assasine.name = input(">>")
        print("\n")
        print("█████████████████████████████████████████████████████████████████████")
        print("█                   HELLO     " + pc_Assasine.name + "                                    ")
        print("█████████████████████████████████████████████████████████████████████")
        print("\n")
        time.sleep(2)
        os.system('cls')
        save_game_1()
        for i in range(10):
            print(t.Save)
            time.sleep(0.8)
            os.system("cls")
        Quests.General_Level_1()
    input()
Start_normal()

