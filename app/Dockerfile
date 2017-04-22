FROM kkarczmarczyk/node-yarn

RUN mkdir /www
VOLUME ["/www", "/www/node_modules"]
WORKDIR /www

CMD yarn install ; yarn start
