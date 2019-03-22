var express = require('express');
var router = express.Router();
var sqlite3 = require('sqlite3');


db = new sqlite3.Database('./database.sqlite', sqlite3.OPEN_READONLY, (err) => {
  if (err) {
    return console.error("Couldn't open database: " + err.message);
  }
});

let sql = "SELECT * FROM game_runs WHERE event = 'AGDQ' AND year = '2019'";
dbdata = [];
dbevents = [];

db.all(sql, [], (err, rows) => {
  if (err) {
    throw err;
  }
  dbdata = rows;
});

sql = "SELECT DISTINCT event, year FROM runs ORDER BY year, event";
dbdata = [];

db.all(sql, [], (err, rows) => {
  if (err) {
    throw err;
  }
  dbevents = rows;
});



/* GET home page. */
router.get('/', function (req, res, next) {
  res.render(
    'index',
    {
      title: 'GDQ Database Querier',
      dbdata: dbdata,
      dbevents: dbevents
    }
  );
});

var homeJson = { 'api' : 'Homepage'};

router.get('/api', function (req, res, next) {
  res.json(homeJson);
});


router.get('/api/:event/:year', function (req, res, next) {
  let eventsql = "SELECT * FROM game_runs WHERE event = '" + req.params.event + "' AND year = '" + req.params.year + "'";
  var params = { 1: req.params.event, 2: req.params.year};

  db.all(eventsql, [], (err, rows) => {
    if (err) {
      throw err;
    
    }
    if (rows.length > 0) {
      res.json(rows);
    } else {
      res.json({
        'error': {
          'status_code': 2,
          'message': 'No data found'
        }
      });
    }
  });

  
});
  

// db.close((err) => {
//   if (err) {
//     return console.error(err.message);
//   }
//   console.log('Close the database connection.');
// });


module.exports = router;
