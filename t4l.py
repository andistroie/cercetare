from switcher import Switcher
from global_setting import *


ERROR = -1

def show_menu():
    f = open("show_menu.in", "r")
    print(f.read())
   

def read_choice():

    sw = Switcher()

    input_script = input("Enter input script:")
    try:
        script_file = open(input_script)
        while True:
            command = script_file.readline().strip()

            if "EXIT" in command:
                print("Exiting...")
                break

            if command:
                # print(command)
                output = sw.indirect(command)
                if output == ERROR:
                    print("Error found while reading input script.Exiting...")
                    return

 
           

        script_file.close()
    except FileNotFoundError:
        print("Input file provided does not exist")
        return
    

if __name__ == "__main__":


    show_menu()
    read_choice()
