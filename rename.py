import os
from pathlib import Path

home = str(Path.home())
path = home + '/Desktop/ml/YOLOv3-Series/[part 4]OpenLabelling/bbox_txt'
# dirs = os.listdir(path)

n = 0


for image in os.scandir(path):
	os.rename(image.path, os.path.join(path, '{:03}.txt'.format(n)))
	n += 1