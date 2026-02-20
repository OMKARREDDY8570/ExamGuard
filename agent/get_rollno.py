import tkinter as tk
from tkinter import simpledialog, messagebox

def get_roll_number():

    root = tk.Tk()
    root.withdraw()  # Hide the main Tk window

    while True:
        roll_number = simpledialog.askstring(
            "ExamGuard Consent",
            "Enter your Roll Number:"
        )

        
        if roll_number is None or roll_number.strip() == "":
            messagebox.showwarning(
                "Invalid Input",
                "Roll number is required to start the exam."
            )
            continue  

        
        if not roll_number.strip().isalnum():
            messagebox.showwarning(
                "Invalid Input",
                "Roll number format is invalid. Please try again."
            )
            continue
        confirm =messagebox.askyesno('Conform Roll number',f"you entered:{roll_number}\nIs this correct")
        
        if confirm:
            break
        else:
            continue  

    root.destroy()
    return roll_number.strip()

