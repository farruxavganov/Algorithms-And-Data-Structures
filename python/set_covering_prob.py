states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

def set_covering(stations: dict, states_needed: set) -> set:
	final_stations = set()
	while states_needed:
		states_covered = set()
		best_station = None
		for station, states_for_station in stations.items():
			covered = states_needed & states_for_station
			if len(covered) > len(states_covered):
				best_station = station
				states_covered = covered
		states_needed -= states_covered
		final_stations.add(best_station)
	return final_stations
		
	
	
print(set_covering(stations,states_needed))
