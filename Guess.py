import random

guess = False

def hint(number):
    global guess
    if(number < answer): print("Higher")
    elif(number > answer): print("Lower")
    elif(number == answer): 
        print(f"That's correct the number is {number}")
        guess = True
    

print("Guess the number")

answer = random.randint(1,100)

while not guess:
    number = int(input("Type your number: "))
    hint(number)



    
