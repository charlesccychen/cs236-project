
labels = ['hen', 'traffic_light', 'dock', 'monarch', 'gar', 'chow', 'whistle', 'killer_whale', 'diamondback', 'malinois', 'starfish', 'rocking_chair', 'bee', 'liner', 'cradle', 'Irish_terrier']
labels_l2 = ['edentate', 'clock', 'breathing_device', 'summer_squash', 'pan', 'hawk', 'pelagic_bird', 'strongbox', 'shark', 'turnstone', 'machine', 'fabric', 'spitz', 'door', 'terrier', 'eraser', 'farm_building', 'theater', 'mastiff', 'pistol', 'trouser', 'newt', 'wall_unit', 'pinscher', 'coffee_maker', 'clip', 'sea_turtle', 'place_of_worship', 'cabinet', 'lamp', 'finch', 'egret']
labels_l3 = ['building','toy_dog','adornment','toothed_whale','ball','visual_signal','plant','digital_computer','aquatic_bird','fruit','fastener','electronic_device','sweater','boa','dog','lever','wagon','top','opener','paper','home_appliance','appliance','associate','food','anseriform_bird','crustacean','contestant','musical_instrument','feline','mask','cat','vegetable']
assert len(set(labels+labels_l2+labels_l3)) == len(labels+labels_l2+labels_l3)

for label in (labels_l2 + labels_l3):
	experiment_name = 'l23-imagenetglove13epochs-%s' % label
	contents = 'cd /cluster/project; python sample_pixelcnnpp.py --train 0 --dataset imagenet32 --output_dir outputs/samples2x6-%s --model_checkpoint outputs/pixelcnn-glove-imagenet32/models/epoch_12.pt --conditioning glove --label %s; mv outputs/samples2x6-%s/samples/0000000000001.png outputs/samples2x6-%s/' % (experiment_name, label, experiment_name, experiment_name)
	open('/cluster/jobs/new/a-%s' % experiment_name, 'w').write(contents)

for label in (labels_l2 + labels_l3):
	experiment_name = 'l23-imagenetbert13epochs-%s' % label
	contents = 'cd /cluster/project; python sample_pixelcnnpp.py --train 0 --dataset imagenet32 --output_dir outputs/samples2x6-%s --model_checkpoint outputs/pixelcnn-bert-imagenet32/models/epoch_12.pt --conditioning bert --label %s; mv outputs/samples2x6-%s/samples/0000000000001.png outputs/samples2x6-%s/' % (experiment_name, label, experiment_name, experiment_name)
	open('/cluster/jobs/new/b-%s' % experiment_name, 'w').write(contents)
