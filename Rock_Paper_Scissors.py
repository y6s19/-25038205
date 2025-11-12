import tkinter as tk
from tkinter import messagebox
import random

# --- Game Logic ---
def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    result = ""

    if choice == computer_choice:
        result = "It's a tie! 🤝"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "You win! 🎉"
    else:
        result = "You lose! 💀"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Rock, Paper, Scissors ✊✋✌️")
root.geometry("400x400")
root.config(bg="#222")

title_label = tk.Label(
    root, text="Rock, Paper, Scissors", 
    font=("Helvetica", 18, "bold"), 
    bg="#222", fg="white"
)
title_label.pack(pady=20)

# Frame for buttons
button_frame = tk.Frame(root, bg="#222")
button_frame.pack(pady=20)

def create_button(text):
    return tk.Button(
        button_frame, text=text, font=("Helvetica", 14), width=10,
        bg="#444", fg="white", activebackground="#666",
        command=lambda: play(text)
    )

rock_button = create_button("Rock")
paper_button = create_button("Paper")
scissors_button = create_button("Scissors")

rock_button.grid(row=0, column=0, padx=10)
paper_button.grid(row=0, column=1, padx=10)
scissors_button.grid(row=0, column=2, padx=10)

# Result Label
result_label = tk.Label(
    root, text="", font=("Helvetica", 14), 
    bg="#222", fg="lightgreen"
)
result_label.pack(pady=40)

# Quit Button
quit_button = tk.Button(
    root, text="Quit", font=("Helvetica", 12),
    bg="#aa3333", fg="white", command=root.destroy
)
quit_button.pack(pady=10)

root.mainloop()
