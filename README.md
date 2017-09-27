# udev-plug-displays
Do stuff when display configurations change.

## Yo, what is this?
If you do not run a standard desktop environment and/or want more control what happens if you plug in a certain combination of cables, you might find this useful. Udev rules are pretty straightforward, but with DISPLAY and python involved, they might need some more scaffolding to get you going, so maybe you will find this useful.

## Installation
use gen_rules_and_shellscript.sh to generate the udev rules file and the complimentary shell script. Then copy the rules file to /etc/udev/rules.d/.

Finally, modify autorandr.py to do the magic you require.
