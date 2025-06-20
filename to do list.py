import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# GUI setup
root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=0, padx=5)

add_btn = tk.Button(frame, text="Add Task", command=add_task)
add_btn.grid(row=0, column=1)

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack()

del_btn = tk.Button(root, text="Delete Selected", command=delete_task)
del_btn.pack(pady=5)

root.mainloop()