import tkinter as tk
import random

# 🎯 List of motivational quotes
quotes = [
    "Believe in yourself and all that you are.",
    "Push yourself, because no one else is going to do it for you.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Dream it. Wish it. Do it.",
    "Don't watch the clock; do what it does. Keep going.",
    "Success is not for the lazy.",
    "Little things make big days.",
    "It’s going to be hard, but hard does not mean impossible.",
    "The key to success is to focus on goals, not obstacles.",
    "Start where you are. Use what you have. Do what you can."
]

# 🔁 Function to display a random quote
def show_quote():
    selected_quote = random.choice(quotes)
    quote_label.config(text=selected_quote)

# 🖼️ Create main window
root = tk.Tk()
root.title("💬 Random Quote Generator")
root.geometry("500x300")
root.configure(bg="#f0f0f0")

# 🧾 Heading label
tk.Label(root, text="Click the Button to Get Inspired!", font=("Helvetica", 14, "bold"), bg="#f0f0f0").pack(pady=10)

# 📢 Label to display the quote
quote_label = tk.Label(root, text="", wraplength=400, justify="center", font=("Helvetica", 12), bg="#ffffff", fg="#333333", relief="solid", bd=1, padx=10, pady=10)
quote_label.pack(pady=20)

# 🔘 Button to trigger quote
generate_button = tk.Button(root, text="🔄 Generate Quote", command=show_quote, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
generate_button.pack()

# 🧠 Run the app
root.mainloop()
