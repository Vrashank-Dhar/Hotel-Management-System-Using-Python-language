import tkinter as tk
from tkinter import messagebox
from admin import login_admin
from booking import book_room
from checkin import check_in
from checkout import check_out
from billing import generate_bill

def main_menu():
    root = tk.Tk()
    root.title("Hotel Management System")
    root.geometry("300x300")

    tk.Label(root, text="Hotel Management System", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="Admin Login", command=login_admin).pack(pady=5)
    tk.Button(root, text="Book Room", command=book_room).pack(pady=5)
    tk.Button(root, text="Check-in", command=check_in).pack(pady=5)
    tk.Button(root, text="Check-out", command=check_out).pack(pady=5)
    tk.Button(root, text="Billing", command=generate_bill).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
