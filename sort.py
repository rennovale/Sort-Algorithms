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

