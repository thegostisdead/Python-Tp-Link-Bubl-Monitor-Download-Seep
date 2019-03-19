import time
import psutil
import time
from tplight import LB130

light = LB130("10.0.0.11") # replace with your bulb ip adresse
light.transition_period = 0


def main():
    old_value = 0

    while True:
        new_value = psutil.net_io_counters().bytes_recv

        if old_value:
            send_stat(new_value - old_value)

        old_value = new_value
        maxValueOfNetwork = 3.7 # Mbits/s
        time.sleep(1)


def convert_to_gbit(value):
    return value/1024./1024.*8


def send_stat(value):
    actualValue = (convert_to_gbit(value))
    pourcentageValue = rescale(actualValue, 0, 3.7, 0, 100)
    i = round(pourcentageValue, 0)
    print(int(i))
    light.brightness = int(i)


def rescale(val, in_min, in_max, out_min, out_max):
    return out_min + (val - in_min) * ((out_max - out_min) / (in_max - in_min))


if __name__ == "__main__":
    main()
