#include <stdio.h>

// function declars
int select(int nums[], int start, int size);
int selectionSort(int nums[], int size);

// main function
int main(){
	int arr[10] = {5,8,6,7,10,2,3,0,8,1};
	int size = sizeof(arr) / sizeof(arr[0]);

	selectionSort(arr, size);

	for (int i = 0; i < size; ++i)
	{
		printf("%d\n", arr[i]);
	}
	
	return 0;
}

// select index
int select(int nums[], int start, int size) {
	int minIndex = start;
	for(int i = start; i < size; i++)
	{
		if(nums[minIndex] > nums[i]){
			minIndex = i;
		}
	}

	return minIndex;
}

// sort array
int selectionSort(int nums[], int size) {
	for (int i = 0; i < size; ++i)
	{
		int minIndex = select(nums, i, size);
		int temp = nums[i];
		nums[i] = nums[minIndex];
		nums[minIndex] = temp;
	}
}