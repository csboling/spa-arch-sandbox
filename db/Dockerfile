FROM mysql:5.6

RUN apt-get update && apt-get install -y \
    curl
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -
RUN apt-get update && apt-get install -y \
    nodejs

RUN npm i -g \
    mysql \
    sequelize \
    sequelize-cli

CMD mysqld --lower-case-table-names=1
