docker-compose up -d
docker exec -it app_dev bash -c 'yarn install && yarn run compile'
