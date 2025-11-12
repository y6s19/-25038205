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
import tkinter as tk
from tkinter import messagebox
import random, os

SCORE_FILE = "rps_score.txt"

# --- Load & Save Scores ---
def load_score():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            data = f.read().strip().split(",")
            if len(data) == 3:
                return list(map(int, data))
    return [0, 0, 0]  # wins, losses, ties

def save_score():
    with open(SCORE_FILE, "w") as f:
        f.write(f"{scores[0]},{scores[1]},{scores[2]}")

# --- Game Logic ---
def play(choice):
    global rounds
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    result = ""

    if choice == computer_choice:
        result = "It's a tie! 🤝"
        scores[2] += 1
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "You win! 🎉"
        scores[0] += 1
    else:
        result = "You lose! 💀"
        scores[1] += 1

    rounds += 1
    update_labels(computer_choice, result)
    save_score()
    animate_result()

def update_labels(comp_choice, result):
    result_label.config(text=f"Computer chose: {comp_choice}\n{result}")
    score_label.config(
        text=f"🏆 Wins: {scores[0]}   💀 Losses: {scores[1]}   🤝 Ties: {scores[2]}"
    )
    round_label.config(text=f"Round: {rounds}")

def reset_game():
    global scores, rounds
    if messagebox.askyesno("Reset Game", "Are you sure you want to reset your score?"):
        scores = [0, 0, 0]
        rounds = 0
        save_score()
        update_labels("—", "Game reset! 🔄")

def animate_result():
    # Flash text color animation for 3 steps
    colors = ["lightgreen", "yellow", "white"]
    def step(i=0):
        if i < len(colors):
            result_label.config(fg=colors[i])
            root.after(150, step, i + 1)
    step()

# --- GUI Setup ---
root = tk.Tk()
root.title("Rock, Paper, Scissors ✊✋✌️")
root.geometry("420x480")
root.config(bg="#222")

title_label = tk.Label(
    root, text="Rock, Paper, Scissors", 
    font=("Helvetica", 20, "bold"), 
    bg="#222", fg="white"
)
title_label.pack(pady=20)

# Load saved score
scores = load_score()
rounds = 0

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
    root, text="Make your move!", font=("Helvetica", 14, "bold"), 
    bg="#222", fg="white"
)
result_label.pack(pady=30)

# Score + Round Labels
score_label = tk.Label(
    root, text=f"🏆 Wins: {scores[0]}   💀 Losses: {scores[1]}   🤝 Ties: {scores[2]}",
    font=("Helvetica", 12), bg="#222", fg="lightblue"
)
score_label.pack(pady=5)

round_label = tk.Label(
    root, text=f"Round: {rounds}", font=("Helvetica", 12),
    bg="#222", fg="lightgray"
)
round_label.pack(pady=5)

# Control Buttons
control_frame = tk.Frame(root, bg="#222")
control_frame.pack(pady=30)

reset_button = tk.Button(
    control_frame, text="🔄 Reset", font=("Helvetica", 12),
    bg="#555", fg="white", command=reset_game
)
reset_button.grid(row=0, column=0, padx=20)

quit_button = tk.Button(
    control_frame, text="❌ Quit", font=("Helvetica", 12),
    bg="#aa3333", fg="white", command=root.destroy
)
quit_button.grid(row=0, column=1, padx=20)

root.mainloop()
