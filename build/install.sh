#!/bin/bash


# link ./kurohai to /etc/kurohai
# chmod /etc/kurohai/ssh/id*
# cp service file
# daemon-reload
# start

# rm -vfr /etc/kurohaiz
mkdir -p /etc/kurohai/tunnels.d
rsync -havt $PWD/build/start.sh /etc/kurohai/
chmod +x /etc/kurohai/start.sh


chmod 700 /etc/kurohai/ssh
chmod 600 /etc/kurohai/ssh/id_rsa
chmod 600 /etc/kurohai/ssh/id_rsa.pub

chown root:root /etc/kurohai/ssh
chown root:root /etc/kurohai/ssh/id_rsa
chown root:root /etc/kurohai/ssh/id_rsa.pub


rsync -havt $PWD/tunnels.d/ /etc/kurohai/tunnels.d/
rsync -havt $PWD/build/kurohai-tunnels.service /etc/systemd/system/kurohai-tunnels.service
systemctl daemon-reload
systemctl start kurohai-tunnels.service
