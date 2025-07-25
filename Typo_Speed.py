import tkinter as tk    # tkinter is used to create the GUI (windows, buttons, text box, etc.)
import time             # time helps track typing time for calculating WPM (Words Per Minute)

# 👨‍🏫 Paragraph to be typed
paragraph = "Practice makes perfect, especially when it comes to typing. Focus on each word and avoid rushing to reduce mistakes. With consistent effort, your fingers will move faster and more accurately. Keep practicing daily to see steady improvement in both speed and accuracy."

# 🔄 Global Variables
start_time = 0
time_left = 60  # seconds
timer_running = False

# ⏱ Function: Start typing and start timer
def start_typing():
    global start_time, time_left, timer_running
    entry.config(state="normal")      # Textbox enable
    entry.delete("1.0", tk.END)       # Clear old text
    result_label.config(text="")      # Clear result
    time_left = 60                    # Reset timer
    start_time = time.time()          # Store start time
    timer_running = True
    update_timer()                    # Start updating timer

# ⌛ Function: Update timer every second
def update_timer():
    global time_left, timer_running
    if timer_running and time_left > 0:
        timer_label.config(text=f"⏳ Time Left: {time_left}s")
        time_left -= 1
        window.after(1000, update_timer)  # Call again after 1 sec
    elif timer_running:
        timer_label.config(text="⏰ Time's up!")
        check_results()
        entry.config(state="disabled")
        timer_running = False

# 📊 Function: Calculate WPM and Accuracy
def check_results():
    end_time = time.time()
    typed_text = entry.get("1.0", tk.END).strip()
    time_taken = max(end_time - start_time, 1)  # To avoid division by 0

    # 💬 Word Count
    typed_words = typed_text.split()
    total_words = len(typed_words)

    # 📏 WPM = Words per minute
    wpm = round((total_words / time_taken) * 60)

    # 🎯 Accuracy = Correct words match with paragraph
    original_words = paragraph.split()
    correct = sum(1 for i in range(min(len(typed_words), len(original_words)))
                  if typed_words[i] == original_words[i])
    accuracy = round((correct / len(original_words)) * 100)

    result_label.config(text=f"🧠 Speed: {wpm} WPM   🎯 Accuracy: {accuracy}%")

# 🖼 GUI Setup
window = tk.Tk()
window.title("Typing Speed Test")
window.geometry("900x500")
window.config(bg="white")

# Title
tk.Label(window, text="Typing Speed Test", font=("Arial", 24, "bold"), bg="lightyellow").pack(pady=10)

# Show paragraph
tk.Label(window, text=paragraph, font=("Arial", 14), wraplength=800, bg="white").pack(pady=10)

# Entry box for typing
entry = tk.Text(window, height=6, width=90, font=("Arial", 13), state="disabled")
entry.pack(pady=10)

# Timer
timer_label = tk.Label(window, text="⏳ Time Left: 60s", font=("Arial", 14), fg="red", bg="white")
timer_label.pack(pady=5)

# Result Label
result_label = tk.Label(window, text="", font=("Arial", 16), fg="green", bg="white")
result_label.pack(pady=10)

# Buttons
btn_frame = tk.Frame(window, bg="white")
btn_frame.pack()

tk.Button(btn_frame, text="▶ Start", font=("Arial", 12), bg="lightblue", command=start_typing).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="✔ Submit", font=("Arial", 12), bg="lightgreen", command=lambda:[check_results(), entry.config(state="disabled")]).grid(row=0, column=1, padx=10)

window.mainloop()
