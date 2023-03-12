kata = (0, 4, 132.42222, 10000, 12345.67)
# kata = (0, 4, 132.42222, 10000, 0.1234567)

def  write_power(number):
	if number >= 1:
		ln = len(str(number).split('.')[0])
		if ln > 1:
			integ = number / 10**(ln-1)
		if ln < 10:
			return(print('{:.2f}e+0{power}' .format(integ, power=ln-1), end=''))
		else:
			return(print('{:.2f}e+{power}' .format(integ, power=ln-1), end=''))
	else:
		ln = 0
		while number < 1:
			number *= 10
			ln += 1
		if ln < 10:
			return(print('{:.2f}e-0{power}' .format(number, power=ln), end=''))	
		else:
			return(print('{:.2f}e-{power}' .format(number, power=ln), end=''))	

print('module_0{mod}, ex_0{ex} : {dec}, ' .format(mod=kata[0], ex=kata[1], dec=round(kata[2], 2)), end='')
write_power(kata[3])
print(', ', end='')
write_power(kata[4])