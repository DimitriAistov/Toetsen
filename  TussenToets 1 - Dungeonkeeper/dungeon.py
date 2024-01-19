import time, math, random

player_attack = 1
player_defense = 0
player_health = 3
rupees = 0

Kamer2_getal1 = random.randint(10,25)
Kamer2_getal2 = random.randint(-5,75)
Kamer2_getal3 = Kamer2_getal1 + Kamer2_getal2
antwoord = 0

items1 = ["schild","zwaard"]

kamer3_item_gepakt = False

kamer6_bezocht = False

# === [kamer 1] === #
def kamer1():
    global player_attack, player_defense, player_health, kamer3_item_gepakt,antwoord ,rupees

    print('Door de twee grote deuren loop je een gang binnen.')
    print('Het ruikt hier muf en vochtig.')
    print('Je ziet een deur voor je.')
    
    kamer7()
    print('')
    time.sleep(1)


# === [kamer 7] === #
def kamer7():
    global player_attack, player_defense, player_health, kamer3_item_gepakt,antwoord, rupees
    print("Je komt de kamer in ")
    print("Je vindt een rupee")
    rupees +=1
    print(f"Je hebt nu {rupees} rupee")
    print("Je kunt kiezen om naar kamer 2 of naar kamer 3 te gaan")
    kamer7_deur = int(input("Welke kamer kies je (2/3) "))
    
    if kamer7_deur == 2:
        kamer2()
    elif kamer7_deur == 3:
        kamer8()


    print("")
    time.sleep(1)

# === [kamer 2] === #
def kamer2():
    global player_attack, player_defense, player_health, kamer3_item_gepakt, antwoord, rupees
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een sleutel vast.')
    print('Op zijn borst zit een numpad met de toetsen 9 t/m 0.')
    print(f'Daarboven zie je een som staan {Kamer2_getal1} + {Kamer2_getal2} =?')
    antwoord = int(input('Wat toets je in? '))

    if antwoord == Kamer2_getal3:
        print('Het standbeeld laat de sleutel vallen en je pakt het op')
    else:
        print('Er gebeurt niets....')

    print('Je zie een deur achter het standbeeld.')
    
    kamer2_deur = int(input("Kies je voor de deur naar kamer 6 of kamer 3? (6/3)"))
    if kamer2_deur == 3:
        kamer3()
    elif kamer2_deur == 6:
        kamer6()

    print('')
    time.sleep(1)


# === [kamer 6] === #
def kamer6():
    global player_attack, player_defense, player_health, kamer3_item_gepakt, antwoord, rupees
    zombie_attack = 1
    zombie_defense = 0
    zombie_health = 2
    print(f'Je loopt de kamer binnen.')
    print('Je loopt tegen een zombie aan.')

    zombie_hit_damage = (zombie_attack - player_defense)
    if zombie_hit_damage <= 0:
        print('Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade doen.')
    else:
        zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
            
        player_hit_damage = (player_attack - zombie_defense)
        player_attack_amount = math.ceil(zombie_health / player_hit_damage)


        if player_attack_amount < zombie_attack_amount:
            print(f'In {player_attack_amount} rondes versla je de zombie.')
            player_health = player_health - player_attack_amount * zombie_attack
            print(f'Je health is nu {player_health}.')

        else:
            print('Helaas is de zombie te sterk voor je.')
            print("------------------")
            print('|    Game over.  |')
            print("------------------")
            exit()

    kamer3()
    print('')
    time.sleep(1)


# === [kamer 8] === #
def kamer8():
    global player_attack, player_defense, player_health, kamer3_item_gepakt,item, antwoord,rupees



# === [kamer 3] === #
def kamer3():
    global player_attack, player_defense, player_health, kamer3_item_gepakt,item, antwoord,rupees
    item = random.choice(items1)
    if items1[0]:
        player_defense += 1
    if items1[1]:
        player_attack += 2
    player_health +=1
    kamer3_item_gepakt = True
    print('Je duwt hem open en stapt een hele lange kamer binnen.')
    print(f'In deze kamer staat een tafel met daarop een {item} en een healing potion.')
    print(f'Je pakt het {item} op en houd het bij je.')
    print("Je gebruikt meteen de healing potion")
    print("De healing potion geeft je +1 health")
    print(f"Je health is nu {player_health}")
    print('Op naar de volgende deur.')

    print("Je ziet een goblin die iets verkoopt")
    print("Hij heeft: ")
    print("Muts [1 rupee | +1 defence]")
    kamer3_kopen = input("Wil je dit kopen? (ja/nee)").lower()
    if kamer3_kopen == "ja":
        print("Je hebt een muts gekocht van de goblin")
        rupees -=1
        print(f"Je hebt nu nog {rupees} rupees")
        player_defense +=1
        print(f"Je hebt nu {player_defense} defense")

    
    kamer4()

    print('')
    time.sleep(1)


# === [kamer 4] === #
def kamer4():
    global player_attack, player_defense, player_health, kamer3_item_gepakt, item, antwoord, rupees
    zombie_attack = 2
    zombie_defense = 0
    zombie_health = 3
    print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
    print('Je loopt tegen een zombie aan.')

    zombie_hit_damage = (zombie_attack - player_defense)
    if zombie_hit_damage <= 0:
        print('Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade doen.')
    else:
        zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
            
        player_hit_damage = (player_attack - zombie_defense)
        player_attack_amount = math.ceil(zombie_health / player_hit_damage)

        if player_attack_amount < zombie_attack_amount:
                print(f'In {player_attack_amount} rondes versla je de zombie.')
                player_health = player_health - player_attack_amount * zombie_attack
                print(f'Je health is nu {player_health}.')
        else:
            print('Helaas is de zombie te sterk voor je.')
            print("------------------")
            print('|    Game over.  |')
            print("------------------")
            exit()
    
    kamer5()
    print('')
    time.sleep(1)


# === [kamer 5] === #
def kamer5():
    global player_attack, player_defense, player_health, item, antwoord, rupees
    print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
    print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
    print('Je loopt er naartoe.')
    print("Je ziet een sleutelgat")

    if antwoord == Kamer2_getal3:
        print("Je gebruikt de sleutel van kamer 2 en hij past.")
        print("De schatkist gaat open")
        print("--------------------------")
        print("|    Je hebt Gewonnen!   |")
        print("--------------------------")

    elif antwoord == 0:
        print("Je hebt geen sleutel")
        print("Je hebt verloren")
        print("--------------------------")
        print("|    Je hebt Verloren!   |")
        print("--------------------------")


kamer1()