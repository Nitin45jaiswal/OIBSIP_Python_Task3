# Random Password Generator - Dark Black & Blue Theme

import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Password Generator")
        self.root.geometry("460x420")
        self.root.resizable(False, False)

        # Dark Theme Colors
        self.bg_color = "#0f0f0f"       # Black
        self.blue_color = "#1f6feb"     # Blue
        self.text_color = "#ffffff"     # White
        self.entry_bg = "#1c1c1c"       # Dark Gray

        self.root.configure(bg=self.bg_color)

        self.build_ui()

    def build_ui(self):
        title = tk.Label(
            self.root,
            text="Random Password Generator",
            font=("Segoe UI", 18, "bold"),
            bg=self.bg_color,
            fg=self.blue_color
        )
        title.pack(pady=12)

        options_frame = tk.Frame(self.root, bg=self.bg_color)
        options_frame.pack(pady=10)

        tk.Label(options_frame, text="Password Length:",
                 font=("Segoe UI", 11),
                 bg=self.bg_color,
                 fg=self.text_color).grid(row=0, column=0, sticky="w")

        self.length_var = tk.IntVar(value=12)

        self.length_slider = tk.Scale(
            options_frame,
            from_=6,
            to=64,
            orient="horizontal",
            variable=self.length_var,
            length=250,
            bg=self.bg_color,
            fg=self.text_color,
            troughcolor=self.blue_color,
            highlightthickness=0
        )
        self.length_slider.grid(row=0, column=1, pady=5)

        self.use_letters = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)
        self.exclude_similar = tk.BooleanVar(value=False)

        checkbox_style = {
            "bg": self.bg_color,
            "fg": self.text_color,
            "selectcolor": self.entry_bg,
            "activebackground": self.bg_color,
            "activeforeground": self.blue_color
        }

        tk.Checkbutton(options_frame, text="Include Letters (A–Z, a–z)",
                       variable=self.use_letters, **checkbox_style).grid(row=1, column=0, columnspan=2, sticky="w")

        tk.Checkbutton(options_frame, text="Include Numbers (0–9)",
                       variable=self.use_digits, **checkbox_style).grid(row=2, column=0, columnspan=2, sticky="w")

        tk.Checkbutton(options_frame, text="Include Symbols",
                       variable=self.use_symbols, **checkbox_style).grid(row=3, column=0, columnspan=2, sticky="w")

        tk.Checkbutton(options_frame,
                       text="Exclude Similar Characters (O, 0, l, 1)",
                       variable=self.exclude_similar, **checkbox_style).grid(row=4, column=0, columnspan=2, sticky="w")

        self.output_box = tk.Entry(
            self.root,
            width=45,
            font=("Consolas", 11),
            bg=self.entry_bg,
            fg=self.blue_color,
            insertbackground="white"
        )
        self.output_box.pack(pady=15)

        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=5)

        button_style = {
            "width": 14,
            "bg": self.blue_color,
            "fg": "white",
            "activebackground": "#1554c0",
            "activeforeground": "white",
            "bd": 0
        }

        tk.Button(button_frame, text="Generate",
                  command=self.generate_password, **button_style).grid(row=0, column=0, padx=6)

        tk.Button(button_frame, text="Copy",
                  command=self.copy_password, **button_style).grid(row=0, column=1, padx=6)

        tk.Button(button_frame, text="Clear",
                  command=self.clear_output, **button_style).grid(row=0, column=2, padx=6)

        note = tk.Label(
            self.root,
            text="Tip: Longer passwords with mixed characters are more secure.",
            font=("Segoe UI", 9),
            bg=self.bg_color,
            fg="#aaaaaa"
        )
        note.pack(pady=12)

    def build_character_pool(self):
        pool = ""

        if self.use_letters.get():
            pool += string.ascii_letters
        if self.use_digits.get():
            pool += string.digits
        if self.use_symbols.get():
            pool += "!@#$%^&*()-_=+[]{};:,.<>?/"

        if self.exclude_similar.get():
            for ch in "O0l1I":
                pool = pool.replace(ch, "")

        return pool

    def generate_password(self):
        length = self.length_var.get()
        pool = self.build_character_pool()

        if not pool:
            messagebox.showerror("Selection Error", "Please select at least one character type.")
            return

        password = "".join(random.choice(pool) for _ in range(length))
        self.output_box.delete(0, tk.END)
        self.output_box.insert(0, password)

    def copy_password(self):
        password = self.output_box.get()
        if not password:
            messagebox.showwarning("No Password", "Generate a password first.")
            return
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")

    def clear_output(self):
        self.output_box.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
