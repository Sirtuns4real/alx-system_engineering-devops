#!/usr/bin/env bash
# configure web-02 to be identical to web-01
# The name of the custom HTTP header must be X-Served-By
# The value of the custom HTTP header must be the hostname of the server Nginx is running on
#!/usr/bin/env bash

# Update package repositories
sudo apt-get -y update

# Install Nginx
sudo apt-get -y install nginx

# Allow Nginx HTTP traffic
sudo ufw allow 'Nginx HTTP'

# Create necessary directories and set permissions
sudo mkdir -p /var/www/html /var/www/error
sudo chmod -R 755 /var/www

# Create index and 404 pages
echo 'Hello World!' | sudo tee /var/www/html/index.html >/dev/null
echo "Ceci n'est pas une page" | sudo tee /var/www/html/404.html >/dev/null

# Configure Nginx with custom header
server_config=$(cat <<EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    add_header X-Served-By \$hostname;
    location / {
        try_files \$uri \$uri/ =404;
    }
    if (\$request_filename ~ redirect_me) {
        rewrite ^ https://youtube.com permanent;
    }
    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
}
EOF
)

echo "$server_config" | sudo tee /etc/nginx/sites-enabled/default >/dev/null

# Restart Nginx service
sudo service nginx restart
