import csv

with open('', mode='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['', '', ''])
    employee_writer.writerow(['', '', ''])