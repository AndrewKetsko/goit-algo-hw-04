import sys
from pathlib import Path,PurePath
from colorama import Fore,Style
import os

def print_tree(path,tab=0):
    for el in path.iterdir():
        if el.is_file():
            print(Fore.RED+' '*tab+'📜 '+os.path.basename(el))
        else:
            print(Fore.GREEN+' '*tab+'📂 '+el.parts[len(el.parts)-1])
            print_tree(el,tab+4)


def main():
    args=sys.argv

    if len(args)==1:
        print('path is empty')
        return 
    path=Path(args[1])

    if path.is_dir()!=True and path.exists()!=True:
        print('path in not a directory or not exists')
        return
    
    print('\n')
    print_tree(path)
    print(Style.RESET_ALL)


if __name__=="__main__":
    main()