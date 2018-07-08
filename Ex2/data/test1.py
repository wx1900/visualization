import csv
import plotly.plotly as py

both = open('both_sexes.csv', 'r')
reader = csv.reader(both, delimiter=',')
white = []
black = []
hispan = []

FI = 0
for row in reader:
	if (FI == 0):
		FI = 1
		print('9:' + row[9] + ' 10:' + row[10] + '11:' + row[11])
		print('27:' + row[27] + '28:' + row[28] + '29:' + row[29])
		print('45:' + row[45] + '46:' + row[46] + '47:' + row[47])
		
	else:
		x = 9
		for i in range(0, 5):
			for j in range(0, 3):
				print(str(x+i+j*18) + row[x+i+j*18] )
				if row[x + i + j * 18] == 'NA':
					print(x+i+j*18)
					row[x + i + j * 18] = 0
		# Year.append(row[1])
		white.append(float(row[9]) + float(row[27]) + float(row[45]))
		black.append(float(row[10]) + float(row[28]) + float(row[46]))
		hispan.append(float(row[11]) + float(row[29]) + float(row[47]))

# with open('both_sexes_education.csv', 'w') as csvfile:
# 	writer = csv.writer(csvfile, delimiter=',')
# 	for i in range(Year):
# 		writer.writerow(Year[i] + ',')
with open('both_sexes_race.csv', 'w') as file:
	file.write('year,white,black,hispanic\n')
	for i in range(len(white)):
		file.write(str(white[i]) + ',' + str(black[i]) + ',' + str(hispan[i]) + '\n')

