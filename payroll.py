"""

Program: payroll.py
Project 4.12
Author: Brandon

Inputa a filename from the user and prints to terminal a report of the wages paid to the employees for a given period. Report is in tabular format with a header.
"""

# Take the input from the user
fileName = input("Please enter the filename to analyse >> ")

# Open the input file
inputFile = open(fileName, 'r')

# Print the report header
print("%-15s%-10s%-12s" % ("Name", "Hours", "Total Pay"))

# Read the data from the input file, calculate total pay and print info in tabular format
for line in inputFile:
	listData = line.split()
	name = listData[0]
	hours = int(listData[1])
	payRate = float(listData[2])
	totalPay = hours * payRate
	print("%-15s%-10d%-12.2f" % (name, hours, totalPay))