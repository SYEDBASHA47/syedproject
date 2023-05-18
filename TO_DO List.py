import tkinter as tk
from tkinter import messagebox


class ToDoList:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")
        master.config(bg='grey')
        self.task_list = tk.Listbox(master, width=80,height=10)
        self.task_list.pack(pady=10)
        self.new_task = tk.Entry(master, width=30)
        self.new_task.pack()
        self.priority = tk.StringVar()
        self.priority.set('low')
        self.low_priority = tk.Radiobutton(master, text="Low Priority", variable=self.priority, value='low')
        self.medium_priority = tk.Radiobutton(master, text="Medium Priority", variable=self.priority, value='medium')
        self.high_priority = tk.Radiobutton(master, text="High Priority", variable=self.priority, value='high')
        self.low_priority.pack(pady=5)
        self.medium_priority.pack(pady=5)
        self.high_priority.pack(pady=5)
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)
        self.clear_button = tk.Button(master, text="Clear All Tasks", command=self.clear_tasks)
        self.clear_button.pack(pady=5)
        self.search_label = tk.Label(master, text="Search:")
        self.search_label.pack(pady=5)
        self.search_entry = tk.Entry(master, width=30)
        self.search_entry.pack(pady=5)
        self.search_button = tk.Button(master, text="Search", command=self.search_tasks)
        self.search_button.pack(pady=5)

    def add_task(self):
        task = self.new_task.get()
        priority = self.priority.get()
        if task == "":
            messagebox.showwarning("Warning", "Please enter a task!")
        else:
            task_with_priority = f"{priority.upper()}: {task}"
            self.task_list.insert(tk.END, task_with_priority)
            self.new_task.delete(0, tk.END)

    def remove_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task!")

    def clear_tasks(self):
        self.task_list.delete(0, tk.END)

    def search_tasks(self):
        query = self.search_entry.get()
        self.task_list.selection_clear(0, tk.END)
        if query:
            for i in range(self.task_list.size()):
                task = self.task_list.get(i)
                if query.lower() in task.lower():
                    self.task_list.selection_set(i)
        else:
            messagebox.showwarning("Warning", "Please enter a search query!")


if __name__ == "__main__":
    root = tk.Tk()
    todo = ToDoList(root)
    root.mainloop()
