import tkinter as tk
from tkinter import messagebox
import random

# --- Logic Section ---

def play(user_choice):
    """Handles the game logic when a button is pressed."""
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)
    
    # Display choices
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    comp_choice_label.config(text=f"Computer Choice: {computer_choice}")
    
    # Determine Winner
    if user_choice == computer_choice:
        result = "It's a Tie!"
        color = "gray"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You Win! 🎉"
        color = "green"
    else:
        result = "Computer Wins! 🤖"
        color = "red"
    
    result_label.config(text=result, fg=color)

def reset_game():
    """Resets the labels to their starting state."""
    user_choice_label.config(text="Your Choice: ")
    comp_choice_label.config(text="Computer Choice: ")
    result_label.config(text="Choose your move!", fg="black")

# --- GUI Section ---

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x450")

# Title
title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), pady=20)
title.pack()

# Display Choices
user_choice_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12))
user_choice_label.pack()

comp_choice_label = tk.Label(root, text="Computer Choice: ", font=("Arial", 12))
comp_choice_label.pack()

# Display Result
result_label = tk.Label(root, text="Choose your move!", font=("Arial", 16, "bold"), pady=20)
result_label.pack()

# Buttons Frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

rock_btn = tk.Button(btn_frame, text="Rock", width=10, bg="#ff9999", 
                     command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(btn_frame, text="Paper", width=10, bg="#ffff99", 
                      command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(btn_frame, text="Scissors", width=10, bg="#99ff99", 
                         command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

# Reset Button
reset_btn = tk.Button(root, text="Reset Game", command=reset_game, bg="lightgrey")
reset_btn.pack(pady=10)

root.mainloop()