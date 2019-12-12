import numpy as np
import json

embeddings = {}
glove_file = 'datasets/glove.6B.300d.txt'
print('Reading Glove')
lines = open(glove_file, 'r').read().split('\n')
print('Read Glove into memory, processing lines')
for line in lines:
	if not line:
		continue
	parts = line.split(' ')
	token = parts[0].lower()
	embedding = np.array(parts[1:], dtype=np.float)
	embeddings[token] = embedding

del lines

embedding_data = {}
map_files = ['datasets/ImageNet32/map_clsloc.txt', 'datasets/ImageNet32/map_clsloc2.txt', 'datasets/ImageNet32/map_clsloc3.txt']
lines = []
for map_file in map_files:
	lines += open(map_file, 'r').read().split('\n')
lines += list('  %s' % s.replace(' ', '_') for s in ['car','bowed stringed instrument','snipe','mastiff','shop','cream','light','fastener','spaniel','domestic cat','hand glass','concoction','garment','bridge','cuckoo','chair','hound','vessel','reservoir','stony coral','swine','hymenopterous insect','phasianid'])
for line in lines:
	if not line:
		continue
	_, _, label = line.split(' ')
	tokens = label.lower().replace('-', '_').replace('\'s', '').replace('\'', '_').replace('__', '_').replace('__', '_').split('_')
	new_tokens = []
	for token in tokens:
		if not token in embeddings:
			print('ERROR: %s' % token)
			for i in range(3, len(token)):
				first, second = token[0:i], token[i:]
				if first in embeddings and second in embeddings:
					print('MANUALLY TOKENIZED: %r, %r' % (first, second))
					new_tokens.append(first)
					new_tokens.append(second)
					break
		else:
			new_tokens.append(token)
	print(new_tokens)
	embedding = np.zeros(300, dtype=np.float)
	for token in new_tokens:
		embedding += embeddings[token]
		embedding_data[token] = list(float(f) for f in embeddings[token])
	embedding_data[label] = list(float(f) for f in embedding)

open('datasets/ImageNet32/map_clsloc_synthesized_glove.json', 'w').write(json.dumps(embedding_data, indent=2))
