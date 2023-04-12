#include <stdio.h>

// function declaration
int binarySearch(int arr[], int target, int low, int high);

int main(){
	int arr[] = {1,2,3,4,5,6};

	int length = sizeof(arr) / sizeof(arr[0]);
	int result = binarySearch(arr, -88, 0, length - 1);
	
	printf("%d", result);
	return 0;
}

//function declaration
int binarySearch(int arr[], int target, int low, int high){

	while(low <= high){
		int mid = low + (high - low) / 2;
		int guess = arr[mid];

		if(guess == target){
			return mid;
		}

		if(guess < target){
			low = mid + 1;
			continue;
		}

		high = mid - 1;
	}

	return -1;
}