import os
import random
import sys
import time
import character
import inventory
import magic
import text as t


class Lokacje:

    def __init__(self,name,levdeng):
        self.name = name
        self.levdeng = levdeng
        self.status = 0
class ucze:
    def __init__(self,name):
        self.name = name
        self.power =random.randint(1,9)
        self.stat = 0

###URON I CHILL Z WALKI

Your_Hero = character.Character(" Dima" , 100 , 100 , 100 , 100 , 10 , 1)
umre_lub_nie = 0
# Black Magic
bm_avada = magic.Spell("Avada Kedavra", 99, 100, "black")
bm_cruciatus = magic.Spell("Cruciatus Curse", 70, 70, "black")
bm_knockback = magic.Spell("Knockback Jinx", 10, 10, "black")
bm_oppugno = magic.Spell("Oppugno Jinx", 15, 15, "black")
bm_sectumsempra = magic.Spell("Sectumsempra", 60, 60, "black")
bm_stinging = magic.Spell("Stinging Jinx", 20, 20, "black")
bm_toenail = magic.Spell("Toenail-Growing Hex", 5, 5, "black")

# White Magic
wm_confundo = magic.Spell("Confundo", 15, 15, "white")
wm_expelliarmus = magic.Spell("Expelliarmus", 25, 25, "white")
wm_finestra = magic.Spell("Finestra", 10, 10, "white")
wm_levicorpus = magic.Spell("Levicorpus", 10, 10, "white")
wm_muffliato = magic.Spell("Muffliato", 15, 15, "white")
wm_petrificus = magic.Spell("Petrificus Totalus", 25, 25, "white")
wm_stupefy = magic.Spell("Stupefy", 20, 20, "white")

All_magic = [bm_avada,bm_cruciatus,bm_knockback,bm_oppugno,bm_sectumsempra,bm_stinging,bm_toenail,wm_confundo,wm_expelliarmus,wm_finestra,wm_levicorpus,wm_muffliato,wm_petrificus,wm_stupefy]

# Attack Potions
pt_confusing = inventory.Item("Białe szkło przecił smogów", "attack", "Może pomóc w walcę z smogiem. Ma zdolność do przebicia skóry smoga ")
pt_death = inventory.Item("Eliksyr Bora", "attack", "Eliksyr za pomocą którego możemy stworzyć bardzo potężny mecz który ma wielki damage")
pt_emerald = inventory.Item("Nefriwe szkło", "attack", "Może pomóc w walce z smogiem. Ma zdolność do wstrzymania ognia Smoga ")

###############LVL_1 QUESTS#######################
Lok_1_LV_1 = Lokacje("Black_Town",2)
Lok_2_LV_1 = Lokacje("Goast_Town",4)
Lok_3_LV_1 = Lokacje("Jaskinia Druida",1)
Lok_4_LV_1 = Lokacje("Latający most",3)
Lok_5_LV_1 = Lokacje("Niebiańska_kużnia",5)
###############LVL_2 QUESTS#######################
Lok_1_LV_2 = Lokacje("Forest",4)
Lok_2_LV_2 = Lokacje("Desert",4)
Lok_3_LV_2 = Lokacje("Myśliwski dom",3)
Lok_4_LV_2 = Lokacje("Zamek",4)
Lok_5_LV_2 = Lokacje("Most smoga",2)
###############LVL_3 QUESTS#######################
Lok_1_LV_3 = Lokacje("Pekielne góry",5)
Lok_2_LV_3 = Lokacje("Miasto goblinów",8)
Lok_3_LV_3 = Lokacje("Dolina werwolfów",9)
Lok_4_LV_3 = Lokacje("Błoto",5)
Lok_5_LV_3 = Lokacje("Piekelna kużnia",7)
All_location = [Lok_1_LV_1,Lok_2_LV_1,Lok_3_LV_1,Lok_4_LV_1,Lok_5_LV_1,Lok_1_LV_2,Lok_2_LV_2,Lok_3_LV_2,Lok_4_LV_2,Lok_5_LV_2,Lok_1_LV_3,Lok_2_LV_3,Lok_3_LV_3,Lok_4_LV_3,Lok_5_LV_3]
def Save():
    saveGame = open("save_place.txt", "w")
    for i in All_location:
        saveGame.write(str(i.status)+"\n")
    saveGame.close()
def Load():
    Load_game = open("save_place.txt", "r")
    j = 0
    for i in Load_game:
        All_location[j].status = int(i)
        j = j + 1
    Load_game.close()
def save_game_2():
    plik = open('save_level.txt','w')
    plik.write(str('2'))
    plik.close()
def save_game_3():
    plik = open('save_level.txt','w')
    plik.write(str('3'))
    plik.close()
def print_for_sumbols(costam):
    for i in costam:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)
def heal_mana():
    Your_Hero.health = 100
    Your_Hero.mana = 100
def print_location_1():

    for i in range(len(All_location)):
        if i < 4 or i == 4:
            print("Name:  "+ All_location[i].name)
            print("Level_danger:  " + str(All_location[i].levdeng))
            if All_location[i].status == int(0):
                print_for_sumbols("Status: not pass\n")
            else:
                print_for_sumbols("Status:  pass\n")
        if i > 4:
            print("\nZamknięte lokację ####\n")
            print("Name:  " + All_location[i].name + ":  close  at that Level")
            print("Level_danger:  " + str(All_location[i].levdeng))
        print("\n_______________________________")
def print_location_2():

    for i in range(len(All_location)):
        if  i < 9 or i == 9:
            print("Name:  "+ All_location[i].name)
            print("Level_danger:  " + str(All_location[i].levdeng))
            if All_location[i].status == int(0):
                print_for_sumbols("Status: not pass\n")
            else:
                print_for_sumbols("Status:  pass\n")
        if i > 9:
            print("\nZamknięte lokację ####\n")
            print("Name:  " + All_location[i].name + ":  close  at that Level")
            print("Level_danger:  " + str(All_location[i].levdeng))
        print("\n_______________________________")
def print_location_3():
    for i in range(len(All_location)):
            print("Name:  "+ All_location[i].name)
            print("Level_danger:  " + str(All_location[i].levdeng))
            if All_location[i].status == int(0):
                print_for_sumbols("Status: not pass\n")
            else:
                print_for_sumbols("Status:  pass\n")
            print("\n_______________________________")
############################ LEVEL 1
def General_Level_1():
    t.print_Quest_Start()
    print("\n")
    os.system('cls')
    print(t.maps_start)
    print("█████████████████████████████████████████████████████████████████████")
    print("║                    PRESS ENTER TO DELIVER TO LEVEL 1              ║")
    print("█████████████████████████████████████████████████████████████████████")
    print("\n")
    input()
    os.system('cls')
    print(t.maps_NORTH)
    print("█████████████████████████████████████████████████████████████████████")
    print("║                          DELIVER SUCCESS                          ║")
    print("█████████████████████████████████████████████████████████████████████")
    time.sleep(7)
    os.system('cls')
    Rekursywna_LVL_1()
def Rekursywna_LVL_1():
    HTODO = input("║║║Wpisz co chcesz zrobić║║║-║║║albo help dla pomocy║║║ >>> ")

    if HTODO in ("help","Help","HELP"):
        print(t.help_text)
        print("\n")
        Rekursywna_LVL_1()
    elif HTODO in ("Next_level","NEXT_LEVEL","next_level","next_Level"):
        for i in range(4):
            if All_location[i].status == int(0):
                print("Niestety masz jeszcze lokacje w których nie byłeś, muszisz wykonać zadania w każdej")
                Rekursywna_LVL_1()
        save_game_2()
        for i in range(10):
            print(t.Save)
            time.sleep(0.8)
            os.system("cls")
        General_Level_2()
    elif HTODO in ("Save","SAVE","save"):
        Save()
        print_for_sumbols("Your game saved!!!\n")
        time.sleep(3)
        Rekursywna_LVL_1()
    elif HTODO in ("quit","Quit","QUIT"):
        sys.exit()
    elif HTODO in ("Check","check","CHECK",):
        print("╔═══════════════════════════════════════════════════════════════════╗")
        print("║                         DOSTĘPNE LOKACJĘ NA 1 LVL                 ║")
        print("╚═══════════════════════════════════════════════════════════════════╝")
        print_location_1()
        Rekursywna_LVL_1()
    elif HTODO in ("Do_kwest","do_kwest","DO_KWEST"):
        WTODO = input(" ║║║ Prosze wpisać nazwę lokacji ║║║  :>>>> ")
        if WTODO in ("Black_Town","Goast_Town","Jaskinia Druida","Latający most","Niebiańska_kużnia","Forest","Desert",
                     "Myśliwski dom","Zamek","Most smoga","Pekielne góry","Miasto goblinów","Dolina werwolfów","Błoto","Piekelna kużnia"):
            if WTODO == "Black_Town":
                if Lok_1_LV_1.status == int(0):
                    Quest_LV_1_1()
                    przygoda_1()
                    Lok_1_LV_1.status = int(1)
                    Rekursywna_LVL_1()
                else:
                    print_for_sumbols("Już byłeś w tej lokacji , przejdż do innej")
                    Rekursywna_LVL_1()
            if WTODO == "Goast_Town":
                if Lok_2_LV_1.status == int(0):
                    Quest_LV_1_2()
                    przygoda_2()
                    Lok_2_LV_1.status = int(1)
                    Rekursywna_LVL_1()
                else:
                    print_for_sumbols("Już byłeś w tej lokacji , przejdż do innej")
                    Rekursywna_LVL_1()
            if WTODO == "Jaskinia Druida":
                if Lok_3_LV_1.status == int(0):
                    Quest_LV_1_3()
                    przygoda_3()
                    Lok_3_LV_1.status = int(1)
                    Rekursywna_LVL_1()
                else:
                    print_for_sumbols("Już byłeś w tej lokacji , przejdż do innej")
                    Rekursywna_LVL_1()
            if WTODO == "Latający most":
                if Lok_4_LV_1.status == int(0):
                    Quest_LV_1_4()
                    przygoda_4()
                    Lok_4_LV_1.status = int(1)
                    Rekursywna_LVL_1()
                else:
                    print_for_sumbols("Już byłeś w tej lokacji , przejdż do innej")
                    Rekursywna_LVL_1()
            if WTODO == "Niebiańska_kużnia":
                if Lok_5_LV_1.status == int(0):
                    Quest_LV_1_5()
                    przygoda_5()
                    Lok_5_LV_1.status = int(1)
                    Rekursywna_LVL_1()
                else:
                    print_for_sumbols("Już byłeś w tej lokacji , przejdż do innej")
                    Rekursywna_LVL_1()


        else:
            print_for_sumbols("Niestety nie znależliśmy takiej lokacji albo jest zamknięta\n")
            Rekursywna_LVL_1()
    else:
        print_for_sumbols("Niestety wpisałeś niepoprawne zanaczenie !!! Wpisz help")
        Rekursywna_LVL_1()
def Quest_LV_1_1():
    print_for_sumbols(t.Quest_LV_1_1)
    left_Right = input(">>>")
    if left_Right == "left":
        print("██ ██ ██ Zgadnołeś przechodzimy do kolejnego kwesta ██ ██ ██")
        print("\n")
        print("╔══════════════════════════════════════════╗")
        print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
        print("╚══════════════════════════════════════════╝")
        input()
    else:
        print("██ ██ ██ Oh, niestety nie zgadnąłeś ██ ██ ██")
        print("██ ██ ██ sprobój jeszcze raz ██ ██ ██")
        Quest_LV_1_1()
def Quest_LV_1_2():
        os.system('cls')
        print_for_sumbols(t.Quest_LV_1_2)
        duch_hp = int(50)
        Your_Hero.display_actions()
        action_y = input("██ ██ WRITE ATTACK , MAGIC , OR LOSE ██ ██   >>>")
        if action_y in ("attack" , "Attack" , "ATTACK" ,"Magic","magic","MAGIC","lose","Lose","LOSE"):
            if action_y in ("attack","Attack","ATTACK"):
                duch_hp = duch_hp - random.randrange(49,52)
                if duch_hp < 1:
                    print("██ ██ ██ Zabiłeś Ducha ██ ██ ██")
                    time.sleep(3)
                else:
                    print("██ ██ ██ Niestety nie zabiłeś go ██ ██ ██")
                    Your_Hero.health = Your_Hero.health - 10
                    print("\n")
                    print("Twoje zdrowie po walcę: " + str(Your_Hero.health))

            elif action_y in ("Magic","magic","MAGIC"):

                for i in range(len(All_magic)):
                    print(i)
                    print("name spall:     " +All_magic[i].name)
                    print("damage spall:    "+ str(All_magic[i].damage))
                    print("cost spall:     " + str(All_magic[i].damage))
                    print("\n")

                print("██ ██ ██ Choise spell  (write name!) ██ ██ ██")
                spell_name = input(">>>")
                for i in range(len(All_magic)):
                    if All_magic[i].name == spell_name:
                        while duch_hp > int(0):
                          duch_hp = duch_hp - All_magic[i].damage
                          Your_Hero.mana = Your_Hero.mana - All_magic[i].cost
                          print("Duch HP NOW:  " + str(duch_hp))
                          print("Jeszcze raz korzystamy z: " + All_magic[i].name)
                          Your_Hero.health = Your_Hero.health - 10
                        print("\n")
                        print("██ ██ ██ Zabiłeś Ducha ██ ██ ██")
                        print("\n")
                        print("██ ██ ██ Twoje mana po walcę: " + str(Your_Hero.mana))
                        print("\n")
                        print("██ ██ ██ Twoje hp po walcę: " + str(Your_Hero.health))
                        if Your_Hero.health < 0:
                            print("Niestety zmarłeś ")
                            time.sleep(5)
                            Quest_LV_1_2()


                print("\n")
                print("╔══════════════════════════════════════════╗")
                print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
                print("╚══════════════════════════════════════════╝")
                input("Diałą :)")
            else:
                print("██ ██ ██ Nawet nie myśliałem że jesteś takim bojazkim ██ ██ ██")
                print("\n")
                print("╔══════════════════════════════════════════╗")
                print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
                print("╚══════════════════════════════════════════╝")
                input("Diałą :)")
        else:
            print("██ ██ ██ Wpisałeś nieprawidłowe znaczenie. To będzie pouczenie dla ciebie. Nie zobaczyś walki((( ██ ██ ██")
            print("\n")
            print("╔══════════════════════════════════════════╗")
            print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
            print("╚══════════════════════════════════════════╝")
            input()
