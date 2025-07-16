from random import *
print("***** welcome to rock, paper, scissors! *****")
while True:
    player=input("enter your choise (rock, paper, scissors) \n")
    select=["rock","paper","scissors"]
    computer=choice(select)
    print("player choose =",player)
    print("computer choose =",computer)
    #if(player!="rock"or"scissors"or"paper"):
    #   print("invalid choise\n")
    #   break
    if (player==computer):
        print("tie ")
        print("you both selected =",player)
    elif(player=="rock"):
        if(computer=="paper"):
            print("computer wins\n")
        else:
            print("you win\n")
    elif(player=="paper"):
            if(computer=="scissors"):
                print("computer wins\n")
            else:
                print("you win\n") 
    elif(player=="scissors"):
            if(computer=="rock"):
                print("computer win\n")
            else:
                print("you win\n")
    
    repeat=input("play again ? (yes/no)\n")
    if repeat.lower()!="yes":
      print("*** thank you for playing ***\n")
      break