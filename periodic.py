from global_setting import OTHER_DEFAULTS 


class Periodic:


# Remap the point (xx,yy,zz) into the periodic box,
# no matter how far away it is. Adjust true flag accordingly.
# Only do it if periodicity is on.
#       argument variables
#       real*8 xx,yy,zz
#       integer itrue
  
    def remap(self, xx, yy, zz, itrue):

    if OTHER_DEFAULTS.perflagx  == 0:
        while xx < OTHER_DEFAULTS.box[1][1]:
            xx = xx + OTHER_DEFAULTS.xprd
            itrue = itrue - 1
        while xx >= OTHER_DEFAULTS.box[2][1]:
            xx = xx - OTHER_DEFAULTS.xprd
            itrue = itrue + 1
    
    if OTHER_DEFAULTS.perflagy == 0:
        while yy < OTHER_DEFAULTS.box[1][2]:
            yy = yy + yy + OTHER_DEFAULTS.yprd
            itrue = itrue - 1000
        while yy >= OTHER_DEFAULTS.box[2][2]:
            yy = yy - OTHER_DEFAULTS.yprd
            itrue = itrue + 1000
    
    if OTHER_DEFAULTS.perflagz == 0:
        while zz < OTHER_DEFAULTS.box[1][3]:
            zz = zz + OTHER_DEFAULTS.zprd
            itrue = itrue - 1000000
        while zz >= OTHER_DEFAULTS.box[2][3]:
            zz = zz - OTHER_DEFAULTS.zprd
            itrue = itrue + 1000000

        

    return xx, yy, zz, itrue

# !c enforce PBC on appropriate dims, no matter which box image the particles are in
# !c requires true(n) to be allocated and sets it to the correct value
# !c argument variables
#       integer igrp
   

   def pbc(self, igrp):

       for ith  in range (OTHER_DEFAULTS.first[igrp], OTHER_DEFAULTS.first[igrp + 1] - 1):
            i = OTHER_DEFAULTS.list[ith]
            xx, yy, zz =  self.remap(OTHER_DEFAULTS.x[1][i], OTHER_DEFAULTS.x[1][i], OTHER_DEFAULTS.x[1][i], OTHER_DEFAULTS.true[i])
            OTHER_DEFAULTS.x[1][i] = xx

# !c minimum image convention inside a periodic box
# !c adjust dx,dy,dz to magnitude and sign of shortest distance in box

    def minimg(self, dx, dy, dz):

        if OTHER_DEFAULTS.perflagx == 0:
            if abs(dx) > OTHER_DEFAULTS.xprd_half:
                if dx < 0.0:
                    dx = dx + OTHER_DEFAULTS.xprd
                else:
                    dx = dx - OTHER_DEFAULTS.xprd

        if OTHER_DEFAULTS.perflagy == 0:
            if abs(dy) > OTHER_DEFAULTS.yprd_half:
                if dy < 0.0:
                    dy = dy + OTHER_DEFAULTS.yprd
                else:
                    dy = dy - OTHER_DEFAULTS.yprd

        if OTHER_DEFAULTS.perflagz == 0:
            if abs(dz) > OTHER_DEFAULTS.zprd_half:
                if dz < 0.0:
                    dz = dz + OTHER_DEFAULTS.zprd
                else:
                    dz = dz -OTHER_DEFAULTS.zprd
        
        return dx, dy, dz

# !c Returns the image indices ix,iy,iz of the box, according to the true-flag
    def get_image_index2(self, iat):
        ix = 0
        iy = 0
        iz = 0
        return ix, iy, iz

    def get_image_index(self, itrue):

        d = itrue
        rem = d % 1000
        ix = rem - 500
        d = d / 1000
        rem = d % 1000
        iy = rem - 500
        d = d / 1000
        rem = d % 1000
        iz =  rem - 500

        return ix, iy, iz

# !c Returns the true-flag, according to the image indices ix,iy,iz of the box

    def get_itrue(self, ix, iy, iz):
        
        itrue = (500 + iz) * 1000000 + + (500 + iy) * 1000 + (500 + ix)
        return itrue

# !c Sets *prd and *prd_half - call every time the box size changes

    def set_prd(self):
        
        OTHER_DEFAULTS.xprd = OTHER_DEFAULTS.box[2][1] - OTHER_DEFAULTS.box[1][1]
        OTHER_DEFAULTS.xprd_half = OTHER_DEFAULTS.xprd * 0.5
        OTHER_DEFAULTS.yprd = OTHER_DEFAULTS.box[2][2] - OTHER_DEFAULTS.box[1][2]
        OTHER_DEFAULTS.yprd_half = OTHER_DEFAULTS.yprd * 0.5
        OTHER_DEFAULTS.zprd = OTHER_DEFAULTS.box[2][3] - OTHER_DEFAULTS.box[1][3]
        OTHER_DEFAULTS.zprd_half = OTHER_DEFAULTS.zprd * 0.5


    def clean_edges(self):

        if OTHER_DEFAULTS.x_unclean == None
            OTHER_DEFAULTS.x_unclean = OTHER_DEFAULTS.x

        print("cleaning up boundaries so no molecule is bonded over a border")

        for k in range (0, OTHER_DEFAULTS.nlist):
            np = OTHER_DEFAULTS.first[k + 1] - OTHER_DEFAULTS.first[k]
            for i in range (0, np):
                ith = OTHER_DEFAULTS.list[OTHER_DEFAULTS.first[k] + i - 1]
                for j in range (0, np):
                    jth = OTHER_DEFAULTS.list[OTHER_DEFAULTS.first[k] + j - 1]
                    dxx = OTHER_DEFAULTS.x[1][ith] - OTHER_DEFAULTS.x[1][jth]
                    dyy = OTHER_DEFAULTS.x[2][ith] - OTHER_DEFAULTS.x[2][jth]
                    dzz = OTHER_DEFAULTS.x[3][ith] - OTHER_DEFAULTS.x[3][jth]
                    if abs(dxx) > OTHER_DEFAULTS.xprd_half:
                        if dxx < 0.0:
                            OTHER_DEFAULTS.x[1][ith] = OTHER_DEFAULTS.x[1][ith] + OTHER_DEFAULTS.xprd
                        else :
                            OTHER_DEFAULTS.x[1][ith] = OTHER_DEFAULTS.x[1][ith] - OTHER_DEFAULTS.xprd

                    if abs(dyy) > OTHER_DEFAULTS.yprd_half:
                        if dyy < 0.0:
                            OTHER_DEFAULTS.x[2][ith] = OTHER_DEFAULTS.x[2][ith] + OTHER_DEFAULTS.yprd
                        else :
                            OTHER_DEFAULTS.x[2][ith] = OTHER_DEFAULTS.x[2][ith] - OTHER_DEFAULTS.yprd

                    if abs(dzz) > OTHER_DEFAULTS.zprd_half:
                        if dzz < 0.0:
                            OTHER_DEFAULTS.x[3][ith] = OTHER_DEFAULTS.x[3][ith] + OTHER_DEFAULTS.zprd
                        else :
                            OTHER_DEFAULTS.x[3][ith] = OTHER_DEFAULTS.x[3][ith] - OTHER_DEFAULTS.zprd

        

        def x_unclean_edges(self):
            
            print ("Uncleaning borders, back to initial geometry")
            OTHER_DEFAULTS.x = OTHER_DEFAULTS.x_unclean  
