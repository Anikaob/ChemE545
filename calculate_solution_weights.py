def calculate_solution_weights(molecular_weights, solutions_needed):
    for i in range(len(solutions_needed)):
        chemical, concentration = solutions_needed[i].split('-')
        # take off the M from concentration and convert to float
        concentration = concentration[:-1]
        if chemical in molecular_weights:
            solutions_needed[i] = f"{chemical}-{concentration}-{molecular_weights[chemical]*float(concentration)}"
        else:
            solutions_needed[i] = f"{chemical}-{concentration}-unknown"
    return solutions_needed
