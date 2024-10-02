contacts={}

def parse_input(command):
    cmd,*args = command.split()
    cmd=cmd.strip()
    return cmd,args

def add_contact(args):
    if len(args)!=2:
        return('wrong params q-ty')
    name,phone=args
    contacts[name]=phone
    return('contact added')

def change_contact(args):
    if len(args)!=2:
        return('wrong params q-ty')
    name,phone=args
    if contacts.get(name):
        contacts[name]=phone
        return('contact changed')
    return('invalid name')

def show_phone(args):
    if contacts.get(args[0]):
        return(f'{args[0]}:{contacts[args[0]]}')
    return('invalid name')

def show_all():
    list=''
    for key, value in contacts.items():
        list+=f'{key}:{value}\n'
    return list

def main():
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()
        command,args=parse_input(command)

        match(command):
            case('close'):
                print("Good bye!")
                break  
            case('exit'):
                print("Good bye!")
                break 

            case('hello'):
                print("How can I help you?")

            case('add'):
                print(add_contact(args))

            case('change'):
                print(change_contact(args))

            case('phone'):
                print(show_phone(args))

            case('all'):
                print(show_all())

            case(_):
                print("Invalid command.")


if __name__ == "__main__":
    main()