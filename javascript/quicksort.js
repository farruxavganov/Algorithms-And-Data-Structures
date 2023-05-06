function quicksort(arr){
	if(arr.length < 2)
		return arr;

	let pivot = arr.splice(Math.floor(Math.random() * arr.length),1)[0];
	let left = [];
	let right = [];
	for (let i = 0; i < arr.length; i++){
		if(pivot > arr[i])
			left.push(arr[i]);
		else
			right.push(arr[i]);
	}
		
	return [...quicksort(left), pivot, ...quicksort(right)];
}