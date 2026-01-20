# Task 2

import csv

employees = ""

def read_employees():
    employee_data = {}
    rows = []
    counter = 0

    try:
        with open("../csv/employees.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if counter == 0:
                    employee_data["fields"] = row
                else:
                    rows.append(row)
                counter += 1
            employee_data["rows"] = rows
            return employee_data
    except Exception as e:
        print(e)
        return None
    

employees = read_employees()
print(employees)

# Task 3

def column_index(column_header):
    return employees["fields"].index(column_header)

employee_id_column = column_index("employee_id")

print(column_index("first_name"))
print(employee_id_column)

# Task 4

name_index = column_index("first_name")

def first_name(row_number):
    return employees["rows"][row_number][name_index]

# Task 5

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches=list(filter(employee_match, employees["rows"]))
    return matches

# Task 6 

def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

# Task 7

def sort_by_last_name():
    last_name_index = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_index])
    return employees["rows"]

sort_by_last_name()

# Task 8

def employee_dict(row):
    return dict(zip(employees["fields"][1:], row[1:]))

an_employee = employee_dict(employees["rows"][0])
print(an_employee)

# Task 9

def all_employees_dict():
    result = {}

    for row in employees["rows"]:
        employee_id = row[0]                 
        result[employee_id] = employee_dict(row)

    return result

all_employees = all_employees_dict()
print(all_employees)

# Task 10

import os

def get_this_value():
    return os.getenv("THISVALUE")
print(get_this_value())

# Task 11

import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("I love desserts")
print(custom_module.secret)

# Task 12

def read_csv_file(file_path):
    with open(file_path, "r") as file:
        reader = csv.reader(file)

        fields = next(reader)
        rows = []

        for row in reader:
            rows.append(tuple(row))

    return {
        "fields": fields,
        "rows": rows
    }

def read_minutes():
    minutes1 = read_csv_file("../csv/minutes1.csv")
    minutes2 = read_csv_file("../csv/minutes2.csv")

    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

# Task 13

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    combined = set1.union(set2)
    return combined

minutes_set = create_minutes_set()

# Task 14

from datetime import datetime

def create_minutes_list():
    minutes_list = list(
        map(
            lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
            minutes_set
        )
    )
    return minutes_list

minutes_list = create_minutes_list()
print(minutes_list)

# Task 15

def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    
    converted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_list))
    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        for row in converted_list:
            writer.writerow(row)
            return converted_list

final_minutes_list = write_sorted_list()
print(final_minutes_list)