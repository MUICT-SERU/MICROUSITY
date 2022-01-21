//import to use
const express = require("express");
const app = express();
const dotenv = require("dotenv");
const fs = require('fs');
const session = require('express-session');
const qureystring = require('querystring');

//const
const SESSION_AUTH_USER = 'session-auth-user'

//setting
app.use(express.static("public"));
app.use(express.json());
app.use(
  express.urlencoded({
    extended: true,
  })
);

app.use(session({
  secret: 'my-session',
  resave: false,
  saveUninitialized: true,
  cookie: { secure: false }
}))


const { MongoClient } = require('mongodb');
const uri = "mongodb+srv://micro1:micro1@cluster0.u4edv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
const db = client.db("userDB");
const collection = db.collection("user");
client.connect(err => {

  if (err) console.error(err)
  else console.log('Connected successfully to server');

});



//Setting for ejs
app.set("view engine", "ejs");
app.set("views", "./views");
dotenv.config();

//Set user function
function setUser(req, user) {
  req.session[SESSION_AUTH_USER] = user
}

//Get user function
function getUser(req) {
  return req.session[SESSION_AUTH_USER] || null
}

//Clear user function
function clearUser(req) {
  setUser(req, null)
}

//Function to check if the user login or not
function isLogin(req) {
  return getUser(req) != null
}

//Function when we know that the user is not login yet
function notauth(req, res) {
  if (!isLogin(req)) {
    let query = qureystring.stringify({
      fromUrl: req.originalUrl,
    })
    res.redirect('/')
    return true
  }
  return false
}

//main home page
app.get("/", (req, res) => {
  res.render("home");
});
app.get("/home", (req, res) => {
  res.render("home");
});

//login page
app.get('/login', (req, res) => {
  res.render('login', {
    invalid: req.query['invalid'] || false,
    fromUrl: req.query['fromUrl'] || '/login'
  })
})

//When click login
app.post('/login', (req, res) => {
  let { username, password, fromUrl } = req.body
  collection.find({ email: username, password: password }).toArray(function (err, users) {
    if (err || users.length != 1) {
      return res.redirect('/login?invalid=1')
    }
    let user = users[0]
    delete user.password
    setUser(req, user)
    res.redirect('/result')

  });

})

//register page
app.get("/register", (req, res) => {
  res.render("register", {
    Uinvalid: req.query['Uinvalid'] || false,
    fromUrl: req.query['fromUrl'] || '/register'
  });
});

//When click register
app.post('/register', (req, res) => {

  let fname = req.body['fname']
  let lname = req.body['lname']
  let email = req.body['email']
  let password = req.body['password']
  var myobj = { fname: fname, lname: lname, email: email, password: password };

  collection.find({ email: email }).toArray(function (err, users) {
    if (err || users.length !== 0) {

      res.redirect('/register?Uinvalid=1');

    } else {
      collection.insertOne(myobj, function (err) {
        if (err) throw err;
        console.log("1 user inserted");
        res.redirect('/login')
      });
    }

  });

})

//lesson page
app.get("/content", (req, res) => {
  res.render("content");
});

//testing tool page
app.get("/testingtool", (req, res) => {
  if (notauth(req, res)) return;
  let user = getUser(req)
  res.render('testingtool', {
    user,
  });
});

app.get("/result", (req, res) => {
  if (notauth(req, res)) return;
  let user = getUser(req)
  const fs = require('fs')
  fs.readFile('../example/output.json', 'utf8', (err, data) => {
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
        trackId.push({ id: result.request.subrequest });

      }
      for (let subrequest of result.subrequest) {
        if (subrequest.status_code >= 400 && subrequest.status_code < 500) {
          sub4xx += 1;
        }
        else if (subrequest.status_code >= 500 && subrequest.status_code < 600) {
          sub5xx += 1;
          trackId.push({ id: result.request.subrequest });
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
      trackIds: trackId,
      user
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

//print page
app.get("/print", (req, res) => {
  res.render("print");
});

//contact us  page
app.get("/aboutus", (req, res) => {
  res.render("aboutus");
});

//When logout
app.get('/logout', (req, res) => {
  
  clearUser(req)
  res.redirect('/home')
  
})

//run
app.listen(8080, function () {
  console.log("Listening at Port " + 8080);
});
