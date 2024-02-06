#Перше завдання
def total_salary(path):
    try:
        with open(path, 'r') as worker_base:
            worker_base = worker_base.read()
            worker_base_list = worker_base.split('\n')
    
        salarys = []    
        for workers_info in worker_base_list:
            workers_info = workers_info.split(',')
            if len(parts) >= 2:
                salary = int(parts[1].strip())
                salarys.append(salary)
        total_salarys = sum(salarys)
        average_salarys = int(sum(salarys) / len(salarys))
        print(f"Загальна сума заробітної плати: {total_salarys}, Середня заробітна плата: {average_salarys}")
    except FileNotFoundError:
        print(f'File {path} not found!')

    return

total_salary("C:\\python\\goit-algo-hw-04\\goit-algo-hw-04.txt")



#Друге завдання 
def get_cats_info(path):
    try:
        with open(path, 'r') as cats_base:
            cats_base = cats_base.read()
            cats_base = cats_base.split('\n')
            cats_list = []
            for cats_info in cats_base:
                cats_info = cats_info.split(',')
                if len(cats_info) >= 3:
                    cats_dict = {"id": cats_info[0], "name": cats_info[1], "age":int(cats_info[2])}
                    cats_list.append(cats_dict)
        print(cats_list)

    except FileNotFoundError:
        print(f'File {path} not found!')
    return

get_cats_info("C:\\python\\goit-algo-hw-04\\get_cats_info.txt")


#Четверте завдання
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated"
    else:
        return "Contact not found!"
        

def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found!"
        

def show_all(contacts):
    for name, phone in contacts.items():
        return f'{name}: {phone}'



def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            if (change_contact(args, contacts)) is not None:
                print(change_contact(args, contacts))
        elif command == "phone":
            if show_phone(args, contacts) is not None:
                print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
