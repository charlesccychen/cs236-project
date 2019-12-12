def load_clsloc(path):
	lines = open(path).read().split('\n')
	result = []
	for line in lines:
		if not line:
			continue
		result.append(line.split(' ')[2])
	return result

l1 = load_clsloc('datasets/ImageNet32/map_clsloc.txt')
l2 = load_clsloc('datasets/ImageNet32/map_clsloc2.txt')
l3 = load_clsloc('datasets/ImageNet32/map_clsloc3.txt')

assert len(l1) == len(l2) and len(l2) == len(l3)

import collections
import json

children = collections.defaultdict(set)
for i in range(len(l1)):
	l1_value = l1[i]
	l2_value = l2[i]
	l3_value = l3[i]
	children[l3_value].add(l2_value)
	children[l3_value].add(l1_value)
	children[l2_value].add(l1_value)
parents = collections.defaultdict(set)
for cat, childs in children.items():
	for child in childs:
		parents[child].add(cat)

for key in list(parents.keys()):
	parents[key] = list(parents[key])
open('parents.json', 'w').write(json.dumps(parents))
