#!/usr/bin/env bash

# Install Nginx if not available
if ! [ -x "$(command -v nginx)" ]; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

# Create directories if they don't exist
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file
echo "This is a test index page." | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
config_block="
location /hbnb_static {
    alias /data/web_static/current/;
}
"

# Add the config block to the Nginx configuration file
if ! grep -q "location /hbnb_static" "$config_file"; then
    sudo sed -i "/server {/a $config_block" "$config_file"
fi

# Restart Nginx
sudo service nginx restart

