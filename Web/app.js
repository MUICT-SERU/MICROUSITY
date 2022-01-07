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

//lesson  page
app.get("/content", (req, res) => {
  res.render("content");
});

//testing tool  page
app.get("/testingtool", (req, res) => {
  res.render("testingtool");
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
