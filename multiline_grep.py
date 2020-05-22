#multiline grep

def catch(lines):
	flag = False
	i = 0
	for i in range(len(lines)):
		if 'Serial Number: SN3321123210' in line[i]:
			flag = True

			if flag:
				for j in range( 20):
					if 'BLOB' in lines [i + j]:
						print (lines[i+j])
						flag =False
						break

				i = i + j
				flag = False		


f = open('shad1.log')
a = f.read()
f.close()
b = a.split('\n')
catch(b)

