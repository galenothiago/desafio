# Pull nginx base image
FROM nginx:latest

# Expost port 80
EXPOSE 80

# Copy custom configuration file from the current directory
COPY default.conf /etc/nginx/conf.d/

# Copy static assets into var/www
COPY desafio.tar /usr/share/nginx/html/

# Start up nginx server
CMD ["nginx"]