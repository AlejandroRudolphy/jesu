def mas_adultos(cola_actual, m, s = []):
	if len(s) == m:
		return 
	else:
		for i in range(len(cola_actual)):
			cont = 0
			for k in range(len(cola_actual)):
				if cola_actual[i] < cola_actual[k]:
					cont += 1
			if len(cola_actual) == 0:
				break
			s.append(cont)
			cola_actual.pop(0)
			mas_adultos(cola_actual, m)
	return s		
cola_actual = [5,7,4,10,8,11]
m = len(cola_actual)
n_ = mas_adultos(cola_actual, m)
print(n_)