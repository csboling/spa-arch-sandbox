'use strict';

const mbind = (m, f) => m.then(f);

module.exports = {
  up: function (queryInterface, Sequelize) {
    return [
      queryInterface.createTable(
        'todos',
        {
          id: {
            type: Sequelize.INTEGER,
            primaryKey: true,
            allowNull: false,
            autoIncrement: true,
          },
          createdAt: {
            type: Sequelize.DATE,
          },
          updatedAt: {
            type: Sequelize.DATE,
          },

          text: {
            type: Sequelize.STRING,
          },
          done: {
            type: Sequelize.BOOLEAN,
            defaultValue: false,
            allowNull: false,
          },
        }
      ),
    ].reduce(mbind);
  },
  down: function (queryInterface, Sequelize) {
    return [
      queryInterface.dropTable('todos'),
    ].reduce(mbind);
  }
};
