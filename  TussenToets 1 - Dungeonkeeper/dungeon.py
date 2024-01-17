import time, math, random

player_attack = 1
player_defense = 0
player_health = 3

Kamer2_getal1 = random.randint(10,25)
Kamer2_getal2 = random.randint(-5,75)
Kamer2_getal3 = Kamer2_getal1 + Kamer2_getal2

items1 = ["schild","zwaard"]


# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [kamer 2] === #
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
print('')
time.sleep(1)

# === [kamer 6] === #
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
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de zombie te sterk voor je.')
        print("------------------")
        print('|    Game over.  |')
        print("------------------")
        exit()
print('')
time.sleep(1)


# === [kamer 3] === #
item = random.choice(items1)
if items1[0]:
    player_defense += 1
if items1[1]:
    player_attack += 2

print('Je duwt hem open en stap een hele lange kamer binnen.')
print(f'In deze kamer staat een tafel met daarop een {item}.')
print(f'Je pakt het {item} op en houd het bij je.')
print('Op naar de volgende deur.')
print('')
time.sleep(1)

# === [kamer 4] === #
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
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de zombie te sterk voor je.')
        print("------------------")
        print('|    Game over.  |')
        print("------------------")
        exit()
print('')
time.sleep(1)

# === [kamer 5] === #
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

else:
    print("Je hebt geen sleutel")
    print("Je hebt verloren")
    print("--------------------------")
    print("|    Je hebt Verloren!   |")
    print("--------------------------")