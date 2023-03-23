from random import randint

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

'''TODO: Critical hit system, magic, shop, inventory, gender, different arenas with different enemy types'''
'''TODO: Experience levels system'''
'''TODO: implement randints to make class (and race?) definitions more natural and precise'''
'''TODO: implement ASCII art using PIL.Image custom greyscale function in a separate module'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

enemy_list = ["Orc", "Goblin", "Thief", "Scag", "Gnoll"]  # a list of available enemy types


class Hero:  # main character class

    def __init__(self):
        self.name = None
        self.race = ""
        self.charclass = ""
        self.xl = 1
        self.max_HP = None
        self.HP = 100
        self.MP = 100
        self.strength = 5
        self.agility = 5
        self.endurance = 5
        self.intelligence = 5
        self.luck = 5
        self.crit_modifier = (self.agility // 2) + (self.luck // 1.5) + randint(1, ((self.agility+self.luck) // 2))
        self.inventory = []
        self.damage = ((randint(6, 7) + self.strength) + (self.endurance // 2) + (self.luck // 5)) +\
                      (randint(3, 5) if "Shortsword" in self.inventory else 0) +\
                      (randint(1, 4) if "Dagger" in self.inventory else 0) +\
                      (randint(2, 4) if "Wooden Staff" in self.inventory else 0)
        self.spells = []
        self.gold = 100
        
    def greet(self):
        self.name = input("What's your name? >>> ")
        while len(self.name) == 0:
            self.name = input("Enter your name, please! >>> ")
        else:
            print(f"\nGreetings, {self.name}!\n")
    
    def race_creation(self):
        select = None
        while select != "1":
            selection = input("Select your race:\n 1. Human\n 2. Elf\n 3. Orc\n >>> ")

            if selection == "1":
                select = input("Humans are equally skilled at everything.\n"
                               "They have average stats and can master any skill.\n"
                               "Do you want to be a Human?\n\n"
                               "1. Yes 2. No >>> ")

                if select == "1":
                    self.race = "Human"
                    self.strength += 5
                    self.agility += 5
                    self.endurance += 5
                    self.intelligence += 5
                    self.luck += 5

                elif select == "2":
                    print("")

                elif select not in "12":
                    print("\nType in '1' or '2', please.\n")

            elif selection == "2":
                select = input("Elves are masters of evasive combat and adept in magic.\n"
                               "They tend to be more fragile than other races.\n"
                               "Are you an Elf?\n\n"
                               "1. Yes 2. No >>> ")

                if select == "1":
                    self.race = "Elf"
                    self.strength += 4
                    self.agility += 7
                    self.endurance += 2
                    self.intelligence += 7
                    self.luck += 5
                    self.HP = 80
                    self.MP = 150

                elif select == "2":
                    print("")

                elif select not in "12":
                    print("\nType in '1' or '2', please.\n")

            elif selection == "3":
                select = input("Orcs are masters of combat, able to deliver terrifying blows.\n"
                               "They have excellent HP and strength, but are somewhat clumsy.\n"
                               "Are you an Orc?\n\n"
                               "1. Yes 2. No >>> ")

                if select == "1":
                    self.race = "Orc"
                    self.strength += 9
                    self.agility += 2
                    self.endurance += 7
                    self.intelligence += 2
                    self.luck += 5
                    self.HP = 150
                    self.MP = 80

                if select == "2":
                    print("")

            elif selection not in "12":
                input("\nType in '1' or '2', please.\n")

    def class_creation(self):

        select = None
        while select != "1":
            class_selection = input("Select your class:\n 1. Warrior\n 2. Rogue\n 3. Mage\n >>> ")

            if class_selection == "1":
                select = input("Warriors are masters of close combat.\n"
                               "They start with a short sword and a leather armor.\n"
                               "Do you want to be a Warrior?\n\n"
                               " 1. Yes 2. No >>> ")

                if select == "1":
                    self.charclass = "Warrior"
                    self.HP += 30
                    self.strength += 3
                    self.endurance += 2
                    self.inventory = ["Shortsword", "Leather Armor", "Buckler"]
                    self.spells = ["Mighty Thrust", "Shield Slam", "Rush"]

                elif select == "2":
                    print("")

                elif select not in "12":
                    print("\nType in '1' or '2', please.\n")

            elif class_selection == "2":
                select = input("Rogues are agile and stealthy fighters.\n"
                               "They are attuned to shadows and can attack with both hands.\n"
                               "They start with a iron dagger and a robe.\n"
                               "Are you a Rogue?\n\n 1. Yes 2. No >>> ")

                if select == "1":
                    self.charclass = "Rogue"
                    self.HP += 15
                    self.MP += 15
                    self.agility += 3
                    self.luck += 2
                    self.inventory = ["Dagger", "Dark Hood", "Potion of Invisibility"]
                    self.spells = ["Chameleon", "Stab Attack", "Shadow Lance"]

                elif select == "2":
                    print("")

                elif select not in "12":
                    print("\nType in '1' or '2', please.\n")

            elif class_selection == "3":
                select = input("Mages are skilled at arcane arts.\n"
                               "They have impressive mana reserves and know some battle spells from the start.\n"
                               "Are you a Mage?\n\n"
                               "1. Yes 2. No >>> ")
                if select == "1":
                    self.charclass = "Mage"
                    self.MP += 50
                    self.intelligence += 4
                    self.agility += 1
                    self.inventory = ["Wooden Staff", "Book of Spells", "Wizard Hat"]
                    self.spells = ["Firebolt", "Minor Healing", "Immolate"]

                elif select == "2":
                    print("")

                elif select not in "12":
                    print("\nType in '1' or '2', please.\n")

            self.max_HP = self.HP

    def examine_self(self):
        print(f"\nYou are {self.name} the {self.race}, level {self.xl} {self.charclass}. "
              f"You have {self.strength} Str, {self.agility} Agi, {self.endurance} End, {self.intelligence} "
              f"Int and {self.luck} Luck.\n\nYou have {self.HP} HP and {self.MP} MP.\n")

        print(f"Your inventory: {self.inventory}")
        print(f"Known spells: {self.spells}\n")
        
    def heal(self):
        self.HP = self.max_HP


class Enemy:
    def __init__(self):
        self.type = enemy_list[randint(0, 4)]
        self.strength = 5
        self.agility = 5
        self.endurance = 5
        self.intelligence = 5
        self.luck = 5
        self.crit_modifier = (self.agility // 2) + (self.luck // 1.5) + randint(1, ((self.agility+self.luck) // 2))
        self.HP = 100
        self.xl = randint(1, 2)
        self.damage = (5 + self.strength + self.endurance // 2 + self.luck // 5)
        if self.xl == 2:
            self.strength += randint(1, 5)
            self.agility += randint(1, 5)
            self.endurance += randint(1, 5)
            self.intelligence += randint(1, 5)
            self.luck += randint(1, 5)
            self.HP += randint(30, 50)
        if self.type == "Orc":
            self.strength += 3
            self.agility -= 3
            self.HP += 10
            self.damage += 2
        elif self.type == "Goblin":
            self.strength -= 2
            self.endurance -= 2
            self.agility += 4
            self.HP -= 30
        elif self.type == "Thief":
            self.agility += 3
            self.strength -= 1
            self.endurance -= 2
            self.HP += 10
        elif self.type == "Scag":
            self.endurance += 2
            self.strength += 2
            self.luck -= 4
            self.HP += 15
            self.damage += 1
        elif self.type == "Gnoll":
            self.agility += 1
            self.strength += 1
            self.endurance += 1
            self.luck += 1
            self.intelligence += 1
            self.HP -= 25
            
    def examine(self):
        print(f"\nYou see a hostile {self.type}\n"
              f"It has {self.strength} Str, {self.agility} Agi,\n{self.endurance} End,"
              f" {self.intelligence} Int and {self.luck} Luck.\n"
              f"It can deal up to {int(self.damage + self.crit_modifier)} damage and has {self.HP} HP.\n")


def save():
    save_list = [
        str(h.name),
        str(h.race),
        str(h.charclass),
        str(h.xl),
        str(h.max_HP),
        str(h.HP),
        str(h.MP),
        str(h.strength),
        str(h.agility),
        str(h.endurance),
        str(h.intelligence),
        str(h.luck),
        str(h.crit_modifier),
        str(h.inventory),
        str(h.damage),
        str(h.spells),
        str(h.gold)
    ]

    file = open("save.txt", "w")
    for stat in save_list:
        file.write(stat + "\n")
    file.close()


def battle():

    e = Enemy()
    print(f"{h.name}, you enter the Arena. Hundreds of citizens are watching you.\n\n"
          f"Your opponent today is level {e.xl} {e.type}.\n")

    print(f"It has {e.strength} Str, {e.agility} Agi, {e.endurance} End, "
          f"{e.intelligence} Int and {e.luck} Luck.\n\n"
          f"It can deal up to {int(e.damage + e.crit_modifier)} damage and has {e.HP} HP.\n")

    print("")

    while e.HP and h.HP > 0:
        print("\nSelect a body part to attack:\n")
        attack_roll = input(" 1. Attack head\n 2. Attack chest\n 3. Attack hands\n 4. Attack legs\n>>> ")
        print("\nSelect a body part to defend:\n")
        defense_roll = input(" 1. Protect head\n 2. Protect chest\n 3. Protect hands\n 4. Protect legs\n>>> ")

        enemy_attack_roll = randint(1, 4)
        enemy_defense_roll = randint(1, 4)

        body_parts = {1: "head", 2: "chest", 3: "hands", 4: "legs"}

        while attack_roll in ["1", "2", "3", "4"]:
            break
        else:
            input("\nInvalid input. Please, try again.\n")
            continue

        while defense_roll in ["1", "2", "3", "4"]:
            break
        else:
            input("\nInvalid input. Please, try again.\n")
            continue

        if int(attack_roll) == enemy_defense_roll:
            print(f"\nYou attack {e.type}'s {body_parts[int(attack_roll)]}. It blocks.\n")

        elif int(attack_roll) != enemy_defense_roll:
            h_actual = h.damage + randint(1, int(h.crit_modifier)) +\
                           (randint(1, int(h.crit_modifier // 2)) if attack_roll == "1" else 0) + \
                           (randint(1, int(h.crit_modifier // 3)) if attack_roll == "2" else 0)
            e.HP -= h_actual
            print(f"\nYou hit {e.type}'s {body_parts[int(attack_roll)]} and deal {h_actual} damage. "
                  f"It now has {e.HP} HP")

        if enemy_attack_roll == int(defense_roll):

            print(f"\n{e.type} attacks your {body_parts[enemy_attack_roll]}. You block.\n")

        elif enemy_attack_roll != int(defense_roll):

            e_actual = e.damage + randint(1, int(e.crit_modifier)) +\
                           (randint(1, int(e.crit_modifier // 2)) if enemy_attack_roll == 1 else 0) + \
                           (randint(1, int(e.crit_modifier // 3)) if enemy_attack_roll == 2 else 0)
            h.HP -= e_actual

            print(f"{e.type} hits your {body_parts[enemy_attack_roll]} and deal {e_actual} damage. "
                  f"You now have {h.HP} HP")

        if e.HP <= 0:
            print(f"\nYou have defeated the {e.type}!\n")
            input("Press any key to continue...")
            break

        if h.HP <= 0:
            print("\nYOU ARE DEAD\n")
            input("Press any key to exit...")
            quit()

        if e.HP and h.HP <= 0:
            print("\nYOU ARE DEAD\n")
            input("Press any key to exit...")
            quit()


h = Hero()

#  main game loops

run = True
menu = True
play = False
shop = False

while run:
    while menu:
        print("1. NEW GAME")
        print("2. LOAD GAME")
        print("3. IN DEVELOPMENT")
        print("4. QUIT GAME")
        
        choice = input(">>> ")
        
        if choice == "1":
            h.greet()
            h.race_creation()
            h.class_creation()
            h.examine_self()
            print("\nPress any key to continue...\n")
            save()
            print("\nAutosaving...\n")
            menu = False
            play = True
        elif choice == "2":
            f = open("save.txt", "r")
            load_list = f.readlines()
            h.name = load_list[0][:-1]
            h.race = load_list[1][:-1]
            h.charclass = load_list[2][:-1]
            h.xl = int(load_list[3][:-1])
            h.max_HP = int(load_list[4][:-1])
            h.HP = int(load_list[5][:-1])
            h.MP = int(load_list[6][:-1])
            h.strength = int(load_list[7][:-1])
            h.agility = int(load_list[8][:-1])
            h.endurance = int(load_list[9][:-1])
            h.intelligence = int(load_list[10][:-1])
            h.luck = int(load_list[11][:-1])
            h.crit_modifier = float(load_list[12][:-1])
            h.inventory = load_list[13][:-1]
            h.damage = int(load_list[14][:-1])
            h.spells = load_list[15][:-1]
            h.gold = int(load_list[16][:-1])
            f.close()
            print(f"\nWelcome back, {h.name}!\n")
            menu = False
            play = True
        elif choice == "3":
            pass
        elif choice == "4":
            quit()
        
    while play:
        print("1. Visit the Arena")
        print("2. Visit a local Shop")
        print("3. Examine self")
        print("4. Save Game")
        print("5. Back to main Menu")
        choice = input(">>>> ")
        
        if choice == "1":
            battle()
            play = True
        elif choice == "2":
            shop = True
        elif choice == "3":
            h.examine_self()
        elif choice == "4":
            save()
            print("\nGame saved successfully.\nPress any key to continue...\n")
        elif choice == "5":
            print("\nReturning to main Menu.\nPress any key to continue...\n")
            play = False
            menu = True
        elif choice not in "12345":
            print("\nIncorrect input. Please, try again.\n")
            print("")
            
        if shop:
            print("\nWelcome to my humble shop!\n")
            print("1. Restore health --- 0 gold\n")
            print("2. Longsword --- 350 gold\n")
            print("3. Exit shop\n")

        shop_choice = input("")

        if shop_choice == "1":
            print("\nYour wounds are magically healed.\n")
            print(f"You feel much better, healed {h.max_HP - h.HP} points. You have {h.max_HP} HP now.\n")
            h.heal()
            shop = True
        elif shop_choice == "2":
            print("\nIn development.\n")
            print("")
            shop = True
        elif shop_choice == "3":
            shop = False
            play = True
        elif shop_choice not in "123":
            print("\nIncorrect input. Please, try again.\n")
            print("")
            shop = True
