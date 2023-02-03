import tkinter as tk
from tkinter import ttk

def add_task():
    task = task_input.get()
    task_list.insert("end", task)
    task_input.delete(0, "end")

def remove_task():
    task_list.delete(tk.ACTIVE)

root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("300x400")

task_frame = ttk.Frame(root, padding="10 10 10 10")
task_frame.grid(column=0, row=0)

task_input = ttk.Entry(task_frame, width=30)
task_input.grid(column=0, row=0, pady=10)

add_button = ttk.Button(task_frame, text="Add", command=add_task)
add_button.grid(column=1, row=0)

task_list = tk.Listbox(root)
task_list.grid(column=0, row=1, padx=10, pady=10)

remove_button = ttk.Button(root, text="Remove", command=remove_task)
remove_button.grid(column=0, row=2, pady=10)

root.mainloop()
