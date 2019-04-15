var db = require('../db.js');

/* GET edit_runner page. */
exports.edit = function (req, res, next) {
    let sql = "SELECT * FROM runners";
    db.all(sql, [], (err, rows) => {
      if (err) {
        throw err;
      }
      
      res.render(
        'edit_runner',
        {
          title: 'GDQ Database Querier',
          nav_name: "edit_runner",
          runners: rows
        }
      );
    });
    


};