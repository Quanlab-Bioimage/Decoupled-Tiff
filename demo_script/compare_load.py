import cpptiff
from libtiff import TIFF
import tifffile
import os
import time
from DecTIFFIO import DecReadTifClass


if __name__ == '__main__':
    type = 0
    path = r'./test_data_for_read'
    if type == 0:  ### read time for Dec-Tiff
        obj = DecReadTifClass()
        print('StartRead')
        frame = 153   # 153 for 10G, 291 for 20G, 408 for 30G, 532 for 40G, 762 for 60G, 990 for 80G.
        s1 = time.time()
        for i in range(frame):
            obj.AddPath(os.path.join(path, str(i) + '.tif'))
        for i in range(frame):
            # print('GetImg: ', name)
            img = obj.GetImg()
        print('Dec-Tiff TotalTime: ', time.time() - s1)
    elif type == 1:  ### read time for Cpp-Tiff
        s1 = time.time()
        i_start = 0
        i_end = 153
        for i in range(i_start, i_end):
            im = cpptiff.read_tiff(os.path.join(path, str(i) + '.tif'))
        print('Cpp-Tiff TotalTime: ', time.time() - s1)
    elif type == 2:  ### read time for Tifffile
        i_start = 0
        i_end = 153
        s1 = time.time()
        for i in range(i_start, i_end):
            tifffile.imread(os.path.join(path, str(i) + '.tif'))
        print('Tifffile TotalTime: ', time.time() - s1)
    elif type == 3:  ### read time for Libtiff
        i_start = 0
        i_end = 153
        s1 = time.time()
        for i in range(i_start, i_end):
            tif = TIFF.open(os.path.join(path, str(i) + '.tif'), mode='r')
            images = [image for image in tif.iter_images()]
        print('Libtiff TotalTime: ', time.time() - s1)
