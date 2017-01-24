def selectionsort(numbers):
	smaller = 0

	for i in range(len(numbers)):
		smaller = i 
		for j in range(smaller, len(numbers)):
			if numbers[smaller] > numbers[j]:
				smaller = j 
		numbers[smaller], numbers[i] = numbers[i], numbers[smaller]

def insertionsort(numbers):
	for i in range(1, len(numbers)):
		value = numbers[i]
		j = i
		while j > 0 and value < numbers[j-1]:
			numbers[j] = numbers[j-1]
			j -= 1
		numbers[j] = value

def mergesort(numbers):
	pass
	
def quicksort(numbers):
	pass
	
def heapsort(numbers):
	pass

def main():
	list = []
	while(True):
		try:
			x = input()
			list.append(int(x))
		except(EOFError):	
			break
	
	if(sys.argv[1] == '1'):
		selectionsort(list)
	elif(sys.argv[1] == '2'):
		insertionsort(list)
	elif(sys.argv[1] == '3'):
		mergesort(list)
	elif(sys.argv[1] == '4'):
		quicksort(list)
	elif(sys.argv[1] == '5'):
		heapsort(list)

	for each in list:
		print each


if __name__ == '__main__':
	main()
	

