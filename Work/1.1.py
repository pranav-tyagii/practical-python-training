# sears.py

bill_thickness = 0.11 * 0.001  # Meters (0.11 mm)
sears_height = 442  # Height (meters)
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print("Number of days", day)
print("Number of bills", num_bills)
print("Final height", num_bills * bill_thickness)

s = "hello wordl "
# using the open we can read any file
with open(
    r"C:\Users\pranav.tyagi\Downloads\Training\practical-python-training\Work\Data\dowstocks.csv"
) as file:
    lines = file.readlines()
# Adding the path of the portfolio.csv file to read

dir_portofolio = r"C:\Users\pranav.tyagi\Downloads\Training\practical-python-training\Work\Data\portfolio.csv"
with open(dir_portofolio) as file:
    lines = file.read()
#print(lines)

# with open(dir_portofolio) as file:
#     for line in file:
#         print(line , end='')
f = open(dir_portofolio, 'rt')
headers = next(f)
print(headers)
