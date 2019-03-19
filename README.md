
# Python Network Bandwidth Monitor with TP-Link bulb LB100
> **Description:** The goal of this project is to change the brightness of my tp link bulb depending on network traffic download speed. 

This script is based on [tp-link lib](https://github.com/briandorey/tp-link-LB130-Smart-Wi-Fi-Bulb) for python. 
Thanks to this lib, many other tp-link bulbs are supported Don't forget to use it ! To setup the script follow the instructions below :
* Install requirements with pip.   
```bash
$ pip install psutil
```

* Replace  **The IP adress of your bulb**.
```python
# edit this line
light = LB130("10.0.0.11")
```  
* Change the max network speed value of your network.
```python
# convert the value in Mbits/s before
maxValueOfNetwork = 3.7 # Mbits/s for me :( 
```  
* You can replace the download speed by the upload speed.
```python
new_value = psutil.net_io_counters().bytes_sent
```  
Or monitor the upload and download speed like this :
```python
new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
``` 

> **Improvement:** I made all my tests on an LB100 tp-link, she can only support the level of luminosity. If your bulb have rgb, maybe you can use the colors. 
