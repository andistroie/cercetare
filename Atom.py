class Atom:
    id = None
    molecule_tag = None
    atom_type = None
    q = None
    x = None 
    y = None
    z = None
    nx = None
    ny = None
    nz = None

    velocity = (None, None, None)

    def __init__(self, id, atom_type, molecule_tag, q, x, y, z, nx, ny, nz):
        self.id = id
        self.molecule_tag = molecule_tag
        self.atom_type = atom_type
        self.q = q
        self.x = x
        self.y = y
        self.z = z
        self.nx = nx
        self.ny = ny
        self.nz = nz

    def get_velocities(self):
        return self.velocity

    def set_velocities(self, velocity):
        self.velocity = velocity

    def print_atom(self):
        str = "  {} {} {} {} {} {} {} {} {} {} \n".format(self.id,  self.molecule_tag, self.atom_type, self.q, self.x, self.y, self.z, self.nx, self.ny, self.nz)
        return str

    def print_velocity(self):
        str = " {} {} {} {} \n".format(self.id, self.velocity[0], self.velocity[1], self.velocity[2]) 
        return str