def Quest_LV_1_3():
    os.system("cls")
    print_for_sumbols(t.Quest_LV_1_3)
    time.sleep(5)
    print("\n")
    print(" ██ ██ ██ Wpisz inną nazwe każdej rośliny dwa razy ██ ██ ██")
    print(t.pole_for_quest_Lv_1_3)
    rosly_count = 0
    while rosly_count < 6:
     roslina_h = input(" ██ ██ Wpisz nazwę rośliny ██ ██ >>")
     if roslina_h in ("ty3434",  "fg3423","gfg333"):
         if roslina_h == "ty3434":
             print("Dostałeś 1 Trizalię.")
             rosly_count = rosly_count + 1
         elif roslina_h == "fg3423":
             print("Dostałeś 1 Bretos.")
             rosly_count = rosly_count + 1
         else:
             print("Dostałeś 1 Broska.")
             rosly_count = rosly_count + 1
     else:
        (print(" ██ ██ ██ Wpisałeś coś innego. Niestety Druid nie uratował ciebie, spróbój jeszcze raz ██ ██ ██"))
        time.sleep(4)
        Quest_LV_1_3()
    print("██ ██ ██ Dostałeś wszystkie potrzebne rośliny ██ ██ ██")
    print("\n")
    print("   ██ ██ ██ Druid uratował tobie życie ██ ██ ██")
    print("\n")
    print("╔══════════════════════════════════════════╗")
    print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
    print("╚══════════════════════════════════════════╝")
    input()
def Quest_LV_1_4():
    os.system("cls")
    print_for_sumbols(t.Quest_LV_1_4)
    H_M_Space = input("preeeeeesssssss >>>>>    ")
    if len(H_M_Space) < 11:
        print(" ██ ██ ██ Niestety, tobie nie wystarczyło szybkości  ██ ██ ██")
        print("\n")
        print(" ██ ██ ██ (za mało naciśnień 'SPACE')  SPRÓBÓJ JESZCZE RAZ  ██ ██ ██")
        time.sleep(3)
        Quest_LV_1_4()
    else:
        print(" ██ ██ ██  uhhhhhh... Zdążyłeś, prawie zginąłeś. Jeszcze będziesz mieć szanse , zabić smoga , ale nie teraz  ██ ██ ██")
    print("\n")
    print("╔══════════════════════════════════════════╗")
    print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
    print("╚══════════════════════════════════════════╝")
    input()
    Lok_4_LV_1.status = True
def Quest_LV_1_5():
    os.system("cls")
    print_for_sumbols(t.Quest_LV_1_5)
    print("██ ██ ██ Kiedy zobaczysz mysz: press enter ██ ██ ██")
    print("██ ██ ██ Muszisz zabić 10 myszej ██ ██ ██")
    killed_mause = int(0)
    while  killed_mause < 10:
        req = random.randint(3,7)
        time.sleep(req)
        print(t.mause)
        kill_m = input("kill mouse   >>>> ")
        print("\n")
        szansa_k = random.randint(1,100)
        if szansa_k > 35:
            killed_mause = killed_mause + 1
            print("██ ██ ██ Zabiłeś mysz ██ ██ ██")
            print(" Zabiłeś na ten moment: " + str(killed_mause))
        else:
            print("██ ██ ██ Nie zabiłeś sprobój jeszcze raz ██ ██ ██")
            print(" Zabiłeś na ten moment: " + str(killed_mause))

    print("██ ██ ██ Zabiłeś 10 mysz !!!! ██ ██ ██")
    print("\n")
    print("██ ██ ██ Kowal oddaje tobie 'Białe Szkło' ██ ██ ██")
    print("\n")
    time.sleep(3)
    os.system("cls")
    print_for_sumbols(t.Get_Item_1)
    print("\n")
    print("╔══════════════════════════════════════════╗")
    print("║       PRESS ENTER  GO  TO LEVEL 2        ║")
    print("╚══════════════════════════════════════════╝")
    input()
############################# LEVEL 2
def General_Level_2():
        os.system('cls')
        print(t.maps_NORTH)
        print("█████████████████████████████████████████████████████████████████████")
        print("║                    PRESS ENTER TO DELIVER TO LEVEL 2              ║")
        print("█████████████████████████████████████████████████████████████████████")
        print("\n")
        input()
        os.system('cls')
        print(t.maps_WEST)
        print("█████████████████████████████████████████████████████████████████████")
        print("║                          DELIVER SUCCESS                          ║")
        print("█████████████████████████████████████████████████████████████████████")
        time.sleep(7)
        os.system('cls')
        Rekursywna_LVL_2()
def Rekursywna_LVL_2():
    HTODO = input("║║║Wpisz co chcesz zrobić║║║-║║║albo help dla pomocy║║║ >>> ")

    if HTODO in ("help","Help","HELP"):
        print(t.help_text)
        print("\n")
        Rekursywna_LVL_2()
    elif HTODO in ("Next_level","NEXT_LEVEL","next_level","next_Level"):
        for i in range(9):
            if All_location[i].status == int(0):
                print("Niestety masz jeszcze lokacje w których nie byłeś, muszisz wykonać zadania w każdej")
                Rekursywna_LVL_2()
        save_game_3()
        for i in range(10):
            print(t.Save)
            time.sleep(0.8)
            os.system("cls")
        General_Level_3()
    elif HTODO in ("Save","SAVE","save"):
        Save()
        print_for_sumbols("Your game saved!!!\n")
        time.sleep(3)
        Rekursywna_LVL_2()
    elif HTODO in ("quit","Quit","QUIT"):
        sys.exit()
    elif HTODO in ("Check","check","CHECK",):
        print("╔═══════════════════════════════════════════════════════════════════╗")
        print("║                         DOSTĘPNE LOKACJĘ NA 2 LVL                 ║")
        print("╚═══════════════════════════════════════════════════════════════════╝")
        print_location_2()
        Rekursywna_LVL_2()
    elif HTODO in ("Do_kwest","do_kwest","DO_KWEST"):
        WTODO = input(" ║║║ Prosze wpisać nazwę lokacji ║║║  :>>>> ")
        if WTODO in ("Black_Town","Goast_Town","Jaskinia Druida","Latający most","Niebiańska_kużnia","Forest","Desert",
                     "Myśliwski dom","Zamek","Most smoga","Pekielne góry","Miasto goblinów","Dolina werwolfów","Błoto","Piekelna kużnia"):
            if WTODO == "Forest":
                if Lok_1_LV_2.status == int(0):
                    Quest_LV_2_1()
                    przygoda_6()
                    przygoda_7()
                    Lok_1_LV_2.status = int(1)
                    Rekursywna_LVL_2()
                else:
                    print_for_sumbols("Już byłeś w tej lokacji , przejdż do innej")
                    Rekursywna_LVL_2()
            if WTODO == "Desert":
                if Lok_3_LV_2.status == int(0):
                    Quest_LV_2_2()
                    przygoda_8()
                    przygoda_9()
                    Lok_2_LV_2.status = int(1)
                    Rekursywna_LVL_2()
                else:
                    print_for_sumbols("Już byłeś w tej lokacji , przejdż do innej")
                    Rekursywna_LVL_2()
            if WTODO == "Myśliwski dom":
                if Lok_3_LV_2.status == int(0):
                    Quest_LV_2_3()
                    przygoda_10()
                    przygoda_11()
                    Lok_3_LV_2.status = int(1)
                    Rekursywna_LVL_2()
                else:
                    print_for_sumbols("Już byłeś w tej lokacji , przejdż do innej")
                    Rekursywna_LVL_2()
            if WTODO == "Zamek":
                if Lok_4_LV_2.status == int(0):
                    Quest_LV_2_4()
                    przygoda_12()
                    przygoda_13()
                    Lok_4_LV_2.status = int(1)
                    Rekursywna_LVL_2()
                else:
                    print_for_sumbols("Już byłeś w tej lokacji , przejdż do innej")
                    Rekursywna_LVL_2()
            if WTODO == "Most smoga":
                if Lok_5_LV_2.status == int(0):
                    Quest_LV_2_5()
                    przygoda_14()
                    przygoda_15()
                    Lok_5_LV_2.status = int(1)
                    Rekursywna_LVL_2()
                else:
                    print_for_sumbols("Już byłeś w tej lokacji , przejdż do innej")
                    Rekursywna_LVL_2()


            else:
                print_for_sumbols("Niestety nie znależliśmy takiej lokacji albo jest zamknięta\n")
                Rekursywna_LVL_2()
    else:
        print_for_sumbols("Niestety wpisałeś niepoprawne zanaczenie !!! Wpisz help")
        Rekursywna_LVL_2()
def Quest_LV_2_1():
    print_for_sumbols(t.Quest_LV_2_1)
    print("██ ██ ██ Niestety nie pamiętasz dokładnie nazwe spella ██ ██ ██")
    print("\n")
    print("██ ██ ██ Muszisz wiedzieć napełno żeby uratować wiewiórkę, a nie zabić ją ██ ██ ██")
    print("██ ██ ██ Początek spella to Mu .... hmmm . Otwórz magiczną książkę. >>PRESS ENTER ██ ██ ██")
    input()
    print("\n")

    for i in range(len(All_magic)):
        print(i)
        print("name spall:     " + All_magic[i].name)
        print("damage spall:    " + str(All_magic[i].damage))
        print("cost spall:     " + str(All_magic[i].damage))
        print("\n")
        time.sleep(0.6)

    print("██ ██ ██ Choise spell  (write full name!) ██ ██ ██")
    spell_name = input(">>>")
    if spell_name == wm_muffliato.name:
              Your_Hero.health = Your_Hero.health - wm_muffliato.damage
              Your_Hero.mana = Your_Hero.mana - wm_muffliato.cost
              print("██ ██ ██ Udało się , wiewiórka będzie żyć!!  ██ ██ ██")
              print("\n")
              print("██ ██ ██ Jako podarunek od wiewiórek dostałeś sok drzewa  ██ ██ ██")
              print("\n")
              print("██ ██ ██ Twoje mana na ten moment:  " + str(Your_Hero.mana))
              print("██ ██ ██ Twoje hp na ten moment:  " + str(Your_Hero.health))
              print("\n")
              print("╔══════════════════════════════════════════╗")
              print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
              print("╚══════════════════════════════════════════╝")
              input()
    else:
        print("██ ██ ██ Niestety wybrałeś nie ten spell i wiewiórka umarła. R.I.P.  ██ ██ ██")
        Quest_LV_2_1()
