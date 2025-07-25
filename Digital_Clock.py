# 📦 Import necessary modules
import tkinter as tk           # For GUI
from time import strftime      # For getting system time in formatted string

# 🖼 Create the main window
root = tk.Tk()
root.title("Digital Clock")    # Title of the window

# ⏰ Function to update the time every second
def time():
    # Format: Hour:Minute:Second AM/PM and Date
    string = strftime('%H:%M:%S %p\n%D')  # %p = AM/PM, %D = MM/DD/YY
    label.config(text=string)            # Update label text
    label.after(1000, time)              # Call this function again after 1000ms (1 second)

# 🏷 Create and place a label for displaying time
label = tk.Label(root, font=('calibri', 50, 'bold'), background='yellow', foreground='black')
label.pack(anchor='center')  # Center align the label

# ▶ Start the clock
time()

# 🌀 Start the Tkinter event loop
root.mainloop()
