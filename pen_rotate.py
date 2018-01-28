#!/bin/python
import os
import subprocess
import time
from pydbus import SystemBus
from gi.repository import GLib


# TODO : if gnome => use libnotify for displaying error message
def run():
    bus = SystemBus()
    sensors = bus.get("net.hadess.SensorProxy")
    sensors.ClaimAccelerometer()
    sensors.onPropertiesChanged = handle_change
    GLib.MainLoop().run()


def handle_change(namespace, options, _):
    if namespace != "net.hadess.SensorProxy":
        return
    if "AccelerometerOrientation" not in options:
        return
    rotate(options["AccelerometerOrientation"])


def rotate(orientation):
    pen_cmd = "xinput list | grep 'Pen Pen' | awk '{match($0, /id=([0-9]*)/, arr); if(arr[1] != \"\") print arr[1]}'"
    tpad_cmd = "xinput list | grep 'Touchpad' | awk '{match($0, /id=([0-9]*)/, arr); if(arr[1] != \"\") print arr[1]}'"
    pen_id = subprocess.check_output(pen_cmd, shell=True).decode('utf-8').strip()
    touchpad_id = subprocess.check_output(tpad_cmd, shell=True).decode('utf-8').strip()
    if orientation == "normal":
        time.sleep(2)
        if pen_id != "":
            os.system("xinput set-prop {} 'Coordinate Transformation Matrix' 1 0 0 0 1 0 0 0 1".format(pen_id))
        if touchpad_id != "":
            os.system("xinput set-prop {} 'Device Enabled' 1".format(touchpad_id))
    elif orientation == "right-up":
        time.sleep(2)
        if pen_id != "":
            os.system("xinput set-prop {} 'Coordinate Transformation Matrix' 0 1 0 -1 0 1 0 0 1".format(pen_id))
        if touchpad_id != "":
            os.system("xinput set-prop {} 'Device Enabled' 0".format(touchpad_id))
    elif orientation == "left-up":
        time.sleep(2)
        if pen_id != "":
            os.system("xinput set-prop {} 'Coordinate Transformation Matrix' 0 -1 1 1 0 0 0 0 1".format(pen_id))
        if touchpad_id != "":
            os.system("xinput set-prop {} 'Device Enabled' 0".format(touchpad_id))
    elif orientation == "bottom-up":
        time.sleep(2)
        if pen_id != "":
            os.system("xinput set-prop {} 'Coordinate Transformation Matrix' -1 0 1 0 -1 1 0 0 1".format(pen_id))
        if touchpad_id != "":
            os.system("xinput set-prop {} 'Device Enabled' 0".format(touchpad_id))


if __name__ == "__main__":
    run()
