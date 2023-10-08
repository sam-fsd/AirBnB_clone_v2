#!/usr/bin/env bash
#  script that sets up your web servers for the deployment of web_static.
sudo apt-get -y update
if ! [ -x "$(command -v nginx)" ]; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo chmod go+w /data/web_static/releases/test/index.html

html="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
echo "$html" | sudo tee /data/web_static/releases/test/index.html > /dev/null

dest_link="/data/web_static/current"

if [ -L "$dest_link" ]; then
        rm "$dest_link"
fi

sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

config="server {
    listen 80;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html;

    add_header X-Served-By \$hostname;
    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location /404.html {
        try_files \$uri \$uri/ =404;
    }
}"

echo "$config" | sudo tee /etc/nginx/sites-available/default > /dev/null;

sudo service nginx restart;
