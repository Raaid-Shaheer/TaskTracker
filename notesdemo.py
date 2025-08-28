import json
import sys
from datetime import datetime

FILENAME = "notesdemo.json"

# Load notes
# Load notes
try:
    with open(FILENAME, "r") as f:
        content = f.read().strip()
        notesdemo = json.loads(content) if content else []
except FileNotFoundError:
    notesdemo = []
except json.JSONDecodeError:
    print(f"Error: {FILENAME} contains invalid JSON. Starting with an empty list.")
    notesdemo = []

# Check if command is given
if len(sys.argv) < 2:
    print("Please follow the format: python filename command [arguments]")
    sys.exit(1)

command = sys.argv[1].lower()

# ---------- ADD ----------
if command == "add":
    if len(sys.argv) < 3:
        print("Please provide a title for the task after the 'add' command.")
        sys.exit(1)
    title = sys.argv[2]
    description = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else ""
    new_task = {
        "id": len(notesdemo) + 1,
        "title": title,
        "description": description,
        "status": "in-progress",  # default status
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    notesdemo.append(new_task)
    with open(FILENAME, "w") as f:
        json.dump(notesdemo, f, indent=4)
    print("Task Added Successfully:", title)

# ---------- LIST ----------
elif command == "list":
    # default show all tasks
    if len(sys.argv) == 2:
        tasks_to_display = notesdemo
    else:
        subcommand = sys.argv[2].lower()
        if subcommand == "todo":
            tasks_to_display = [t for t in notesdemo if t.get('status') == "todo"]
        elif subcommand == "in-progress":
            tasks_to_display = [t for t in notesdemo if t.get('status') == "in-progress"]
        elif subcommand == "done":
            tasks_to_display = [t for t in notesdemo if t.get('status') == "done"]
        elif subcommand == "not-done":
            tasks_to_display = [t for t in notesdemo if t.get('status') != "done"]
        else:
            print("Invalid subcommand: Use either todo, in-progress, done")
            sys.exit(1)

    if not tasks_to_display:
        print("No tasks available to list.")
    else:
        for i, task in enumerate(tasks_to_display, 1):
            title = task.get('title', task.get('note', 'Untitled'))
            description = task.get('description', '')
            print(f"{i}. {title} ({task.get('status','N/A')})")
            print(f"   ID: {task.get('id', i)} | Description: {description} | Created: {task.get('created_at','N/A')} | Updated: {task.get('updated_at','N/A')}")

# ---------- DELETE ----------
elif command == "delete":
    if len(sys.argv) < 3:
        print("Please provide the task number to delete or 'all' after the 'delete' command to delete all tasks.")
        sys.exit(1)
    if sys.argv[2].lower() == "all":
        confirm = input("Are you sure you want to delete ALL tasks? (yes/no): ").strip().lower()  
        if confirm == "yes":
            notesdemo.clear()
            with open(FILENAME, "w") as f:
                json.dump(notesdemo, f, indent=4)
            print("Deleted All Tasks")
        else:
            print("Operation cancelled.")
        sys.exit(0)
    try:
        task_index = int(sys.argv[2]) - 1
        deleted_task = notesdemo.pop(task_index)
        with open(FILENAME, "w") as f:
            json.dump(notesdemo, f, indent=4)
        print(f"Deleted Task: {deleted_task.get('title', deleted_task.get('note','Untitled'))}")
    except (ValueError, IndexError):
        print("Invalid Task Number")

# ---------- UPDATE ----------
elif command == "update":
    if len(sys.argv) < 4:
        print("Format: python notesdemo.py update task_number new_title [new_description...]")
        sys.exit(1)
    try:
        task_index = int(sys.argv[2]) - 1
        new_title = sys.argv[3]
        new_description = " ".join(sys.argv[4:]) if len(sys.argv) > 4 else notesdemo[task_index].get('description','')
        
        old_title = notesdemo[task_index].get('title','Untitled')
        old_description = notesdemo[task_index].get('description','')
        
        # Update title and description
        notesdemo[task_index]['title'] = new_title  
        notesdemo[task_index]['description'] = new_description
        notesdemo[task_index]['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Save changes
        with open(FILENAME, "w") as f:
            json.dump(notesdemo, f, indent=4)
        
        print(f"Updated Task {task_index + 1}: {new_title}")
        print(f"Old Title: {old_title} | Old Description: {old_description}")
        
    except (ValueError, IndexError):
        print("Invalid Task Number")

        

# ---------- STATUS ----------
elif command == "status":
    if len(sys.argv) < 4:
        print("Format: python notesdemo.py status task_number new_status")
        sys.exit(1)
    try:
        task_index = int(sys.argv[2]) - 1
        new_status = sys.argv[3].lower()
        if new_status not in ["todo","in-progress","done"]:
            print("Invalid status: Select either todo, in-progress, done")
        else:
            notesdemo[task_index]['status'] = new_status
            notesdemo[task_index]['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(FILENAME, "w") as f:
                json.dump(notesdemo, f, indent=4)
            print(f"Updated Status of Task {task_index + 1} to {new_status}")
    except (ValueError, IndexError):
        print("Invalid Task Number")

# ---------- INVALID COMMAND ----------
else:
    print("Invalid Command: Use add, list, delete, update, or status")
