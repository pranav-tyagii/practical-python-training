file_path = r"C:\Users\pranav.tyagi\Downloads\Training\practical-python-training\Work\Data\missing.csv"
def py_cost(file):
    f = open(file, 'rt')
    Total_cost = []
    headers = next(f)
    for line_no, line in enumerate(f):
        row = line.split(',')
        if row[0] == '' or row[1] == '' or row[2] == '':
            Total_cost += [line_no]
    return Total_cost


print(py_cost(file_path))