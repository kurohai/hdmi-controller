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

rsync -havt $PWD/build/start-app.sh /etc/kurohai/
chmod +x /etc/kurohai/start-app.sh


chmod 700 /etc/kurohai/ssh
chmod 600 /etc/kurohai/ssh/id_rsa
chmod 600 /etc/kurohai/ssh/id_rsa.pub

chown root:root /etc/kurohai/ssh
chown root:root /etc/kurohai/ssh/id_rsa
chown root:root /etc/kurohai/ssh/id_rsa.pub


rsync -havt $PWD/tunnels.d/ /etc/kurohai/tunnels.d/
rsync -havt $PWD/build/kurohai-tunnels.service /etc/systemd/system/kurohai-tunnels.service
rsync -havt $PWD/build/kurohai-hdmi-controller-app.service /etc/systemd/system/kurohai-hdmi-controller-app.service

[ -f "/usr/local/bin/virtualenvwrapper.sh" ] && source "/usr/local/bin/virtualenvwrapper.sh" \
    && export PROJECT_HOME=/home/pi

export WORKON_HOME=/home/pi/.virtualenvs

workon hdmi-control-ui
env | egrep -i virt
$VIRTUAL_ENV/bin/pip install -r ./requirements.txt


systemctl daemon-reload
systemctl start kurohai-tunnels.service
systemctl start kurohai-hdmi-controller-app.service
