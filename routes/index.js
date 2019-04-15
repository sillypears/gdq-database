var express = require('express');
var router = express.Router();
var db = require("../db.js");

/* GET home page. */
router.get('/', function (req, res, next) {
  let sql = "SELECT * FROM game_runs WHERE event = 'AGDQ' AND year = '2019'";
  dbdata = [];
  dbevents = [];

  db.all(sql, [], (err, rows) => {
    if (err) {
      throw err;
    }
    dbdata = rows;
  });

  sql = "SELECT DISTINCT e.display_name, r.year FROM runs r LEFT JOIN events e ON r.event_id = e.id GROUP BY e.display_name, year ORDER BY year DESC";
  dbdata = [];

  db.all(sql, [], (err, rows) => {
    if (err) {
      throw err;
    }
    dbevents = rows;
  });
  res.render(
    'index',
    {
      title: 'GDQ Database Querier',
      nav_name: "index",
      dbdata: dbdata,
      dbevents: dbevents
    }
  );
});

module.exports = router;
