import random
import tkinter as tk

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

def play_game(user_input):
    global user_wins, computer_wins
    
    random_number = random.randint(0, 2)  
    computer_pick = options[random_number]
    result = ""
    
    if user_input == computer_pick:
        result = "It's a tie!"
    elif (user_input == "rock" and computer_pick == "scissors") or \
         (user_input == "paper" and computer_pick == "rock") or \
         (user_input == "scissors" and computer_pick == "paper"):
        result = "You won!"
        user_wins += 1
    else:
        result = "You lost!"
        computer_wins += 1
    
    result_label.config(text=f"Computer picked: {computer_pick}\n{result}")
    score_label.config(text=f"You: {user_wins}  |  Computer: {computer_wins}")

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x500")
root.config(bg="#000000") 

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 24, "bold") , fg="#ffffff",  bg="#000000")
title_label.pack(pady=20)

rock_button = tk.Button(root, text="Rock", font=("Arial", 14), command=lambda: play_game("rock"),  fg="#ffffff",  bg="#000000")
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", font=("Arial", 14), command=lambda: play_game("paper"),  fg="#ffffff",  bg="#000000")
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", font=("Arial", 14), command=lambda: play_game("scissors"),  fg="#ffffff",  bg="#000000")
scissors_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 16), fg="#ffffff",  bg="#000000")
result_label.pack(pady=20)

score_label = tk.Label(root, text="You: 0  |  Computer: 0", font=("Arial", 16))
score_label.pack(pady=20)

root.mainloop()
