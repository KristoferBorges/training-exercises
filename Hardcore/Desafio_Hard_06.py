tamanho = int(input("Tamanho: "))
c = 1
for i in range (0, tamanho):
	if i == 0:
		print(" " * (tamanho -i) + "*")
	elif i == 1:
		print(" " * (tamanho -i) + "*" * (i + 2))
	else:
		print(" " * (tamanho -i) + "*" * (i + c))
	c += 1