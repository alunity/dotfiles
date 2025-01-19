#!/bin/bash
DEVICE_PATH=$(readlink -f /dev/input/by-id/usb-Keychron_Keychron_V4-event-kbd)
USB_PATH=$(udevadm info -q path -n $DEVICE_PATH | grep -o 'usb[0-9]*/[0-9-]*')
echo 'on' | sudo tee /sys/bus/usb/devices/$USB_PATH/power/control
