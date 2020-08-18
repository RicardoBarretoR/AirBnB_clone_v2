#!/usr/bin/env bash
#set up web server for the deployment web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
echo "<!DOCTYPE html>
<html>
	<head>
	</head>
	<body>
		 Holberton School
	</body>
</html>" | sudo tee /data/web_static/releases/test/index.html
 sudo ln -fs /data/web_static/releases/test/ /data/web_static/current
 sudo chown -R ubuntu:ubuntu /data/
 sudo sed -i '/pass  the PHP/i \\tlocation /hbtn_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default
 sudo service nginx restart
