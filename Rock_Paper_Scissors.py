import tkinter as tk
from tkinter import messagebox
import random, os
from matplotlib import pyplot as plt

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
    colors = ["lightgreen", "yellow", "white"]
    def step(i=0):
        if i < len(colors):
            result_label.config(fg=colors[i])
            root.after(150, step, i + 1)
    step()

# --- Menu & Extra Features ---
def show_rules():
    messagebox.showinfo(
        "Game Rules",
        "🪨 Rock beats Scissors\n📜 Paper beats Rock\n✂️ Scissors beats Paper\n\n"
        "Try to beat the computer! The game keeps score automatically."
    )

def show_summary():
    total = sum(scores)
    if total == 0:
        messagebox.showinfo("Summary", "No games played yet!")
        return
    win_rate = round((scores[0] / total) * 100, 1)
    msg = (
        f"📊 Match Summary\n\n"
        f"Rounds Played: {total}\n"
        f"Wins: {scores[0]}\n"
        f"Losses: {scores[1]}\n"
        f"Ties: {scores[2]}\n\n"
        f"Win Rate: {win_rate}%"
    )
    messagebox.showinfo("Game Over", msg)

def show_chart():
    total = sum(scores)
    if total == 0:
        messagebox.showwarning("Stats", "Play a few rounds first!")
        return
    labels = ["Wins", "Losses", "Ties"]
    plt.pie(scores, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Your RPS Statistics")
    plt.show()

def back_to_menu():
    main_frame.pack_forget()
    menu_frame.pack(pady=50)

def start_game():
    menu_frame.pack_forget()
    main_frame.pack(pady=10)

# --- GUI Setup ---
root = tk.Tk()
root.title("Rock, Paper, Scissors ✊✋✌️")
root.geometry("430x500")
root.config(bg="#222")

# Load saved score
scores = load_score()
rounds = 0

# --- MENU FRAME ---
menu_frame = tk.Frame(root, bg="#222")
menu_title = tk.Label(
    menu_frame, text="🎮 Rock, Paper, Scissors", 
    font=("Helvetica", 22, "bold"), bg="#222", fg="white"
)
menu_title.pack(pady=20)

tk.Button(menu_frame, text="▶️ Start Game", font=("Helvetica", 14), bg="#4CAF50", fg="white", command=start_game).pack(pady=10)
tk.Button(menu_frame, text="📖 Rules", font=("Helvetica", 14), bg="#555", fg="white", command=show_rules).pack(pady=10)
tk.Button(menu_frame, text="📊 View Stats", font=("Helvetica", 14), bg="#444", fg="white", command=show_chart).pack(pady=10)
tk.Button(menu_frame, text="❌ Exit", font=("Helvetica", 14), bg="#aa3333", fg="white", command=root.destroy).pack(pady=20)

menu_frame.pack(pady=50)

# --- MAIN GAME FRAME ---
main_frame = tk.Frame(root, bg="#222")

title_label = tk.Label(main_frame, text="Rock, Paper, Scissors", font=("Helvetica", 20, "bold"), bg="#222", fg="white")
title_label.pack(pady=10)

button_frame = tk.Frame(main_frame, bg="#222")
button_frame.pack(pady=10)

def create_button(text):
    return tk.Button(button_frame, text=text, font=("Helvetica", 14), width=10,
                     bg="#444", fg="white", activebackground="#666",
                     command=lambda: play(text))

rock_button = create_button("Rock")
paper_button = create_button("Paper")
scissors_button = create_button("Scissors")

rock_button.grid(row=0, column=0, padx=10)
paper_button.grid(row=0, column=1, padx=10)
scissors_button.grid(row=0, column=2, padx=10)

result_label = tk.Label(main_frame, text="Make your move!", font=("Helvetica", 14, "bold"), bg="#222", fg="white")
result_label.pack(pady=25)

score_label = tk.Label(main_frame, text=f"🏆 Wins: {scores[0]}   💀 Losses: {scores[1]}   🤝 Ties: {scores[2]}",
                       font=("Helvetica", 12), bg="#222", fg="lightblue")
score_label.pack(pady=5)

round_label = tk.Label(main_frame, text=f"Round: {rounds}", font=("Helvetica", 12), bg="#222", fg="lightgray")
round_label.pack(pady=5)

control_frame = tk.Frame(main_frame, bg="#222")
control_frame.pack(pady=20)

reset_button = tk.Button(control_frame, text="🔄 Reset", font=("Helvetica", 12), bg="#555", fg="white", command=reset_game)
reset_button.grid(row=0, column=0, padx=10)

summary_button = tk.Button(control_frame, text="📋 Summary", font=("Helvetica", 12), bg="#444", fg="white", command=show_summary)
summary_button.grid(row=0, column=1, padx=10)

menu_button = tk.Button(control_frame, text="🏠 Menu", font=("Helvetica", 12), bg="#333", fg="white", command=back_to_menu)
menu_button.grid(row=0, column=2, padx=10)

root.mainloop()

# 🎮 Game Description & Added Features:
# This is an advanced version of the Rock, Paper, Scissors game built using Python's tkinter library.
# It combines core gameplay with several modern UI and UX enhancements.
#
# ✅ Features Added So Far:
# 1. Score Tracking – Keeps count of player wins, losses, and ties.
# 2. Round Counter – Displays the number of rounds played in the current session.
# 3. Persistent Score Saving – Stores scores in a text file so they remain after closing the game.
# 4. Reset Functionality – Allows players to reset all scores and start fresh.
# 5. Animated Result Text – Adds simple color animation for visual feedback.
# 6. Main Menu Screen – Includes Start, Rules, Stats, and Exit options for a complete app feel.
# 7. Rules / Instructions Popup – Shows how to play and what beats what.
# 8. Match Summary – Displays total games played, win rate, and detailed results.
# 9. Statistics Chart – Generates a pie chart (using matplotlib) showing wins/losses/ties.
# 10. Menu Navigation – Lets players go back to the main menu anytime.
#
# 💡 Future Enhancement Ideas:
# - Add sound effects and background music.
# - Use emoji or image buttons for Rock, Paper, and Scissors.
# - Include a "Best of 5" or "Timed Mode" challenge option.
# - Add achievements, player names, and streak tracking.
# - Implement gesture or voice input for an interactive experience.
#
# 🧠 Created for learning and fun — demonstrates GUI design, state management, and persistent data in Python!
