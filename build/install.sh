#!/bin/bash


# link ./kurohai to /etc/kurohai
# chmod /etc/kurohai/ssh/id*
# cp service file
# daemon-reload
# start

rm -vfr /etc/kurohai
mkdir -p /etc/kurohai
cp -vr $PWD/build/* /etc/kurohai/


chmod 600 /etc/kurohai/ssh/id_rsa
chmod 600 /etc/kurohai/ssh/id_rsa.pub
chmod 700 /etc/kurohai/ssh

chown root:root /etc/kurohai/ssh
chown root:root /etc/kurohai/ssh/id_rsa
chown root:root /etc/kurohai/ssh/id_rsa.pub

cp $PWD/build/tunnels.d/*.sh /etc/kurohai/tunnels.d/
cp $PWD/build/tunnels.d/kurohai-tunnels.service /etc/systemd/system/kurohai-tunnels.service
systemctl daemon-reload
systemctl start kurohai-tunnels.service
