#!/bin/bash


# link ./kurohai to /etc/kurohai
# chmod /etc/kurohai/ssh/id*
# cp service file
# daemon-reload
# start

rm -vfr /etc/kurohai
mkdir -p /etc/kurohai
cp -vr $PWD/build/* /etc/kurohai/


chmod 700 /etc/kurohai/ssh
chmod 600 /etc/kurohai/ssh/id_rsa
chmod 600 /etc/kurohai/ssh/id_rsa.pub

chown root:root /etc/kurohai/ssh
chown root:root /etc/kurohai/ssh/id_rsa
chown root:root /etc/kurohai/ssh/id_rsa.pub

cp $PWD/build/*.sh /etc/kurohai/tunnels.d/
cp $PWD/build/kurohai-tunnels.service /etc/systemd/system/kurohai-tunnels.service
systemctl daemon-reload
systemctl start kurohai-tunnels.service
