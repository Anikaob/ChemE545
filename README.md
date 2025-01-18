# ChemE545 HW1
### Anika O'Brian
This repository contains two Python utility functions for chemical engineering calculations and data extraction.
## Functions
### 1. extract_parameter
This function extracts specific parameters from unit operations data. It takes a unit operation name, parameter name, and index as inputs and returns a formatted string containing the value.
Usage:
provide some unit operations data and then use something similar to the following line
result = extract_parameter("distillation_column", "temperature", 1)
This will Return: "distillation_column_temperature_160"

Parameters:
unit_name (str): Name of the unit operation (e.g., "distillation_column", "reactor")
parameter_name (str): Name of the parameter to extract (e.g., "temperature", "pressure")
index (int): Index of the value to retrieve from the parameter list

### 2. calculate_solution_weights
This function calculates the weight of chemicals needed for preparing solutions of specific concentrations.

You need to provide specific Parameters:
molecular_weights (dict): Dictionary of chemicals and their molecular weights
solutions_needed (list): List of strings in the format "chemical-concentrationM"

It will return:
Modified list where each entry is formatted as "chemical-concentration-weight"
Weight is calculated as molecular_weight * concentration
If chemical is not found in molecular_weights, weight is replaced with "unknown"

## Notebook
You can also use the jupyter notebook provided to use the functions described above. You will also find example inputs and tests to demonstrate the intended output.
