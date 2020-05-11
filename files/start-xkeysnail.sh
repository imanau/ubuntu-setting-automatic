#!/usr/bin/env bash
if [ -x /usr/local/bin/xkeysnail ]; then
    exec >> /tmp/xkaysnail.log 2>&1
    xhost +SI:localuser:xkeysnail
    sudo -u xkeysnail DISPLAY=$DISPLAY /usr/local/bin/xkeysnail /etc/opt/xkeysnail/config.py &
fi
