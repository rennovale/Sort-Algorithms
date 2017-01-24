import sys

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
	if len(numbers) > 1:
		numbers_1 = numbers[0:int(len(numbers)/2)]
		numbers_2 = numbers[int(len(numbers)/2):]

		numbers_1 = mergesort(numbers_1)
		numbers_2 = mergesort(numbers_2)

		new_list = []
		while len(numbers_1) > 0 and len(numbers_2) > 0 :
			if numbers_1[0] < numbers_2[0]:
				new_list.append(numbers_1.pop(0))
			else:
				new_list.append(numbers_2.pop(0))

		while len(numbers_1) > 0:
			new_list.append(numbers_1.pop(0))
		while len(numbers_2) > 0:
			new_list.append(numbers_2.pop(0))

		return new_list
	return numbers
	
def quicksort(numbers, begin, end):
	def sort(numbers, left, right):
		pivo = numbers[end]
		wall = left - 1 
		for j in range(left, right):
			if pivo > numbers[j]:
				wall += 1
				numbers[j], numbers[wall] = numbers[wall], numbers[j]
		numbers[end], numbers[wall+1] = numbers[wall+1], numbers[end]
		return wall + 1, left, right

	if begin < end:
		wall, left, right = sort(numbers, begin, end)
		quicksort(numbers, left, wall - 1)
		quicksort(numbers, wall + 1, right)
	
def heapsort(numbers):
	def heap(numbers, begin, end):
		aux = numbers[begin]
		j = 2*begin + 1
		while j <= end:
			if j < end:
				if numbers[j] < numbers[j + 1]: # check the bigger son
					j += 1
			if aux < numbers[j]:
				numbers[begin], begin = numbers[j], j
				j = 2 * begin + 1
			else:
				j = end + 1 # force exit since aux is bigger than sons 
		numbers[begin] = aux
	
	for i in range((len(numbers)-1)/2, -1, -1):
		heap(numbers, i, len(numbers)-1)
		
	for i in range(len(numbers)-1, -1 , -1):
		numbers[i], numbers[0] = numbers[0], numbers[i]
		heap(numbers, 0, i - 1)


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
		list = mergesort(list)
	elif(sys.argv[1] == '4'):
		quicksort(list, 0, len(list)-1)
	elif(sys.argv[1] == '5'):
		heapsort(list)

	for each in list:
		print each


if __name__ == '__main__':
	main()
	

