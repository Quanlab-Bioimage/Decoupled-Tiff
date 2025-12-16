# Demo script for comparison of Dec-Tiff, Cpp-Tiff, Tifffile, Libtiff

## Prerequisites for the demo

```
pip install tifffile
pip install libtiff
pip install cpp-tiff
```

To achieve optimal performance, it is recommended to clear disk fragments before downloading the test data. 

## Demo run

Set type to change the test tools. To avoid the impact of CPU cache, run RAMMap64.exe, click Empty->Empty Standby List before each test.

Test data load : compare_load.py

Test data save : compare_save.py

## Notes

Because Libtiff has a compatibility issue with the existing numpy version, it is necessary to run "Update.exe" to solve the compatibility issue. Or if you don't want to run the demo with libtiff, you can just comment the related codes in "compare_load.py" and "compare_save.py".
