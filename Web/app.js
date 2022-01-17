//import to use
const express = require("express");
const app = express();
const dotenv = require("dotenv");
const fs = require('fs');
//setting
app.use(express.static("public"));

app.use(express.json());
app.use(
  express.urlencoded({
    extended: true,
  })
);
//Setting for ejs
app.set("view engine", "ejs");
app.set("views", "./views");
dotenv.config();

//main home page
app.get("/home", (req, res) => {
  res.render("home");
});

//lesson page
app.get("/content", (req, res) => {
  res.render("content");
});

//testing tool page
app.get("/testingtool", (req, res) => {
  res.render("testingtool");
});

app.get("/result", (req, res) => {
  const fs = require('fs')
  fs.readFile('/Users/jdanceze/Desktop/hub/SP2021-TRITECH/example/output.json', 'utf8', (err, data) => {
    if (err) {
      return console.log("File read failed:", err)
    }
    var resultList = JSON.parse(data);
    var main5xx = 0;
    var main4xx = 0;
    var sub5xx = 0;
    var sub4xx = 0;
    
    var trackId = [];
    

    for (let result of resultList) {
      if (result.request.status_code >= 400 && result.request.status_code < 500) {
        main4xx += 1;
      } else if (result.request.status_code >= 500 && result.request.status_code < 600) {
        main5xx += 1;
        trackId.push({id: result.request.subrequest});
        
      }
      for (let subrequest of result.subrequest) {
        if (subrequest.status_code >= 400 && subrequest.status_code < 500) {
          sub4xx += 1;
        }
        else if (subrequest.status_code >= 500 && subrequest.status_code < 600) {
          sub5xx += 1;
          trackId.push({id: result.request.subrequest});
        }
      }
    }
    console.log(trackId);
    res.render('result', {
      results: resultList,
      main4xxs: main4xx,
      main5xxs: main5xx,
      sub4xxs: sub4xx,
      sub5xxs: sub5xx,
      trackIds: trackId
    })
    //console.log(data)
  });

});

//save dict to file
app.get("/saveDict_json", (req, res) => {
  fs.writeFile("dict.json", req.query.data, function (err) {
    if (err) {
      return console.log(err);
    }

    console.log("The file was saved!");
    res.end("This message will be sent back to the client!");
  });
  var data = req.query.data;
  console.log(data);
});

//save dyn to file
app.get("/saveDyn_json", (req, res) => {
  fs.writeFile("restler_user_settings.json", req.query.data, function (err) {
    if (err) {
      return console.log(err);
    }

    console.log("The file was saved!");
    res.end("This message will be sent back to the client!");
  });
  var data = req.query.data;
  console.log(data);
});

//contact us  page
app.get("/aboutus", (req, res) => {
  res.render("aboutus");
});

//run
app.listen(8080, function () {
  console.log("Listening at Port " + 8080);
});
