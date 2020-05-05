#python program to illustrate a loop with condition at the bottom
# roll a dice untill user chooses to exit

# import random module
import random

while True:
    input("press enter to roll the dice ")

    # get a nmumber between 1 and 6
    num = random.randint(1,6)
    print("You got",num)
    print('Roll again ?(y/n)')
    option =input();
    #condition
    if option == "n":
        break
