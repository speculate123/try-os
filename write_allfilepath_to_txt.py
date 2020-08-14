import os
import glob

fishdir = 'home/abc/darknet_fish/fish_data'
filename = glob.glob(os.path.join(fishdir, 'good_test/*.jpg'))
with open('test.txt', 'w') as f:
  for i in range(len(filename)):
    f.write(filename[i] + '\n')