def Quest_LV_2_2():
     os.system("cls")
     print_for_sumbols(t.Quest_LV_2_2)
     Robak_hp = int(550)
     print("██ ██ ██ uhhh. Wygląda na to że ten rabak ma dużo hp ██ ██ ██")
     print("\n")
     print("██ ██ ██ Muszisz coś wymyśleć żeby pokonać go!!!!! ██ ██ ██")
     print("\n")
     print("██ ██ ██ Co robimy !!!!! ██ ██ ██")
     print("\n")
     print("╔═══════════════════════════╗")
     print("║          Actions          ║")
     print("╚═══════════════════════════╝")
     print("What would you like to do?\n")
     print("1. Po prostu Atakować   (wpisz: atakować)\n")
     print("2. Coś wymyśleć        (wpisz: wymyśleć)\n")
     Action_cheng = input(">>>>>>")
     if Action_cheng == "atakować":
        Your_Hero.display_actions()
        action_y = input("██ ██ WRITE ATTACK , MAGIC , OR LOSE ██ ██   >>>")
        if action_y in ("attack", "Attack", "ATTACK", "Magic", "magic", "MAGIC", "lose", "Lose", "LOSE"):
            if action_y in ("attack", "Attack", "ATTACK"):
                Robak_hp = Robak_hp - random.randrange(70, 100)
                if Robak_hp < 1:
                    print("██ ██ ██ Zabiłeś Robaka ██ ██ ██")
                else:
                    print("██ ██ ██ Niestety nie zabiłeś go. Zmarłeś ██ ██ ██")
                    Your_Hero.health = Your_Hero.health - 60
                    print("\n")
                    print("Twoje zdrowie po walcę: 0 ")
                    time.sleep(4)
                    if Your_Hero.health < 0:
                        print("Niestety zmarłeś ")
                        time.sleep(5)
                        Quest_LV_2_2()
                    else:
                        Quest_LV_2_2()

            elif action_y in ("Magic", "magic", "MAGIC"):

                for i in range(len(All_magic)):
                    print(i)
                    print("name spall:     " + All_magic[i].name)
                    print("damage spall:    " + str(All_magic[i].damage))
                    print("cost spall:     " + str(All_magic[i].damage))
                    print("\n")

                print("██ ██ ██ Choise spell  (write name!) ██ ██ ██")
                spell_name = input(">>>")
                for i in range(len(All_magic)):
                    if All_magic[i].name == spell_name:
                        while Your_Hero.mana > int(0):
                            Robak_hp = Robak_hp - All_magic[i].damage
                            Your_Hero.mana = Your_Hero.mana - All_magic[i].cost
                            print("Robak HP NOW:  " + str(Robak_hp))
                            print("Jeszcze raz korzystamy z: " + All_magic[i].name)
                            Your_Hero.health = Your_Hero.health - 49
                            if Your_Hero.health < 0:
                                print("Niestety zmarłeś ")
                                time.sleep(5)
                                Quest_LV_2_2()
                        print("\n")
                        print("██ ██ ██ Niestety nie zabiłeś Rabaka ██ ██ ██")
                        print("\n")
                        print("██ ██ ██ Twoje mana po walcę: " + str(Your_Hero.mana))
                        print("\n")
                        print("██ ██ ██ Twoje hp po walcę: " + str(Your_Hero.health))
                        if Your_Hero.health < 0:
                            print("Niestety zmarłeś ")
                            time.sleep(5)
                            Quest_LV_2_2()

            else:
                Quest_LV_2_2()
        else:
            print(
                "██ ██ ██ Wpisałeś nieprawidłowe znaczenie. To będzie pouczenie dla ciebie. Zmarłeś ██ ██ ██")
            print("\n")
            time.sleep(3)
            Quest_LV_2_2()
            input()

     elif Action_cheng == "wymyśleć":
         print("\n")
         print("██ ██ ██ Patrz Robak puszcza w ciebie kwas solny. Możesz probować odbiłać  go i celuj tym kwasem w rabaka ██ ██ ██ \n")
         while Robak_hp > 50:

             print(t.kaplia)
             print(" ██ ██ ██ Celuj kwasem w rabaka!!!!!!    ██ ██ ██ ")
             print(" ██ ██ ██ Kwas leci!!!!!!!!              ██ ██ ██ ")
             input(">>> ENTER")
             Robak_hp = Robak_hp - 100
             time.sleep(1)
         print(" ██ ██ ██ Teraz robak jest słaby, to twój szans go zabić  ██ ██ ██ ")
         print("\n")
         Your_Hero.display_actions()
         action_y = input("██ ██ WRITE ATTACK , MAGIC , OR LOSE ██ ██   >>>")
         if action_y in ("attack", "Attack", "ATTACK", "Magic", "magic", "MAGIC", "lose", "Lose", "LOSE"):
             if action_y in ("attack", "Attack", "ATTACK"):
                 Robak_hp = Robak_hp - random.randrange(49, 52)
                 if Robak_hp < 1:
                     print("\n")
                     print("██ ██ ██ Zabiłeś Robaka witam!! Dostałeś z niego: 'Skóra robaka' ██ ██ ██")
                     time.sleep(1)
                     print("\n")
                     print("╔══════════════════════════════════════════╗")
                     print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
                     print("╚══════════════════════════════════════════╝")
                     input("")
                 else:
                     print("██ ██ ██ Niestety nie zabiłeś go ██ ██ ██")
                     Your_Hero.health = Your_Hero.health - 10
                     time.sleep(3)
                     Quest_LV_2_2()

             elif action_y in ("Magic", "magic", "MAGIC"):

                 for i in range(len(All_magic)):
                     print(i)
                     print("name spall:     " + All_magic[i].name)
                     print("damage spall:    " + str(All_magic[i].damage))
                     print("cost spall:     " + str(All_magic[i].damage))
                     print("\n")

                 print("██ ██ ██ Choise spell  (write name!) ██ ██ ██")
                 spell_name = input(">>>")
                 for i in range(len(All_magic)):
                     if All_magic[i].name == spell_name:
                         while Robak_hp > int(0):
                             Robak_hp = Robak_hp - All_magic[i].damage
                             Your_Hero.mana = Your_Hero.mana - All_magic[i].cost
                             print("Robak HP NOW:  " + str(Robak_hp))
                             print("Jeszcze raz korzystamy z: " + All_magic[i].name)
                             Your_Hero.health = Your_Hero.health - 10
                         print("\n")
                         print("██ ██ ██  Zabiłeś Robaka witam!! Dostałeś z niego: 'Skóra robaka' ██ ██ ██")
                         print("\n")
                         print("██ ██ ██ Twoje mana po walcę: " + str(Your_Hero.mana))
                         print("\n")
                         print("██ ██ ██ Twoje hp po walcę: " + str(Your_Hero.health))
                         print("\n")
                         if Your_Hero.health < 0:
                             print("Niestety zmarłeś ")
                             time.sleep(5)
                             Quest_LV_2_2()

                 print("\n")
                 print("╔══════════════════════════════════════════╗")
                 print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
                 print("╚══════════════════════════════════════════╝")
                 input("")
             else:
                 print("██ ██ ██ Nawet nie myśliałem że jesteś takim bojazkim ██ ██ ██")
                 print("\n")
                 time.sleep(3)
                 Quest_LV_2_2()
         else:
             print(
                 "██ ██ ██ Wpisałeś nieprawidłowe znaczenie. To będzie pouczenie dla ciebie. Nie zobaczyś walki((( ██ ██ ██")
             print("\n")
             Quest_LV_2_2()
def Quest_LV_2_3():
    os.system("cls")
    print_for_sumbols(t.Quest_LV_2_3)
    print("██ ██ ██ Gramy do jednego . Jeżeli przegrasz oddajesz 2000 s. hahahaah ██ ██ ██")
    print("\n")
    print("██ ██ ██ ZACZYNAMY ██ ██ ██ ")
    print("\n")
    print(" ██ ██ ██ Wpisz 1,2 lub 3 dla gry ██ ██ ██")
    print("\n")
    print("1. Pokaż Papier")
    print("2. Pokaż Kamień")
    print("3. Pokaż Nożyczki")
    print("\n")
    tr = int(input(">>> "))
    o_h = random.randint(1, 3)
    if tr == o_h:
        print("to samo , jeszcze raz")
        time.sleep(3)
        Quest_LV_2_3()
    else:
        if tr == 1 and o_h == 2:
            print("\n")
            print("██ ██ ██ WYGRAłEŚ !!! ██ ██ ██ ")
            print("\n")
            print("██ ██ ██ Wykupiłeś niewolnika. Jego imię: 'AZARD' ██ ██ ██ ")
            print("██ ██ ██ Od teraz to twój nowy przyjaciel ██ ██ ██ ")
            print("\n")
            print("╔══════════════════════════════════════════╗")
            print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
            print("╚══════════════════════════════════════════╝")
            input("")
        elif tr == 1 and o_h == 3:
            print("\n")
            print("██ ██ ██ PRZEGRAłEŚ !!! ██ ██ ██ ")
            print("\n")
            print("██ ██ ██ Niestety nie udało się  wykupić niewolnika.  ██ ██ ██ ")
            print("██ ██ ██ Niestety, nie masz septimów. Nie zawsze robić dobrze - robić poprawnie  ██ ██ ██ ")
            print("\n")
            time.sleep(3)
            Quest_LV_2_3()
        elif tr == 2 and o_h == 1:
            print("\n")
            print("██ ██ ██ PRZEGRAłEŚ !!! ██ ██ ██ ")
            print("\n")
            print("██ ██ ██ Niestety nie udało się  wykupić niewolnika.  ██ ██ ██ ")
            print("██ ██ ██ Niestety, nie masz septimów. Nie zawsze robić dobrze - robić poprawnie  ██ ██ ██ ")
            print("\n")
            time.sleep(3)
            Quest_LV_2_3()
        elif tr == 2 and o_h == 3:
            print("\n")
            print("██ ██ ██ WYGRAłEŚ !!! ██ ██ ██ ")
            print("\n")
            print("██ ██ ██ Wykupiłeś niewolnika. Jego imię: 'AZARD' ██ ██ ██ ")
            print("██ ██ ██ Od teraz to twój nowy przyjaciel ██ ██ ██ ")
            print("\n")
            print("╔══════════════════════════════════════════╗")
            print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
            print("╚══════════════════════════════════════════╝")
            input("")
        elif tr == 3 and o_h == 1:
            print("\n")
            print("██ ██ ██ WYGRAłEŚ !!! ██ ██ ██ ")
            print("\n")
            print("██ ██ ██ Wykupiłeś niewolnika. Jego imię: 'AZARD' ██ ██ ██ ")
            print("██ ██ ██ Od teraz to twój nowy przyjaciel ██ ██ ██ ")
            print("\n")
            print("╔══════════════════════════════════════════╗")
            print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
            print("╚══════════════════════════════════════════╝")
            input("")
        else:
            print("\n")
            print("██ ██ ██ PRZEGRAłEŚ !!! ██ ██ ██ ")
            print("\n")
            print("██ ██ ██ Niestety nie udało się  wykupić niewolnika.  ██ ██ ██ ")
            print("██ ██ ██ Niestety, nie masz septimów. Nie zawsze robić dobrze - robić poprawnie  ██ ██ ██ ")
            print("\n")
            time.sleep(3)
            Quest_LV_2_3()
def Quest_LV_2_4():
    heal_mana()
    os.system("cls")
    print_for_sumbols(t.Quest_LV_2_4)
    print_for_sumbols(" ██ ██ ██  Wszedłeś w zamek i widzisz dwie osyby  ██ ██ ██")
    print("\n")
    print_for_sumbols(" ██ ██ ██  Jedna i druga wygląda jako twój Azard  i mówie: POMÓŻ MNIE!!!! ██ ██ ██")
    print("\n")
    print_for_sumbols(" ██ ██ ██  Okazało się że to był zamek czarownicy ██ ██ ██")
    print("\n")
    print_for_sumbols(" ██ ██ ██  Teraz muszisz zrozumieć kto jest kto i uratować Azarda ██ ██ ██")
    print("\n")
    print_for_sumbols(" ██ ██ ██  Problem też w tym że czarownica też wie wszystko o Azardzie oprócz smutnych czasów w jego życie ██ ██ ██")
    print("\n")
    print("Wybierz pytanie które pomoże tobie znaleść kolegę na 100%")

    print_for_sumbols("      1. Kiedy urodziłeś się?")
    print_for_sumbols("      2. co jest najważniejsze dla ciebie?")
    print_for_sumbols("      3. Jak okazało się tak że zostałeś niewolnikem?")
    print_for_sumbols("      4. Ile masz lat?")
    print_for_sumbols("      5. Kiedy zmarł twój tato?")
    print("\n")
    print("Wpisz pytanie!     (wpisz numer pytania)")
    rt = int(input(">>>"))
    if rt == 3:
        print("\n")
        print_for_sumbols(" ██ ██ ██ Wybrałeś prawidłowe pytanie ██ ██ ██ ")
        print("\n")
        print_for_sumbols("   ██ ██ ██ Odpowiedż może wiedzieć tylko twój kolega ██ ██ ██ ")
        print("\n")
        print_for_sumbols("   ██ ██ ██ Czarowniczka Uciekła. Wychodzicie w z tego Zamka ██ ██ ██ ")
        print("\n")
        print("╔══════════════════════════════════════════╗")
        print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
        print("╚══════════════════════════════════════════╝")
        input("")
    else:
        print_for_sumbols(" ██ ██ ██ Wybrałeś nie  prawidłowe pytanie ██ ██ ██ ")
        print("\n")
        print_for_sumbols(" ██ ██ ██ Wybrałeś czarowniczke i zabiłeś swojego kolegę ██ ██ ██ ")
        Quest_LV_2_4()
def Quest_LV_2_5():
    heal_mana()
    os.system('cls')
    print_for_sumbols(t.Quest_LV_2_5)
    print(" ██ ██ ██  TERAZ CZAS WYBORU   ██ ██ ██")
    print("\n")
    print(" ██ ██ ██  PAMIETAJ O CEL!!!!!!   ██ ██ ██")
    print("\n")

    print("╔══════════════════════════════╗")
    print("║  1. Oddaj kolegę jako ofiarę ║")
    print("╚══════════════════════════════╝")
    print("\n")
    print("╔═════════════════════════════════════════════╗")
    print("║  2. Zakączyć przygodę,ale uratujęsz kolegę  ║")
    print("╚═════════════════════════════════════════════╝")
    print("█ wpisz 1 lub 2")
    qer = int(input(">>>"))
    if qer == 1:
        print(" ██ ██ ██ Wybrałeś uratować świat , a nie kolegę  ██ ██ ██ ")
        print("\n")
        print(" ██ ██ ██  MAG --- ODDAJE TOBIE ELIKSYR BORA  ██ ██ ██ ")
        time.sleep(3)
        os.system("cls")
        print_for_sumbols(t.Get_Item_2)
        print("\n")
        print("╔══════════════════════════════════════════╗")
        print("║       PRESS ENTER  GO  TO LEVEL 3        ║")
        print("╚══════════════════════════════════════════╝")
        input()
    else:
        print(" ██ ██ ██ Wybrałeś uratować kolegę , a nie świat  ██ ██ ██ ")
        print("\n")
        print(" ██ ██ ██  Nie dostałeś eliskyra i końszysz przygodę  ██ ██ ██ ")
        print("\n")
        print("╔══════════════════════════════════════════╗")
        print("║       PRESS ENTER  TO  RESTART QUEST 5   ║")
        print("╚══════════════════════════════════════════╝")
        input()
        Quest_LV_2_5()
############################# LEVEL 3
def General_Level_3():
        os.system('cls')
        print(t.maps_WEST)
        print("█████████████████████████████████████████████████████████████████████")
        print("║                    PRESS ENTER TO DELIVER TO LEVEL 3              ║")
        print("█████████████████████████████████████████████████████████████████████")
        print("\n")
        input()
        os.system('cls')
        print(t.maps_EAST)
        print("█████████████████████████████████████████████████████████████████████")
        print("║                          DELIVER SUCCESS                          ║")
        print("█████████████████████████████████████████████████████████████████████")
        time.sleep(7)
        os.system('cls')
        Rekursywna_LVL_3()
