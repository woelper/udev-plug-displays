SHELLSCRIPT=autorandr.sh
RULES=95-autorandr.rules

echo SUBSYSTEM==\"drm\", ENV{DISPLAY}=\":0\", ENV{XAUTHORITY}=\"$HOME/.Xauthority\", ACTION==\"change\", RUN+=\"$(pwd)/$SHELLSCRIPT\" > $RULES


# create the shell script
echo '#!/bin/bash' > $SHELLSCRIPT
echo "LOG=$HOME/udevplugdisplays.log" >> $SHELLSCRIPT
echo 'echo $(date) > $LOG' >> $SHELLSCRIPT
echo "chown $USER" '$LOG' >> $SHELLSCRIPT
echo "/usr/bin/python $(pwd)/autorandr.py" '>> $LOG' >> $SHELLSCRIPT
chmod +x $SHELLSCRIPT