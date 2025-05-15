# FileName: Mad_Libs_Devin_Lawrence_Complex.py
# Name: Devin Lawrence
# Period: 5th Hour
# Date: May 14, 2025
import csv
import random
import os
import tkinter as tk
from tkinter import messagebox, TclError
import requests
from PIL import Image, ImageTk
from io import BytesIO

IMAGE_URL = "https://www.looneylabs.com/sites/default/files/styles/large/public/marketing_images/MadLibsTheGameLogo.png?itok=30iJpJUb"

def load_logo(size=(300, 100)):
    """Fetch and return a PhotoImage of the Mad Libs logo, or None on failure."""
    try:
        resp = requests.get(IMAGE_URL, timeout=5)
        resp.raise_for_status()
        img = Image.open(BytesIO(resp.content))
        img = img.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception:
        return None

def is_valid_word(word, check_ing=False):
    """Check if input is valid: letters only, not empty, optionally ends with 'ing'."""
    if not word or not word.isalpha() or any(c.isdigit() for c in word):
        return False
    if check_ing and not word.lower().endswith("ing"):
        return False
    return True

def play_madlib(root=None, use_gui=True):
    # Locate CSV
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "mad_libs.csv")
    
    # Read CSV
    mad_libs = []
    try:
        with open(csv_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                mad_libs.append(row)
    except FileNotFoundError:
        msg = f"'{csv_path}' not found. Put 'mad_libs.csv' alongside this script."
        if use_gui and root:
            messagebox.showerror("Error", msg)
        else:
            print("Error:", msg)
        if root: root.quit()
        return
    
    if not mad_libs:
        msg = "CSV is empty or invalid."
        if use_gui and root:
            messagebox.showerror("Error", msg)
        else:
            print("Error:", msg)
        if root: root.quit()
        return

    # Store selected story and inputs
    selected = [random.choice(mad_libs)]
    current_inputs = [None]  # Store current inputs for reuse
    
    # Input variables
    vars_ = {
        "adjective1": tk.StringVar(),
        "noun1": tk.StringVar(),
        "verb1": tk.StringVar(),
        "animal": tk.StringVar(),
        "place": tk.StringVar(),
        "object": tk.StringVar(),
        "adjective2": tk.StringVar(),
    }
    entries = {}
    
    # Row selection
    row_ids = [row["row_id"] for row in mad_libs]
    selected_row = tk.StringVar(value="Random")  # Default to random
    
    def get_inputs():
        if use_gui and root:
            if not all(v.get().strip() for v in vars_.values()):
                messagebox.showwarning("Warning", "Please fill in all fields!")
                return None
            inputs = {k: v.get().strip() for k, v in vars_.items()}
            # Validate inputs
            for k, v in inputs.items():
                check_ing = k == "verb1"
                if not is_valid_word(v, check_ing=check_ing):
                    messagebox.showwarning("Warning", f"Invalid {k.replace('1', '').replace('2', '')}: Use letters only{' and end in -ing' if check_ing else ''}.")
                    return None
            current_inputs[0] = inputs
            return inputs
        else:
            inputs = {}
            for key, prompt_key in [
                ("adjective1", "adjective1_prompt"),
                ("noun1", "noun1_prompt"),
                ("verb1", "verb1_prompt"),
                ("animal", "animal_prompt"),
                ("place", "place_prompt"),
                ("object", "object_prompt"),
                ("adjective2", "adjective2_prompt")
            ]:
                prompt = selected[0].get(prompt_key, f"Enter a {key.replace('1', '').replace('2', '')}: ")
                value = input(prompt).strip()
                check_ing = key == "verb1"
                while not is_valid_word(value, check_ing=check_ing):
                    value = input(f"Please enter a valid {key.replace('1', '').replace('2', '')} (letters only{' and ending in -ing' if check_ing else ''}): ").strip()
                inputs[key] = value
            current_inputs[0] = inputs
            return inputs
    
    def update_selected_row(*args):
        row_id = selected_row.get()
        if row_id == "Random":
            selected[0] = random.choice(mad_libs)
        else:
            for row in mad_libs:
                if row["row_id"] == row_id:
                    selected[0] = row
                    break
            else:
                messagebox.showwarning("Warning", f"Row ID {row_id} not found. Using random story.")
                selected[0] = random.choice(mad_libs)
        # Update prompts in GUI
        if use_gui and root:
            for widget in frame.winfo_children():
                if isinstance(widget, tk.Label) and widget != row_label:
                    widget.destroy()
                if isinstance(widget, tk.Entry):
                    widget.destroy()
            entries.clear()
            for col, key in prompts:
                label = selected[0].get(col, f"Enter a {key.replace('1', '').replace('2', '')}:")
                tk.Label(frame, text=label, bg="#008080", fg="white", font=("Arial", 14)).pack(anchor="w", pady=(5,0))
                e = tk.Entry(frame, textvariable=vars_[key], font=("Arial", 12))
                e.pack(fill=tk.X, pady=(0,10))
                entries[key] = e
    
    def show_story(ans, row_id):
        try:
            story_text = selected[0]["story"].format(**ans)
        except KeyError:
            msg = "Template placeholders mismatch."
            if use_gui and root:
                messagebox.showerror("Error", msg)
            else:
                print("Error:", msg)
            return
        
        if use_gui and root:
            win = tk.Toplevel(root)
            win.title("Your Mad Lib Story")
            win.geometry("1000x800")
            win.configure(bg="#008080")
            
            # Logo
            logo_img = load_logo()
            if logo_img:
                lbl_logo = tk.Label(win, image=logo_img, bg="#008080")
                lbl_logo.image = logo_img
                lbl_logo.pack(pady=10)
            
            # Row ID
            tk.Label(win, text=f"Mad Lib Row ID: {row_id}", bg="#008080", fg="white", font=("Arial", 14)).pack(pady=5)
            
            # Story text
            text = tk.Text(win, wrap=tk.WORD, font=("Arial", 24), bg="white")
            text.insert(tk.END, story_text)
            text.config(state="disabled")
            text.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
            
            # Button frame
            btn_frame = tk.Frame(win, bg="#008080")
            btn_frame.pack(pady=10)
            
            # Done? button
            def on_done():
                if messagebox.askyesno("Continue?", "Do another Mad Lib with new inputs?"):
                    selected[0] = random.choice(mad_libs)
                    for v in vars_.values(): v.set("")
                    for e in entries.values(): e.config(state="normal")
                    submit_btn.config(state="normal")
                    reset_btn.config(state="disabled")
                    resubmit_different_btn.config(state="disabled")
                    selected_row.set("Random")
                    win.destroy()
            
            tk.Button(btn_frame, text="Done?", command=on_done, bg="white", fg="black", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
            
            # Close All button
            def on_close_all():
                root.quit()
                root.destroy()
            
            tk.Button(btn_frame, text="Close All", command=on_close_all, bg="white", fg="black", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
            
            # Restart button
            def on_restart():
                for v in vars_.values(): v.set("")
                for e in entries.values(): e.config(state="normal")
                submit_btn.config(state="normal")
                reset_btn.config(state="disabled")
                resubmit_different_btn.config(state="disabled")
                selected_row.set("Random")
                selected[0] = random.choice(mad_libs)
                current_inputs[0] = None
                win.destroy()
            
            tk.Button(btn_frame, text="Restart", command=on_restart, bg="white", fg="black", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
            
            # Run Different Mad Lib button
            def on_different():
                available = [row for row in mad_libs if row["row_id"] != selected[0]["row_id"]]
                if not available:
                    messagebox.showwarning("Warning", "No other Mad Libs available.")
                    return
                selected[0] = random.choice(available)
                if current_inputs[0]:
                    show_story(current_inputs[0], selected[0]["row_id"])
                    win.destroy()
            
            tk.Button(btn_frame, text="Run Different Mad Lib", command=on_different, bg="white", fg="black", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
        
        else:
            print(f"\n=== Your Mad Lib Story (Row ID: {row_id}) ===")
            print(story_text)
            print("\n[1] Another Mad Lib  [2] Different Mad Lib with same inputs  [3] Quit")
            choice = input("> ").strip()
            if choice == "1":
                new = get_inputs()
                if new:
                    selected[0] = random.choice(mad_libs)
                    show_story(new, selected[0]["row_id"])
            elif choice == "2":
                available = [row for row in mad_libs if row["row_id"] != selected[0]["row_id"]]
                if not available:
                    print("No other Mad Libs available.")
                elif current_inputs[0]:
                    selected[0] = random.choice(available)
                    show_story(current_inputs[0], selected[0]["row_id"])
    
    def on_submit():
        ans = get_inputs()
        if ans:
            for e in entries.values(): e.config(state="disabled")
            submit_btn.config(state="disabled")
            reset_btn.config(state="normal")
            resubmit_different_btn.config(state="normal")
            show_story(ans, selected[0]["row_id"])
    
    def on_reset():
        for v in vars_.values(): v.set("")
        for e in entries.values(): e.config(state="normal")
        submit_btn.config(state="normal")
        reset_btn.config(state="disabled")
        resubmit_different_btn.config(state="disabled")
        selected_row.set("Random")
        selected[0] = random.choice(mad_libs)
    
    def on_resubmit_different():
        if not current_inputs[0]:
            messagebox.showwarning("Warning", "No inputs available to resubmit.")
            return
        available = [row for row in mad_libs if row["row_id"] != selected[0]["row_id"]]
        if not available:
            messagebox.showwarning("Warning", "No other Mad Libs available.")
            return
        selected[0] = random.choice(available)
        for e in entries.values(): e.config(state="normal")
        submit_btn.config(state="normal")
        show_story(current_inputs[0], selected[0]["row_id"])
    
    # Build GUI
    if use_gui and root:
        frame = tk.Frame(root, bg="#008080")
        frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # Row selection dropdown
        row_label = tk.Label(frame, text="Select Mad Lib Row ID (or Random):", bg="#008080", fg="white", font=("Arial", 14))
        row_label.pack(anchor="w", pady=(10,0))
        row_menu = tk.OptionMenu(frame, selected_row, "Random", *row_ids, command=update_selected_row)
        row_menu.config(font=("Arial", 12))
        row_menu.pack(fill=tk.X, pady=(0,20))
        
        prompts = [
            ("adjective1_prompt", "adjective1"),
            ("noun1_prompt", "noun1"),
            ("verb1_prompt", "verb1"),
            ("animal_prompt", "animal"),
            ("place_prompt", "place"),
            ("object_prompt", "object"),
            ("adjective2_prompt", "adjective2"),
        ]
        for col, key in prompts:
            label = selected[0].get(col, f"Enter a {key.replace('1', '').replace('2', '')}:")
            tk.Label(frame, text=label, bg="#008080", fg="white", font=("Arial", 14)).pack(anchor="w", pady=(5,0))
            e = tk.Entry(frame, textvariable=vars_[key], font=("Arial", 12))
            e.pack(fill=tk.X, pady=(0,10))
            entries[key] = e
        
        # Button frame
        btn_frame = tk.Frame(frame, bg="#008080")
        btn_frame.pack(pady=20)
        
        submit_btn = tk.Button(btn_frame, text="Submit", command=on_submit, bg="white", fg="black", font=("Arial", 12))
        submit_btn.pack(side=tk.LEFT, padx=5)
        
        reset_btn = tk.Button(btn_frame, text="Reset", command=on_reset, bg="white", fg="black", font=("Arial", 12), state="disabled")
        reset_btn.pack(side=tk.LEFT, padx=5)
        
        resubmit_different_btn = tk.Button(btn_frame, text="Resubmit with Different Row ID", command=on_resubmit_different, bg="white", fg="black", font=("Arial", 12), state="disabled")
        resubmit_different_btn.pack(side=tk.LEFT, padx=5)
    else:
        print("Let's make a crazy story! Enter words with letters only (no numbers or symbols).")
        print("\nAvailable Mad Lib Row IDs:", ", ".join(row_ids))
        row_choice = input("Enter a Row ID or press Enter for random: ").strip()
        if row_choice in row_ids:
            for row in mad_libs:
                if row["row_id"] == row_choice:
                    selected[0] = row
                    break
        ans = get_inputs()
        if ans:
            show_story(ans, selected[0]["row_id"])

if __name__ == "__main__":
    try:
        root = tk.Tk()
        root.title("Mad Lib Game")
        root.geometry("500x850")
        root.configure(bg="#008080")
        
        # Main logo
        logo = load_logo()
        if logo:
            lbl_main_logo = tk.Label(root, image=logo, bg="#008080")
            lbl_main_logo.image = logo
            lbl_main_logo.pack(pady=10)
        
        play_madlib(root, use_gui=True)
        root.mainloop()
        print("Tkinter mainloop exited.")
    except (TclError, ImportError):
        print("GUI unavailable; running console mode.")
        print("Welcome to the Awesome Mad Lib Game!")
        print("Give us some silly words to make a funny story!")
        print("We'll pick a random story or a specific one, so play as much as you want!\n")
        play_madlib(use_gui=False)