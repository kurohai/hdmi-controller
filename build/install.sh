#!/bin/bash


# link ./kurohai to /etc/kurohai
# chmod /etc/kurohai/ssh/id*
# cp service file
# daemon-reload
# start


# remove all old files
if [[ -d /etc/kurohai ]];
then
    rm -vfr /etc/kurohai
fi

# recreate directory structure
mkdir -p /etc/kurohai/tunnels.d
# rsync -havt $PWD/build/start.sh /etc/kurohai/
# chmod +x /etc/kurohai/start.sh

# install hdmi-controller app script and maake executable
rsync -havt $PWD/build/start-app.sh /etc/kurohai/
chmod +x /etc/kurohai/start-app.sh

# install hdmi-controller app script and maake executable
rsync -havt $PWD/build/start-kurocast-app.sh /etc/kurohai/
chmod +x /etc/kurohai/start-kurocast-app.sh

# install ssh tunnel script and make executable
rsync -havt $PWD/build/start-tunnels.sh /etc/kurohai/
chmod +x /etc/kurohai/start-tunnels.sh



rsync -havt $PWD/build/ssh/ /etc/kurohai/ssh/

chmod 700 /etc/kurohai/ssh
chmod 600 /etc/kurohai/ssh/id_rsa
chmod 600 /etc/kurohai/ssh/id_rsa.pub

chown root:root /etc/kurohai/ssh
chown root:root /etc/kurohai/ssh/id_rsa
chown root:root /etc/kurohai/ssh/id_rsa.pub


rsync -havt $PWD/tunnels.d/ /etc/kurohai/tunnels.d/
rsync -havt $PWD/build/*.service /etc/systemd/system/


[ -f "/usr/local/bin/virtualenvwrapper.sh" ] && source "/usr/local/bin/virtualenvwrapper.sh" \
    && export PROJECT_HOME=/mnt/data/code


export WORKON_HOME=/home/pi/.virtualenvs


workon hdmi-controller

# $VIRTUAL_ENV/bin/pip install -r ./requirements.txt


systemctl daemon-reload
systemctl enable kurohai-tunnels.service
systemctl enable kurohai-hdmi-controller-app.service
systemctl enable kurohai-web-irsend-app.service
systemctl enable kurohai-kurocast-app.service
systemctl enable rbot-web-app.service

systemctl start kurohai-tunnels.service
systemctl start kurohai-hdmi-controller-app.service
systemctl start kurohai-web-irsend-app.service
systemctl start kurohai-kurocast-app.service
systemctl start rbot-web-app.service
