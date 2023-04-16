//frist example for selection sort

// it should return number index
function select(nums, start){
	let length = nums.length;
	let minIndex = start;

	for (let i = start; i < length; i++){
		if(nums[i] < nums[minIndex]){
			minIndex = i;
		}
	}

	return minIndex;
}

function selectionSort(nums) {
	for(let i = 0; i < nums.length; i++){
		let minIndex = select(nums, i);
		let temp = nums[minIndex];
		nums[minIndex] = nums[i];
		nums[i] = temp;
	}
}