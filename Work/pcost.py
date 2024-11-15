# pcost.py
#
# Exercise 1.27
file_path = r"C:\Users\pranav.tyagi\Downloads\Training\practical-python-training\Work\Data"
def py_cost(file, file_name):
    f = open(file+file_name, 'rt')
    Total_cost = 0
    headers = next(f)
    for line in f:
        row = line.split(',')
        Total_cost += int(row[1]) * float(row[2])
    return Total_cost
print('total cost', py_cost(file_path, r"\portfolio.csv"))
import gzip
dir_portofolio_gz = r"C:\Users\pranav.tyagi\Downloads\Training\practical-python-training\Work\Data\portfolio.csv.gz"
with gzip.open(dir_portofolio_gz, 'rt') as f:
    for line in f:
        print(line, end = '')
# Checking the error handling for the missing values files 
print(py_cost(file_path, r"\missing.csv"))
#Creating the tuple 
t = ('google', 100, 230.445)
