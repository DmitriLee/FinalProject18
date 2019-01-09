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
  print("The pilot lands on some trees which lessens the damage, but it is still a plane crash. The pilot died. RIP the pilot. Lose 20 health points. (And give a moment of silence.")
  hp -= 20
else:
  jump = input("You jumped out late and won't be slowed down completely. You see a group of trees and a body of water. Which do you aim to land on? (T or W)")
  if jump=="T":
    print ("Good choice. Landing on water is dangerous. You land on a tree and hit a few branches. Lose 10 health points.")
    hp -= 10 
  else: 
    print ("Wrong choice. Water is worse to land on than concrete. Lose 20 health points.")
    hp -= 20

print(hp)

print("You now are lost in the forest. ")