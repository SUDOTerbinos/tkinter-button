import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

root = tk.Tk()
root.title("Tkinter Button Example")

label = tk.Label(root, text="Click the button below!")
label.pack(pady=10)

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

root.mainloop()
