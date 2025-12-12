class AtomPosition:
    def __init__(self, atom_name, x, y, z):
        self.name = atom_name
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)


def load_data():
    with open('animate_coords', 'r') as file:
        lines = file.readlines()
        atom_number = int(lines[1])
        res = [[]]
        iteration_number = 0
        for i in range(2, len(lines)):
            try:
                atom_number, x, y, z = lines[i].split(' ')
                # print(atom_number, x, y, z, iteration_number)
                atom = AtomPosition(atom_number, x, y, z)
                res[iteration_number].append(atom)
            except ValueError as err:
                # print("new line")
                iteration_number += 1
                res.append([])
        return res
    

if __name__ == '__main__':
    print(load_data())