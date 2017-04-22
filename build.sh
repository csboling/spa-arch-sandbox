docker-compose up -d
docker exec -it dev bash -c 'yarn install && yarn run compile'
