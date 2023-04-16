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


//next example

function findIndex(nums) {
	let minIndex = 0;

	for(let i = 0; i < nums.length; i++){
		if(nums[i] < nums[minIndex]){
			minIndex = i
		}
	}

	return minIndex;
}

function swapIndex(nums) {
	let length = nums.length;
	let newNums = []
	for(let i = 0; i < length; i++){
		let minIndex = findIndex(nums);
		newNums.push(nums.splice(minIndex, 1)[0]);
	}

	return newNums;
}
