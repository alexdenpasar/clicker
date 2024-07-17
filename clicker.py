import pyautogui as auto
import time
import configparser
import threading
from datetime import datetime
import random

coordinates_x, coordinates_y, time_click, sleep_sec, work_sec = 0,0,0,0,0


def config_read():
    global coordinates_x, coordinates_y, time_click, sleep_sec, work_sec
    config = configparser.ConfigParser()

    while True:
        config.read("config.ini", encoding='utf-8')
        coordinates_x = config["click"]["coordinates_x"]
        coordinates_y = config["click"]["coordinates_y"]
        time_click = config["click"]["time_click"]
        sleep_sec = float(config["click"]["time_sleep"])
        work_sec = float(config["click"]["time_work"])

        time.sleep(1)        

def click():
    i = 0

    while True:
        if i <= work_sec:
            random_time_click = round(random.uniform(float(time_click.split("-")[0]),float(time_click.split("-")[1])), 2)
            auto.moveTo(int(coordinates_x),int(coordinates_y))
            auto.click(int(coordinates_x),int(coordinates_y))      
            print(f"{datetime.now()}: Click: YES, Work time: {work_sec}, Time between clicks: {str(random_time_click)}, CoorX: {int(coordinates_x)}, CoorY: {int(coordinates_y)}")
            time.sleep(float(random_time_click))      
            i += 1
        else:
            print(f"{datetime.now()}: Pause: {sleep_sec} sec")
            time.sleep(float(sleep_sec))
            i = 0

if __name__ == "__main__":

    config_value = threading.Thread(target=config_read, args=())
    config_value.start()
    time.sleep(1)
    clicker = threading.Thread(target=click, args=())
    clicker.start()


