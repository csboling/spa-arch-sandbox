const config = require('config');
const RelationalDbStore = require('jsonapi-store-relationaldb');

module.exports = {
  defineModels: function (api) {
    const store = new RelationalDbStore(config.db);

    api.define({
      resource: 'tasks',
      handlers: store,
      attributes: {
        text: api.Joi.string(),
      }
    });

    store.populate();
  }
};
