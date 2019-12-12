cat datasets/ImageNet32/map_clsloc2.txt | cut -d' ' -f3,3 | sort | uniq | sort -R | head -n 32 > 2
cat datasets/ImageNet32/map_clsloc3.txt | cut -d' ' -f3,3 | sort | uniq | sort -R | head -n 32 > 3
