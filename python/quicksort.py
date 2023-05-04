from random import randrange

def quicksort(arr: list[int]) -> list:
	if len(arr) < 2:
		return arr
	pivot = arr.pop(randrange(len(arr)))
	left = [num for num in arr if num <= pivot]
	right =[num for num in arr if num > pivot]
		
	return quicksort(left) + [pivot] + quicksort(right)

