import csv

with open('../csv/employees.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

employee_names = [f"{row[1]} {row[2]}" for row in rows[1:]]

employee_names_e = [name for name in employee_names if "e" in name]

print(employee_names)
print(employee_names_e)