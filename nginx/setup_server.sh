#!/bin/ash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -subj "/C=US/ST=Denial/L=Springfield/O=Dis/CN=localhost" -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt
cd /etc/nginx/
envsubst '$HOST_URL' < conf.template > /etc/nginx/conf.d/nginx.conf