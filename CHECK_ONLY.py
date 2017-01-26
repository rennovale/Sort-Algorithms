def main():
	list = []
	while(True):
		try:
			x = input()
			list.append(int(x))
		except(EOFError):	
			break
			
	list = list[1:]
	list.sort()
	
	for each in ['1', '2', '3', '4', '5']:
		f = open('out' + each + '.txt', 'r')
		list2 = f.readlines()
		
		for i in range (len(list2)):
			list2[i] = int(list2[i].replace('\n', ''))
		
		if list== list2:
			print('(' + each + ') - Okey')
		else:
			print 'Error!'

if __name__ == '__main__':
	main()
