# Decoupled-Tiff
## Hardware Requirements
**The library requires only about 16GB of RAW computer for minimum performance, and the following specifications are recommended for best performance**
* RAM: 128+ GB
* CPU: 8+ cores, over 3.50GHz/core

## Environmental requirements
* Operating system: windows （python == 3.8, DecTIFFIO-0.1.0-py3-none-any-win.whl)
* Operating system: ubuntu 22.04 (gcc 11.4.0, python 3.10.12, DecTIFFIO-0.1.0-py3-none-any-linux.whl)
* When writing pictures in batches, ensure that disk C has a large space. You are advised to write more than twice the size of each batch of pictures
  
## Scope of application
### Fast reading of TIF images in batches, currently supported:
* 8Bit + 2D
* 8Bit + 3D
* 16Bit + 2D
* 16Bit + 3D
* Other data types have not yet been tested   

### Fast writing of TIF images in batches, currently supported:
* 8Bit + 2D

* 8Bit + 3D

* 16Bit + 2D

* 16Bit + 3D

* Other data types have not yet been tested

### Fast loading of Bio-VS format  

## Test data
https://zenodo.org/record/8385040

## Install
```
cd DecTIFFIOWhl
pip install DecTIFFIO-0.1.0-py3-none-any.whl
```
## Demo
### Example Read
```
import os
from DecTIFFIO import DecReadTifClass

if __name__ == '__main__':    
    path = r'./'
    ls = os.listdir(path)
    obj = DecReadTifClass()
    for name in ls:
        obj.AddPath(os.path.join(path, name))
    for name in ls:
        img = obj.GetImg()
        print(name, img.shape, img.max(), img.min())
```
### Example Write
**In the example of quick graph writing, the data is generated randomly and the generation speed is slow. Please wait. When "StartWrite" is printed, the data generation ends and the quick graph writing begins**
```
import os, time
from os.path import join
from DecTIFFIO.DecWriteTif import DecWriteClass
import numpy as np

if __name__ == '__main__':
    # Saved file path. Need to modify
    savePath = r'E:\SpeedWriteTifTestData'
    '''random images'''
    # random images number
    imgNumber = 20
    os.makedirs(savePath, exist_ok=True)
    imgLs = []
    for i in range(imgNumber):
        imgLs.append(np.random.randint(255, size=(32000, 40000), dtype=np.uint8))
    '''Start Speed Write'''
    print('StartWrite')
    writeObj = DecWriteClass()
    s1 = time.time()
    for ii in range(imgNumber):
        writeObj.AddPath(join(savePath, str(ii).zfill(5) + '.tif'), imgLs[ii])
    for ii in range(imgNumber):
        add = writeObj.WriteOk()
        name = os.path.basename(add)
        print(name, 'Finish!')
    print('TotalTime: ', time.time() - s1)
    writeObj.Close()
```
### Example Load of Bio-VS format
```
from DecTIFFIO import BVReader
import time

if __name__ == '__main__':
    bv_cfg = r'E:\ZHM_BV\config.cfg'
    readObj = BVReader()
    minx = 0
    maxx = 500
    miny = 0
    maxy = 500
    minz = 0
    maxz = 500
    level = 0
    readObj.addROIWork(bv_cfg, level, minx, maxx, miny, maxy, minz, maxz)
    img = readObj.getROIResult()
    del img
```
## Result
This read and write method can maximize the efficiency of disk and CPU, and achieve efficient and fast reading and writing Tif images.

## Video Read
[The video for fast reading images](https://github.com/QuantingweiImage/BioimageVision-SpeedTIFIO/assets/41601635/c5f85bf8-ab4e-4c8c-a2a1-713db3d16004)
## Video Write
[The video for fast Writing images](https://github.com/Quanlab-Bioimage/BioimageVision-SpeedTIFF/assets/41601635/34a59c19-3ddc-47e2-bc6a-25acfa97d2c3)

## Notes

The API for load of Bio-VS format on linux version is coming soon.

## Technique Help
quxuzhong@hust.edu.cn
