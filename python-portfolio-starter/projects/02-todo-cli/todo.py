import json
import sys
from pathlib import Path

DATA = Path(__file__).parent / "tasks.json"

def load_tasks():
    if DATA.exists():
        return json.loads(DATA.read_text(encoding="utf-8"))
    return []

def save_tasks(tasks):
    DATA.write_text(json.dumps(tasks, indent=2), encoding="utf-8")

def add_task(text):
    tasks = load_tasks()
    tasks.append({"text": text, "done": False})
    save_tasks(tasks)
    print("Added:", text)

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, 1):
        mark = "[x]" if t["done"] else "[ ]"
        print(f"{i}. {mark} {t['text']}")

def done_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        tasks[index-1]["done"] = True
        save_tasks(tasks)
        print("Marked done:", tasks[index-1]["text"])
    else:
        print("Invalid index.")

def delete_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index-1)
        save_tasks(tasks)
        print("Deleted:", removed["text"])
    else:
        print("Invalid index.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python todo.py [add|list|done|delete] <args>")
        return
    cmd = sys.argv[1]
    if cmd == "add":
        add_task(" ".join(sys.argv[2:]).strip())
    elif cmd == "list":
        list_tasks()
    elif cmd == "done":
        if len(sys.argv) < 3:
            print("Provide task index")
        else:
            done_task(int(sys.argv[2]))
    elif cmd == "delete":
        if len(sys.argv) < 3:
            print("Provide task index")
        else:
            delete_task(int(sys.argv[2]))
    else:
        print("Unknown command:", cmd)

if __name__ == "__main__":
    main()