def Rekursywna_LVL_3():
    HTODO = input("║║║Wpisz co chcesz zrobić║║║-║║║albo help dla pomocy║║║ >>> ")

    if HTODO in ("help","Help","HELP"):
        print(t.help_text)
        print("\n")
        Rekursywna_LVL_3()
    elif HTODO in ("Next_level","NEXT_LEVEL","next_level","next_Level"):
        for i in range(14):
            if All_location[i].status == int(0):
                print("Niestety masz jeszcze lokacje w których nie byłeś, muszisz wykonać zadania w każdej")
                Rekursywna_LVL_3()
        Quest_BOSS()
    elif HTODO in ("Save","SAVE","save"):
        Save()
        print_for_sumbols("Your game saved!!!\n")
        time.sleep(3)
        Rekursywna_LVL_3()
    elif HTODO in ("quit","Quit","QUIT"):
        sys.exit()
    elif HTODO in ("Check","check","CHECK",):
        print("╔═══════════════════════════════════════════════════════════════════╗")
        print("║                         DOSTĘPNE LOKACJĘ NA 3 LVL                 ║")
        print("╚═══════════════════════════════════════════════════════════════════╝")
        print_location_3()
        Rekursywna_LVL_3()
    elif HTODO in ("Do_kwest","do_kwest","DO_KWEST"):
        WTODO = input(" ║║║ Prosze wpisać nazwę lokacji ║║║  :>>>> ")
        if WTODO in ("Black_Town","Goast_Town","Jaskinia Druida","Latający most","Niebiańska_kużnia","Forest","Desert",
                     "Myśliwski dom","Zamek","Most smoga","Pekielne góry","Miasto goblinów","Dolina werwolfów","Błoto","Piekelna kużnia"):
            if WTODO == "Pekielne góry":
                if Lok_1_LV_3.status == int(0):
                    Quest_LV_3_1()
                    przygoda_16()
                    Lok_1_LV_3.status = int(1)
                    Rekursywna_LVL_3()
                else:
                    print_for_sumbols("Już byłeś w tej lokacji , przejdż do innej")
                    Rekursywna_LVL_3()
            if WTODO == "Miasto goblinów":
                if Lok_3_LV_3.status == int(0):
                    Quest_LV_3_2()
                    przygoda_17()
                    Lok_2_LV_3.status = int(1)
                    Rekursywna_LVL_3()
                else:
                    print_for_sumbols("Już byłeś w tej lokacji , przejdż do innej")
                    Rekursywna_LVL_3()
            if WTODO == "Dolina werwolfów":
                if Lok_3_LV_3.status == int(0):
                    Quest_LV_3_3()
                    przygoda_18()
                    Lok_3_LV_3.status = int(1)
                    Rekursywna_LVL_3()
                else:
                    print_for_sumbols("Już byłeś w tej lokacji , przejdż do innej")
                    Rekursywna_LVL_3()
            if WTODO == "Błoto":
                if Lok_4_LV_3.status == int(0):
                    Quest_LV_3_4()
                    przygoda_19()
                    Lok_4_LV_3.status = int(1)
                    Rekursywna_LVL_3()
                else:
                    print_for_sumbols("Już byłeś w tej lokacji , przejdż do innej")
                    Rekursywna_LVL_3()
            if WTODO == "Piekelna kużnia":
                if Lok_5_LV_3.status == int(0):
                    Quest_LV_3_5()
                    przygoda_20()
                    Lok_5_LV_3.status = int(1)
                    Quest_BOSS()
                else:
                    print_for_sumbols("Już byłeś w tej lokacji , przejdż do innej")
                    Rekursywna_LVL_3()


        else:
            print_for_sumbols("Niestety nie znależliśmy takiej lokacji albo jest zamknięta\n")
            Rekursywna_LVL_3()
    else:
        print_for_sumbols("Niestety wpisałeś niepoprawne zanaczenie !!! Wpisz help")
        Rekursywna_LVL_3()
def Quest_LV_3_1():
    heal_mana()
    os.system("cls")
    print_for_sumbols(t.Quest_LV_3_1)
    print(" ██ ██ ██  Wybierz znaczenie pozioma głosności, jakie twoim zdaniem odpowiada rysunku  ██ ██ ██")
    print("\n")
    print_for_sumbols(t.Poziom)
    print("\n")
    pozio = int(input(">>> "))
    if pozio > 65 and pozio < 75:
       print(" ██ ██ ██  Zgadnołeś  poziom.  ██ ██ ██")
       print("\n")
       print("██ ██ ██  Zostałeś właścicielem tego zwirzęta. Nie mamy dużo czasu. W DROGĘ!!!!!!!!! ██ ██ ██")
       print("\n")
       print("╔══════════════════════════════════════════╗")
       print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
       print("╚══════════════════════════════════════════╝")
       input("")
    else:
        print("██ ██ ██  Ohhhh nie  , to było za głosno , albo za cicho  ██ ██ ██")
        print("\n")
        print("██ ██ ██  spróbój uciekać,  albo spróbój walczyć się   ██ ██ ██")
        print("\n")
        mysza_hp = int(100)
        Your_Hero.display_actions()
        action_y = input("██ ██ WRITE ATTACK , MAGIC , OR LOSE ██ ██   >>>")
        if action_y in ("attack", "Attack", "ATTACK", "Magic", "magic", "MAGIC", "lose", "Lose", "LOSE"):
            if action_y in ("attack", "Attack", "ATTACK"):
                mysza_hp = mysza_hp - random.randrange(95, 130)
                if mysza_hp < 1:
                    print("██ ██ ██ Zabiłeś Mysze ██ ██ ██")
                    print("██ ██ ██ Ale ztraciłeś ostatni szansa na to żeby przejść tę ścieżkę ██ ██ ██")
                    time.sleep(4)
                    Quest_LV_3_1()
                else:
                    print("██ ██ ██ Niestety nie zabiłeś go. Zmarłeś ██ ██ ██")
                    Your_Hero.health = Your_Hero.health - 30
                    print("\n")
                    print("Twoje zdrowie po walcę: 0 ")
                    time.sleep(4)
                    if Your_Hero.health < 0:
                        print("Niestety zmarłeś ")
                        time.sleep(5)
                        Quest_LV_3_1()
                    else:
                        Quest_LV_3_1()

            elif action_y in ("Magic", "magic", "MAGIC"):

                for i in range(len(All_magic)):
                    print(i)
                    print("name spall:     " + All_magic[i].name)
                    print("damage spall:    " + str(All_magic[i].damage))
                    print("cost spall:     " + str(All_magic[i].damage))
                    print("\n")

                print("██ ██ ██ Choise spell  (write name!) ██ ██ ██")
                spell_name = input(">>>")
                for i in range(len(All_magic)):
                    if All_magic[i].name == spell_name:
                        while Your_Hero.mana > int(0):
                            mysza_hp = mysza_hp - All_magic[i].damage
                            Your_Hero.mana = Your_Hero.mana - All_magic[i].cost
                            print(" Nietoper HP NOW:  " + str(mysza_hp))
                            print("Jeszcze raz korzystamy z: " + All_magic[i].name)
                            Your_Hero.health = Your_Hero.health - 90
                            if Your_Hero.health < 0:
                                break
                        print("\n")
                        print("██ ██ ██ Niestety nie zabiłeś Nietopera ██ ██ ██")
                        print("\n")
                        print("██ ██ ██ Twoje mana po walcę: " + str(Your_Hero.mana))
                        print("\n")
                        print("██ ██ ██ Twoje hp po walcę: " + str(Your_Hero.health))
                        if Your_Hero.health < 0:
                            print("Niestety zmarłeś ")
                            time.sleep(5)
                            Quest_LV_3_1()

            else:
                Quest_LV_3_1()
