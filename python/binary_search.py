#it should return target index if target in arr
def binary_search(arr: list, target: int) -> int:
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

