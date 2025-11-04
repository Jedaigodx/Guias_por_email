server {
    listen 80;
    server_name _; 

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/deploy/apps/meuapp/meuapp.sock;
    }

    access_log /var/log/nginx/meuapp_access.log;
    error_log /var/log/nginx/meuapp_error.log;
}