def Quest_LV_3_2():
    heal_mana()
    os.system("cls")
    glob = int(1)
    while glob == int(1):
            print_for_sumbols(t.Quest_LV_3_2)
            req = int(1)
            Rand_tawerna = random.randint(1,3)
            while req == int(1):
                print_for_sumbols(" ██ ██ ██  Zaszedłeś w pierszą tawernę   ██ ██ ██")
                print_for_sumbols("\n")
                print_for_sumbols(" ██ ██ ██  Tam wszyscy piją. Zapytałeś się, czy ktoś wie kogoś pod nazwiskiem 'Szary'   ██ ██ ██")
                print_for_sumbols("\n")
                print_for_sumbols(" ██ ██ ██  Główny goblin powiedział że wie gdzie on jest, ale 3 osoby chcą porywalizować z tobą w umijętności pić piwo   ██ ██ ██")
                print_for_sumbols("\n")
                print_for_sumbols(" ██ ██ ██  Niestety muszisz wypić najwięcej i nie zasnąć od razu. żeby dowiedzieć się gdzie jest Szary   ██ ██ ██")
                print("\n")
                print(t.Piwo)
                print_for_sumbols("██ ██ ██ press enter to drink!!!! ██ ██ ██")
                input()
                First_szanse = int(10)
                Second_szanese = int(11)
                Thir_szanse = int(8)
                Twoj_szanese = random.randint(19,100)
                if Twoj_szanese > First_szanse:
                    print(" ██ ██ ██ wypiłeś więcej, czym pierwszy goblin, jeszcze dwa goblina czekają na ciebie   ██ ██ ██ ")
                    print("\n")
                    print(t.Piwo)
                    print_for_sumbols("██ ██ ██ press enter to drink!!!! ██ ██ ██")
                    Twoj_szanese = random.randint(8, 70)
                    input()
                    if Twoj_szanese > Second_szanese:
                        print(" ██ ██ ██ wypiłeś więcej, czym drugi  goblin, jeszcze jeden goblin czeka na ciebie   ██ ██ ██ ")
                        print("\n")
                        print(t.Piwo)
                        print_for_sumbols("██ ██ ██ press enter to drink!!!! ██ ██ ██")
                        Twoj_szanese = random.randint(8, 60)
                        input()
                        if Twoj_szanese > Thir_szanse:
                            print(" ██ ██ ██ Witam wypiłeś tak dużo piła  ██ ██ ██ ")
                            if Rand_tawerna == int(1):
                                print("\n")
                                print(" ██ ██ ██ ohhhh , dobrze powiem gdzie on jest. Szaryyyyyyy!!!! do ciebie przyśli.  ██ ██ ██ ")
                                print("\n")
                                print(" ██ ██ ██ Znalazłeś Szarego i on powiedział że powie tobie informacje jeżeli dostaniesz naszyjnik Werwolfów i oddasz go jemu  ██ ██ ██ ")
                                print("\n")
                                print("╔══════════════════════════════════════════╗")
                                print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
                                print("╚══════════════════════════════════════════╝")
                                req = int(0)
                                input("")
                                glob = int(0)
                            else:
                                print("\n")
                                print(
                                    " ██ ██ ██ ohhhh , dobrze powiem gdzie on jest. Szaryyyyyyy!!!! do ciebie przyśli.  ██ ██ ██ ")
                                print("\n")
                                print(
                                    " ██ ██ ██ Niestety Szarego niema w tej tawernie  ██ ██ ██ ")
                                print("\n")
                                print("██ ██ ██ Enter dla następnej tawerny ██ ██ ██")
                                req = int(0)
                                input()

                        else:
                            print(" ██ ██ ██ Niestety zginołeś od takiej ilości piwa!!.  ██ ██ ██ ")
                            time.sleep(3)
                            Quest_LV_3_2()
                    else:
                        print(" ██ ██ ██ Niestety zginołeś od takiej ilości piwa!!.  ██ ██ ██ ")
                        time.sleep(3)
                        Quest_LV_3_2()
                else:
                    print(" ██ ██ ██ Niestety zginołeś od takiej ilości piwa!!.  ██ ██ ██ ")
                    time.sleep(3)
                    Quest_LV_3_2()
            os.system("cls")
            qer = int(1)
            while qer == int(1):
                print_for_sumbols(" ██ ██ ██  Zaszedłeś w drugą tawernę   ██ ██ ██")
                print_for_sumbols("\n")
                print_for_sumbols(" ██ ██ ██  Tam wszyscy tańczą. Zapytałeś się, czy ktoś wie kogoś pod nazwiskiem 'Szary'   ██ ██ ██")
                print_for_sumbols("\n")
                print_for_sumbols(" ██ ██ ██  Główny goblin powiedział że wie gdzie on jest, ale 3 osoby chcą porywalizować z tobą w umijętności tańczyć   ██ ██ ██")
                print_for_sumbols("\n")
                print_for_sumbols(" ██ ██ ██  Niestety muszisz zatańczyć  najlepiej  i nie przegrać od razu. żeby dowiedzieć się gdzie jest Szary   ██ ██ ██")
                print("\n")
                print_for_sumbols("██ ██ ██ press enter dla tego żeby tańczyć !!!! ██ ██ ██")
                input()
                First_szanse = int(10)
                Second_szanese = int(11)
                Thir_szanse = int(8)
                Twoj_szanese = random.randint(19,100)
                if Twoj_szanese > First_szanse:
                    print(" ██ ██ ██ Tańczyłeś lepiej  czym pierwszy goblin, jeszcze dwa goblina czekają na ciebie   ██ ██ ██ ")
                    print("\n")
                    print_for_sumbols("██ ██ ██ press enter dla tego żeby tańczyć !!!! ██ ██ ██")
                    Twoj_szanese = random.randint(8, 70)
                    input()
                    if Twoj_szanese > Second_szanese:
                        print(" ██ ██ ██ Tańczyłeś lepiej  czym drugi  goblin, jeszcze jeden goblin czeka na ciebie   ██ ██ ██ ")
                        print("\n")
                        print_for_sumbols("██ ██ ██ press enter dla tego żeby tańczyć !!!! ██ ██ ██")
                        Twoj_szanese = random.randint(8, 60)
                        input()
                        if Twoj_szanese > Thir_szanse:
                            print(" ██ ██ ██ Tańczyłeś najliepiej!!!! Super  ██ ██ ██ ")
                            if Rand_tawerna == int(2):
                                print("\n")
                                print(" ██ ██ ██ ohhhh , dobrze tańczysz, powiem gdzie on jest. Szaryyyyyyy!!!! do ciebie przyśli.  ██ ██ ██ ")
                                print("\n")
                                print(" ██ ██ ██ Znalazłeś Szarego i on powiedział że powie tobie informacje jeżeli dostaniesz naszyjnik Werwolfów i oddasz go jemu  ██ ██ ██ ")
                                print("\n")
                                print("╔══════════════════════════════════════════╗")
                                print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
                                print("╚══════════════════════════════════════════╝")
                                qer = int(0)
                                input("")
                                glob = int(0)
                            else:
                                print("\n")
                                print(
                                    " ██ ██ ██ ohhhh , dobrze powiem gdzie on jest. Szaryyyyyyy!!!! do ciebie przyśli.  ██ ██ ██ ")
                                print("\n")
                                print(
                                    " ██ ██ ██ Niestety Szarego niema w tej tawernie  ██ ██ ██ ")
                                print("\n")
                                print("██ ██ ██ Enter dla następnej tawerny ██ ██ ██")
                                qer = int(0)
                                input()

                        else:
                            print(" ██ ██ ██ Niestety zginołeś od takiej ilości tańców!!.  ██ ██ ██ ")
                            time.sleep(3)
                            Quest_LV_3_2()
                    else:
                        print(" ██ ██ ██ Niestety zginołeś od takiej ilości tańców!!.  ██ ██ ██ ")
                        time.sleep(3)
                        Quest_LV_3_2()
                else:
                    print(" ██ ██ ██ Niestety zginołeś od takiej ilości tańców!!.  ██ ██ ██ ")
                    time.sleep(3)
                    Quest_LV_3_2()
            os.system("cls")
            erq = int(1)
            while erq == int(1):
                print_for_sumbols(" ██ ██ ██  Zaszedłeś w trzecią tawernę   ██ ██ ██")
                print_for_sumbols("\n")
                print_for_sumbols(" ██ ██ ██  Tam wszyscy śpiewają . Zapytałeś się, czy ktoś wie kogoś pod nazwiskiem 'Szary'   ██ ██ ██")
                print_for_sumbols("\n")
                print_for_sumbols(
                    " ██ ██ ██  Główny goblin powiedział że wie gdzie on jest, ale 3 osoby chcą porywalizować z tobą w umijętności śpiewać   ██ ██ ██")
                print_for_sumbols("\n")
                print_for_sumbols(
                    " ██ ██ ██  Niestety muszisz śpiewać  najlepiej  i nie przegrać od razu. żeby dowiedzieć się gdzie jest Szary   ██ ██ ██")
                print("\n")
                print_for_sumbols("██ ██ ██ press enter dla tego żeby śpiewać !!!! ██ ██ ██")
                input()
                First_szanse = int(10)
                Second_szanese = int(11)
                Thir_szanse = int(8)
                Twoj_szanese = random.randint(19, 100)
                if Twoj_szanese > First_szanse:
                    print(" ██ ██ ██ Śpiewałeś lepiej  czym pierwszy goblin, jeszcze dwa goblina czekają na ciebie   ██ ██ ██ ")
                    print("\n")
                    print_for_sumbols("██ ██ ██ press enter dla tego żeby śpiewać !!!! ██ ██ ██")
                    Twoj_szanese = random.randint(8, 70)
                    input()
                    if Twoj_szanese > Second_szanese:
                        print(" ██ ██ ██ Śpiewałeś lepiej  czym drugi  goblin, jeszcze jeden goblin czeka na ciebie   ██ ██ ██ ")
                        print("\n")
                        print_for_sumbols("██ ██ ██ press enter dla tego żeby śpiewać !!!! ██ ██ ██")
                        Twoj_szanese = random.randint(8, 60)
                        input()
                        if Twoj_szanese > Thir_szanse:
                            print(" ██ ██ ██ Śpiewałeś  najliepiej!!!! Super  ██ ██ ██ ")
                            if Rand_tawerna == int(3):
                                print("\n")
                                print(
                                    " ██ ██ ██ ohhhh , dobrze Śpiewasz, powiem gdzie on jest. Szaryyyyyyy!!!! do ciebie przyśli.  ██ ██ ██ ")
                                print("\n")
                                print(
                                    " ██ ██ ██ Znalazłeś Szarego i on powiedział że powie tobie informacje jeżeli dostaniesz naszyjnik Werwolfów i oddasz go jemu  ██ ██ ██ ")
                                print("\n")
                                print("╔══════════════════════════════════════════╗")
                                print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
                                print("╚══════════════════════════════════════════╝")
                                erq = int(0)
                                input("")
                                glob = int(0)
                            else:
                                print("\n")
                                print(
                                    " ██ ██ ██ ohhhh , dobrze powiem gdzie on jest. Szaryyyyyyy!!!! do ciebie przyśli.  ██ ██ ██ ")
                                print("\n")
                                print(
                                    " ██ ██ ██ Niestety Szarego niema w tej tawernie  ██ ██ ██ ")
                                print("\n")
                                print("██ ██ ██ Enter dla następnej tawerny ██ ██ ██")
                                erq = int(0)
                                input()

                        else:
                            print(" ██ ██ ██ Niestety zginołeś od takiej ilości piwa!!.  ██ ██ ██ ")
                            time.sleep(3)
                            Quest_LV_3_2()
                    else:
                        print(" ██ ██ ██ Niestety zginołeś od takiej ilości piwa!!.  ██ ██ ██ ")
                        time.sleep(3)
                        Quest_LV_3_2()
                else:
                    print(" ██ ██ ██ Niestety zginołeś od takiej ilości piwa!!.  ██ ██ ██ ")
                    time.sleep(3)
                    Quest_LV_3_2()
def Quest_LV_3_3():
    heal_mana()
    os.system("cls")
    print_for_sumbols(t.Quest_LV_3_3)
    print("╔═══════════════════════════╗")
    print("║          Actions          ║")
    print("╚═══════════════════════════╝")
    print("What would you like to do?\n")
    print_for_sumbols("██ ██ ██ 1. Zostać werwólfem    (wpisz : 1) ██ ██ ██\n")
    print_for_sumbols("██ ██ ██ 2. Zabić wszystkich    (wpisz : 2) ██ ██ ██\n")
    ap = int(input(">>>:  "))

    if ap == int(2):
        wk = 0
        while wk != 5:
            Wer_hp = int(40)
            Your_Hero.display_actions()
            action_y = input("██ ██ WRITE ATTACK , MAGIC , OR LOSE ██ ██   >>>")
            if action_y in ("attack", "Attack", "ATTACK", "Magic", "magic", "MAGIC", "lose", "Lose", "LOSE"):
                if action_y in ("attack", "Attack", "ATTACK"):
                    Wer_hp = Wer_hp - random.randrange(39, 50)
                    if Wer_hp < 1:
                        print("██ ██ ██ Zabiłeś jednego werwólfa  ██ ██ ██")
                        heal_mana()
                        wk = wk + 1
                        print("██ ██ ██ Zostało się zabić:  " + str(5 - wk) + "  ██ ██ ██")
                        print("'Skorzystałeś z eliksyra: 100% życia + 100% many'")
                        Wer_hp = 40
                        time.sleep(2)
                    else:
                        print("██ ██ ██ Niestety nie zabiłeś go ██ ██ ██")
                        Your_Hero.health = Your_Hero.health - 100
                        print("\n")
                        print("Twoje zdrowie po walcę: " + str(Your_Hero.health))
                        time.sleep(3)
                        Quest_LV_3_3()

                elif action_y in ("Magic", "magic", "MAGIC"):

                    for i in range(len(All_magic)):
                        print(i)
                        print("name spall:     " + All_magic[i].name)
                        print("damage spall:    " + str(All_magic[i].damage))
                        print("cost spall:     " + str(All_magic[i].damage))
                        print("\n")

                    print("██ ██ ██ Choise spell  (write name!) ██ ██ ██")
                    spell_name = input(">>>")
                    for i in range(len(All_magic)):
                        if All_magic[i].name == spell_name:
                            while Wer_hp > int(0):
                                Wer_hp = Wer_hp - All_magic[i].damage
                                Your_Hero.mana = Your_Hero.mana - All_magic[i].cost
                                print("werwólf HP NOW:  " + str(Wer_hp))
                                print("Jeszcze raz korzystamy z: " + All_magic[i].name)
                                Your_Hero.health = Your_Hero.health - 10
                            print("\n")
                            print("██ ██ ██ Zabiłeś jednego werwólfa ██ ██ ██")
                            print("\n")
                            print("██ ██ ██ Twoje mana po walcę: " + str(Your_Hero.mana))
                            print("\n")
                            print("██ ██ ██ Twoje hp po walcę: " + str(Your_Hero.health))
                            if Your_Hero.health == 0:
                                print("Niestety zmarłeś ")
                                time.sleep(5)
                                Quest_LV_3_3()
                            heal_mana()
                            wk = wk + 1
                            print("██ ██ ██ Zostało się zabić:  " + str(5 - wk) + "  ██ ██ ██")
                            print("'Skorzystałeś z eliksyra: 100% życia + 100% many'")
                            time.sleep(2)
                            Wer_hp = 40

                else:
                    print("██ ██ ██ Nawet nie myśliałem że jesteś takim bojazkim ██ ██ ██")
                    print("\n")
                    time.sleep(3)
                    Quest_LV_3_3()
            else:
                print("██ ██ ██ Wpisałeś nieprawidłowe znaczenie. To będzie pouczenie dla ciebie. Nie zobaczyś walki((( ██ ██ ██")
                time.sleep(3)
                Quest_LV_3_3()
        print("\n")
        print_for_sumbols("██ ██ ██ Zabiłeś wszystkich słabych wierwólfów. Czeka na ciebie Król ██ ██ ██\n")
        print_for_sumbols("██ ██ ██ Ma dużo hp. Nie możesz od razu go zabić!!! ██ ██ ██\n")
        print_for_sumbols("██ ██ ██ Spróbuj  uniknąć ataky a za tym wykorzystaj spell: 'Petrificus Totalus' jakie zabiera 100 hp u werwólfów ██ ██ ██\n")
        print_for_sumbols("██ ██ ██ POWODZIENIA!!!! ██ ██ ██\n")
        print_for_sumbols("╔═══════════════════════════╗\n")
        print_for_sumbols("║     Król Wer: 900 hp      ║\n")
        print_for_sumbols("╚═══════════════════════════╝\n")
        print("\n")
        time.sleep(3)
        os.system("cls")
        Your_Hero.health = int(300)
        bn = int(0)
        bm = int(0)
        while bn != int(9):
            bm = int(0)
            while bm != 3:
                gh = random.randint(0,100)
                print(t.ataka_W)
                print("██ ██ ██  Enter dla żeby uniknąć ataki  ██ ██ ██ ")
                input()
                if gh > 10:
                    bm = bm + 1
                    print("██ ██ ██  Odbiłeś atakę. Zostało jeszcze odbić: " + str(3-bm) + "  ██ ██ ██ \n")
                else:
                    print("██ ██ ██ Niestety nie odbiłeś ataki ██ ██ ██ \n")
                    Your_Hero.health = Your_Hero.health - 50
                    print("██ ██ ██  Życie po atacę:  "+str(Your_Hero.health)+"/300  ██ ██ ██")
                    if Your_Hero.health == 0:
                        print_for_sumbols("██ ██ ██  Niestety zmarłeś  ██ ██ ██ ")
                        Quest_LV_3_3()
            print("██ ██ ██  Odbiłeś 3 ataki , skorzystaj z spela !!!! ██ ██ ██ \n")
            input(" ██ ██ ██ Wpisz: magic - żeby otwożyć swoją książkę          >>>> ")
            for i in range(len(All_magic)):
                print(i)
                print("name spall:     " +All_magic[i].name)
                print("damage spall:    "+ str(All_magic[i].damage))
                print("cost spall:     " + str(All_magic[i].damage))
                print("\n")
            tyu =  input(" ██ ██ ██  Wpisz spell >>>  ")

            if tyu == "Petrificus Totalus":
                bn = bn + 1
                print("██ ██ ██  OHHHH , ten wilk naprawdę tego nie czekał , dałaj dalej ██ ██ ██ \n")
                print("██ ██ ██  Życie króla: "+str((9-bn)*100)+"/900  ██ ██ ██ ")
            else:
                print("██ ██ ██  Wpisałeś nie ten spell, spróbuj jeszcze raz  ██ ██ ██ \n")
        print("██ ██ ██  WITAM , zabiłeś króla . Dostajeś naszyjnik. Dawaj szybciej nie mamy dużo czasu!!!!  ██ ██ ██ \n")
        print("\n")
        print("╔══════════════════════════════════════════╗")
        print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
        print("╚══════════════════════════════════════════╝")
        input()

    elif ap == int(1):
        print_for_sumbols("██ ██ ██  Wybrałeś prostą drogę !!!!  ██ ██ ██ \n")
        print_for_sumbols("██ ██ ██  Dla tego żeby zostać Werwólfem   ██ ██ ██\n")
        print_for_sumbols("██ ██ ██  1) Wypić krwi człowieka    ██ ██ ██\n")
        print_for_sumbols("██ ██ ██  2) Musisz złożyć przysięgę Werwólfa  ██ ██ ██\n")
        print("press enter to drink blood")
        input()
        print("\n")
        print("press enter to złożyć przysięgę Werwólfa ")
        input()
        print("\n")
        print("██ ██ ██  WITAM , Zostałeś Werwólfem . Dostajeś naszyjnik. Dawaj szybciej nie mamy dużo czasu!!!!  ██ ██ ██ \n")
        print("╔══════════════════════════════════════════╗")
        print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
        print("╚══════════════════════════════════════════╝")
        input()
