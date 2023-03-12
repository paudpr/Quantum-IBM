kata = (2019, 9, 25, 3, 30)

def date_formatter(date):
	if len(str(date[1])) != 2:
		print('0' + str(date[1]) + '/', end='')
	else:
		print(date[1] +  '/', end='')
	if len(str(date[2])) != 2:
		print('0' + str(date[2]) + '/', end='')
	else:
		print(str(date[2]) +  '/', end='')
	print(str(date[0]) + ' ', end='')
	if len(str(date[3])) != 2:
		print('0' + str(date[3]) + ':', end='')
	else:
		print(date[3] +  ':', end='')
	if len(str(date[4])) != 2:
		print('0' + str(date[4]))
	else:
		print(date[4])

date_formatter(kata)