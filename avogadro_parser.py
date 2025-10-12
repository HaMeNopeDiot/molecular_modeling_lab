def read_file(filepath):
    res = []
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    atom_numbers = lines[0]
    comment = lines[1]
    for atom in lines[2:]:
        name, x, y, z = atom.split(' ')
        res.append((x, y, z))
    return res


def write_file(filepath, atom_names, atoms_coordinates, comment=''):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(len(atoms_coordinates))
        file.write(comment)
        for atom_coordinates, name in zip(atoms_coordinates, atom_names):
            file.write(f'{name} {atom_coordinates[0]} {atom_coordinates[1]} {atom_coordinates[2]}')