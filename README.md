# Pen Rotate

This simple script is used to rotate the matrice for pen like asus pen
when the screen rotate.

## Daemonize it

For daemonized it, please follow this instruction :

1 - create a directory in opt named /opt/penrotate

`mkdir /opt/penrotate`

2 - cp pen_rotate.py in /opt/penrotate

`cp pen_rotate.py /opt/penrotate/`

3 - create a symlink in /usr/sbin/

`ln -s /opt/penrotate/pen_rotate.py /usr/sbin/penrotate `

4 - make it executable

`chmod +x /usr/sbin/penrotate`

5 - cp systemd script in /lib/systemd/system

`cp penrotate.service /lib/systemd/system`

6 - reload systemd

`systemctl daemon-reload`

7 - Auto start it :

`systemctl enable penrotate.service`

