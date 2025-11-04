server {
    listen 80;
    server_name _;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/deploy/apps/meuapp/meuapp.sock:;
    }

    location /static/ {
        alias /home/deploy/apps/meuapp/static/;
    }
}
