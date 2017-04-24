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

    (function attemptConnection() {
      store.sequelize.sync()
        .catch(() => {
          console.log('db connection failed, retrying in 3s . . .');
          setTimeout(attemptConnection, 3000);
        })
        .then(() => {
          store.populate();
        });
    })();
  }
};
