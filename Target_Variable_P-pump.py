import csv
import pandas as pd



def function_for_target_variable():
    target_variable = 1
    difference = 10
    power = 0
    count = 0
    while power <= 8:
        for target_variable in range (1,10):
            for count in range (117):
                print(target_variable * pow(difference, power))
        power = power + 1

csv_file = "step_microliter_ramp_profile.csv"

column_index = 1

new_column_values = [function_for_target_variable()]


# Read the existing data from the CSV file
existing_data = []
with open(csv_file, "r") as file:
    reader = csv.reader(file)
    existing_data = list(reader)

for i, row in enumerate(existing_data):
    if i == 0:  # Skip the header row
        continue
    row[column_index] = new_column_values[i]  # Assuming the new values list matches the number of data rows

# Write the updated data back to the CSV file
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(existing_data)
  
    

    
