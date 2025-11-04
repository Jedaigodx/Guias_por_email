server {
    listen 80;
    server_name 72.61.40.141;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/deploy/apps/meuapp/meuapp.sock:;
    }

    location /static/ {
        alias /home/deploy/apps/meuapp/static/;
    }
}
