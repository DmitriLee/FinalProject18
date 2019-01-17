print ("Welcome to the Survival Game! We're going to give you 100 health points, try to go through the whole game before you run out.")

hp=100

x = input("Do you want to play? (yes or no)")
if x=="yes":
    print ("Great!")
else:
    print ("oh, ok. Bye then.")
    end

print("You are flying in a plane across the country to California. Private Flight of course. Suddenly the plane starts to fall. You have two options: Brace for impact or find a parachute and jump.")

plane = input("Which one? (B or J)")

if plane =="B":
  print("The pilot lands on some trees which lessens the damage, but it is still a plane crash. The pilot died. RIP the pilot. Lose 30 health points. (And give a moment of silence.)")
  hp -= 30
else:
  jump = input("You jumped out late and won't be slowed down completely. You see a group of trees and a body of water. Which do you aim to land on? (T or W)")
  if jump=="T":
    print ("Good choice. Landing on water is dangerous. You land on a tree and hit a few branches. Lose 20 health points.")
    hp -= 20
  else:
    print ("Wrong choice. Water is worse to land on than concrete. You also need to swim to shore. Lose 40 health points.")
    hp -= 40

print(hp)

print ("The woods are not a place you are familiar with. Are you leaving for a better place to find shelter or stay where you are?")
place = input("(L or S)")

if place=="L":
  print("You get lost in the woods and now can't even find where you started from. Not having water you are dazed and confused. You have to settle for a poor shelter. Lose 11 health points")
  hp -= 11
else:
  print ("You are able to save energy but the shelter is not good. Lose 5 health points for the bad rest.")
  hp -= 5

print(hp)

print("The next morning, you wake up. You need to go find drinking water before you dehydrate. Do you go left or right?")

water = input("(L or R)")

if water=="L":
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

