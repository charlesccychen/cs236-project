
labels = ['hen', 'traffic_light', 'dock', 'monarch', 'gar', 'chow', 'whistle', 'killer_whale', 'diamondback', 'malinois', 'starfish', 'rocking_chair', 'bee', 'liner', 'cradle', 'Irish_terrier']
for label in labels:
	# contents = 'cd /cluster/project; python sample_pixelcnnpp.py --train 0 --dataset imagenet32 --output_dir outputs/samples2x6-imagenetbert13epochs-%s --model_checkpoint outputs/pixelcnn-bert-imagenet32/models/epoch_12.pt --conditioning bert --label %s' % (label, label)
	contents = 'cd /cluster/project; python sample_pixelcnnpp.py --train 0 --dataset imagenet32 --output_dir outputs/samples2x6-imagenetglove13epochs-%s --model_checkpoint outputs/pixelcnn-glove-imagenet32/models/epoch_12.pt --conditioning glove --label %s' % (label, label)
	# contents = 'cd /cluster/project; python sample_pixelcnnpp.py --train 0 --dataset imagenet32 --output_dir outputs/samples2x6-imagenetglove2epochs-%s --model_checkpoint outputs/pixelcnn-glove-imagenet32/models/epoch_1.pt --conditioning glove --label %s' % (label, label)
	# contents = 'cd /cluster/project; python sample_pixelcnnpp.py --train 0 --dataset imagenet32 --output_dir outputs/samples2x6-imagenetbert2epochs-%s --model_checkpoint outputs/pixelcnn-bert-imagenet32/models/epoch_1.pt --conditioning bert --label %s; mv outputs/samples2x6-imagenetbert2epochs-%s/samples/0000000000001.png outputs/samples2x6-imagenetbert2epochs-%s/' % (label, label, label, label)
	open('/cluster/jobs/new/a-%s' % label, 'w').write(contents)
