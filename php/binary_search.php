<?php
	function binarySearch($arr, $target) {
		$low = 0;
		$high = count($arr) - 1;
		while ($low <= $high) {
			$mid = floor(($high + $low) / 2);
			$guess = $arr[$mid];

			if ($guess == $target) {
				return $mid;
			}

			if ($guess < $target) {
				$low = $mid + 1;
				continue;
			}

			$high = $mid - 1;
		}

		return -1;
	}
?>