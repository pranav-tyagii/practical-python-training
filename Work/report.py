# report.py
#
# Exercise 2.4
import csv
file = r"C:\Users\pranav.tyagi\Downloads\Training\practical-python-training\Work\Data\portfolio.csv"
file_prices = r"C:\Users\pranav.tyagi\Downloads\Training\practical-python-training\Work\Data\prices.csv"
def read_portfolio(filename):
    '''Create the tuple for the give data of a portfolio file'''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            portfolio += (row[0], row[1])
    return portfolio
print(read_portfolio(file))

def read_prices(filename):
    dict = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            dict[row[0]] = row[1] 
    return rows
print(read_prices(file_prices))