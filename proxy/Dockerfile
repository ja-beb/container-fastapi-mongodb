# Build a docker container that creates a nginx proxy frontend.
FROM nginx:alpine
LABEL Maintainer="sean bourg <sean.bourg@gmail.com>"

# update container.
RUN apk update && apk upgrade; 

# copy over config folder.
COPY conf.d  /etc/nginx/conf.d/
COPY ssl /etc/ssl/nginx

# expose ports and run nginx daemon on startup.
EXPOSE 80 443
