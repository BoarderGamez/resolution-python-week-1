import argparse, sys, os, json
from rich import print
from rich.panel import Panel
parser = argparse.ArgumentParser()
#Var
TASKS_FILE = "tasks.json"
#Fun
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    if os.path.getsize(TASKS_FILE) == 0:
        return []
    with open(TASKS_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_task(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=2)
def main():
    parser.add_argument("task", type=str, nargs="?", help="Task to add")
    args = parser.parse_args()
    if len(sys.argv) ==1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args.task:
        if args.task=="JENIN":
            print("[italic blue]GOOD MORNING![/italic blue][bold red] You have found me, [/bold red][yellow]so I found the rich text library was cool so I'm playing" \
            "around in this easter egg!")
            print(Panel("[italic red]You have found[/italic red][bold yellow] ME!"))
        else:
            TasksHeheBadVariableNamesThatWontBiteMeBackLater= load_tasks()
            if len(TasksHeheBadVariableNamesThatWontBiteMeBackLater) == 0:
                IdNew = 1
            else:
                IdNew = TasksHeheBadVariableNamesThatWontBiteMeBackLater[-1]["id"]+1
            TasksHeheBadVariableNamesThatWontBiteMeBackLater.append({"done":False,"id":IdNew,"task":args.task})
            save_task(TasksHeheBadVariableNamesThatWontBiteMeBackLater)
            print(f"Task {args.task} added with ID of {IdNew}")
if __name__ == "__main__":
    main()