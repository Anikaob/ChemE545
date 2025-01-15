def extract_parameter(unit_name, parameter_name, index):
    if unit_name in unit_operations_data:
        if parameter_name in unit_operations_data[unit_name]:
            if index < len(unit_operations_data[unit_name][parameter_name]):
                return f"{unit_name}_{parameter_name}_{unit_operations_data[unit_name][parameter_name][index]}"
            else:
                return "Invalid input"
        else:
            return "Invalid input"
    else:
        return "Invalid input"
