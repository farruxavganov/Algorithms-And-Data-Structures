//it should return target index
function binarySearch(arr, target) {
	let left = 0;
	let right = arr.length - 1;

	while(left <= right){
		let mid = Math.floor((left + right) / 2);
		let guess = arr[mid];

		if(guess === target)
			return mid

		if(guess < target){
			left = mid + 1;
			continue
		}

		right = mid - 1;
	}

	return -1
}