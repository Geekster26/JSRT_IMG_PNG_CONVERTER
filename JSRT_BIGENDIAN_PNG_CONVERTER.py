# -*- coding: utf-8 -*-
"""
Created on Mon May  6 18:23:03 2019

@author: svs26
"""

import os
import numpy as np
import scipy as sci
import imageio
directory = 'C://Users//svs26//Downloads//jsrt-parser-master//jsrt-parser-master//All247images//'

for filename in os.listdir(directory):
    if filename.endswith(".IMG"):
        raw_image = np.fromfile(directory+filename, dtype=">i2").reshape((2048, 2048))
        raw_image = raw_image.astype(np.int, casting='safe')
        imageio.imwrite(directory+filename+str(".png"),raw_image)
        continue
    else:
        continue
