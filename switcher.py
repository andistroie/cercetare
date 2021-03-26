from global_setting import *
import random
from LammpsInputFile import *

ERROR = -1
SUCCES = 0

defaults = OTHER_DEFAULTS()
class Switcher:

    inputfile_handler = None

    def indirect(self, index):

        command = index.split()
        method_name = 'func_'+ str(command[0])
        method = getattr(self, method_name, lambda :'Invalid')

        return method(command)


    def func_GLOBAL_VAR(self, command):
        

        #Global_var seed iseed[integer] {reinit|other}
        if command[1] == "SEED" :
            if command[2].isnumeric():
                iseed = int(command[2])
            else:
                print("Bad syntax in command : ")
                print(command)
            
            if command[3] == "REINIT":
                # TODO : 
                # call random_seed(put = (/iseed/))   
                # iseed = ranmars(iseed)
                pass
            else:
                print("Bad syntax in command : ")
                print(command)

        #Global_var unit_style  <lj/real/metal/si/cgs/electron/micro/nano>           
        if command[1] == "UNIT_STYLE":
            unit_style = command[2]
            if unit_style in ['LJ', 'REAL', 'METAL', 'SI', 'CGS', 'ELECTRON', 'MICRO', 'NANO']:
                defaults.unit_style = unit_style.upper()
                CONSTANTS.unit_style = unit_style.upper()
            else:
                print("INVALID UNIT STYLE in command:")
                print(command)
                return ERROR
            
           
        #Global_var atom_style  integer (2 or 5)
        #1=angle 2=atomic     3=body  4=bond    5=charge    6=dipole 7=electron 8=ellipsoid 9=full 10=line 
        # 11=meso 12=molecular 13=peri 14=sphere 15=template 16=tri   17=wavepacket" 

        if command[1] == "ATOM_STYLE":
                atom_style = command[2]
                if (int(atom_style) < 1) or (int(atom_style) > 17):
                    print("Invalid choice")
                    return ERROR
                if (int(atom_style) != 2) and (int(atom_style) != 5):
                    print("Currently not implemented:")
                    print(command)
                defaults.atomstyle = int(atom_style)

        if command[1] == "NMOLECULAR":
            nmolecular = command[2]
            if (int(nmolecular) != 0) and (int(nmolecular) != 1):
                    print("NMOLECULAR should be 0 or 1:")
                    print(command)
            else:
                defaults.nmolecular = nmolecular


        #Global_var XBox  xlo xhi (real, xlo<xhi)   ! case (21)
        if command[1] == "XBOX":
            
            if len(command) != 4:
                print("Invalid choice of xdimensions in command")
                print(command)
                return ERROR
            xlo = float(command[2])
            xhi = float(command[3])

            if xlo > xhi:
                print("Xhi must be greater than xlo")
                print(command)
            else:
            # TODO
            #     box(1,1) = dvar1
            #     box(2,1) = dvar2
            #    call set_prd()
                pass

        if command[1] == "YBOX":
            pass
        if command[1] == "ZBOX":
            pass

        return SUCCES


    def func_READ(self, command):

        #Read Data_file filename {delete|other}       !c    case (2)    
        if command[1] == "DATA_FILE":
            if len(command) < 3:
                print("No data file provided")
                return ERROR
            filename = command[2]
            try:
                input_file = open(filename)
                # Already read a data file?
                if (len(command) == 4) and (command[3] == "DELETE"):
                    if defaults.isalloc:
                        # TODO - delete previous saved list of atoms?
                        # call free_atom_memory()
                        self.inputfile_handler = None
                        defaults.isalloc = False
                self.inputfile_handler = LammpsInputFile(filename)
                self.inputfile_handler.read_file()
                defaults.isalloc = True
                
                input_file.close()

            except FileNotFoundError:
                print("Input file provided does not exist")
                return ERROR
        
        else:
            # Other types currently not implemented
            pass

    
    def func_WRITE(self, command):
        #WRITE Data_file filename ff_info{1|0} {overwrite|other}       !      case (51)   
        # ff_info? - not used yet
        if command[1] == "DATA_FILE":
            if len(command) < 3:
                print("No data file provided")
                return ERROR
            filename = command[2]
            print (filename)
            self.inputfile_handler.write_to_file(filename)
        else:
            # Other types currently not implemented
            pass

    


    # def func_25():
    #     print("TODO")
    #     # do not understand
    #     # call multi_list_choice(grps,ngrps,ok)
    #     #     if (.not. ok) cycle

    #     try:
    #         temperature = float(input("Select temperature: "))
    #     except ValueError:
    #         print ("Not a valid input!\n\n")
    #         return
    #     try:
    #         freedom_dg = int(input("Select restricted degrees of freedom: "))
    #     except ValueError:
    #         print ("Not a valid input!\n\n")
    #         return

    #     if (temperature < 0) or (freedom_dg < 0):
    #         print("Temperature  or restricted freedom degrees < 0")
    #         return
        


        
