import numpy as np


def lennard_johnson_potential(r, eps=0.0103, sigma=0.3405):
    """
        @brief Calculates the Lennard Johnson potential between 2 particles with the same epsilon and sigma values
        @param r Difference between 2 particles positions?
        @param eps Epsilon parameter in the potential formula, a table value for an atom
        @param sigma Sigma parameter in the potential formula, a table value for an atom
        @returns Potential energy value between 2 particles
    """
    if r < 1e-13:
        r = 1e-9
    return 4*eps*((sigma / r)**12 - (sigma / r)**6)


def total_potential_for_particle(rs: np.ndarray, particle_index: int):
    """
        @brief Calculates the total pair potential for a particle in the multi-particle system
        @param rs Array of all particles positions
        @param particle_index Defines which particle's potential to find
        @returns The total pair potential
    """
    distances = [abs(r - rs[particle_index]) for i, r in enumerate(rs) if i != particle_index]
    potentials = [lennard_johnson_potential(d) for d in distances]
    return np.sum(potentials)


def leapfrog_solve(
    r0: list[float] | np.ndarray, time_step = 1e-8, 
    iterations = 500, capture_every_nth_iteration = 10,
    masses:list[float] | np.ndarray | float = 39.962384
    ):
    """
        @brief Evolves the multi-particle system through time
        @param r0 Particles starting position
        @param time_step Time step, h in the formula
        @param iterations This many iterations will be done before exiting
        @param capture_every_nth_iteration Every nth iteration positions of the particles will be stored for returning. Time step between them
                is time_step * capture_every_nth_iteration
        @param masses Masses of particles, just leave it be, it's argons mass right now
        @returns List of all particle positions
    """
    size = len(r0)

    if isinstance(masses, float) or isinstance(masses, int):
        masses = np.full(size, masses)
    elif isinstance(masses, list):
        masses = np.array(masses)

    rs = np.array(r0)
    vs = np.zeros(size) # half a step in front of rs, due to the algorithm

    # This is how he explained, right?
    captured_rs = []
    captured_us = []
    # for i in range(iterations):
    #     rs = rs + time_step * vs

    #     potentials = [total_potential_for_particle(rs, i) for i in range(size)]
    #     momentary_forces = time_step * (potentials / masses)
    #     vs = vs + momentary_forces

    #     if i % capture_every_nth_iteration == 0:
    #         captured_rs.append(rs)

    # # This is how internet tells me it's done. At least for a kick-drift-kick from
    # # v_{i + 1/2} = v_i + 1/2 a_i \delta t
    # # x_{i + 1} = x_i + x_{i + 1/2} \delta t
    # # v_{i + 1} = v_{i + 1/2} + 1/2 a_{i+1} \delta t
    potentials = [total_potential_for_particle(rs, i) for i in range(size)]
    momentary_forces = 0.5 * time_step * (potentials / masses)
    vs = momentary_forces
    for i in range(iterations):
        rs = rs + time_step * vs

        potentials = np.array([total_potential_for_particle(rs, i) for i in range(size)])
        momentary_forces = time_step * (potentials / masses)
        vs = vs + momentary_forces

        if i % capture_every_nth_iteration == 0:
            captured_rs.append(rs)
            captured_us.append(sum(potentials))

    return captured_rs, captured_us