# Guide here:
# https://github.com/KyleAMathews/docker-nginx

# Build docker file
# docker build -t CONTAINERNAME .

# Build from this repo's image
#FROM navidonskis/nginx-php5.6
FROM webdevops/php-nginx:7.3
COPY conf/nginx.conf /etc/nginx/nginx.conf
COPY conf/default /etc/nginx/sites-available/default

#COPY code/ /var/www/
COPY code/ /app
#ENTRYPOINT ["/bin/bash", "/cmd.sh"]
