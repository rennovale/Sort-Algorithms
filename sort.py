import sys
import timeit

def selectionsort(numbers):
	smaller = 0

	for i in xrange(len(numbers)):
		smaller = i 
		for j in xrange(smaller, len(numbers)):
			if numbers[smaller] > numbers[j]:
				smaller = j 
		numbers[smaller], numbers[i] = numbers[i], numbers[smaller]

def insertionsort(numbers):
	for i in xrange(1, len(numbers)):
		value = numbers[i]
		j = i
		while j > 0 and value < numbers[j-1]:
			numbers[j] = numbers[j-1]
			j -= 1
		numbers[j] = value

def mergesort(lista):
	if len(lista) > 1:

		meio = len(lista)/2

		listaDaEsquerda = lista[:meio]
		listaDaDireita = lista[meio:]

		mergesort(listaDaEsquerda)
		mergesort(listaDaDireita)

		i = 0
		j = 0
		k = 0

		while i < len(listaDaEsquerda) and j < len(listaDaDireita):

			if listaDaEsquerda[i] < listaDaDireita[j]:
				lista[k]=listaDaEsquerda[i]
				i += 1
			else:
				lista[k]=listaDaDireita[j]
				j += 1
			k += 1

		while i < len(listaDaEsquerda):

			lista[k]=listaDaEsquerda[i]
			i += 1
			k += 1

		while j < len(listaDaDireita):
			lista[k]=listaDaDireita[j]
			j += 1
			k += 1

	
def quicksort(numbers, begin, end):
	def sort(numbers, left, right):
		pivo = numbers[end]
		wall = left - 1 
		for j in xrange(left, right):
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
	
	for i in xrange((len(numbers)-1)/2, -1, -1):
		heap(numbers, i, len(numbers)-1)
		
	for i in xrange(len(numbers)-1, -1 , -1):
		numbers[i], numbers[0] = numbers[0], numbers[i]
		heap(numbers, 0, i - 1)
		
def map(x, in_min, in_max, out_min, out_max):
	return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def bucketsort(list):
	n = len(list)
	max_v = max(list)
	min_v = min(list)
	bucket_range = 1000
	bucket = [[]]* n

	for x in xrange(n):
		
		index = int(map(list[x], min_v, max_v, 0, n-1))
		bucket[index] = bucket[index] + [list[x]]

	for x in xrange(n):
		bucket[x].sort()
	list = []
	for i in xrange(n):
		for j in bucket[i]:
			list.append(j)
	return list



def countsort(list):

	def key(index, min_v):
		if (min_v >= 0):
			return index
		else:
			return index - min_v

	min_v = min(list)
	max_v = max(list)

	if min_v > 0:
		count_list = [0]*(max_v+1)
	else:
		count_list = [0]*(max_v - min_v + 1)

	for x in list:
		count_list[key(x, min_v)] += 1

	for each in xrange(1, len(count_list)):
		count_list[each] += count_list[each-1]

	output = [0]*(len(list))
	for each in list:
		k = key(each, min_v)
		count_list[k] -= 1
		output[count_list[k]] = each
	return output

def radix(list, exp):
	min_v = min(list)
	max_v = max(list)	

	count_list = [0]*10
	output = [0]*(len(list))

	for x in list:
		index = (x/exp)
		count_list[ (index)%10 ] += 1

	for each in xrange(1, 10):
		count_list[each] += count_list[each-1]


	for i in xrange(len(list)-1, -1, -1):
		index = (list[i]/exp)
		output[count_list[index%10]-1] = list[i]
		count_list[index%10] -= 1

	return output	

def radixsort(list):
	
	if(min(list) <0):
		n_list = []
		x = 0
		while x != len(list):
			if (list[x] < 0):
				n_list.append(-list.pop(x))
				x -= 1
			x += 1 
		max_v = max(n_list)
		exp = 1
		while (max_v/exp) > 0:
			n_list = radix(n_list,exp)
			exp *= 10		
		n_list.reverse()
		for x in xrange(len(n_list)):
			n_list[x] *= -1
			
	max_v = max(list)
	exp = 1
	min_v = min(list)
	n = len(list)		
	while (max_v/exp) > 0:
		list = radix(list,exp)
		exp *= 10	
	
	list = n_list + list
	return list

def main():
	list = []
	while(True):
		try:
			x = input()
			list.append(int(x))
		except(EOFError):	
			break
	
	
	list = list[1:]
	
	if(sys.argv[1] == '1'):
		selectionsort(list)
	elif(sys.argv[1] == '2'):
		insertionsort(list)
	elif(sys.argv[1] == '3'):
		mergesort(list)
	elif(sys.argv[1] == '4'):
		quicksort(list, 0, len(list)-1)
	elif(sys.argv[1] == '5'):
		heapsort(list)
	elif(sys.argv[1] == '6'):
		list = countsort(list)
	elif(sys.argv[1] == '7'):
		list = radixsort(list)
	elif(sys.argv[1] == '8'):
		list = bucketsort(list)
	
	for each in list:
		print each

if __name__ == '__main__':
	main()
	

