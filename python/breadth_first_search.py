from collections import deque
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def is_that_seller(name: str) -> bool:
	return name[-1] == "m";

def search(graph: dict, name: str) -> bool:
	search_queue = deque()
	search_queue += graph[name]
	searched = []

	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if is_that_seller(person):
				print(f"{person} find")
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
	return False

print(search(graph, "you"))