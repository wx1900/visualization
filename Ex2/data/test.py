import csv
import plotly.plotly as py

both = open('women.csv', 'r')
reader = csv.reader(both, delimiter=',')
HS = []
SC = []
BAp = []
BAo = []
GD = []
FI = 0
Year = []
for row in reader:
	if (FI == 0):
		FI = 1
		print(row[1])
		print('4:' + row[4] + ' 5:' + row[5] + '6:' + row[6] + '7:' + row[7] + '8:' + row[8])
		print('22:' + row[22] + '23:' + row[23] + '24:' + row[24] + '25:' + row[25] + '26:' + row[26])
		print('40:' + row[40] + '41:' + row[41] + '42:' + row[42] + '43:' + row[43] + '44:' + row[44])
		
	else:
		x = 4
		for i in range(0, 5):
			for j in range(0, 3):
				print(str(x+i+j*18) + row[x+i+j*18] )
				if row[x + i + j * 18] == 'NA':
					print(x+i+j*18)
					row[x + i + j * 18] = 0
		Year.append(row[1])
		HS.append(float(row[4]) + float(row[22]) + float(row[40]))
		SC.append(float(row[5]) + float(row[23]) + float(row[41]))
		BAp.append(float(row[6]) + float(row[24]) + float(row[42]))
		BAo.append(float(row[7]) + float(row[25]) + float(row[43]))
		GD.append(float(row[8]) + float(row[26]) + float(row[44]))

# with open('both_sexes_education.csv', 'w') as csvfile:
# 	writer = csv.writer(csvfile, delimiter=',')
# 	for i in range(Year):
# 		writer.writerow(Year[i] + ',')
with open('women_education.csv', 'w') as file:
	file.write('year,HS,SC,BAp,BAo,GD\n')
	for i in range(len(Year)):
		file.write(str(Year[i]) + ',' + str(HS[i]) + ',' + str(SC[i]) + ',' + str(BAp[i]) + ',' + str(BAo[i]) + ',' + str(GD[i]) + '\n')

