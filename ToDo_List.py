import os
import time
import json

todo_list = []
json_loaded = False

def clear():
    os.system('clear')

def sleep(duration):
    time.sleep(duration)

def error(reason=0):
    clear()
    match reason:
        case 0:
            print(f"Error: Input not recognized")
        case 1:
            print(f"Warning!: Unsaved Changes Detected")
        case 2:
            print(f"Error: File Not Found")
    sleep(1)

def main_menu():
    global json_loaded
    clear()
    prompt = "ToDo List\n"
    if json_loaded:
        prompt += "\n[json loaded]"
    else:
        prompt += "\n"
    prompt += f"\nYou currently have {len(todo_list)} items."
    prompt += "\n"
    prompt += "\n1) Add Item"
    prompt += "\n2) View Items"
    prompt += "\n3) Remove Item"
    prompt += "\n4) Mark Item as Done"
    prompt += "\n5) Save to Json"
    prompt += "\n6) Load from Json"
    prompt += "\n7) Quit"
    print(prompt)
    while True:
        choice = str(input("\n> "))
        match choice:
            case '1':
                add_item()
            case '2':
                view_items()
            case '3':
                remove_item()
            case '4':
                mark_done()
            case '5':
                save_json()
            case '6':
                load_json()
            case '7':
                clear()
                exit(0)
            case _:
                error()

def add_item():
    clear()
    prompt = "ToDo List\n"
    prompt += "\nPlease name your new item"
    print(prompt)
    while True:
        item_name = str(input("\n> "))
        confirm_name(item_name)

def confirm_name(item_name):
    clear()
    prompt = "ToDo List\n"
    prompt += f"Are you sure you would like to add '{item_name}'?"
    prompt += f"\n\n[Yes] or [No]"
    print(prompt)
    choice = str(input("> "))
    match choice.lower():
        case "yes":
            todo_list.append({'name': item_name, 'complete': False})
            main_menu()
        case "no":
            main_menu()

def view_items():
    clear()
    prompt = "ToDo List\n"
    prompt += f"\nYou currently have {len(todo_list)} items."
    for num, item in enumerate(todo_list, 1):
        prompt += f"\n{num}: {item['name']} | "
        if item['complete'] == False:
            prompt += f"Incomplete"
        else:
            prompt += f"Complete!"
    prompt += "\n\n[Back] to go Back"
    print(prompt)
    choice = str(input("\n> "))
    if choice == 'back':
        main_menu()
    else:
        error()
        view_items()

def remove_item():
    clear()
    prompt = "ToDo List\n"
    if not todo_list:
        prompt += "\nYou need to add an item before you can remove one."
        prompt += "\nLest you want to create a paradox."
        print(prompt)
        choice = str(input("\n> "))
        if choice == 'back':
            main_menu()
    else:
        prompt += "\nTo remove an item, type it's index number"
        for num, item in enumerate(todo_list, 1):
            prompt += f"\n{num}: {item['name']}"
        print(prompt)
        choice = int(input("\n> "))
        if choice == num:
            confirm_delete(item)
        else:
            error()

def confirm_delete(item):
    clear()
    prompt = "ToDo List\n"
    prompt += f"\nAre you sure you'd like to delete '{item['name']}'?"
    prompt += "\n[Yes] or [No]"
    print(prompt)
    choice = str(input("\n> "))
    match choice.lower():
        case 'yes':
            todo_list.remove(item)
            remove_item()
        case 'no':
            main_menu()

def mark_done():
    clear()
    prompt = "ToDo List\n"
    if not todo_list:
        prompt += "\nYou have to have an item, to mark it as complete."
        prompt += "\nPlease create one"
        prompt += "\n\n[Back] to go back"
        print(prompt)
        choice = str(input("> "))
        if choice.lower() == 'back':
            main_menu()
    else:
        prompt += f"\nYou currently have {len(todo_list)} items."
        prompt += "\nTo mark an item as complete, type it's index number."
        for num, item in enumerate(todo_list, 1):
            prompt += f"\n{num}: {item['name']}"
        print(prompt)
        choice = int(input("\n> "))
        if choice == num:
            confirm_done(item)
        else:
            error()
            mark_done()

def confirm_done(item):
    clear()
    prompt = "ToDo List\n"
    prompt += f"\nConfirm, mark {item['name']} as Complete"
    prompt += "\n[Yes] or [No]"
    print(prompt)
    choice = input("\n> ")
    if choice.lower() == 'yes':
        item['complete'] = True
    elif choice.lower() == 'no':
        pass
    else:
        error()
    view_items()

def save_json():
    clear()
    prompt = "ToDo List\n"
    prompt += "\nPlease name your file:"
    prompt += "\n[Back] to go back"
    print(prompt)
    choice = str(input("\n> ")).lower()
    if choice == 'back':
        main_menu()
    else:
        file_path = f"{choice}.json"
        confirm_file_name(file_path)

def confirm_file_name(file_path):
    clear()
    prompt = "ToDo List\n"
    prompt += f"\nAre you sure you would like to save your ToDo List to '{file_path}'?"
    prompt += "\n[Yes] or [No]"
    print(prompt)
    choice = str(input("\n> "))
    if choice == 'yes':
        with open(file_path, 'w') as json_file:
            json.dump(todo_list, json_file, indent=4)
        unsaved_changes = False
        main_menu()
    else:
        main_menu()
        unsaved_changes = True

def load_json():
    global todo_list
    global json_loaded
    clear()
    prompt = "ToDo List\n"
    prompt += "\nTo load a Json file, please type it's name without the extension."
    prompt += "\n[Back] to go back"
    print(prompt)
    choice = input("\n> ")
    if choice.lower() == 'back':
        main_menu()
    else:
        push_choice = choice
        confirm_load(push_choice)

def confirm_load(push_choice):
    global todo_list
    global json_loaded
    clear()
    prompt = "ToDo List\n"
    prompt += f"\nAre you sure you would like to load '{push_choice}.json'?"
    prompt += "\n[Yes] or [No]"
    print(prompt)
    choice = input("\n> ")
    file_path = f"{push_choice}.json"
    if choice.lower() == 'yes':
        try:
            with open(file_path, 'r') as json_file:
                todo_list = json.load(json_file)
                json_loaded = True
        except FileNotFoundError:
            error(2)
    elif choice.lower() == 'no':
        load_json()
    else:
        error()
    main_menu()


if __name__ == '__main__':
    main_menu()
