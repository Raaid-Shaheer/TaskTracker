https://roadmap.sh/projects/task-tracker

Task Tracker CLI

A simple Command-Line Interface (CLI) tool to track tasks, manage their statuses, and store them in a JSON file.

This project is built in Python and helps you practice file handling, CLI arguments, and basic task management.

---

## Features

* Add a new task with a title and optional description
* Update a task’s title and description
* Delete a specific task or all tasks
* Mark a task as `todo`, `in-progress`, or `done`
* List all tasks or filter by status
* Tracks creation and last update timestamps

---

## Task Properties

Each task in `notesdemo.json` contains:

| Property      | Description                                |
| ------------- | ------------------------------------------ |
| `id`          | Unique identifier for the task             |
| `title`       | Task title                                 |
| `description` | Short description (optional)               |
| `status`      | Task status: `todo`, `in-progress`, `done` |
| `created_at`  | Date & time when the task was created      |
| `updated_at`  | Date & time when the task was last updated |

---

## Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd TaskTracker
```

2. Make sure Python 3.x is installed.
3. The project uses a JSON file (`notesdemo.json`) for storing tasks. It will be created automatically on first run if it doesn’t exist.

---

## Usage

Run the program from the command line:

```bash
python notesdemo.py <command> [arguments]
```

### Commands

* **Add a task**

```bash
python notesdemo.py add "Task Title" "Optional description"
```

* **List tasks**

```bash
python notesdemo.py list             # Lists all tasks
python notesdemo.py list todo        # Lists tasks with status 'todo'
python notesdemo.py list in-progress # Lists tasks 'in-progress'
python notesdemo.py list done        # Lists tasks marked 'done'
```

* **Update a task**

```bash
python notesdemo.py update <task_number> "New Title" "New description"
```

* **Delete a task**

```bash
python notesdemo.py delete <task_number>
python notesdemo.py delete all       # Deletes all tasks
```

* **Change task status**

```bash
python notesdemo.py status <task_number> <todo|in-progress|done>
```

---

## Example

```bash
python notesdemo.py add "Buy groceries" "Milk, eggs, and bread"
python notesdemo.py list
python notesdemo.py update 1 "Buy groceries & cook" "Add vegetables"
python notesdemo.py status 1 done
python notesdemo.py delete all
```

---

## Notes

* The program handles invalid inputs gracefully.
* Timestamps are automatically updated on creation and modification.
* Tasks are stored in `notesdemo.json` in the project directory.

---

