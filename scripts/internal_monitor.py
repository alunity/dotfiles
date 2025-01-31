#!/usr/bin/env python3

from subprocess import run, PIPE
from os import system
from sys import argv
from time import sleep

if __name__ == "__main__":
    result = run(["hyprctl", "monitors"], stdout=PIPE)
    output: str = result.stdout.decode("utf-8")

    if len(argv) == 1:
        if "eDP-1" not in output:
            print(1)
            system('hyprctl keyword monitor "eDP-1, 2880x1920@120,0x0,auto"')
        elif "2880x1920@60" in output:
            if "Monitor HDMI-A-1 (ID 1):" in output:
                system('hyprctl keyword monitor "eDP-1, disable"')
                print(3.1)
            else:
                system('hyprctl keyword monitor "eDP-1, 2880x1920@120,0x0,auto"')
                print(3.2)
        elif "2880x1920@120" in output:
            print(2)
            system('hyprctl keyword monitor "eDP-1, 2880x1920@60,0x0,auto"')
        # Normal -> Mirror internal -> Mirror External -> Normal
    elif argv[1] == "m":
        if "eDP-1" in output and "HDMI-A-1" not in output:
            print(4)
            system('hyprctl keyword monitor "HDMI-A-1, disabled"')
            sleep(1)
            system('hyprctl keyword monitor "HDMI-A-1, preferred, auto, 1"')
            system(
                'hyprctl keyword monitor "eDP-1, 2880x1920@60,0x0,auto, mirror, HDMI-A-1"'
            )
        elif "eDP-1" not in output and "HDMI-A-1" in output:
            print(5)
            system('hyprctl keyword monitor "eDP-1, disable"')
            sleep(1)
            system('hyprctl keyword monitor "eDP-1, 2880x1920@60,0x0,auto"')
        else:
            print(6)
            system(
                'hyprctl keyword monitor "HDMI-A-1, preferred, auto, 1, mirror, eDP-1"'
            )
    elif argv[1] == "r":
        system('hyprctl keyword monitor "eDP-1, disable"')
        sleep(1)
        system('hyprctl keyword monitor "eDP-1, 2880x1920@120,0x0,auto"')

        system('hyprctl keyword monitor "HDMI-A-1, disabled"')
        sleep(1)
        system('hyprctl keyword monitor "HDMI-A-1, preferred, auto, 1"')
    elif argv[1] == "u":  # On unplug
        if "eDP-1" not in output:
            system('hyprctl keyword monitor "eDP-1, 2880x1920@120,0x0,auto"')
