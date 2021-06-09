from global_setting import OTHER_DEFAULTS
from Atom import Atom
from LammpsInputFile import *

class Kinetics:

    @staticmethod
    def calc_mc_pos(atom_list, lif_object, point):
        masses = lif_object.get_masses()
        xcm = 0
        ycm = 0
        zcm = 0
        wgrp = 0
        if len(atom_list) == 0:
            return
        for atom in atom_list:
            res =  [item for item in masses if item[0] == atom.atom_type]
            wi = res[0][1]
            xcm = xcm + wi * atom.x
            ycm = ycm + wi * atom.y
            zcm = zcm + wi * atom.z
            wgrp = wgrp + wi

        if (wgrp == 0):
            print('Wrgp is zero, division by zero not possible')
            return
        point.append(xcm / wgrp)
        point.append(ycm / wgrp)
        point.append(zcm / wgrp)

        print("Mass center of the list is : " + str(point[0]) + " " + str(point[1]) + " " + str(point[2]))

    # Mass center for given set of coordinates
    @staticmethod
    def calc_mc_pos2(np, xyz, masses, point):
        xcm = 0
        ycm = 0
        zcm = 0
        wgrp = 0
        if(np == 0):
            return
        for i in range(0, np):
            wi = masses[i]
            xcm = xcm + wi * xyz[i][0]
            ycm = ycm + wi * xyz[i][1]
            zcm = zcm + wi * xyz[i][2]
            wgrp = wgrp + wi
            if (wgrp == 0):
                print('Wrgp is zero, division by zero not possible')
                return
        point.append(xcm / wgrp)
        point.append(ycm / wgrp)
        point.append(zcm / wgrp)

        print("Mass center is: " + str(point[0]) + " " + str(point[1]) + " " + str(point[2]))

        
    # Calculate linear momentum of a set of aprticles
    @staticmethod
    def calc_lin_mom(atom_list, lif_object):

        px = 0
        py = 0
        pz = 0

        if len(atom_list) == 0:
            return

        masses = lif_object.get_masses()

        for atom in atom_list:
            res =  [item for item in masses if item[0] == atom.atom_type]
            wi = res[0][1]
            px = px + wi * atom.get_velocities()[0]
            py = py + wi * atom.get_velocities()[1]
            pz = pz + wi * atom.get_velocities()[2]

        print(" Px, Py, Pz are: " + str(px) + " " + str(py) + " " + str(pz))
        return (px, py, pz)

    @staticmethod
    def calc_mc_vel(atom_list, lif_object):

        if len(atom_list) == 0:
            return

        masses = lif_object.get_masses()
        wgrp = 0
        for atom in atom_list:
            wgrp = wgrp + [item for item in masses if item[0] == atom.atom_type][0][1]

        if wgrp <= (1e-10):
            return

        (px, py, pz) = Kinetics.calc_lin_mom(atom_list, lif_object)

        vxcm = px / wgrp
        vycm = py / wgrp	
        vzcm = pz / wgrp

        print("Vxcm, Vyxm, Vzcm are: " + str(vxcm) + " " + str(vycm) + " " + str(vzcm))
        return (vxcm, vycm, vzcm)

    @staticmethod
    def calc_ang_mom(atom_list, lif_object, point):
        angm = [0, 0, 0]

        if len(atom_list) == 0:
            return
        masses = lif_object.get_masses()
        for atom in atom_list:
            res =  [item for item in masses if item[0] == atom.atom_type]
            wi = res[0][1]
            xi = atom.x - point[0]
            yi = atom.y - point[1]
            zi = atom.z - point[2]
            vels = atom.get_velocities()

            angm[0] = angm[0] + wi * ( yi * vels[2] - zi * vels[1])
            angm[1] = angm[1] + wi * ( zi * vels[0] - xi *vels[2])
            angm[2] = angm[2] + wi * ( xi * vels[1] - yi * vels[0])

        print("Angm0, Angm1, Angm2 are: " + str(angm[0]) + " " + str(angm[1]) + " " + str(angm[2]))
        return angm