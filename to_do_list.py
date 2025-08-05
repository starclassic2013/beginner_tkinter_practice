import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To do List")
root.geometry("500x500")

tasks = []

def add_task():
    task = entry.get()
    if task != (""):
        listbox.insert(tk.END, task)
        tasks.append(task)
        
    else:
        messagebox.showwarning("Enter a New Task")
        
def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
        tasks.pop(selected[0])
        
    except:
        messagebox.showwarning("Select an item to Delete")

        

        

#io

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width = 60)
entry.grid(row=0,column=1)
entry.bind("<Return>", lambda event: add_task())

add_button = tk.Button(frame, text ="Add Task", command=add_task)
add_button.grid(row=0,column=2,padx=5)

listbox = tk.Listbox(root, width=90, height=52)
listbox.pack(pady=10)

delete_button = tk.Button(root, text= "Delete Task", command = delete_task)
delete_button.pack(pady = 10)



root.mainloop()










        















