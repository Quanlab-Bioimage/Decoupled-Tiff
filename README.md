# BioimageVision-SpeedTIF





批量快速读取Tif图像，当前支持
8 + Lzw/未压缩数据
16Bit + Lzw/未压缩数据
其他的数据类型暂未测试

环境
```
Python==3.8
```
构建
```
cd SpeedTifIOWhl
pip install SpeedTifIO-1.0-py3-none-any.whl
```
例子
```
import os
from SpeedTifIO import SpeedReadTifClass

if __name__ == '__main__':    
    path = r'H:\TDIA1302b002_DataSet11'
    ls = os.listdir(path)
    obj = SpeedReadTifClass()
    for name in ls:
        obj.AddPath(os.path.join(path, name))
    for name in ls:
        img = obj.GetImg()
        print(name, img.shape, img.max(), img.min())
```
**数据图**

**视频**
