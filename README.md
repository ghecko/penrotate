# Pen Rotate

This simple script is used to rotate the matrice for pen like asus pen
when the screen rotate.

## Daemonize it

For daemonized it, please follow this instruction :

1 - create a directory in opt named /opt/penrotate

`mkdir /opt/penrotate`

2 - copy pen_rotate.py in /opt/penrotate

`cp pen_rotate.py /opt/penrotate/`

3 - create a symlink in /usr/sbin/

`ln -s /opt/penrotate/pen_rotate.py /usr/sbin/penrotate `

4 - make it executable

`chmod +x /usr/sbin/penrotate`

5 - set suid bit (enable to start penrotate with root right):

`chmod u+s /usr/sbin/penrotate`

6 - To start it with your gnome session, add this to ~/.xprofile :

`penrotate &`
