import sys
from pathlib import Path
from colorama import Fore,Style

def print_tree(path,tab=0):
    for el in path.iterdir():
        if el.is_file():
            print(Fore.RED+' '*tab+'📜 '+el.parts[-1])
        else:
            print(Fore.GREEN+' '*tab+'📂 '+el.parts[-1])
            print_tree(el,tab+4)


def main():
    args=sys.argv

    if len(args)==1:
        print('path is empty')
        return 
    path=Path(args[1])

    if not path.is_dir() and not path.exists():
        print('path in not a directory or not exists')
        return
    
    print('\n')
    print_tree(path)
    print(Style.RESET_ALL)


if __name__=="__main__":
    main()