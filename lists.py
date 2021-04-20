from global_setting import OTHER_DEFAULTS
import random
from LammpsInputFile import *

class Lists: 

    @staticmethod
    def list_reorder_random(lif_object):
        atoms_number = lif_object.get_header()["atoms"]
        l = [idx for idx in range(1, atoms_number+1)]
        random.shuffle(l)
        
        atoms_list = lif_object.get_atoms()

        for atom in atoms_list:
            atom.set_new_id(l[atoms_list.index(atom)])
        atoms_list.sort(key=lambda atom: atom.get_new_id())
        
            