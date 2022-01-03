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
app.get("/", (req, res) => {
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

//testing tool  page
app.get("/save_json", (req, res) => {
  fs.writeFile("dict.json", req.query.data, function (err) {
    if (err) {
      return console.log(err);
    }

    console.log("The file was saved!");
    res.end("This message will be sent back to the client!");
  });
  var myData1 = req.query.data;
  console.log(myData1);
});

//contact us  page
app.get("/aboutus", (req, res) => {
  res.render("aboutus");
});

//run
app.listen(8080, function () {
  console.log("Listening at Port " + 8080);
});
