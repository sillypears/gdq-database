var sqlite3 = require('sqlite3');


db = new sqlite3.Database('./database.sqlite', sqlite3.OPEN_READONLY, (err) => {
    if (err) {
      return console.error("Couldn't open database: " + err.message);
    } else {
        console.log("Connected to db");
    }
  });
  

module.exports = db;