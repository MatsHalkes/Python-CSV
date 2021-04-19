import pandas

df = pandas.read_csv('hrdata.csv', 
index_col='Name'
purse_dates=['Hire Date'],
header=0,
names=['Empolyee', 'Hired', 'Salary', 'Sick Days']
)