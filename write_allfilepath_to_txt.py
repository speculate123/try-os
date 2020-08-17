import os
import glob
import random

datadir = '/mlsteam/lab/darknet/data_roaddamage/'

filename = glob.glob(os.path.join(datadir, 'Adachi/*.jpg'))

random.shuffle(filename)

split = int(len(filename)*0.9)

with open('train.txt', 'w') as f:
  for i in range(split):
    f.write(filename[i] + '\n')
    
with open('test.txt', 'w') as f:
  for i in range(len(filename)-split):
    f.write(filename[i+split] + '\n')
