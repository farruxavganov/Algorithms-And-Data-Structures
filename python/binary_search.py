#it should return target index if target in arr
def binary_search(arr: list[int], target: int) -> int:
	"""Binary search algorithm for int values"""
	left = 0
	right = len(arr) - 1
	
	while left <= right:
		mid = (left + right) // 2
		guess = arr[mid]
		
		if guess == target:
			return mid
		if guess <= target:
			left = mid + 1
			continue
		right = mid - 1
		
	return -1 #if value none in arr

#sorted array
arr = [1,3,4,5,6]

#it should return index 3
result = binary_search(arr, 5)
print(result)
