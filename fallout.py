skilltype = 0
skill = 0     
strength = 0
charisma = 0
intelligence = 0
luck = 0
SkillPoints = 15
SkillNum = 0
StartStart = 0
Mainstart = 0
SkillAmount = 0

def Start():
    StartMenu_a = True
    while StartMenu_a == True:
        print(f"\nSKILL POINTS: {SkillPoints}")
        print(f"-------- Skills ---------\n 1. Strength: {strength}\n 2. Charisma: {charisma}\n 3. Intelligence: {intelligence}\n 4. Luck: {luck}")
        StartStart = str(input("Would you like to add, remove, or confirm your skills? "))
        test = StartStart.lower()
        print(test)
        if test == "add":
            AddStart()
        elif StartStart == "remove":
            RemoveStart()
        elif StartStart == "confirm":
            if SkillPoints > 0:
                con = str(input("Are you sure you would like to continue?\nYou haven't used up all of your skill points \nType 'Confirm' Again to confirm your stats. Type anyhting else to go back. "))
                if con == "confirm":
                    Game()
                else:
                    Start()
            else:
                con = str(input("Are you sure you would like to continue?\nType 'Confirm' Again to confirm your stats. Type anyhting else to go back. "))
                if con == "confirm":
                    Game()
                else:
                    Start()
        StartMenu_a = False

def addskills(skill):
    global skilltype, StartMenu, SkillNum, SkillPoints, strength, charisma, intelligence, luck
    print(f"\nCURRENT POINTS: {SkillPoints}")
    AddPoints = int(input(f"How many points would you like to put into {skill}? "))
    if AddPoints > SkillPoints:
        print("Error: You do not have enough skill points!")
        Start()
    else:
        SkillPoints -= AddPoints
        if SkillNum == 1:
            strength += AddPoints
        elif SkillNum == 2:
            charisma += AddPoints
        elif SkillNum == 3:
            intelligence += AddPoints
        elif SkillNum == 4:
            luck += AddPoints
        print(f"Added {AddPoints} to {skill}")
        AddStart()
    
def AddStart():
    StartMenu = True
    global SkillNum
    while StartMenu == True:
        print(f"\nSKILL POINTS: {SkillPoints}")
        print(f"-------- Skills ---------\n 1. Strength: {strength}\n 2. Charisma: {charisma}\n 3. Intelligence: {intelligence}\n 4. Luck: {luck}\n 5. Finish")
        Mainstart = int(input("Choose which stat you would like to upgrade: \n"))
        if Mainstart != 5:
            if Mainstart == 1:
                SkillNum = 1
                skill = "Strength"
            elif Mainstart == 2:
                SkillNum = 2
                skill = "Charisma"
            elif Mainstart == 3:
                SkillNum = 3
                skill = "Intelligence"
            elif Mainstart == 4:
                SkillNum = 4
                skill = "Luck"
            addskills(skill)
        else:
            Start()
        StartMenu = False

def RemoveStart():
    StartMenu = True
    global SkillNum
    while StartMenu == True:
        print(f"\nSKILL POINTS: {SkillPoints}")
        print(f"-------- Skills ---------\n 1. Strength: {strength}\n 2. Charisma: {charisma}\n 3. Intelligence: {intelligence}\n 4. Luck: {luck}\n 5. Finish")
        Mainstart = int(input("Choose which stat you would like to reduce: \n"))
        if Mainstart != 5:
            if Mainstart == 1:
                SkillNum = 1
                skill = "Strength"
            elif Mainstart == 2:
                SkillNum = 2
                skill = "Charisma"
            elif Mainstart == 3:
                SkillNum = 3
                skill = "Intelligence"
            elif Mainstart == 4:
                SkillNum = 4
                skill = "Luck"
            removeskills(skill)
        else:
            Start()
        StartMenu = False

def removeskills(skill):
    global skilltype, SkillNum, SkillPoints, strength, charisma, intelligence, luck
    print(f"\nCURRENT POINTS: {SkillPoints}")
    ReducePoints = int(input(f"How many points would you like to remove from {skill}? "))
    print(strength)
    if SkillNum == 1:
        SkillAmount = strength
        print(SkillAmount)
        print(strength)
    elif SkillNum == 2:
        SkillAmount = charisma
    elif SkillNum == 3:
        SkillAmount = intelligence
    elif SkillNum == 4:
        SkillAmount = luck
    print(SkillAmount)
    if ReducePoints > SkillAmount:
        print("Error: You do not have enough skill points!")
        RemoveStart()
    else:
        SkillPoints += ReducePoints
        if SkillNum == 1:
            strength -= ReducePoints
        elif SkillNum == 2:
            charisma -= ReducePoints
        elif SkillNum == 3:
            intelligence -= ReducePoints
        elif SkillNum == 4:
            luck -= ReducePoints
        print(f"Removed {ReducePoints} from {skill}")
        RemoveStart()

def Game():
    print("\n\n\n\n\n\n\n\n\n\nStarting game...")
    print("The year is 2280. Back in the year 2077, Nuclear bombs destroyed the Earth.\n\nYou were born and raised in an underground bunker, with many other families after the bombs fell.\nBut now, your vault is at risk as the water chip no longer works.\n\nYou have been selected to enter the wasteland of the Captiol City to try and find a water chip to bring back to the vault.\nThe whole vault is counting on you...")
    Choice = int(input("Do you exit the vault and try to find a water chip?\n1. Yes\n2. No"))
    if Choice == 1:
        print("You exit the Vault")
    elif Choioce == 2:
        print("You were forced out of your vault into the wasteland.")
Start()