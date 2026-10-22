from datetime import datetime


PRIORITIES = ("Low", "Medium", "High")
STATUSES = ("Incomplete", "Complete")


def prompt_non_empty(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("This field cannot be empty.")


def prompt_editable(message, current):
    value = input(f"{message} [{current}]: ").strip()
    return value or current


def prompt_due_date(current=None):
    while True:
        prompt = "Due date (YYYY-MM-DD)"
        if current:
            prompt += f" [{current}]"
        prompt += ": "
        value = input(prompt).strip()
        if not value and current:
            return current
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Enter a valid date in YYYY-MM-DD format.")


def prompt_choice(message, choices, current=None):
    print(message)
    for number, choice in enumerate(choices, start=1):
        print(f"{number}. {choice}")

    while True:
        prompt = "Choose an option"
        if current:
            prompt += f" [{choices.index(current) + 1}]"
        value = input(f"{prompt}: ").strip()
        if not value and current:
            return current
        if value.isdigit() and 1 <= int(value) <= len(choices):
            return choices[int(value) - 1]
        print(f"Enter a number from 1 to {len(choices)}.")


def display_tasks(tasks):
    if not tasks:
        print("\nNo academic tasks found.")
        return

    print("\nAcademic Tasks")
    print("-" * 105)
    print(f"{'ID':<5}{'Title':<24}{'Due date':<14}{'Priority':<10}"
          f"{'Status':<14}Description")
    print("-" * 105)
    for task in tasks:
        print(
            f"{task['id']:<5}{task['title'][:22]:<24}{task['due_date']:<14}"
            f"{task['priority']:<10}{task['status']:<14}{task['description']}"
        )
    print("-" * 105)


def find_task(tasks, task_id):
    return next((task for task in tasks if task["id"] == task_id), None)


def prompt_task_details():
    title = prompt_non_empty("Title: ")
    description = prompt_non_empty("Description: ")
    due_date = prompt_due_date()
    priority = prompt_choice("Priority", PRIORITIES)
    status = prompt_choice("Completion status", STATUSES)
    return title, description, due_date, priority, status


def create_task(tasks):
    title, description, due_date, priority, status = prompt_task_details()
    next_id = max((task["id"] for task in tasks), default=0) + 1
    tasks.append(
        {
            "id": next_id,
            "title": title,
            "description": description,
            "due_date": due_date,
            "priority": priority,
            "status": status,
        }
    )
    print("Task created successfully.")


def update_task(tasks):
    if not tasks:
        print("\nNo tasks to update.")
        return

    display_tasks(tasks)
    while True:
        value = input("Enter the task ID to update (or 0 to cancel): ").strip()
        if value.isdigit():
            task_id = int(value)
            if task_id == 0:
                return
            task = find_task(tasks, task_id)
            if task:
                break
        print("Enter a valid task ID.")

    print("Press Enter to keep the current value.")
    task["title"] = prompt_editable("Title", task["title"])
    task["description"] = prompt_editable("Description", task["description"])
    task["due_date"] = prompt_due_date(task["due_date"])
    task["priority"] = prompt_choice("Priority", PRIORITIES, task["priority"])
    task["status"] = prompt_choice(
        "Completion status", STATUSES, task["status"]
    )
    print("Task updated successfully.")


def delete_task(tasks):
    if not tasks:
        print("\nNo tasks to delete.")
        return

    display_tasks(tasks)
    while True:
        value = input("Enter the task ID to delete (or 0 to cancel): ").strip()
        if value.isdigit():
            task_id = int(value)
            if task_id == 0:
                return
            task = find_task(tasks, task_id)
            if task:
                break
        print("Enter a valid task ID.")

    confirmation = input(f"Delete '{task['title']}'? (y/n): ").strip().lower()
    if confirmation == "y":
        tasks.remove(task)
        print("Task deleted successfully.")
    else:
        print("Deletion cancelled.")


def main():
    tasks = []
    while True:
        print(
            "\nAcademic Task Manager\n"
            "1. Create task\n"
            "2. View tasks\n"
            "3. Update task\n"
            "4. Delete task\n"
            "5. Exit"
        )
        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Please choose an option from 1 to 5.")


if __name__ == "__main__":
    main()
