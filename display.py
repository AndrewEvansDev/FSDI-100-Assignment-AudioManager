import os

def print_menu():
    print("-"* 30 )
    print("** Audio Mgr 3000 **")
    print("-" * 30)

    print("[1] Register Album")
    print("[2] Register Song")
    print("[3] Print Catalog")
    print("[4] Pring Songs of Album")
    print("[5] Count all the songs in the system")
    print("[6] Total $ in the catalog")
    print("[7] Delete Song")
    print("[8] Delete Album")
    print("[9] Print the most expensive album")
    print("[q] Quit")

def print_header(text):
    clear_screen()
    print("-" * 40)
    print(text)
    print("-" * 40)

def clear_screen():
    if(os.name == 'nt'):
        return os.system('cls')
    else:
        return os.system("clear")
    # return os.system('cls' if os.name == 'nt' else 'clear')