def Quest_LV_3_3_2():
    heal_mana()
    os.system("cls")
    print_for_sumbols(t.Quest_LV_3_3_2)
    print("╔══════════════════════════════════════════╗")
    print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
    print("╚══════════════════════════════════════════╝")
    input()
def Quest_LV_3_4():
    heal_mana()
    os.system("cls")
    print_for_sumbols(t.Quest_LV_3_4)
    numbers = []
    for i in range(4):
      numbers.append(random.randint(1, 9))
    ty = 0
    yt = 0
    while ty != 4:
        while yt != 1:
            print_for_sumbols("██ ██ ██  Wpisz znaczenie  ██ ██ ██")
            tyyt = int(input(">>>"))
            if tyyt == numbers[ty]:
                print_for_sumbols(" ██ ██ ██  Zgadnołeś  cyfrę. Przechodiny dalej.  Jeszcze "+str(3-ty)+ " cyfry zostało ██ ██ ██ \n")
                yt = 1
            else:
                print_for_sumbols(" ██ ██ ██  Nie zgadnołeś, próbój dalej  ██ ██ ██ \n")
        yt = 0
        ty = ty+1
    print_for_sumbols("██ ██ ██  WITAM , dostałeś hasło la przejścia. I teraz mamy wolną ddrogę do Piekelnej kużni  ██ ██ ██\n")
    print("╔══════════════════════════════════════════╗")
    print("║   PRESS ENTER TO GO FOR ANOTHER QUEST    ║")
    print("╚══════════════════════════════════════════╝")
    input()
def Quest_LV_3_5():
    heal_mana()
    os.system("cls")
    print_for_sumbols(t.Quest_LV_3_5)
    print_for_sumbols("██ ██ ██  Muszisz wwybrać co jest ważniejsze:  Świat czy twwoje życie  ██ ██ ██\n")
    print("╔═══════════════════════════╗")
    print("║          Actions          ║")
    print("╚═══════════════════════════╝")
    print("What would you like to do?\n")
    print_for_sumbols("██ ██ ██ 1. Oddać życie     (wpisz : 1) ██ ██ ██\n")
    print_for_sumbols("██ ██ ██ 2. Uratować się    (wpisz : 2) ██ ██ ██\n")
    lk = int(input(">>>:  "))
    if lk == int(1):
        print_for_sumbols("██ ██ ██  Gira:  - Niech tak i będzie, oddaje tobie to nefritowwe szkło, ale ty oddasz swwoje życie po walce z bosem  ██ ██ ██")
        time.sleep(3)
        os.system("cls")
        print_for_sumbols(t.Get_Item_3)
        print("\n")
        print("╔══════════════════════════════════════════╗")
        print("║       PRESS ENTER  GO  TO BOSS           ║")
        print("╚══════════════════════════════════════════╝")
        input()
    else:
        print_for_sumbols("██ ██ ██  Gira:  - Niech tak i będzie, niestety nie mogę tobie tak po prostu odddać: niema ofiary - niema szkła   ██ ██ ██")
        time.sleep(3)
        General_Level_1()
def Quest_BOSS():
    os.system("cls")
    print(t.maps_BOSS)
    print("█████████████████████████████████████████████████████████████████████")
    print("║                    PRESS ENTER TO KILL BOSS                       ║")
    print("█████████████████████████████████████████████████████████████████████")
    print("\n")
    input()
    os.system("cls")
    print_for_sumbols(" ██ ██ ██  Doszedłeś do tego momentu kiedy możesz zabić smoga   ██ ██ ██\n")
    print_for_sumbols(" ██ ██ ██  Przed tym wszystkim muszisz stworzyć miecz 'Sagora'   ██ ██ ██\n")
    print_for_sumbols(" ██ ██ ██  Dla tego wrziąłeś swoje wszystkie przedmioty i probujesz przeczytać jeden spell: Expelliarmus   ██ ██ ██\n")
    print_for_sumbols(" ██ ██ ██  Otwórz magiczną ksiązkę i przeczytaj ten spell   ██ ██ ██\n")
    input(" ██ ██ ██ Wpisz: magic - żeby otwożyć swoją książkę          >>>> ")
    for i in range(len(All_magic)):
        print(i)
        print("name spall:     " + All_magic[i].name)
        print("damage spall:    " + str(All_magic[i].damage))
        print("cost spall:     " + str(All_magic[i].damage))
        print("\n")
    tyu = input(" ██ ██ ██  Wpisz spell >>>  ")

    if tyu == "Expelliarmus":
        print("██ ██ ██  Ok, dostałeś najlepszy miecz www Morowindzie ██ ██ ██ \n")
        print("██ ██ ██  Teorytycznie wystarcze jeden raz udarzyć smoga, żeby go zabić  ██ ██ ██ \n")
        print("██ ██ ██  Dobra , widze że on już leczi. Powodzenia !!!!!  ██ ██ ██ \n")
        print("██ ██ ██  PRESS ENTER TO FIGHT  ██ ██ ██ ")
        input()
        os.system("cls")
        print(t.last_drago)
        print("██ ██ ██  już czas walki. Twoje opancerzenie może wytrzymać 10 atak , tak że masz 10 sprób. Wierzymy w ciebie powodzenia   ██ ██ ██ \n")
        drr = (0)
        rr = int(0)
        while rr == int(0):
            print("██ ██ ██  Dawaj on leci!!!!!!!     (ENTER) ██ ██ ██")
            input()
            print("\n")
            szans_dga = random.randint(1, 100)
            if szans_dga < 35:
                print_for_sumbols("██ ██ ██  Witam , witam zabiłeś smoga. Uratowałeś cały świat. Możesz zostawic miecz sobie dla kolejnych przygod!!!!!   ██ ██ ██")
                time.sleep(5)
                os.system("cls")
                print_for_sumbols(t.the_end)
                for i in t.Dragon_died:
                    sys.stdout.write(i)
                    sys.stdout.flush()
                    time.sleep(0.00001)
                rr = rr + 1
            drr = drr + 1
            print("██ ██ ██  Niestety nie zabiłeś go, sprobój jeszcze raz((( ██ ██ ██ \n")
            if drr == int(10):
                print("██ ██ ██  Niestety zmarłeś  ██ ██ ██ \n")
                Quest_BOSS()
            time.sleep(8)
            sys.exit()
    else:
        print("██ ██ ██  Niestety powiedziałeś coś nie tak, wszystkie przedmioty znikneły((( ██ ██ ██ \n")
        Quest_BOSS()

##################################
####Przygody
##################################
def przygoda_1():
    os.system("cls")
    print_for_sumbols("W drodze spotkałeś dziadka\n")
    print_for_sumbols("Niestety on nie umie liczyć , ale chce kupić sobie jedzenie\n")
    print_for_sumbols("Muszisz pomóc mu policzyć ile on ma\n")
    count_C = int(0)
    rand_kil = random.randint(1,15)
    while rand_kil != 0:
        rand_ba = random.randint(1,2)
        if rand_ba == int(1):
            print("Dziadek dostaje banknotę\n")
            print(t.Chajs_1)
            count_C = count_C + 3
            print("poczekać na kolejną\n ")
            input()
        else:
            print("Dziadek dostaje banknotę\n")
            print(t.Chajs_2)
            count_C = count_C + 2
            print("poczekać na kolejną \n")
            input()
        rand_kil = rand_kil - 1
    print("Wpisz ile ma dziadek\n")
    count_p = int(input(":>>"))
    if count_C == count_p:
        print("Dobrze policzyłeś\n")
    else:
        print("Niestety policzyłeś żle, dziadek zmarw z głodu\n")
    print_for_sumbols("Press enten to continue road\n")
    input()
def przygoda_2():
    os.system("cls")
    print_for_sumbols("Obok drogi spotkałeś Barda\n")
    print_for_sumbols("Powiedzał tobie że chcę zaspiewać tobie piosenke \n")
    print_for_sumbols("I po tym możesz ocenić piosenke\n")
    xxx = int(input("czy chcesz posłuchać piosenkę: (wpisz 1 - tak i 0 - nie)  :>>> "))
    if xxx == 1:
        print_for_sumbols('''
    -    Pijemy za naszą młodość, za płynący jak wino czas.
-Za epoki ciemiężców kres, za śmierć, co oszczędziła nas.
-Już wkrótce wypędzimy Cesarstwo z należnej nam ziemi.
-Odzyskamy nasz dom krwią, męstwem i mieczami naszemi.

-Niech żyje Ulfric! Niech żyje! Tyś Najwyższym Królem naszym!
- Ku twej czci śpiewamy pieśni i pijemy wina czasze!

-Walka naszym żywiołem, myśmy Skyrim dzieci.
-Sovngard wzywa - z naszych ciał duch uleci!
-Ale ziemia ta należy do nas, my ją uwolnimy.
-Od plagi kalającej nasze nadzieje oczyścimy.

-Niech żyje Ulfric! Niech żyje! Tyś Najwyższym Królem naszym!
-Ku twej czci śpiewamy pieśni i pijemy wina czasze!
        \n\n''')
        print("Teraz muszisz ocenić piosenkę od 1 do 10\n")
        nnn = int(input("wpisz znaczenie :>>> "))
        if nnn > 5:
            print_for_sumbols("Bard jest bardzo zadowolony z oceny\n")
            print("Press enter to continue road")
            input()
        else:
            print_for_sumbols("Bard jest bardzo nie zadowolony z oceny i zaczęł płakać")
            print("Press enter to continue road")
            input()
    else:
        print("Idzieś dalej nawet nie patrzysz na niego")
        print("Press enter to continue road")
        input()
def przygoda_3():
    os.system("cls")
    print_for_sumbols("Szedłeś po drodzę i zobaczyłeś stary budynek Czarowniczki \n")
    print_for_sumbols(" Możesz dowiedzić się z od niej swoją przyszłość \n")
    print_for_sumbols("Oczy czarowniczki - są zamknięte , zaczynamy zadawaj pytania (press enten dla tego żeby zacząć )\n")
    input()
    yyy = random.randint(1,2)
    print("Player:   - Jak mam na imię ?\n")
    if yyy == 1:
        print("Czarowniczka:  - Dmytro\n")
    else:
        print("Czarowniczka:  - Rostan\n")
    print_for_sumbols("Oczy czarowniczki - są zamknięte , zaczynamy, zadawaj  inne pytania (press enten dla tego żeby zacząć )\n")
    input()
    print("Player:   - Czy zabiję smoka w samym końcu i uratuje świat?\n")
    yyy = random.randint(1, 2)
    if yyy == 1:
        print("Czarowniczka:  - Niestety widzie, że zginiesz\n")
    else:
        print("Czarowniczka:  - Widzę , że będziesz prawdziwym bohaterem i uratujesz świat \n")
    print_for_sumbols("Dowiedziałeś się głowne rzeczy, niestety inne rzeczy czarowniczka już nie widzi\n")
    print_for_sumbols("Press enten to continue road\n")
    input()
def przygoda_4():
    os.system("cls")
    print_for_sumbols(" Iddąc zobaczyłeś most który muszisz przejść, ale niestety nie możesz tego zrobić  \n")
    print_for_sumbols(" znajduje się tam ork który nie przepuści ciebie dopóki nie odgadniesz zagadki \n")
    print_for_sumbols(" możesz pomylić się 3 razy , zaczynamy:  Wpisz odpowiedż\n\n")
    print_for_sumbols('''
        ZAGADKA:
            
            Zawsze przyjdzie, ale nigdy nie przyjdzie dzisiaj. Co to takiego???
    ''')
    rrr = input(":>>>>  ")
    if rrr in ("Jutro","jutro","JUTRO"):
        print_for_sumbols(" WITAM, WITAM , zgadnołeś \n")
        print_for_sumbols("Press enten to continue road\n")
        input()
    else:
        print_for_sumbols(" Niestety  nie zgadnołeś i ork zabił ciebie  \n")
        time.sleep(3)
        przygoda_4()


    input()
def przygoda_5():
    os.system("cls")
    print_for_sumbols(" Zrobiłeś przerwe na odpoczynek w drodze i zauważyłeś butelkę   \n")
    print_for_sumbols(" Przeczytałeś list który tam znajdował się. Nie chciałeś nić robić z tym i poszedłeś spać\n")
    print_for_sumbols(" Rano do ciebie przyśli trzy syna ojca, który zmarł. Okazało się że w liście zapisano miesce gdzie znajduję się cała góra złota\n\n")
    print_for_sumbols(" Również w liście było zakodowane imię syna który dostanie to złoto. To będzie:  1-4-1-13 \n")
    print_for_sumbols(" Imiona synów to: Redgar , Solor i Adam    \n\n")
    time.sleep(4)
    print_for_sumbols(" Dla tego żeby zrozumieć kto dostanie złoto muszisz dostać swój słownik   \n")
    print_for_sumbols(" Press enter to open słownik   \n\n")
    input()
    print('''
        a - 1  b - 2  c - 3 
        d - 4  e - 5  f - 6 
        g - 7  h - 8  i - 9
        j - 10 k - 11 l - 12
        m - 13 n - 14 o - 15
        p - 16 q - 17 r - 18
        s - 19 t - 20 u - 21
        v - 22 w - 23 x - 24
        y - 25 z - 26
    \n''')
    print_for_sumbols("Wpisz imie, jakie twoim zdaniem jest prawidłowe\n")
    ppp = input(":>>> ")
    if ppp in ("Adam","adam","ADAM"):
        print_for_sumbols(" WITAM, WITAM , zgadnołeś. Adam dostaje złoto :)  \n")
        print_for_sumbols("Press enten to continue road\n")
        input()
    else:
        print_for_sumbols(" Niestety to był Adam a nie syn którego ty wybrałeś. Adam nie wytrzymał tego, zabił swoich bratów i siebie...... niestety(((((  \n")
        print_for_sumbols("Press enten to continue road\n")
        input()
