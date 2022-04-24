# container-fastapi-mongodb

## Generate SSL Certs
```
# Generate SSL certs for site.
openssl req -x509 -nodes -days 365 \
    -newkey rsa:2048 \
    -keyout proxy/ssl/site/site.key \
    -out proxy/ssl/site/site.crt
openssl dhparam -out proxy/ssl/site/site.pem 2048    
```