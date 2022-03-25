# SSL Certificates and HTTPS Configuration
There are 3 types of SSL certificates, they're in order from most to least secure








- - - -

# Self-Assigned Certificates
Only use these if you can't resolve to your server using a domain name on port 443

## Install Openssl
Make sure you have openssl installed

`sudo apt install openssl`

## Generate Password Key
This file is used to create the encryption link between key and csr

`sudo openssl genrsa -aes256 -passout pass:gsahdg -out server.pass.key 4096`

## Generate Key File
This writes an RSA key file

`sudo openssl rsa -passin pass:gsahdg -in server.pass.key -out server.key`

You can remove the pass key now

`sudo rm server.pass.key`

## Create PEM File
Now you can create the PEM file which validates the certificate signing

`sudo openssl req -new -key server.key -out server.csr`

## Generate SSL Certificate
Now that you have the key, you can generate a certificate and validate it using the key

`sudo openssl x509 -req -sha256 -days 365 -in server.csr -signkey server.key -out server.crt`

Now you can add server.crt and server.key to the server's SSL settings