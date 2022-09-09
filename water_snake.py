# Snake water gun
# Snake Water Gun Game in Python
# The snake drinks the water, the gun shoots the snake, and gun has no effect on water.

import random
lis=["s" , "w" , "g"]

chance=10
num_of_chance=0
human_point=08
system_point=0

print("\t\t\tSnake Water Gun Game")
print('''RULE: \nSnake vs. Water: Snake drinks the water hence wins.
\nWater vs. Gun: The gun will drown in water, hence a point for water
\nGun vs. Snake: Gun will kill the snake and win''')
print("Give command as \ns for Snake \nw for Water \ng for Gun:")

# making the game in while
while num_of_chance<chance:
    human=input("Enter Your choice: ")
    system = random.choice(lis)

    if human == system:
        human_point+=1
        system_point+=1
        print(f"Your choice is {human} and system choice is {system} \nso Tie")

    # if user enter s
    elif human == "s" and system == "w":
        human_point+=1
        print(f"Your choice is {human} and system choice is {system} \nso Human gets one point.")

    elif human == "s" and system == "g":
        system_point+=1
        print(f"Your choice is {human} and system choice is {system} \nso system gets one point.")

    # if user enter w
    elif human == "w" and system == "s":
        system_point+=1
        print(f"Your choice is {human} and system choice is {system} \nso system gets one point.")

    elif human == "w" and system == "g":
        human_point+=1
        print(f"Your choice is {human} and system choice is {system} \nso Human gets one point.")

    # if user enter g
    elif human == "g" and system == "s":
        human_point+=1
        print(f"Your choice is {human} and system choice is {system} \nso Human gets one point.")

    elif human == "g" and system == "w":
        system_point+=1
        print(f"Your choice is {human} and system choice is {system} \nso system gets one point.")

    else:
        print("Wrong input")

    num_of_chance += 1
    print(f"You left {chance - num_of_chance} out of {chance}")
    print(f"Your score {human_point} and system score {system_point}")

print("Game over")

if human_point<system_point:
    print(f"system win game led by {system_point} points")

elif human_point>system_point:
    print(f"Human win game led by {human_point} points")

else:
    print(f"Game DRAW both gets {human_point} points")