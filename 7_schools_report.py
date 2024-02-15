"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"

Display report for all universities that have a graduation rate for Women over 50%
Display report for all universities that have a total price for in-state students living off campus over $50,000
"""

import json

file_path = "/Users/nathangalindo/Documents/Programming/Academic/mydictionaries/temp/school_data.json"

infile = open(file_path, "r")

list_of_schools = json.load(infile) # converts the json file into a python list

print(type(list_of_schools))

conference = "NCAA"
desired_division = "NAIA conference number football (IC2020)"
female_grad_rate_key = "Graduation rate  women (DRVGR2020)"
off_campus_key = "Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"
desired_schools = []
desired_values = [
    372,
    108,
    107,
    130
]

female_report = []
price_report = []

for school in list_of_schools:
    school_value = school[conference][desired_division]
    for value in desired_values:
        if school_value == value:
            desired_schools.append(school)

for school in desired_schools:
    if school[female_grad_rate_key] > 50:
        entry = dict(school_name=school["instnm"], grad_rate=school[female_grad_rate_key])
        female_report.append(entry)

for school in desired_schools:
    if school[off_campus_key] is not None:
        if school[off_campus_key] > 50_000:
            entry = dict(school_name=school["instnm"], total_price=school[off_campus_key])
            price_report.append(entry)

print("\nAll universities that have a graduation rate for Women over 50%:\n")
for school in female_report:
    print(f"University: {school["school_name"]}\nGraduation Rate for Women: {school["grad_rate"]}\n")

print("\nAll universities that have a total price for in-state students living off campus over $50,000:\n")
for school in price_report:
    print(f"University: {school["school_name"]}\nTotal price for in-state students living off-campus: {school["total_price"]}\n")
