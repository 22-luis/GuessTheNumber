import random
import tkinter as tk

from tkinter.messagebox import showinfo

answer = random.randint(1,100)
guess = False

# function to get a new number
def new():
    global answer, guess
    answer = random.randint(1,100)
    guess = False


def hint(number):
    global guess
    if(number < answer): showinfo(title='Hint', message = "Higher")
    elif(number > answer): showinfo(title='Hint', message = "Lower")
    elif(number == answer): 
        showinfo(title='Answer', message = f"That's correct the number is {number}")
        guess = True
        
# Check if the number is the correct
def check():
    global guess
    if not guess:
        try:
            number = int(input.get())
            hint(number)
        except ValueError:
            showinfo(title='Invalid value', message = "Integers Only")

root = tk.Tk()
root.title('Guess The Number')
root.configure(bg="#AED6F1")

width = 400
height = 400

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - width / 2)
center_y = int(screen_height/2 - height / 2)

root.geometry(f'{width}x{height}+{center_x}+{center_y}')
root.resizable(False, False)

# input 
number = tk.IntVar()
input = tk.Entry(root, font=("Arial", 24))
input.pack(ipadx=4, ipady=20, expand=True )

# check answer button
check = tk.Button(root, text="Check", command=check, bg="#2E86C1", fg="white")
check.pack(ipadx=55, ipady=25, expand=True, side=tk.LEFT, pady = 35)

# New number
new_n = tk.Button(root, text="Get a new number", command=new, bg="#2E86C1", fg="white")
new_n.pack(ipadx=25, ipady=25, expand=True, side=tk.RIGHT, pady = 35)


root.mainloop()


    
