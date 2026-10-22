# Academic Task Manager

A desktop-based academic task management application built with Python and Tkinter. The application allows students to create, view, update, and delete academic tasks through a graphical user interface.

## Features

- Create academic tasks
- View all academic tasks in a table
- Update an existing task by selecting it from the table
- Delete a selected task with confirmation
- Clear the task entry form
- Validate required fields
- Validate due dates using the `YYYY-MM-DD` format
- Select a task priority:
  - Low
  - Medium
  - High
- Select a completion status:
  - Incomplete
  - Complete

## Task Details

Each task contains the following information:

- **ID**: Automatically generated for each task
- **Title**: The name of the academic task
- **Description**: Additional details about the task
- **Due Date**: The date by which the task should be completed
- **Priority**: Low, Medium, or High
- **Completion Status**: Incomplete or Complete

## User Stories

- As a student, I want to create an academic task so that I can record assignments and activities.
- As a student, I want to provide a title for each task so that I can identify it easily.
- As a student, I want to add a description so that I can record important task details.
- As a student, I want to set a due date so that I know when the task must be completed.
- As a student, I want to assign a priority so that I can organize tasks by importance.
- As a student, I want to set a completion status so that I can track my progress.
- As a student, I want to view all my academic tasks so that I can manage my workload.
- As a student, I want to update an existing task so that I can correct or change its details.
- As a student, I want to delete a task so that I can remove tasks that are no longer needed.

## Validation Rules

- The title cannot be empty.
- The description cannot be empty.
- The due date must be entered in the `YYYY-MM-DD` format.
- A task must be selected before it can be updated or deleted.
- Deleting a task requires confirmation.

## Requirements

- Python 3.x
- Tkinter, included with most standard Python installations

## How to Run

From the repository root, run:

```powershell
py pgm1.py
```

Alternatively, use:

```powershell
python pgm1.py
```

## How to Use

1. Run `pgm1.py`.
2. Enter a task title and description.
3. Enter the due date in `YYYY-MM-DD` format.
4. Choose a priority and completion status.
5. Select **Create Task** to add the task to the table.
6. Select a task in the table to load its details into the form.
7. Use **Update Task** to save changes or **Delete Task** to remove the selected task.
8. Use **Clear** to reset the form.

## Data Storage

Tasks are stored in memory while the application is running. Closing the application will clear all tasks because the current implementation does not save data to a file or database.
