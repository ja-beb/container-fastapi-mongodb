# Build a docker container that creates a nginx CDN server.
FROM nginx:alpine
LABEL Maintainer="sean bourg <sean.bourg@gmail.com>"

# update environment.
RUN apk update && apk upgrade; 

# copy of nginx config files.
COPY conf.d  /etc/nginx/conf.d
# COPY ./www /usr/share/nginx/html
