<?php
	function select(&$nums, $start)
	{
		$len = count($nums);
		$minIndex = $start;

		for ($i=$start; $i < $len; $i++) { 
			if ($nums[$i] < $nums[$minIndex]) {
				$minIndex = $i;
			}
		}

		return $minIndex;
	}

	function selectionSort(&$nums)
	{
		for ($i=0; $i < count($nums); $i++) { 
			$minIndex = select($nums, $i);
			$temp = $nums[$i];
			$nums[$i] = $nums[$minIndex];
			$nums[$minIndex] = $temp;
		}
	}
?>