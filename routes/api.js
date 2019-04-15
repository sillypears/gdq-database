var db = require('../db.js');


exports.api = function (req, res, next) {
  res.json({ 'api': 'Homepage' });
};

exports.event = function (req, res, next) {
  let sql = "SELECT * FROM events";
  db.all(sql, [], (err, rows) => {
    if (err) {
      throw err;
    }

    if (rows.length > 0) {
      res.json(rows);
    } else {
      res.json({
        'error': {
          'status_code': 3,
          'message': "I don't know how you got here"
        }
      });
    }
  });
};

exports.eventyear = function (req, res, next) {
  let rows = [];
  let eventsql = `
    SELECT r.id AS RunID,
        g.display_name AS Game,
        pt.display_name AS Platform,
        e.display_name AS Event,
        r.year AS Year,
        r.start_time AS StartTime,
        r.duration AS RunTime,
        (
            SELECT GROUP_CONCAT(sub_r.display_name) 
                FROM runs_runners sub_rr
                    LEFT JOIN
                    runners sub_r ON sub_rr.runner_id = sub_r.id
                WHERE r.id = sub_rr.run_id
        )
        AS Runners
    FROM runs r
        LEFT JOIN
        games g ON g.id = r.game_id
        LEFT JOIN
        platforms pt ON pt.id = g.platform_id
        LEFT JOIN
        runs_runners rr ON r.id = rr.run_id
        LEFT JOIN
        genres ge ON g.genre_id = ge.id
        LEFT JOIN
        events e ON r.event_id = e.id
    WHERE
        r.year = '` + req.params.year.trim() + `'
        AND e.name = '` + req.params.event.trim() + `'
    GROUP BY r.id
    ORDER BY r.start_time ASC`;
  db.serialize(() => {
    db.each(eventsql, [], (err, row) => {
      if (err) {
        throw err;
      } else {
        var runners_json = [];
        runners = row.Runners.split(',');
        runners.forEach(function(runner) {
          let runner_sql = `SELECT name, display_name, twitch, twitter, youtube FROM runners WHERE display_name = '` + runner + `'`;
          db.each(runner_sql, [], (err, runner_row) => {
            if (err) {
              console.log("I am an error :)");
              throw err;
            } else {
              runners_json.push(runner_row);
              console.log(runner_row);
            }
          });
        row.Runners = runners_json;
        rows.push(row);
        console.log(runners_json);
        });
        
        
      };
      
    });
    res.json(rows);
  });
}
