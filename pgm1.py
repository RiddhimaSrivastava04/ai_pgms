import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk


PRIORITIES = ("Low", "Medium", "High")
STATUSES = ("Incomplete", "Complete")


class AcademicTaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Academic Task Manager")
        self.root.geometry("900x560")
        self.root.minsize(760, 480)

        self.tasks = []
        self.next_id = 1
        self.selected_task_id = None

        self.title_var = tk.StringVar()
        self.due_date_var = tk.StringVar()
        self.priority_var = tk.StringVar(value=PRIORITIES[0])
        self.status_var = tk.StringVar(value=STATUSES[0])

        self.create_widgets()

    def create_widgets(self):
        form = ttk.LabelFrame(self.root, text="Task Details", padding=12)
        form.pack(fill="x", padx=12, pady=(12, 6))
        form.columnconfigure(1, weight=1)

        ttk.Label(form, text="Title:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(form, textvariable=self.title_var).grid(
            row=0, column=1, columnspan=3, sticky="ew", padx=5, pady=5
        )

        ttk.Label(form, text="Description:").grid(
            row=1, column=0, sticky="nw", padx=5, pady=5
        )
        self.description_text = tk.Text(form, height=3, width=40, wrap="word")
        self.description_text.grid(
            row=1, column=1, columnspan=3, sticky="ew", padx=5, pady=5
        )

        ttk.Label(form, text="Due date (YYYY-MM-DD):").grid(
            row=2, column=0, sticky="w", padx=5, pady=5
        )
        ttk.Entry(form, textvariable=self.due_date_var, width=18).grid(
            row=2, column=1, sticky="w", padx=5, pady=5
        )

        ttk.Label(form, text="Priority:").grid(
            row=2, column=2, sticky="e", padx=5, pady=5
        )
        ttk.Combobox(
            form,
            textvariable=self.priority_var,
            values=PRIORITIES,
            state="readonly",
            width=12,
        ).grid(row=2, column=3, sticky="w", padx=5, pady=5)

        ttk.Label(form, text="Completion status:").grid(
            row=3, column=0, sticky="w", padx=5, pady=5
        )
        ttk.Combobox(
            form,
            textvariable=self.status_var,
            values=STATUSES,
            state="readonly",
            width=16,
        ).grid(row=3, column=1, sticky="w", padx=5, pady=5)

        buttons = ttk.Frame(form)
        buttons.grid(row=3, column=2, columnspan=2, sticky="e", padx=5, pady=5)
        ttk.Button(buttons, text="Create Task", command=self.create_task).pack(
            side="left", padx=3
        )
        ttk.Button(buttons, text="Update Task", command=self.update_task).pack(
            side="left", padx=3
        )
        ttk.Button(buttons, text="Delete Task", command=self.delete_task).pack(
            side="left", padx=3
        )
        ttk.Button(buttons, text="Clear", command=self.clear_form).pack(
            side="left", padx=3
        )

        table_frame = ttk.LabelFrame(self.root, text="Academic Tasks", padding=8)
        table_frame.pack(fill="both", expand=True, padx=12, pady=(6, 12))
        table_frame.columnconfigure(0, weight=1)
        table_frame.rowconfigure(0, weight=1)

        columns = ("id", "title", "description", "due_date", "priority", "status")
        self.task_table = ttk.Treeview(
            table_frame, columns=columns, show="headings", selectmode="browse"
        )
        headings = {
            "id": ("ID", 45),
            "title": ("Title", 150),
            "description": ("Description", 260),
            "due_date": ("Due Date", 105),
            "priority": ("Priority", 90),
            "status": ("Status", 105),
        }
        for column, (heading, width) in headings.items():
            self.task_table.heading(column, text=heading)
            self.task_table.column(column, width=width, anchor="w")
        self.task_table.grid(row=0, column=0, sticky="nsew")
        self.task_table.bind("<<TreeviewSelect>>", self.load_selected_task)

        scrollbar = ttk.Scrollbar(
            table_frame, orient="vertical", command=self.task_table.yview
        )
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.task_table.configure(yscrollcommand=scrollbar.set)

    def get_form_values(self):
        title = self.title_var.get().strip()
        description = self.description_text.get("1.0", "end").strip()
        due_date = self.due_date_var.get().strip()

        if not title:
            messagebox.showerror("Invalid task", "Title cannot be empty.")
            return None
        if not description:
            messagebox.showerror("Invalid task", "Description cannot be empty.")
            return None
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror(
                "Invalid task", "Due date must use the YYYY-MM-DD format."
            )
            return None

        return {
            "title": title,
            "description": description,
            "due_date": due_date,
            "priority": self.priority_var.get(),
            "status": self.status_var.get(),
        }

    def create_task(self):
        task = self.get_form_values()
        if task is None:
            return
        task["id"] = self.next_id
        self.next_id += 1
        self.tasks.append(task)
        self.refresh_table()
        self.clear_form()
        messagebox.showinfo("Success", "Task created successfully.")

    def update_task(self):
        if self.selected_task_id is None:
            messagebox.showwarning("No selection", "Select a task to update.")
            return
        updated_task = self.get_form_values()
        if updated_task is None:
            return

        for task in self.tasks:
            if task["id"] == self.selected_task_id:
                task.update(updated_task)
                break
        self.refresh_table()
        self.clear_form()
        messagebox.showinfo("Success", "Task updated successfully.")

    def delete_task(self):
        if self.selected_task_id is None:
            messagebox.showwarning("No selection", "Select a task to delete.")
            return
        task = next(
            task for task in self.tasks if task["id"] == self.selected_task_id
        )
        if not messagebox.askyesno(
            "Confirm deletion", f"Delete the task '{task['title']}'?"
        ):
            return

        self.tasks.remove(task)
        self.refresh_table()
        self.clear_form()
        messagebox.showinfo("Success", "Task deleted successfully.")

    def refresh_table(self):
        for item in self.task_table.get_children():
            self.task_table.delete(item)
        for task in self.tasks:
            self.task_table.insert(
                "",
                "end",
                iid=str(task["id"]),
                values=(
                    task["id"],
                    task["title"],
                    task["description"],
                    task["due_date"],
                    task["priority"],
                    task["status"],
                ),
            )

    def load_selected_task(self, _event):
        selected = self.task_table.selection()
        if not selected:
            return
        self.selected_task_id = int(selected[0])
        task = next(
            task for task in self.tasks if task["id"] == self.selected_task_id
        )
        self.title_var.set(task["title"])
        self.description_text.delete("1.0", "end")
        self.description_text.insert("1.0", task["description"])
        self.due_date_var.set(task["due_date"])
        self.priority_var.set(task["priority"])
        self.status_var.set(task["status"])

    def clear_form(self):
        self.selected_task_id = None
        self.title_var.set("")
        self.description_text.delete("1.0", "end")
        self.due_date_var.set("")
        self.priority_var.set(PRIORITIES[0])
        self.status_var.set(STATUSES[0])
        for item in self.task_table.selection():
            self.task_table.selection_remove(item)


def main():
    root = tk.Tk()
    AcademicTaskManager(root)
    root.mainloop()


if __name__ == "__main__":
    main()
