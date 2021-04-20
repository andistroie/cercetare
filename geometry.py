from global_setting import OTHER_DEFAULTS

class Geometry:

    def make_supercell(self):
    #   use mod_global
    #   use list_choices

        print("Make supercell")
        if OTHER_DEFAULTS.isalloc is None or OTHER_DEFAULTS.npartic < 1:
            print("Read data file first")
            return

        print("Select list to copy from")
        # TODO
        # igrp, ok = list_choice()
        igrp = []
        ok = True

        if ox == False:
            return

        cell_thick = int(input("N = "))
        if cell_thick < 1:
            print("Invalid choice!")
            return
        # total number of cells
        ncell1d = cell_thick * 2 + 1
        ncells = ncell1d ** OTHER_DEFAULTS.idimension

        # Optional timeshift of different cells
        # TODO
        ichoice1 = int(input("Timeshift options - copy atoms from: 1 - current data, 2 - given timestamp, 3 - different timesteps"))
        if ichoice in [1, 2, 3] :
            if ichoice1 == 2 or ichoice1 == 3:
                print("To be implemented")
        else:
            print ("Invalid choice")
            return
        
        # Number of atoms given
        nats = OTHER_DEFAULTS.first[igrp + 1] - OTHER_DEFAULTS.first[igrp]
        npartic_old = OTHER_DEFAULTS.npartic
        # Allocate memory
        if ichoice1 == 3:
            # Copy 27 times
            i1stcopy = 1    if ichoice1 == 2 or ichoice1 == 3:
                print("To be implemented")
            npartic_new = OTHER_DEFAULTS.npartic + nats * ncells
            ffoffset = nats
            print("ffoffset is "  + ffoffset)
        else:
            # only copy 26 times
            grps[1] = igrp
            i1stcopy = 2
            npartic_new = OTHER_DEFAULTS.npartic + nats * (ncells - 1)

        OTHER_DEFAULTS.npartic = npartic_new


        
        


        

        
