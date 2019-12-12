import os

labels = ['hen', 'traffic_light', 'dock', 'monarch', 'gar', 'chow', 'whistle', 'killer_whale', 'diamondback', 'malinois', 'starfish', 'rocking_chair', 'bee', 'liner', 'cradle', 'Irish_terrier']

for i in range(13):
	for label in labels:
		# contents = 'cd /cluster/project; python sample_pixelcnnpp.py --train 0 --dataset imagenet32 --output_dir outputs/samples2x6-imagenetbert13epochs-%s --model_checkpoint outputs/pixelcnn-bert-imagenet32/models/epoch_12.pt --conditioning bert --label %s' % (label, label)
		# contents = 'cd /cluster/project; python sample_pixelcnnpp.py --train 0 --dataset imagenet32 --output_dir outputs/samples2x6-imagenetglove13epochs-%s --model_checkpoint outputs/pixelcnn-glove-imagenet32/models/epoch_12.pt --conditioning glove --label %s' % (label, label)
		# contents = 'cd /cluster/project; python sample_pixelcnnpp.py --train 0 --dataset imagenet32 --output_dir outputs/samples2x6-imagenetglove2epochs-%s --model_checkpoint outputs/pixelcnn-glove-imagenet32/models/epoch_1.pt --conditioning glove --label %s' % (label, label)
		epochs = i + 1
		if epochs in (2, 13):
			continue
		full_experiment_name = 'samples2x6-imagenetbert%depochs-%s' % (epochs, label)
		if os.path.exists('outputs/%s' % full_experiment_name):
			continue
		contents = 'cd /cluster/project; python sample_pixelcnnpp.py --train 0 --dataset imagenet32 --output_dir outputs/%s --model_checkpoint outputs/pixelcnn-bert-imagenet32/models/epoch_%d.pt --conditioning bert --label %s; mv outputs/%s/samples/0000000000001.png outputs/%s/' % (full_experiment_name, i, label, full_experiment_name, full_experiment_name)
		open('/cluster/jobs/new/z-%s' % full_experiment_name, 'w').write(contents)


for i in range(13):
	for label in labels:
		# contents = 'cd /cluster/project; python sample_pixelcnnpp.py --train 0 --dataset imagenet32 --output_dir outputs/samples2x6-imagenetbert13epochs-%s --model_checkpoint outputs/pixelcnn-bert-imagenet32/models/epoch_12.pt --conditioning bert --label %s' % (label, label)
		# contents = 'cd /cluster/project; python sample_pixelcnnpp.py --train 0 --dataset imagenet32 --output_dir outputs/samples2x6-imagenetglove13epochs-%s --model_checkpoint outputs/pixelcnn-glove-imagenet32/models/epoch_12.pt --conditioning glove --label %s' % (label, label)
		# contents = 'cd /cluster/project; python sample_pixelcnnpp.py --train 0 --dataset imagenet32 --output_dir outputs/samples2x6-imagenetglove2epochs-%s --model_checkpoint outputs/pixelcnn-glove-imagenet32/models/epoch_1.pt --conditioning glove --label %s' % (label, label)
		epochs = i + 1
		if epochs in (2, 13):
			continue
		full_experiment_name = 'samples2x6-imagenetglove%depochs-%s' % (epochs, label)
		if os.path.exists('outputs/%s' % full_experiment_name):
			continue
		contents = 'cd /cluster/project; python sample_pixelcnnpp.py --train 0 --dataset imagenet32 --output_dir outputs/%s --model_checkpoint outputs/pixelcnn-glove-imagenet32/models/epoch_%d.pt --conditioning glove --label %s; mv outputs/%s/samples/0000000000001.png outputs/%s/' % (full_experiment_name, i, label, full_experiment_name, full_experiment_name)
		open('/cluster/jobs/new/z-%s' % full_experiment_name, 'w').write(contents)
