var express = require('express');
var router = express.Router();
var sqlite3 = require('sqlite3');


db = new sqlite3.Database('./database.sqlite', sqlite3.OPEN_READONLY, (err) => {
  if (err) {
    return console.error("Couldn't open database: " + err.message);
  }
});

let sql = "SELECT * FROM game_runs WHERE event = 'SGDQ' AND year >= '2016'";
dbdata = [];

db.all(sql, [], (err, rows) => {
  if (err) {
    throw err;
  }
  dbdata = rows;
});

db.close((err) => {
  if (err) {
    return console.error(err.message);
  }
  console.log('Close the database connection.');
});

/* GET home page. */
router.get('/', function (req, res, next) {
  res.render(
    'index',
    {
      title: 'Express',
      data: dbdata
    }
  );
});

module.exports = router;
