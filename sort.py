def selectionsort(numbers):
	smaller = 0

	for i in range(len(numbers)):
		smaller = i 
		for j in range(smaller, len(numbers)):
			if numbers[smaller] > numbers[j]:
				smaller = j 
		numbers[smaller], numbers[i] = numbers[i], numbers[smaller]