def przygoda_6():
    os.system("cls")
    print_for_sumbols(" Zauważyłeś starego dziadka który płakał obok swojego domu   \n")
    print_for_sumbols(" Okazało się że jest szlepy i muszisz pomóc mu przygotować eliksyr\n")
    print_for_sumbols(" Dla tego muszisz przeczytać przepis i w prawidłowej kolejności powiedzieć składniki\n\n")
    print_for_sumbols(" Dostajeś przepis , ale kolejność nie jest wiadomia, widzisz tylko jakieś dziwne linie obok każdego składnika \n")
    time.sleep(4)
    print_for_sumbols(" Dla tego żeby zrozumieć co idzie za czym muszisz pomyszleć   \n")
    print_for_sumbols(" Press enter to open:  przepis   \n\n")
    input()
    print('''
        
        Ucho człowieka --
        
        Sok dzewa -
        
        Mysz ----
        
        Oczy kota ---
        
    \n''')
    print_for_sumbols(" Press enter start read \n\n")
    uuu =  input(" Wpisz nazłe  :>> ")
    if uuu == "Sok dzewa":
        print_for_sumbols(" Ok następny")
    else:
        print_for_sumbols("Niestety nie ta kolejność\n")
        time.sleep(3)
        przygoda_6()
    print_for_sumbols(" Press enter start read \n\n")
    uuu = input(" Wpisz nazłe  :>> ")
    if uuu == "Ucho człowieka":
        print_for_sumbols(" Ok następny")
    else:
        print_for_sumbols("Niestety nie ta kolejność\n")
        time.sleep(3)
        przygoda_6()
    print_for_sumbols(" Press enter start read \n\n")
    uuu = input(" Wpisz nazłe  :>> ")
    if uuu == "Oczy kota":
        print_for_sumbols(" Ok następny")
    else:
        print_for_sumbols("Niestety nie ta kolejność\n")
        time.sleep(3)
        przygoda_6()
    print_for_sumbols(" Press enter start read \n\n")
    uuu = input(" Wpisz nazłe  :>> ")
    if uuu == "Mysz":
        print_for_sumbols(" Witam, dziadek dostał elikstr i nie zniszczył pół miasta. Witam\n")
        print_for_sumbols("Press enten to continue road\n")
        input()
    else:
        print_for_sumbols("Niestety nie ta kolejność\n")
        time.sleep(3)
        przygoda_6()
def przygoda_7():
    os.system("cls")
    print_for_sumbols(" Idzieś obok wszi i czujesz że Człowiek krzycze:  - pomocy!!!\n")
    print_for_sumbols(" doszedłeś to człowieka i okazało się że cała jego rodzina została zniszczona przez murderca\n")
    print_for_sumbols(" Muszisz na początku wybrać czy pomożesz mu\n\n")
    nnm = input("press y to accept or n to not accept quest\n :>>> ")
    if nnm == "y":
        print_for_sumbols("Ok. Doszedłeś to człowieka i okazało się że cała jego rodzina została zniszczona przez murderca\n")
        print_for_sumbols("Zaszedłeś w dom i widzisz na stole dłógopis i kartę papieru\n")
        print_for_sumbols("Muszisz zrozumieć na początek skąd przyszedł morderca\n")
        print("Jeby to zrobić muszisz sieść i spróbubować realizować moment zabóstwa, Spróbuj rzucić długopis 4 raz patrząc w 4 różne strony i trzeba porównać początkowe położenie długopisa \n")
        ttr = "lewo"
        pppp = int(1)
        while pppp!= int(0):
            tty = input("Wpisz stronę stronę w którą patrzysz teraz\n")
            if tty == ttr:
                print("Okazało się że gługopis spadł w lewo. Wiesz że ta chata znajduje się w centrum wsi i z każdej strony są mieszkania innych\n")
                print("Okazało się że zabujcą była babcia która mieszkała obok\n")
                print("Pomógłeś to zrobić. Witam\n")
                print_for_sumbols("Press enten to continue road\n")
                input()
                pppp = int(0)
            else:
                print("Niestety położenie nie zgadza się, spróbój jeszcze raz\n")
    else:
        print_for_sumbols("Press enten to continue road\n")
        input()
def przygoda_8():
    os.system("cls")
    print_for_sumbols(" Zobaczyłeś że obok drogi znajduje się Arm-Camp , w którym idzie turniej, Siłowanie na rękę\n")
    print_for_sumbols(" Chcesz sprobować wygrać go\n")
    print_for_sumbols(" Turniej się zaczyna. Są 8 uczęstników muszisz pokonać każdego\n\n")
    Ucze1 = ucze("Ana")
    Ucze2 = ucze("Bartek")
    Ucze3 = ucze("Tom")
    Ucze4 = ucze("Red")
    Ucze5 = ucze("Rot")
    Ucze6 = ucze("Abram")
    Ucze7 = ucze("Reqred")
    Ucze8 = ucze("Ratpaolek")
    Ucze_all = [Ucze1,Ucze2,Ucze3,Ucze4,Ucze5,Ucze6,Ucze7,Ucze8]
    j = int(7)
    while j != 0:
        print_for_sumbols("Twój  rywal to :  "+ Ucze_all[7-j].name + "\n\n")
        print("Press enter żeby sprobować pokonać " + Ucze_all[7-j].name)
        input()
        power = random.randint(9,20)
        if power > Ucze_all[7-j].power:
            print("Wygrałeś u " + Ucze_all[7-j].name)
            j = j - 1
            print("Zostało jeszcze " + str(j+1) )
        else:
            print("Nie wygrałeś u niego spróbuj jeszcze raz")
    print("Wygrałeś u wszystkich dostajesz nagrodę")
    print_for_sumbols("Press enten to continue road\n")
    time.sleep(3)
    input()
def przygoda_9():
    os.system("cls")
    print_for_sumbols(" Obok drogi stoje babcia i chce oddać tobie dziwny list\n")
    print_for_sumbols(" Wziąłeś go i masz tam zapisany dziwny list\n")
    print_for_sumbols(" Zobaczyłeś tam dziwny nadpis\n\n")
    print_for_sumbols("|||Qxgbjkfzv hmb ql piltl  jxmx|||")
    print_for_sumbols("Dowiedziałeś się że to kod Cesarza i kod do niego 3\n")
    print_for_sumbols("____________________________________________________\n")
    yyuu = input("Wpisz tutaj: :>>>")
    if yyuu in ("mapa","Mapa","MAPA"):
        print("Dowiedziałeś się  kod od skryni z złotem którą znalazłeś obok drogi")
        print_for_sumbols("Press enten to continue road\n")
        time.sleep(3)
    else:
        print("Niestety nie zrozumiałeś co robić , zrób coś jeszcze raz")
        przygoda_9()
def przygoda_10():
    os.system("cls")
    print_for_sumbols(" Idziesz przez miasto i widzisz żównieża który probuje pocelić z armaty żeby zniśczyć zamek \n")
    print_for_sumbols(" Możesz sprobować swoje siły w tej sprawie\n")
    qa = 1
    while qa != 0:
        print_for_sumbols(" Wpisz znaczenie kąta pod którym będziesz strzelać\n\n")
        tttt = int(input(":>>>  "))
        if tttt > 20 and tttt < 40:
            print_for_sumbols("Osiągnoweś cel i trafiłeś w zamek. Możesz iść dalej\n")
            print_for_sumbols("Press enten to continue road\n")
            time.sleep(3)
            qa = qa - 1
        else:
            print_for_sumbols("Niestety nie trafiłeś, masz jeszcze dwe próby")
        print_for_sumbols(" Wpisz znaczenie kąta pod którym będziesz strzelać\n\n")
        tttt = int(input(":>>> "))
        if tttt > 55 and tttt < 80:
            print_for_sumbols("Osiągnoweś cel i trafiłeś w zamek. Możesz iść dalej\n")
            print_for_sumbols("Press enten to continue road\n")
            time.sleep(3)
            qa = qa - 1
        else:
            print_for_sumbols("Niestety nie trafiłeś, masz jeszcze jedną próbę")
        print_for_sumbols(" Wpisz znaczenie kąta pod którym będziesz strzelać\n\n")
        tttt = int(input(":>>> "))
        if tttt > 90 and tttt < 99:
            print_for_sumbols("Osiągnoweś cel i trafiłeś w zamek. Możesz iść dalej\n")
            print_for_sumbols("Press enten to continue road\n")
            time.sleep(3)
            qa = qa - 1
        else:
            print_for_sumbols("Niestety nie trafiłeś i już nie  masz  prób")
            przygoda_10()
def przygoda_11():
    os.system("cls")
    print_for_sumbols(" Idziesz obok rzeki i widzisz elfa który za 10 minut oddejdzie na wędkarstwo  \n")
    print_for_sumbols(" Niestety on ma chorobę oczną i nie może dobdze kierować  łodką\n")
    print_for_sumbols(" Wsiadasz w łodkę i przygoda zaczyna się. Będziesz musiał wybrać stronę w której mniejsza szansa na podwodny kamień \n")
    k = 0
    v = random.randint(1,6)
    while v != 0:
        print_for_sumbols("Wpisz lewo lub prawo\n")
        vv = input(" :>>> ")
        vvv = random.randint(1,2)
        if vvv == 1 and vv in ("Lewo","lewo","LEWO"):
            print_for_sumbols("_________________________\n")
            print_for_sumbols("Wybrałeś dobrą stronę, jeszcze trzeba zgadnąć\n\n")
            time.sleep(3)
            v = v - 1
        elif vvv == 2 and vv in ("Prawo","prawo","PRAWO"):
            print_for_sumbols("_________________________\n")
            print_for_sumbols("Wybrałeś dobrą stronę, jeszcze trzeba zgadnąć\n\n")
            time.sleep(3)
            v = v - 1
        elif vvv == 1 and vv in ("Prawo","prawo","PRAWO"):
            print_for_sumbols("_________________________\n")
            print_for_sumbols("Niestety nie zobaczyłeś kamień w wodzie. Nie rób tego!!!!\n")
            time.sleep(3)
            k = k + 1
        elif vvv == 2 and vv in ("Lewo","lewo","LEWO"):
            print_for_sumbols("_________________________\n")
            print_for_sumbols("Niestety nie zobaczyłeś kamień w wodzie. Nie rób tego!!!!\n")
            time.sleep(3)
            k = k + 1
        if k == 4:
            print("Niestety nazbierałeś za dużo kamienia")
            time.sleep(3)
            przygoda_11()
    print_for_sumbols("Press enten to continue road\n")
    input()
def przygoda_12():
    os.system("cls")
    print_for_sumbols("  Wszedłeś na drogę w górach i spotkałeś śnieżnego człowieka , który zgubił swoje zwierzęto  \n")
    print_for_sumbols(" Muszisz mu pomóc go zlaleść!!!!!\n")
    print_for_sumbols(" Dowiedziałeś się że on może być w lesie , w miascie , albo na wsi. Muszisz przejść na każdą lokację i sprobować zawołać zwierzęto) \n")
    print("___________________________________")
    b = 1
    rm = random.randint(1,3)
    while b != 0:
        e = input("Wpisz lokacje w której chcesz szukać \n")
        if e in ("Las","Miasto","Wsi"):
            if e == "Las":
                print_for_sumbols("Jesteś w lasie !!\n")
                print_for_sumbols("Spróbuj zawołać zwierzęto!\n")
                input()
                if rm == 1:
                    print_for_sumbols("Witam znalazłeś zwierzęto!!\n")
                    print_for_sumbols("Snieżny człowiek jest bardzo wdzięczny)!!\n")
                    print_for_sumbols("Press enten to continue road\n")
                    input()
                    b -= 1
                else:
                    print_for_sumbols("Niestey nie znalazłeś zwierzęto na tej lokacji\n")

            elif e == "Miasto":
                print_for_sumbols("Jesteś w Mieście !!\n")
                print_for_sumbols("Spróbuj zawołać zwierzęto!\n")
                input()
                if rm == 2:
                    print_for_sumbols("Witam znalazłeś zwierzęto!!\n")
                    print_for_sumbols("Snieżny człowiek jest bardzo wdzięczny)!!\n")
                    print_for_sumbols("Press enten to continue road\n")
                    input()
                    b -= 1
                else:
                    print_for_sumbols("Niestey nie znalazłeś zwierzęto na tej lokacji\n")

            elif e == "Wsi":
                print_for_sumbols("Jesteś na  Wsi !!\n")
                print_for_sumbols("Spróbuj zawołać zwierzęto!\n")
                input()
                if rm == 3:
                    print_for_sumbols("Witam znalazłeś zwierzęto!!\n")
                    print_for_sumbols("Snieżny człowiek jest bardzo wdzięczny)!!\n")
                    print_for_sumbols("Press enten to continue road\n")
                    input()
                    b -= 1
                else:
                    print_for_sumbols("Niestey nie znalazłeś zwierzęto na tej lokacji\n")
        else:
            print("Wpisałeś nieprawidwołą nazwę lokacji\n")
