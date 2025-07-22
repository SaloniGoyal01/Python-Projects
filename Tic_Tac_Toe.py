import tkinter as tk
from tkinter import messagebox

# Function to check if a player has won
def check_winner():
    global winner
    # All winning combinations
    winning_combos = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]
    
    for combo in winning_combos:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            # Highlight the winning combination
            for idx in combo:
                buttons[idx].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            return

# Function called when a button is clicked
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()

# Function to switch the player
def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

# Setup the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create 9 buttons for the 3x3 grid
buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Track current player and winner status
current_player = "X"
winner = False

# Label to show which player's turn it is
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Start the GUI loop
root.mainloop()
