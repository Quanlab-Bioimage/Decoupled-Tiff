import cpptiff
from libtiff import TIFF
import tifffile
import os
import time
from DecTIFFIO.DecWriteTif import DecWriteClass


if __name__ == '__main__':
    imgNumber = 105
    img = tifffile.imread('./test_data_for_read/0.tif')
    type = 0
    if type == 0:  ### write time for Dec-Tiff
        savePath ='./Dec-Tiff'
        os.makedirs(savePath)
        imgLs = []
        writeObj = DecWriteClass()
        for i in range(imgNumber):
            imgLs.append(img)
        s1 = time.time()
        for ii in range(imgNumber):
            writeObj.AddPath(os.path.join(savePath, str(ii).zfill(5) + '.tif'), imgLs[ii])
        for ii in range(imgNumber):
            add = writeObj.WriteOk()
            name = os.path.basename(add)
        print('Dec-Tiff TotalTime: ', time.time() - s1)
        writeObj.Close()
    elif type == 1:   ### write time for Cpp-Tiff
        savePath = './Cpp-Tiff'
        os.makedirs(savePath)
        s1 = time.time()
        for ii in range(imgNumber):
            name = os.path.join(savePath, str(ii).zfill(5) + '.tif')
            cpptiff.write_tiff(name, img, compression="lzw")
        print('Cpp-Tiff TotalTime: ', time.time() - s1)
    elif type == 2:   ### write time for Tifffile
        savePath = './Tifffile'
        os.makedirs(savePath)
        s1 = time.time()
        for ii in range(imgNumber):
            tifffile.imwrite(os.path.join(savePath, str(ii).zfill(5) + '.tif'), img, compression='lzw')
        print('Tifffile TotalTime: ', time.time() - s1)
    elif type == 3:   ### write time for Libtiff
        savePath = './Libtiff'
        os.makedirs(savePath)
        s1 = time.time()
        for ii in range(imgNumber):
            tif = TIFF.open(os.path.join(savePath, str(ii).zfill(5) + '.tif'), mode='w')
            tif.write_image(img, compression='lzw', write_rgb=False)
            tif.close()
        print('Libtiff TotalTime: ', time.time() - s1)

