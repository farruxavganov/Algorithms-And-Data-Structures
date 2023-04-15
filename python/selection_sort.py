#frist example for selection sort

#it should return min number index in list
def select(nums: list, start: int) -> int:
	length = len(nums)
	pos = start
	for i in range(start, length):
		if nums[i] < nums[pos]:
			pos = i

	return pos

def selection_sort(nums: list) -> None:
	for i in range(len(nums)):
		pos = select(nums, i)
		nums[i], nums[pos] = nums[pos], nums[i]


#next example for selection sort
def findIndex(nums: list) -> int:
	length = len(arr)
	pos = 0
	for i in range(1, length):
		if nums[i] < nums[pos]:
			pos = i

	return pos

def selectionSort(nums: list) -> list:
	newList = []

	for i in range(len(nums)):
		pos = findIndex(nums)
		newList.append(nums.pop(pos))

	return newList

