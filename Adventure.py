import sys

print ("Welcome to the Survival Game! We're going to give you 100 health points, try to go through the whole game before you run out.")

hp=100


x = input("Do you want to play? (yes or no)")
if x=="yes":
    print ("Great!")
else:
    print ("You don't have a choice. Lets play!")

print("You are flying in a plane across the country to California. Private Flight of course. Suddenly the plane starts to fall. You have two options: Brace for impact or find a parachute and jump.")

plane = input("Which one? (B or J)").lower()

if plane =="b":
    print("The pilot lands on some trees which lessens the damage, but it is still a plane crash. The pilot died. RIP the pilot. Lose 30 health points. (And give a moment of silence.)")
    hp -= 30
else:
    jump = input("You jumped out late and won't be slowed down completely. You see a group of trees and a body of water. Which do you aim to land on? (T or W)").lower()
    if jump=="t":
        print ("Good choice. Landing on water is dangerous. You land on a tree and hit a few branches. Lose 20 health points.")
        hp -= 20
    else:
        print ("Wrong choice. Water is worse to land on than concrete. You also need to swim to shore. Lose 50 health points.")
        hp -= 50

print(hp)

print ("The woods are not a place you are familiar with. Are you leaving for a better place to find shelter or stay where you are?")
place = input("(L(leave) or S(shelter))").lower()

if place=="l":
    print("You get lost in the woods and now can't even find where you started from. Not having water you are dazed and confused. You have to settle for a poor shelter. Lose 10 health points")
    hp -= 10
else:
    print ("You are able to save energy but the shelter is not good. Lose 10 health points for the bad rest.")
    hp -= 10

print(hp)

print("Right before you go to sleep you hear rustling behind you. It's an animal, but you don't know what size. Do you try to make yourself look big and intimidating, or do you run away?")
animal = input("(B or R)").lower()
if animal== "b":
    print("Good thing it was only a small animal. (Maybe a raccoon) You can now go back to bed.")
else:
    print("You get away from the animal but now are tired and need to find a new shelter. Lose 5 health points.")

print(hp)

print("The next morning, you wake up. You need to go find drinking water before you dehydrate. You think you hear something to the left. Which do you go left or right?")

water = input("(L or R)").lower()

if water=="l":
    print("You find a small stream. Water found! Plus 5 health points.")
    hp += 5
else:
    print("You can't find any running water. Do you risk drinking stagnant water?")
    stag = input("(yes or no)")
    if stag== "yes":
        print("You have died dysentary. Lose 100 health points")
        hp -= 100
    else:
        print("You didn't drink any water yet. Lose 10 health points.")
        hp -= 10
        print(hp)
        print("Do you want to turn around or keep moving forward?")
        way=input("(T or F)").lower()
        if way=="t":
            print("It takes more energy but you find water.")
        else:
            print("Still you have found no water. Lose 15 health points.")
            hp -= 15
            print(hp)
            print("Now do you turn around or continue your subborn march forward?")
            way2=input("(T or F)").lower()
            if way2=="t":
                print("Good. Now you turn around and find water.")
            else:
                print("Wow... you're still going huh? Well we're gonna take away 20 health points and make you turn around.")
                hp -= 20

print(hp)

if hp<=0:
    print("Wasted")
    sys.exit()

print("Now you need to find food. Do you want to use more energy to risk getting high calorie meat, or do you want to to scavage for low calorie plants.")
food=input("(M or P)").lower()
if food=="m":
    if hp>= 30:
        print("You are able to track down an animal and get food. Gain 5 health points")
        hp += 5
    else:
        print("You don't have the energy to hunt down an animal. lose 15 health points for not eating.")
        hp-=15
else:
    print("The calories you gain is equal to the ones you waste scavenging")

if hp<=0:
    print("Wasted")
    sys.exit()

print("You now must signal someone to get noticed and rescued. Do you use smoke signals for more energy or just wave some branches in the air.")
signal=input("(S or B)")
if signal=="S":
    print("It takes 10 health points to get noticed with the fire, but you are found.")
    hp-=10
    if hp>0:
        print("You won and survived!")
    else:
        print("Wasted")
        sys.exit()
else:
    print("You are not seen (or maybe you are but they thought the branches moving were wind) and took health points to get the branches. You know spend the health points to create a smoke signal.")
    hp-=15
    if hp>0:
        print("You won and survived!")
    else:
        print("Wasted")
        sys.exit()



