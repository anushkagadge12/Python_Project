import tkinter as tk
from tkinter import messagebox

contacts = []

# Used to Add Contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name and phone and email:
        contacts.append([name, phone, email])
        listbox.insert(tk.END, name)
        clear_fields()
    else:
        messagebox.showwarning("Warning", "All fields are required!")

# Used to View Contact
def view_contact():
    try:
        index = listbox.curselection()[0]
        selected_contact = contacts[index]

        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)

        name_entry.insert(0, selected_contact[0])
        phone_entry.insert(0, selected_contact[1])
        email_entry.insert(0, selected_contact[2])

    except:
        messagebox.showwarning("Warning", "Select a contact first!")

# Used to Edit Contact
def edit_contact():
    try:
        index = listbox.curselection()[0]
        contacts[index] = [
            name_entry.get(),
            phone_entry.get(),
            email_entry.get()
        ]
        listbox.delete(index)
        listbox.insert(index, name_entry.get())
        clear_fields()
    except:
        messagebox.showwarning("Warning", "Select a contact to edit!")

# Used to Delete Contact
def delete_contact():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        contacts.pop(index)
        clear_fields()
    except:
        messagebox.showwarning("Warning", "Select a contact to delete!")

# Clear Fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Creates GUI Window
root = tk.Tk()
root.title("Address Book")
root.geometry("400x400")

# Add Labels
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

# Buttons
tk.Button(root, text="Add", command=add_contact).pack(pady=5)
tk.Button(root, text="View", command=view_contact).pack(pady=5)
tk.Button(root, text="Edit", command=edit_contact).pack(pady=5)
tk.Button(root, text="Delete", command=delete_contact).pack(pady=5)

# Listbox
listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)

root.mainloop()