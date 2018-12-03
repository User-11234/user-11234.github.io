import random

gameLose = False
lives = 5
print ("A number has been selected between one and one-hundred.")
x = random.randint(1,100)

while (gameLose == False):

  ans = int(input("What is your guess? "))

  if ans > (x):
    print ("This number is too high!")

  if ans < (x):
    print ("This number is too low...")
  
  if ans == (x):
    print ("You win!")
    gameLose = True
  
  if (lives == 0):
    print ("You lose!")
    gameLose = True

  if (ans == "ValueError"): 
    print ("Please input a number!")

  if (ans > 100) or (ans < 1) :
    print ("This is not within the range.")

  lives = (lives - 1)
  
input()