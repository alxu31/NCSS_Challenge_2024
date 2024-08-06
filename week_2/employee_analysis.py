import csv

data = []
with open("resources/employees.csv") as csvfile:
# with open("employees.csv") as csvfile:
    for row in csv.DictReader(csvfile):
        data.append(row)

h = 0
hName = ''
for row in data:
    service = int(row['yearsOfService'])
    if service > h:
        h = service
        hName = row['employeeName']
print(f"The longest serving employee is {hName} with {h} years of service.")
