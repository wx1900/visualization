import csv
import plotly.plotly as py

both = open('men.csv', 'r')
reader = csv.reader(both, delimiter=',')

FI = 0
header = []
line = []
for row in reader:
	if (FI == 0):
		FI = 1
		with open('men_marriage.csv', 'w') as file:
			for i in range(0, len(row)-1):
				file.write(row[i] + ',')
			file.write(row[len(row)-1] + '\n')	
	else:
		for i in range(len(row)):
			if row[i] == 'NA':
				row[i] = 1
			try:
				if (0.0 < float(row[i]) < 1.0):
					row[i] = 1.0 - float(row[i])
			except Exception as e:
				continue
		with open('men_marriage.csv', 'a') as file:
			for i in range(0, len(row)-1):
				file.write(str(row[i]) + ',')
			file.write(str(row[len(row)-1]) + '\n')

