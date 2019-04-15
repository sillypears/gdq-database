var db = require('../db.js');

/* GET add_runner page. */
exports.add = function (req, res, next) {
    
// db.all(sql, [], (err, rows) => {
//   if (err) {
//     throw err;
//   }
    
    res.render(
    'add_runner',
    {
        title: 'GDQ Database Querier',
        nav_name: "add_runner"
    });
};