def przygoda_13():
    os.system("cls")
    print_for_sumbols("  Idziesz przez drogę i spotkałeś tajemniczego druida który krzycze do ciebie\n")
    print_for_sumbols(" Druid:   - Bohaterze!!! Tam delej po drodzę idą 30 morderców. Jeżeli zapłacisz mnie to sprobuje schronić ciebie za pomocą magii\n")
    print_for_sumbols(" Muszi wybrać czy uwierzyć Druidu czy iść dalej \n")
    print("___________________________________\n")
    ff = input("Press y to accept | Press u to not accept: \n :>>> ")
    yyy = random.randint(1,2)
    if ff =="y":
        if yyy == 1:
            print("___________________________________\n")
            print_for_sumbols(" - Oddałeś druidu część septimów i on zachwał ciebie\n")
            print_for_sumbols("    - Okazało się Druid nie kłamił i uratowałeś się !! \n")
            print_for_sumbols("Press enten to continue road\n")
            input()
        if yyy == 2:
            print("___________________________________\n")
            print_for_sumbols(" - Oddałeś druidu część septimów i on zachwał ciebie\n")
            print_for_sumbols("    - Okazało się Druid  kłamił i nie spotkałeś żadnego morderca!! \n")
            print_for_sumbols("Press enten to continue road\n")
            input()
    else:
        print_for_sumbols("Press enten to continue road\n")
        input()
def przygoda_14():
    os.system("cls")
    print_for_sumbols(" Szedłeś przez pole i zobaczyłeś babcie ktróra płakała\n")
    print_for_sumbols(" Zapytałeś, co się stało. Okazało się że ztraciła swoich krolików w ogrodzie i nie będzie mieć co jeść \n")
    print_for_sumbols(" Możesz pomóc złapać krolików \n")
    print("___________________________________\n")
    uii = input("Press y to accept | Press u to not accept\n  :>>> ")
    if uii == "y":
        print_for_sumbols("Dobra teraz widzisz przed sobą nory krolików\n")
        print_for_sumbols("Kiedy zobaczysz napis łapaj , klikaj 'Enter' \n")
        print("_________________________________________________________\n")
        zk = 0
        while zk != 7:
            ti = random.randint(5,10)
            time.sleep(ti)
            print(t.Lapaj)
            print("_________________________________________________________\n")
            input()
            sk = random.randint(1,100)
            if sk > 25:
                print_for_sumbols("Złapałeś krolika, muszisz złapać jeszcze : " + str(6-zk))
                zk += 1
            else:
                print_for_sumbols("Niestety tym razem nie złapałeś, próbuj jeszcze\n")
        print_for_sumbols("Zebrałeś wszystkich krolików babcia będzie tobie wdzięczna\n")
        print_for_sumbols("Press enten to continue road\n")
        input()
    else:
        print_for_sumbols("Press enten to continue road\n")
        input()
def przygoda_15():
    os.system("cls")
    print_for_sumbols(" Idzieś obok miasta Tok\n")
    print_for_sumbols(" Zobaczyłeś dwóch Chłopów które krzyczą i kłóczą się między sobą  \n")
    print_for_sumbols(" Okazało się że oni dyskutowali na temat Pola powierzchni ogroda jednego z mężczyzn \n")
    print_for_sumbols(" Dla tego żeby to skończyć trzeba otworzyć książke  ' O matematycę Morowinda' \n")
    print("___________________________________\n")
    input("Press enter to open book")
    print(t.kroki)
    kro = 0
    j = random.randint(8,20)
    for i in range(0,j):
        print("Press enter to do one step !!")
        input()
        kro += 1
        print("Ok, na ten moment masz kroków : " + str(kro)+ "\n")
        print("___________________________________\n")
    print_for_sumbols("Ok, na ten moment masz kroków : " + str(kro)+ "\n")
    print("____________________________________________________\n")
    print("No i teraz miszisz wpisać odpowidż, ile wynosi pole \n")
    qqq = int(input(":>>> "))
    if qqq == (kro*2)+(kro/2):
        print_for_sumbols("Odpowiedż jest prawidłowa\n")
        print_for_sumbols("Press enten to continue road\n")
        input()
    else:
        print_for_sumbols("Niestety wpisałeś coś nie to xd\n")
        print_for_sumbols("Press enten to continue road\n")
        input()
def przygoda_16():
    os.system("cls")
    print_for_sumbols(" Szpacerowałeś po porku i spotkałeś jennego z werwólfów, który schował się kiedy ty zabił króla Werwolfów\n")
    print_for_sumbols(" Za pomocą magii on zmienił swój widok na dziewczyne \n")
    qqqqq = random.randint(1,2)
    if qqqqq == 1:
        print_for_sumbols(" Niestety uwierzyłeś w to że dziewczycnie potrzebna pomóc i teraz jesteś w pówapcę\n")
        print_for_sumbols(" Probujesz sobie z tym poradzić  \n")
        print("___________________________________\n")
        print_for_sumbols("Wpisuj odpowiedzi dla tego żeby probować wyjść z półapki\n")
        print_for_sumbols("Pytanie:  Ile to będzie  '144*2+12' \n")
        ast = input()
        if ast =="200":
            print_for_sumbols("Super starajsie dalej!!!")
        else:
            print_for_sumbols("Niestety spadłeś\n ")
            time.sleep(2)
            przygoda_16()
        print_for_sumbols("Pytanie:  Ile werwólfów ty zabiłeś żeby dojść do Króla \n")
        ast = input()
        if ast == "5":
            print_for_sumbols("Super starajsie dalej!!!\n")
        else:
            print_for_sumbols("Niestety spadłeś ")
            time.sleep(2)
            przygoda_16()
        print_for_sumbols("Pytanie:  Jak sie nazywał mag na 1 level \n")
        ast = input()
        if ast == "Torin":
            print_for_sumbols("Super zrobiłeś to możesz uciekać !!!!")
            print_for_sumbols("Press enten to continue road\n")
            input()
        else:
            print_for_sumbols("Niestety spadłeś ")
            time.sleep(2)
            przygoda_16()
def przygoda_17():
    os.system("cls")
    print_for_sumbols(" Wszedłeś w tawernę i zpotkałeś osobę która powiedziała że możesz zagrać w LOTTO \n")
    print_for_sumbols(" Teraz muszesz wybrać grać czy nie ! \n")
    ere = input("Press y to accept | Press u to not accept\n :>>> ")
    if ere == "y":
        print_for_sumbols(" Dobra masz możliwość kupić trzy rodzaje biletów:\n 1. Szansa wygrać - 50% - kosztuje 50 septimów\n2. Szansa wygrać - 30% - kosztuje 30 septimów\n 3. Szansa wygrać - 10% - kosztuje 10 septimów\n ")
        print_for_sumbols(" Teraz muszesz wybrać bilet  (press 1,2 or 3) \n")
        rty = int(input(":>>> "))
        if rty == 1:
            print_for_sumbols("Kupiłeś bilet 50 %\n")
            print_for_sumbols("Teraz naciśni Enter żeby zobaczyć czy ten bilet jest szczęśliwy\n")
            input()
            rtt = random.randint(1,100)
            if rtt < 50:
                print_for_sumbols("Witam, Witam wygrałeś 500 septimów\n")
                print_for_sumbols("Press enten to continue road\n")
                input()
            else:
                print_for_sumbols("Nie w ten raz\n")
                print_for_sumbols("Press enten to continue road\n")
                input()
        elif rty == 2:
            print_for_sumbols("Kupiłeś bilet 30 %\n")
            print_for_sumbols("Teraz naciśni Enter żeby zobaczyć czy ten bilet jest szczęśliwy\n")
            input()
            rtt = random.randint(1, 100)
            if rtt < 30:
                print_for_sumbols("Witam, Witam wygrałeś 500 septimów\n")
                print_for_sumbols("Press enten to continue road\n")
                input()
            else:
                print_for_sumbols("Nie w ten raz((\n")
                print_for_sumbols("Press enten to continue road\n")
                input()
        elif rty == 3:
            print_for_sumbols("Kupiłeś bilet 10 %\n")
            print_for_sumbols("Teraz naciśni Enter żeby zobaczyć czy ten bilet jest szczęśliwy\n")
            input()
            rtt = random.randint(1, 100)
            if rtt < 10:
                print_for_sumbols("Witam, Witam wygrałeś 500 septimów\n")
                print_for_sumbols("Press enten to continue road\n")
                input()
            else:
                print_for_sumbols("Nie w ten raz\n")
                print_for_sumbols("Press enten to continue road\n")
                input()
    else:
        print_for_sumbols("Press enten to continue road\n")
        input()
def przygoda_18():
    os.system("cls")
    print_for_sumbols(" Idziesz i słyszesz że do ciebie zaczyna mówić że potrzebuje pomocy żeby zebrać 'Sok Brzozy' \n")
    print_for_sumbols(" Teraz muszesz wybrać pomóc czy nie! \n")
    ere = input("Press y to accept | Press u to not accept\n :>>> ")
    sok = int(0)
    if ere == "y":
        print_for_sumbols(" Ok dobra teraz będziesz podchodzić do brzozy i probować wzięc sok \n")
        print("Muszisz dostać 2 litra soku, dopóki tego nie zrobisz nie przejdziesz tej przegody\n")
        print("___________________________________\n")
        while sok < int(1000) or sok == int(1000):
            print_for_sumbols(" PRESS ENTER TO TAKE JUISE \n")
            input()
            print("___________________________________\n")
            sok_i = random.randint(100,250)
            print_for_sumbols("W ten raz dostałeś ml soku: " + str(sok_i)+"\n\n")
            sok = sok + sok_i
        print_for_sumbols("Dostałeś soku : " + str(sok)+ " ml.")
        print_for_sumbols("Press enten to continue road\n")
        input()
    else:
        print_for_sumbols("Press enten to continue road\n")
        input()
def przygoda_19():
    os.system("cls")
    print_for_sumbols(" Zobaczyłeś maga który potrzebuje pomocy \n")
    print_for_sumbols(" Teraz muszesz wybrać pomóc czy nie! \n")
    ere = input("Press y to accept | Press u to not accept\n :>>> ")
    if ere == "y":
        print_for_sumbols("Zobaczyłeś maga który stoi obok drogi i coś robi\n")
        print_for_sumbols("Właśnie pogadałeś z nim i okazało się że on otworzył skrynie 'Pandory' i ztracił swoje magiczne zwierzęta\n")
        print_for_sumbols("Dla tego żeby to zrobić muszisz rozdzielić zwierząt na: Drapieżników i Roślinożerne\n")
        print("__________________________________________________________________________________\n")
        print(" UWAGA!! Dla tego  żeby wybierać pisz 1 - dla Drapieżników, 2 - dla Roślinożerów!!!\n\n")
        i = 1
        while i != 0:
            print_for_sumbols("Zobaczyłeś wilka - twój wybur?\n")
            b = input(":>>> ")
            if b == "1":
                print("Super, wilk w półapcę, idziemy dalej\n")
                print("__________________________________________________________________________________\n")
            else:
                print("Niestety wybrałeś nie to, mag zaczął krzyczać na ciebie!!!\n")
                print_for_sumbols("Press enten to continue road\n")
                input()
                i -= 1
            print_for_sumbols("Zobaczyłeś Jelenia - twój wybur?\n")
            b = input(":>>> ")
            if b == "2":
                print("Super, Jeleń w półapcę, idziemy dalej\n")
                print("__________________________________________________________________________________\n")
            else:
                print("Niestety wybrałeś nie to, mag zaczął krzyczać na ciebie!!!\n")
                print_for_sumbols("Press enten to continue road\n")
                input()
                i -= 1
            print_for_sumbols("Zobaczyłeś Zubra - twój wybur?\n")
            b = input(":>>> ")
            if b == "2":
                print("Super, Zubr w półapcę, idziemy dalej\n")
                print("__________________________________________________________________________________\n")
            else:
                print("Niestety wybrałeś nie to, mag zaczął krzyczać na ciebie!!!\n")
                print_for_sumbols("Press enten to continue road\n")
                input()
                i -= 1
            print_for_sumbols("Zobaczyłeś ostatniego tygrysa - twój wybur?\n")
            b = input(":>>> ")
            if b == "1":
                print("Super, tygrys w półapcę, idziemy dalej\n")
                print("__________________________________________________________________________________\n")
                i -= 1
            else:
                print("Niestety wybrałeś nie to, mag zaczął krzyczać na ciebie!!!\n")
                print_for_sumbols("Press enten to continue road\n")
                input()
                i -= 1
        print("__________________________________________________________________________________\n")
        print_for_sumbols("Dobra super, pomogłeś magu!!!\n")
        print_for_sumbols("Press enten to continue road\n")
        input()
    else:
        print_for_sumbols("Press enten to continue road\n")
        input()
def przygoda_20():
    os.system("cls")
    print_for_sumbols(" Idziesz po drodze i zobaczyłeś że dalej stoi niebezpieczny mag. Muszisz sprobować włączyć stels i chicho przejść dalej. \n")
    print_for_sumbols("Ok dobra idziesz. Muszisz wpisać takie znaczenie szybkości bohatera żeby mag go nie usłyszał i nie małe żeby po prostu nie zobaczył ciebie")
    print("____________________________________________________________________________________________\n")
    ty = int(input("Wpisz znaczenie: \n :>>>"))
    if ty > int(25) and ty < int(40):
        print_for_sumbols("Udało się, Mag ci nie zauważył!!!!\n")
        print_for_sumbols("Press enten to continue road\n")
        input()
    else:
        print_for_sumbols("Niestety mag cie zauważył, i zabił cie ((( ")
        przygoda_20()





