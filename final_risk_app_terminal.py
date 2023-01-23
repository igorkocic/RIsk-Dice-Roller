import random
attacker = input("Name of attacker: ")
defender = input("Name of defender: ")
n_soldiers_attacker = int(input(f"Enter number of {attacker}'s soldiers: "))
n_soldiers_defender = int(input(f"Enter number of {defender}'s soldiers: "))
print("\n")
print("--------------------------------------")
print("\n")


def rollDiceAttacker3():
    attacker_dice = 3
    list_attacker = []
    possible_faces = [1,2,3,4,5,6]
    for die in range(attacker_dice):
        roll = random.choice(possible_faces)
        list_attacker.append(roll)
    print(f"{attacker} rolled ", list_attacker)
    return list_attacker


def rollDiceAttacker2():
    attacker_dice = 2
    list_attacker = []
    possible_faces = [1,2,3,4,5,6]
    for die in range(attacker_dice):
        roll = random.choice(possible_faces)
        list_attacker.append(roll)
    print(f"{attacker} rolled ", list_attacker)
    return list_attacker


def rollDiceAttacker1():
    attacker_dice = 1
    list_attacker = []
    possible_faces = [1,2,3,4,5,6]
    for die in range(attacker_dice):
        roll = random.choice(possible_faces)
        list_attacker.append(roll)
    print(f"{attacker} rolled ", list_attacker)
    return list_attacker


def rollDiceDefender2():
    list_defender = []
    defender_dice = 2
    possible_faces = [1,2,3,4,5,6]
    for die in range(defender_dice):
        roll = random.choice(possible_faces)
        list_defender.append(roll)
    print(f"{defender} rolled ", list_defender)
    return list_defender


def rollDiceDefender1():
    list_defender = []
    defender_dice = 1
    possible_faces = [1,2,3,4,5,6]
    for die in range(defender_dice):
        roll = random.choice(possible_faces)
        list_defender.append(roll)
    print(f"{defender} rolled ", list_defender)
    return list_defender


global n_soldier_attacker_after_dice_rolling
global n_soldier_defender_after_dice_rolling 
n_soldier_attacker_after_dice_rolling = n_soldiers_attacker
n_soldier_defender_after_dice_rolling = n_soldiers_defender


while (n_soldier_defender_after_dice_rolling >0) and  (n_soldier_attacker_after_dice_rolling > 1) and (input("press enter to roll the dice") == ''):
    if (n_soldier_defender_after_dice_rolling >=2) & (n_soldier_attacker_after_dice_rolling>=4):
        list_attacker = rollDiceAttacker3()
        list_defender = rollDiceDefender2()
        second_largest_die_attacker = sorted(list_attacker)[-2]
        second_largest_die_defender = sorted(list_defender)[-2]
        if ((max(list_attacker) > max(list_defender)) & (second_largest_die_attacker > second_largest_die_defender)):
            n_soldier_defender_after_dice_rolling -= 2
        elif ((max(list_attacker) > max(list_defender)) & (second_largest_die_attacker <= second_largest_die_defender)):
            n_soldier_attacker_after_dice_rolling -= 1
            n_soldier_defender_after_dice_rolling -=1
        elif ((max(list_attacker) <= max(list_defender)) & (second_largest_die_attacker <= second_largest_die_defender)):
            n_soldier_attacker_after_dice_rolling -=2
        elif ((max(list_attacker) <= max(list_defender)) & (second_largest_die_attacker > second_largest_die_defender)):
            n_soldier_attacker_after_dice_rolling -= 1
            n_soldier_defender_after_dice_rolling -=1
        print(f"{attacker} now has {n_soldier_attacker_after_dice_rolling}")
        print(f"{defender} now has {n_soldier_defender_after_dice_rolling}")
        print("\n")
        print("--------------------------------------")
        print("\n")
    elif (n_soldier_defender_after_dice_rolling ==1) & (n_soldier_attacker_after_dice_rolling>=4):
        list_attacker = rollDiceAttacker3()
        lista_defender = rollDiceDefender1()
        druga_najjaca_kockica_napadaca = sorted(list_attacker)[-2]
        if max(list_attacker) > max(lista_defender):
            n_soldier_defender_after_dice_rolling -= 1
        elif max(list_attacker) <= max(lista_defender):
            n_soldier_attacker_after_dice_rolling -= 1
        print(f"{attacker} now has {n_soldier_attacker_after_dice_rolling}")
        print(f"{defender} now has {n_soldier_defender_after_dice_rolling}")
        print("\n")
        print("--------------------------------------")
        print("\n")
    elif (n_soldier_defender_after_dice_rolling == 1) & (n_soldier_attacker_after_dice_rolling==3):
        list_attacker = rollDiceAttacker2()
        lista_defender = rollDiceDefender1()
        if max(list_attacker) > max(lista_defender) :
            n_soldier_defender_after_dice_rolling -= 1
        elif max(list_attacker) <= max(lista_defender):
            n_soldier_attacker_after_dice_rolling -= 1
        print(f"{attacker} now has {n_soldier_attacker_after_dice_rolling}")
        print(f"{defender} now has {n_soldier_defender_after_dice_rolling}")
        print("\n")
        print("--------------------------------------")
        print("\n")
    elif (n_soldier_defender_after_dice_rolling==1) & (n_soldier_attacker_after_dice_rolling ==2):
        list_attacker = rollDiceDefender1()
        list_defender = rollDiceAttacker1()
        if max(list_attacker) > max(list_defender) :
            n_soldier_defender_after_dice_rolling -= 1
        elif max(list_attacker) <= max(list_defender):
            n_soldier_attacker_after_dice_rolling -= 1
        print(f"{attacker} now has {n_soldier_attacker_after_dice_rolling}")
        print(f"{defender} now has {n_soldier_defender_after_dice_rolling}")
        print("\n")
        print("--------------------------------------")
        print("\n")
    elif (n_soldier_defender_after_dice_rolling>=2) & (n_soldier_attacker_after_dice_rolling ==2):
        list_attacker = rollDiceDefender2()
        list_defender = rollDiceAttacker1()
        if max(list_attacker) > max(list_defender) :
            n_soldier_defender_after_dice_rolling -= 1
        elif max(list_attacker) <= max(list_defender):
            n_soldier_attacker_after_dice_rolling -= 1
        print(f"{attacker} now has {n_soldier_attacker_after_dice_rolling}")
        print(f"{defender} now has {n_soldier_defender_after_dice_rolling}")
        print("\n")
        print("--------------------------------------")
        print("\n")
    elif (n_soldier_defender_after_dice_rolling>=2) & (n_soldier_attacker_after_dice_rolling ==3):
        list_attacker = rollDiceAttacker2()
        list_defender = rollDiceDefender2()
        if max(list_attacker) > max(list_defender) :
            n_soldier_defender_after_dice_rolling -= 1
        elif max(list_attacker) <= max(list_defender):
            n_soldier_attacker_after_dice_rolling -= 1
        print(f"{attacker} now has {n_soldier_attacker_after_dice_rolling}")
        print(f"{defender} now has {n_soldier_defender_after_dice_rolling}")
        print("\n")
        print("--------------------------------------")
        print("\n")
    else:
        print(f"{attacker} now has {n_soldier_attacker_after_dice_rolling}")
        print(f"{defender} now has {n_soldier_defender_after_dice_rolling}")
        break
print("Game Over")