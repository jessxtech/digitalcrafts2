class GoodPlayer:
    def __init__(self, name, health, attack, weapon, points):
        self.name = name
        self.health = health
        self.attack = attack
        self.weapon = weapon
        self. points = points

class Villian:
    def __init__(self, name, health, attack, weapon, points):
        self.name = name
        self.health = health
        self.attack = attack
        self.weapon = weapon
        self.points = points

playerChoice = ""
while playerChoice != "q":
    
    playerChoice = input("""
What would you like to do?\n
Press 1 choose hero\n
Press 2 to name hero\n
Press 3 to check life points\n
Press 4 to check health\n
Press 5 to attack\n
Press q to quit game.
     """)

    if playerChoice == "1":
        heroType = input("What kind of hero are you?")

    if playerChoice == "2":
        heroName = input("What do you want to name your player?")
        print("Your players name is " + heroName)

    if playerChoice == "3":
        print("Your life points is ..")

    if playerChoice == "4":
        print("Your health is ..")

    if playerChoice == "5":
        heroAttack = input("What attack whout you like to use?")
        print(heroAttack + " has been used")




    