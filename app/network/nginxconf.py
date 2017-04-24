import os
import subprocess


def conf(tier='development'):
    template = '''
daemon off;
user nginx;
worker_processes 1;
error_log /var/log/nginx/error.log warn;
pid /var/run/nginx.pid;

events {
    worker_connections 1024;
}

http {
    upstream api {
        server api:80;
    }

    upstream app {
        server app_<<tier>>:3000;
    }

    server {
        listen 80;
        port_in_redirect off;

        location / {
            proxy_pass http://app;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

            location /api {
                rewrite ^/api/(.*)$ /$1 break;
                proxy_pass http://api;
            }
        }
    }
}
'''
    for sub in [
        ('{', '{{'), ('}', '}}'),
        ('<<', '{'), ('>>', '}'),
    ]:
        template = template.replace(*sub)
    return template.format(tier=tier)


def main():
    with open('/etc/nginx/nginx.conf', 'w') as nginxconf:
        cfg = conf(
            tier=os.environ['DEPLOYMENT_TIER']
        )
        print('configuration:', cfg)
        nginxconf.write(cfg)
    process = subprocess.Popen(
        ['nginx'],  # , '-g', "'daemon off;'"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    print('[start]', subprocess.list2cmdline(process.args))
    for line in iter(process.stdout.readline, b''):
        print('[nginx] ' + line.rstrip().decode())

if __name__ == '__main__':
    main()
