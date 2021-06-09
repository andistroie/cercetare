from global_setting import OTHER_DEFAULTS
import random
from LammpsInputFile import *

class Lists: 

    @staticmethod
    def list_reorder_random(lif_object):
        atoms_number = lif_object.get_header()["atoms"]
        l = [idx for idx in range(1, atoms_number+1)] #TODO directly generate list
        random.shuffle(l)
        
        atoms_list = lif_object.get_atoms()

        for atom in atoms_list:
            atom.set_new_id(l[atoms_list.index(atom)])
        atoms_list.sort(key=lambda atom: atom.get_new_id())


    @staticmethod
    def divide_cells(atom_list, region, nx, ny, nz, box, atom_indexed):
        # take region as    
        # region =  {
        # "xlo xhi" : None,
        # "ylo yhi": None,
        # "zlo zhi": None
        # }
        # nx, ny, nz - cells number

        if (region["xlo xhi"][0] > region["xlo xhi"][1]) or (region["ylo yhi"][0] > region["ylo yhi"][1]) or (region["zlo zhi"][0] > region["zlo zhi"][1]):
            print("ERROR x|y|z hi must be greater than x|y|z lo")
            return
        
        
        if (not all(box["xlo xhi"][0] <= a <= box["xlo xhi"][1] for a in [region["xlo xhi"][0],region["xlo xhi"][1]])) or( not all(box["ylo yhi"][0] <= a <= box["ylo yhi"][1] for a in [region["ylo yhi"][0],region["ylo yhi"][1]])) or (not all(box["zlo zhi"][0] <= a <= box["zlo zhi"][1] for a in [region["zlo zhi"][0],region["zlo zhi"][1]])):
            print("Region for x not in box")
            return

        ncells = nx * ny * nz

        clx = (region["xlo xhi"][1] - region["xlo xhi"][0]) / nx
        cly = (region["ylo yhi"][1] - region["ylo yhi"][0]) / ny
        clz = (region["zlo zhi"][1] - region["zlo zhi"][0]) / nz

        for atom in atom_list:
            dx = (atom.x - region["xlo xhi"][0]) / clx
            dy = (atom.y - region["ylo yhi"][0]) / cly
            dz = (atom.z - region["zlo zhi"][0]) / clz

            if ((nx > dx >= 0) and (ny > dy >= 0) and (nz > dz >= 0)):
                # Cell position
                ix = int(dx)
                iy = int(dy)
                iz = int(dz)
                ilist = iz + nz * iy + nz * ny * ix
                if ilist in atom_indexed:
                    atom_indexed[ilist].append(atom)
                else:
                    atom_indexed[ilist] = [atom]

        
            