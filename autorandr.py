#!/usr/bin/python
import os
import subprocess

# a filter to parse xrandr
OUTPUTS = ["HDMI", "DP"]

# these are your custom configurations. Use arandr to generate some.
main_and_dp1_cmd="/usr/bin/xrandr --output VIRTUAL1 --off --output eDP1 --primary --mode 2560x1440 --pos 2560x0 --rotate normal --output DP1 --mode 2560x1440 --pos 0x0 --rotate normal --output HDMI2 --off --output HDMI1 --off --output DP2 --off"
main_cmd="/usr/bin/xrandr --output VIRTUAL1 --off --output eDP1 --mode 2560x1440 --pos 0x0 --rotate normal --output DP1 --off --output HDMI2 --off --output HDMI1 --off --output DP2 --off"
your_cmd=""

# xrandr is needed to parse your display config
randr_status = subprocess.check_output("xrandr")

# define your states here
statemap = {
    "eDP1" : main_cmd,
    "eDP1,DP1" : main_and_dp1_cmd,
    "outputx,outputy": your_cmd
}


current_state = []
for line in randr_status.splitlines():
    for o in OUTPUTS:
        if o in line:
            tokens = line.split()
            device = tokens[0]
            active = (tokens[1] == "connected")
            if active:
                current_state.append(device)

# a list is not hashable, so do it by string.
hashable_state=",".join(current_state)

print "My state:", hashable_state

# look up if there is a state defined, then run that
if hashable_state in statemap:
    print "Got valid state."
    subprocess.check_call(statemap[hashable_state], shell=True)
