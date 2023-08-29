import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []
        
        # Styling
        self.root.configure(bg="#f2f2f2")
        self.root.geometry("300x400")
        
        self.task_entry = tk.Entry(root, width=40, bg="#e6e6e6", font=("Helvetica", 12))
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#4caf50", fg="white", font=("Helvetica", 10, "bold"))
        self.add_button.pack()
        
        self.task_listbox = tk.Listbox(root, width=40, bg="#e6e6e6", font=("Helvetica", 12))
        self.task_listbox.pack(pady=10)
        
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg="#f44336", fg="white", font=("Helvetica", 10, "bold"))
        self.delete_button.pack()
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
            
    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")
            
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
            
def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
