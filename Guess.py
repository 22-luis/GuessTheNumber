import random
import pygame
from pygame_textinput import TextInput

pygame.init()

run = True
guess = False
answer = random.randint(1,100)

#Colors
background = (173, 216, 230)
input = (255, 255, 255) # Blanco
button = (65, 105, 225)
text_C = (0, 0, 0)
right = (46, 204, 113)
wrong = (231, 76, 60)

def circle(surface, color, center, radius):
    pygame.draw.circle(surface, color, center, radius)

# Function to create the rounded button
def rounded_rect(surface, color, rect, radius):
    x, y, width, height = rect
    circle(surface, color, (x + radius, y + radius), radius)
    circle(surface, color, (x + width - radius - 1, y + radius), radius)
    circle(surface, color, (x + radius, y + height - radius - 1), radius)
    circle(surface, color, (x + width - radius - 1, y + height - radius - 1), radius)
    pygame.draw.rect(surface, color, (x + radius, y, width - 2 * radius, height))
    pygame.draw.rect(surface, color, (x, y + radius, width, height - 2 * radius))

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("Guess The Number")

#create the title
title = pygame.font.Font(None, 48)
title_text = title.render("Guess The Number", True, text_C)
title_rect = title_text.get_rect(center=(screen_width//2, 50))

number = TextInput("Arial", 24, text_C, text_C, 3)

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        number.update(event)
            
    screen.fill(background)
    
    screen.blit(title_text,title_rect)
    
    #Create the answer box
    number_rect = pygame.Rect(100, 100, 100, 50)
    rounded_rect(screen, button, number_rect, 15)
    number.set_rect(number_rect)
    
    numberGuess = number.get_text() 
    
    #Create check button
    btn = pygame.Rect(100, 100, 100, 50)
    rounded_rect(screen, button, btn, 15)
    font = pygame.font.Font(None, 24)
    text = font.render("Check", True, text_C)
    screen.blit(text, (122,117))
    
    pygame.display.flip()

""" 


def hint(number):
    global guess
    if(number < answer): print("Higher")
    elif(number > answer): print("Lower")
    elif(number == answer): 
        print(f"That's correct the number is {number}")
        guess = True
    


while not guess:
    number = int(input("Type your number: "))
    hint(number)
 """


    
