import csv

with open('hrdata_modified.csv') as f:
    reader = csv.reader(f)

    found = 0
    #success = 0

    empolyee = input('Enter employee name: ')

    for row in reader:
        if employee in row[0]:
            found = 1
            # in  row[4] == '99-999-9999':
            #       success = 1
    if found == 1:
        print('employee found')
        # if success == 1:
        #     print('Accecss Granted!')
        # else:
        #     print('Access denied!')
    else:
        print('Employee not found')