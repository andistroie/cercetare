from switcher import Switcher
from global_setting import *
from LammpsInputFile import LammpsInputFile
from lists import Lists
from periodic import Periodic

ERROR = -1
SUCCES = 0

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
                output = sw.indirect(command)
                if output == ERROR:
                    print("Error found while applying operation from input script.Exiting...")
                    return

 
           

        script_file.close()
    except FileNotFoundError:
        print("Input file provided does not exist")
        return
    

if __name__ == "__main__":

    # show_menu()
    # read_choice()
    l = LammpsInputFile("333_LA2.DATA")
    # Lists.list_reorder_random(l)
    # l.write_to_file("test.out")

    atom_list = l.get_atoms()
    OTHER_DEFAULTS.box = l.box
  
    # Periodic.pbc(atom_list)
    # atom_list[1].x, atom_list[1].y, atom_list[1].z = Periodic.minimg(atom_list[1].x, atom_list[1].y, atom_list[1].z)
    # print(atom_list[1].x, atom_list[1].y, atom_list[1].z)
    # atom_list[1].x, atom_list[1].y, atom_list[1].z = Periodic.get_image_index(atom_list[1].true)
    # print(atom_list[1].x, atom_list[1].y, atom_list[1].z)

    # print(atom_list[1].x, atom_list[1].y, atom_list[1].z, atom_list[1].true)
    # atom_list[1].true= Periodic.get_itrue(atom_list[1].x, atom_list[1].y, atom_list[1].z)
    # print(atom_list[1].x, atom_list[1].y, atom_list[1].z, atom_list[1].true)
 
    # print(OTHER_DEFAULTS.xprd)
    # Periodic.set_prd()
    # print(OTHER_DEFAULTS.xprd)

    

