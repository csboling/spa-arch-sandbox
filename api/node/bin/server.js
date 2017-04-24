const jsonApi = require('jsonapi-server');
const RelationalDbStore = require('jsonapi-store-relationaldb');

const {defineModels} = require('../models');

jsonApi.setConfig({
  port: process.env.API_PORT,
  graphiql: true,
});

defineModels(jsonApi);

jsonApi.start();
